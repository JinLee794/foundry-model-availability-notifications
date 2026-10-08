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
        .then(function (payload) {
          const records = Array.isArray(payload) ? payload : payload.models || [];
          records.forEach(function (record) { record._key = normalize(record.n); });
          if (!Array.isArray(payload)) payload.models = records;
          return Array.isArray(payload) ? { models: records } : payload;
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
      ? '<span class="lc-badge lc-badge--' + escapeHtml(record.lt) + '" data-tip-title="' + escapeHtml(record.ll) +
        '" data-tip="' + escapeHtml(record.tip || '') + '">' + escapeHtml(record.lb || record.ll) + '</span>'
      : '';
    return (
      '<a class="finder-result' + (active ? ' is-active' : '') + '" role="option" href="' +
      escapeHtml(root + 'models/' + record.s + '/') + '">' +
      '<span class="finder-result__main">' + providerLogo(record.f) + '<strong>' + escapeHtml(record.n) + '</strong>' +
      '<small>' + escapeHtml(record.f) + '</small></span>' +
      '<span class="finder-result__meta">' + meta + '</span>' +
      '<span class="finder-result__tags">' + badge + categories + '</span>' +
      '</a>'
    );
  }

  function providerLogo(family, size) {
    const slug = String(family || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    return '<span class="pv pv--' + slug + (size ? ' pv--' + size : '') + '" aria-hidden="true" title="' + String(family || '').replace(/"/g, '&quot;') + '"></span>';
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
      .then(function (payload) {
        const data = payload.models;
        records = data;
        const families = {};
        data.forEach(function (record) { families[record.f] = (families[record.f] || 0) + 1; });
        if (familyHost) {
          familyHost.innerHTML = Object.keys(families)
            .sort(function (a, b) { return families[b] - families[a] || a.localeCompare(b); })
            .slice(0, 8)
            .map(function (family) {
              return '<button type="button" class="finder-chip finder-chip--family" data-filter="family:' +
                escapeHtml(family) + '">' + providerLogo(family, 'xs') + escapeHtml(family) + ' <span>' + families[family] + '</span></button>';
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

  /* Floating tooltip for any element with data-tip / data-tip-title. */
  const tip = (function () {
    let el = null;
    let owner = null;
    function ensure() {
      if (!el) {
        el = document.createElement('div');
        el.className = 'fm-tip';
        el.setAttribute('role', 'tooltip');
        el.hidden = true;
        document.body.appendChild(el);
      }
      return el;
    }
    function show(target, title, body) {
      const node = ensure();
      owner = target;
      node.innerHTML = (title ? '<strong>' + escapeHtml(title) + '</strong>' : '') +
        (body ? '<span>' + escapeHtml(body) + '</span>' : '');
      node.hidden = false;
      const rect = target.getBoundingClientRect();
      const box = node.getBoundingClientRect();
      const margin = 8;
      let left = rect.left + rect.width / 2 - box.width / 2;
      left = Math.max(margin, Math.min(left, window.innerWidth - box.width - margin));
      let top = rect.top - box.height - margin;
      node.classList.toggle('fm-tip--below', top < margin);
      if (top < margin) top = rect.bottom + margin;
      node.style.left = left + 'px';
      node.style.top = top + 'px';
    }
    function hide(target) {
      if (!el || (target && target !== owner)) return;
      el.hidden = true;
      owner = null;
    }
    function fromEvent(event) {
      const target = event.target.closest && event.target.closest('[data-tip], [data-tip-title]');
      if (target) show(target, target.getAttribute('data-tip-title'), target.getAttribute('data-tip'));
      return target;
    }
    document.addEventListener('pointerover', function (event) {
      if (event.pointerType === 'touch') return;
      fromEvent(event);
    });
    document.addEventListener('pointerout', function (event) {
      const target = event.target.closest && event.target.closest('[data-tip], [data-tip-title]');
      if (target && !target.contains(event.relatedTarget)) hide(target);
    });
    document.addEventListener('focusin', fromEvent);
    document.addEventListener('focusout', function (event) { hide(event.target); });
    document.addEventListener('click', function (event) {
      if (!fromEvent(event)) hide();
    });
    window.addEventListener('scroll', function () { hide(); }, true);
    return { show: show, hide: hide };
  })();
  window.FMTip = tip;

  /* PTU quick estimate (same formula as Microsoft's PTU sizing guide). */
  function mountPtuCalc(el) {
    if (el.dataset.mounted) return;
    el.dataset.mounted = 'true';
    let models = [];
    try { models = JSON.parse(el.dataset.models || '[]'); } catch (e) { return; }
    const field = function (name) { return el.querySelector('[data-calc="' + name + '"]'); };
    const out = function (name) { return el.querySelector('[data-calc-out="' + name + '"]'); };
    const fmt = function (n) { return Math.round(n).toLocaleString(); };
    function update() {
      const model = models.filter(function (m) { return m.m === field('model').value; })[0];
      if (!model) return;
      const regional = field('type').value === 'r';
      const min = regional ? model.rmin : model.gmin;
      const inc = regional ? model.rinc : model.ginc;
      const rpm = Math.max(+field('rpm').value || 0, 0);
      const prompt = Math.max(+field('prompt').value || 0, 0);
      const response = Math.max(+field('response').value || 0, 0);
      const cache = Math.min(Math.max(+field('cache').value || 0, 0), 100) / 100;
      const inputTpm = rpm * prompt;
      const outputTpm = rpm * response;
      const normalized = inputTpm * (1 - cache) + model.ratio * outputTpm;
      const raw = normalized / model.tpm;
      const ptu = raw <= 0 ? 0 : Math.max(min, Math.ceil(raw / inc) * inc);
      out('ptu').textContent = ptu ? fmt(ptu) : '0';
      out('detail').innerHTML =
        '<span>Normalized TPM <b>' + fmt(normalized) + '</b></span>' +
        '<span>Raw estimate <b>' + raw.toFixed(1) + ' PTU</b></span>' +
        '<span>Minimum <b>' + min + '</b> · step <b>' + inc + '</b></span>' +
        '<span>' + fmt(model.tpm) + ' input TPM per PTU · output counts ×' + model.ratio + '</span>';
    }
    el.addEventListener('input', update);
    el.addEventListener('change', update);
    update();
  }

  function mountAll() {
    document.querySelectorAll('[data-model-finder]').forEach(mountFinder);
    document.querySelectorAll('[data-matrix-filter]').forEach(mountMatrixFilter);
    document.querySelectorAll('[data-ptu-calc]').forEach(mountPtuCalc);
    tip.hide();
  }
  window.FMLoadData = loadData;

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

  function setHotRegion(target, on) {
    const el = target && target.closest ? target.closest('[data-wmap] [data-region]') : null;
    if (!el) return;
    const wrap = el.closest('[data-wmap]');
    const key = el.getAttribute('data-region');
    wrap.querySelectorAll('[data-region]').forEach(function (node) {
      node.classList.toggle('is-hot', on && node.getAttribute('data-region') === key);
    });
  }
  document.addEventListener('mouseover', function (e) { setHotRegion(e.target, true); });
  document.addEventListener('mouseout', function (e) { setHotRegion(e.target, false); });
  document.addEventListener('focusin', function (e) { setHotRegion(e.target, true); });
  document.addEventListener('focusout', function (e) { setHotRegion(e.target, false); });

  if (typeof window.document$ !== 'undefined' && window.document$.subscribe) {
    window.document$.subscribe(mountAll);
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mountAll);
  } else {
    mountAll();
  }
})();
