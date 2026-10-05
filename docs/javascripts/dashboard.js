/* Dashboard components: model finder (search + filters) and availability-matrix filter. */
(function () {
  'use strict';

  const RISK_STAGES = new Set(['soon', 'retiring', 'pending']);
  const MAX_RESULTS = 8;
  const dataCache = {};

  function escapeHtml(value) {
    return String(value == null ? '' : value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function normalize(value) {
    return String(value || '').toLowerCase().replace(/[^a-z0-9]/g, '');
  }

  function isSubsequence(needle, haystack) {
    let i = 0;
    for (let j = 0; j < haystack.length && i < needle.length; j++) {
      if (haystack[j] === needle[i]) i++;
    }
    return i === needle.length;
  }

  function score(record, query) {
    if (!query) return 1;
    const name = record._key;
    if (name === query) return 100;
    if (name.startsWith(query)) return 80 - Math.min(name.length - query.length, 30) / 2;
    const idx = name.indexOf(query);
    if (idx >= 0) return 50 - Math.min(idx, 20);
    if (normalize(record.f).startsWith(query)) return 30;
    if (query.length >= 3 && isSubsequence(query, name)) return 10;
    return 0;
  }

  function loadData(src) {
    if (!dataCache[src]) {
      dataCache[src] = fetch(src, { credentials: 'same-origin' })
        .then(function (response) {
          if (!response.ok) throw new Error('HTTP ' + response.status);
          return response.json();
        })
        .then(function (records) {
          records.forEach(function (record) { record._key = normalize(record.n); });
          return records;
        });
    }
    return dataCache[src];
  }

  function matchesFilter(record, filter) {
    if (!filter || filter === 'all') return true;
    if (filter === 'risk') return RISK_STAGES.has(record.lk);
    if (filter === 'preview') return record.lk === 'preview';
    if (filter.indexOf('family:') === 0) return record.f === filter.slice(7);
    return (record.c || []).indexOf(filter) >= 0;
  }

  function renderResult(record, root, active) {
    const categories = (record.c || [])
      .map(function (cat) {
        return '<span class="sku-badge sku-' + escapeHtml(cat.toLowerCase()) + '">' + escapeHtml(cat) + '</span>';
      })
      .join('');
    let meta = '<span>' + record.r + ' region' + (record.r === 1 ? '' : 's') + '</span>';
    if (record.nd) meta += '<span>Retires ' + escapeHtml(record.nd) + '</span>';
    if (record.rp) meta += '<span>→ ' + escapeHtml(record.rp) + '</span>';
    const badge = record.ll
      ? '<span class="lc-badge lc-badge--' + escapeHtml(record.lt) + '">' + escapeHtml(record.ll) + '</span>'
      : '';
    return (
      '<a class="finder-result' + (active ? ' is-active' : '') + '" role="option" href="' +
      escapeHtml(root + 'models/' + record.s + '/') + '">' +
      '<span class="finder-result__main"><strong>' + escapeHtml(record.n) + '</strong>' +
      '<small>' + escapeHtml(record.f) + '</small></span>' +
      '<span class="finder-result__meta">' + meta + '</span>' +
      '<span class="finder-result__tags">' + badge + categories + '</span>' +
      '</a>'
    );
  }

  function mountFinder(el) {
    if (el.dataset.mounted) return;
    el.dataset.mounted = 'true';

    const input = el.querySelector('.model-finder__input');
    const results = el.querySelector('.model-finder__results');
    const familyHost = el.querySelector('[data-family-chips]');
    const root = el.dataset.root || '';
    const kbd = el.querySelector('.model-finder__kbd');
    if (kbd && /Mac|iPhone|iPad/.test(navigator.platform)) kbd.textContent = '⌘ K';

    let records = [];
    let filter = 'all';
    let matches = [];
    let activeIndex = 0;

    function render() {
      const query = normalize(input.value);
      const filtered = records.filter(function (record) { return matchesFilter(record, filter); });
      if (!query && filter === 'all') {
        results.hidden = true;
        results.innerHTML = '';
        matches = [];
        return;
      }
      matches = filtered
        .map(function (record) { return { record: record, score: score(record, query) }; })
        .filter(function (item) { return item.score > 0; })
        .sort(function (a, b) {
          if (b.score !== a.score) return b.score - a.score;
          if (!query && a.record.dd != null && b.record.dd != null) return a.record.dd - b.record.dd;
          return b.record.r - a.record.r || a.record.n.localeCompare(b.record.n);
        })
        .map(function (item) { return item.record; });
      activeIndex = Math.min(activeIndex, Math.max(matches.length - 1, 0));
      results.hidden = false;
      if (!matches.length) {
        results.innerHTML = '<div class="finder-empty">No models match <strong>' + escapeHtml(input.value) +
          '</strong>. Try a shorter name or clear the filter.</div>';
        return;
      }
      const shown = matches.slice(0, MAX_RESULTS);
      const more = matches.length - shown.length;
      results.innerHTML = shown.map(function (record, index) {
        return renderResult(record, root, index === activeIndex);
      }).join('') + (more > 0
        ? '<div class="finder-more">+' + more + ' more · <a href="' + escapeHtml(root + 'models/') + '">browse the full table</a></div>'
        : '');
    }

    function setActive(index) {
      const items = results.querySelectorAll('.finder-result');
      if (!items.length) return;
      activeIndex = (index + items.length) % items.length;
      items.forEach(function (item, i) { item.classList.toggle('is-active', i === activeIndex); });
      items[activeIndex].scrollIntoView({ block: 'nearest' });
    }

    function setFilter(value) {
      filter = value;
      el.querySelectorAll('.finder-chip').forEach(function (chip) {
        chip.classList.toggle('is-active', chip.dataset.filter === value);
      });
      activeIndex = 0;
      render();
    }

    el.addEventListener('click', function (event) {
      const chip = event.target.closest('.finder-chip');
      if (!chip || !el.contains(chip)) return;
      setFilter(chip.classList.contains('is-active') && chip.dataset.filter !== 'all' ? 'all' : chip.dataset.filter);
    });

    input.addEventListener('input', function () { activeIndex = 0; render(); });
    input.addEventListener('keydown', function (event) {
      if (event.key === 'ArrowDown') { event.preventDefault(); setActive(activeIndex + 1); }
      else if (event.key === 'ArrowUp') { event.preventDefault(); setActive(activeIndex - 1); }
      else if (event.key === 'Enter') {
        const active = results.querySelectorAll('.finder-result')[activeIndex];
        if (active) { event.preventDefault(); active.click(); }
      } else if (event.key === 'Escape') {
        input.value = '';
        setFilter('all');
      }
    });

    loadData(el.dataset.src)
      .then(function (data) {
        records = data;
        const families = {};
        data.forEach(function (record) { families[record.f] = (families[record.f] || 0) + 1; });
        if (familyHost) {
          familyHost.innerHTML = Object.keys(families)
            .sort(function (a, b) { return families[b] - families[a] || a.localeCompare(b); })
            .slice(0, 8)
            .map(function (family) {
              return '<button type="button" class="finder-chip finder-chip--family" data-filter="family:' +
                escapeHtml(family) + '">' + escapeHtml(family) + ' <span>' + families[family] + '</span></button>';
            })
            .join('');
        }
        input.placeholder = input.placeholder.replace(/^Search models/, 'Search ' + data.length + ' models');
        render();
      })
      .catch(function () {
        el.classList.add('model-finder--offline');
        results.hidden = false;
        results.innerHTML = '<div class="finder-empty">Model search is unavailable right now. <a href="' +
          escapeHtml(root + 'models/') + '">Browse all models</a> instead.</div>';
      });
  }

  function mountMatrixFilter(input) {
    if (input.dataset.mounted) return;
    input.dataset.mounted = 'true';
    const scope = input.closest('.md-content') || document;
    const rows = Array.prototype.slice.call(scope.querySelectorAll('.matrix-table tbody tr'));
    const counter = scope.querySelector('[data-matrix-count]');
    input.addEventListener('input', function () {
      const query = normalize(input.value);
      let visible = 0;
      rows.forEach(function (row) {
        const show = !query || normalize(row.dataset.region || row.textContent).indexOf(query) >= 0;
        row.hidden = !show;
        if (show) visible++;
      });
      if (counter) counter.textContent = query ? visible + ' of ' + rows.length + ' regions' : rows.length + ' regions';
    });
  }

  function mountAll() {
    document.querySelectorAll('[data-model-finder]').forEach(mountFinder);
    document.querySelectorAll('[data-matrix-filter]').forEach(mountMatrixFilter);
  }

  document.addEventListener('keydown', function (event) {
    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') {
      const input = document.querySelector('[data-model-finder] .model-finder__input');
      if (input) {
        event.preventDefault();
        event.stopPropagation();
        input.focus();
        input.select();
      }
    }
  }, true);

  if (typeof window.document$ !== 'undefined' && window.document$.subscribe) {
    window.document$.subscribe(mountAll);
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mountAll);
  } else {
    mountAll();
  }
})();
