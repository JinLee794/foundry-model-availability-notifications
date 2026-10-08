/* Availability explorer: every model × region × deployment type in one filterable grid. */
(function () {
  'use strict';

  const STAGE_GROUPS = {
    risk: ['soon', 'retiring', 'pending'],
    deprecated: ['deprecated'],
    preview: ['preview'],
    ga: ['ga'],
    untracked: ['untracked'],
    retired: ['retired'],
  };
  const GROUP_ORDER = ['paygo', 'ptu', 'batch', 'partner', 'other'];

  function providerLogo(family) {
    const slug = String(family || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    return '<span class="pv pv--' + slug + '" aria-hidden="true" title="' + String(family || '').replace(/"/g, '&quot;') + '"></span>';
  }

  function esc(value) {
    return String(value == null ? '' : value)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  function norm(value) {
    return String(value || '').toLowerCase().replace(/[^a-z0-9]/g, '');
  }

  function subsequence(needle, hay) {
    let i = 0;
    for (let j = 0; j < hay.length && i < needle.length; j++) if (hay[j] === needle[i]) i++;
    return i === needle.length;
  }

  function readHash() {
    const state = {};
    location.hash.replace(/^#/, '').split('&').forEach(function (part) {
      if (!part) return;
      const pair = part.split('=');
      state[decodeURIComponent(pair[0])] = decodeURIComponent((pair[1] || '').replace(/\+/g, ' '));
    });
    return state;
  }

  function mount(root) {
    if (root.dataset.mounted) return;
    root.dataset.mounted = 'true';

    const grid = root.querySelector('[data-ax-grid]');
    const summary = root.querySelector('[data-ax-summary]');
    const requiredHost = root.querySelector('[data-ax-required]');
    const control = function (name) { return root.querySelector('[data-ax="' + name + '"]'); };
    const siteRoot = root.dataset.root || '';
    const load = window.FMLoadData || function (src) { return fetch(src).then(function (r) { return r.json(); }); };

    let data = null;
    let typeByKey = {};
    let allMask = 0;
    let groupBits = {};
    let view = { rows: [], cols: [] };
    const state = { q: '', p: '', lc: '', g: '', s: 'name', t: '', rg: [], he: true, x: false };

    function applyHash() {
      const h = readHash();
      state.q = h.q || '';
      state.p = h.p || '';
      state.lc = h.lc || '';
      state.g = h.g || '';
      state.s = h.s || 'name';
      state.t = typeByKey[h.t] ? h.t : '';
      state.rg = (h.rg ? h.rg.split(',') : []).filter(function (name) {
        return data.regions.some(function (region) { return region.n === name; });
      });
      state.he = h.he !== '0';
      setExpanded(h.x === '1', true);
      control('q').value = state.q;
      control('p').value = state.p;
      control('lc').value = state.lc;
      control('g').value = state.g;
      control('s').value = state.s;
      control('he').checked = state.he;
    }

    function writeHash() {
      const parts = [];
      ['q', 'p', 'lc', 'g', 't'].forEach(function (key) {
        if (state[key]) parts.push(key + '=' + encodeURIComponent(state[key]));
      });
      if (state.s !== 'name') parts.push('s=' + state.s);
      if (state.rg.length) parts.push('rg=' + state.rg.map(encodeURIComponent).join(','));
      if (!state.he) parts.push('he=0');
      if (state.x) parts.push('x=1');
      const hash = parts.length ? '#' + parts.join('&') : '';
      if (hash !== location.hash) history.replaceState(null, '', location.pathname + location.search + hash);
    }

    function setExpanded(on, quiet) {
      state.x = !!on;
      root.classList.toggle('is-expanded', state.x);
      document.documentElement.classList.toggle('ax-lock', state.x);
      const btn = root.querySelector('[data-ax-action="expand"]');
      if (btn) {
        btn.setAttribute('aria-pressed', state.x ? 'true' : 'false');
        btn.querySelector('span').textContent = state.x ? 'Exit full view' : 'Expand table';
      }
      if (window.FMTip) window.FMTip.hide();
      if (!quiet) writeHash();
    }

    function typeNames(bits) {
      return data.types.filter(function (type) { return bits & type.bit; }).map(function (type) { return type.label; });
    }

    function cellHtml(bits, col) {
      if (!bits) return '<td class="ax-c ax-c--empty" data-col="' + col + '"></td>';
      let dots = '';
      GROUP_ORDER.forEach(function (group) {
        if (bits & groupBits[group]) dots += '<i class="ax-dot ax-dot--' + group + '"></i>';
      });
      return '<td class="ax-c" data-col="' + col + '"><span class="ax-cell">' + dots + '</span></td>';
    }

    function compute() {
      const mask = state.t ? typeByKey[state.t].bit : allMask;
      const query = norm(state.q);
      const stages = state.lc ? STAGE_GROUPS[state.lc] || [state.lc] : null;
      const regionIndex = {};
      data.regions.forEach(function (region, i) { regionIndex[region.n] = i; });
      const required = state.rg.map(function (name) { return regionIndex[name]; });
      const geoCols = [];
      data.regions.forEach(function (region, i) {
        if (!state.g || region.g === state.g) geoCols.push(i);
      });

      const rows = data.models.filter(function (m) {
        if (state.p && m.f !== state.p) return false;
        if (stages && stages.indexOf(m.lk) < 0) return false;
        if (query) {
          const key = m._key || (m._key = norm(m.n));
          if (key.indexOf(query) < 0 && norm(m.f).indexOf(query) !== 0 && !(query.length >= 3 && subsequence(query, key))) return false;
        }
        if (required.length) {
          if (!required.every(function (i) { return m.a[i] & mask; })) return false;
        }
        return geoCols.some(function (i) { return m.a[i] & mask; });
      });

      rows.forEach(function (m) {
        m._hits = geoCols.reduce(function (n, i) { return n + (m.a[i] & mask ? 1 : 0); }, 0);
      });
      rows.sort(function (a, b) {
        if (state.s === 'coverage') return b._hits - a._hits || a.n.localeCompare(b.n);
        if (state.s === 'retire') {
          const da = a.dd == null ? 1e9 : a.dd;
          const db = b.dd == null ? 1e9 : b.dd;
          return da - db || a.n.localeCompare(b.n);
        }
        return a.n.localeCompare(b.n, undefined, { sensitivity: 'base' });
      });

      const cols = geoCols.filter(function (i) {
        if (!state.he || required.indexOf(i) >= 0) return true;
        return rows.some(function (m) { return m.a[i] & mask; });
      });
      return { rows: rows, cols: cols, mask: mask, required: required };
    }

    function render() {
      view = compute();
      const rows = view.rows;
      const cols = view.cols;
      const mask = view.mask;

      // Geography group header
      let geoRow = '<tr class="ax-geo"><th class="ax-sticky" colspan="3"></th>';
      let run = null;
      let span = 0;
      cols.forEach(function (i, k) {
        const geo = data.regions[i].g;
        if (geo !== run) {
          if (run !== null) geoRow += '<th colspan="' + span + '"><span>' + esc(run) + '</span></th>';
          run = geo;
          span = 0;
        }
        span++;
        if (k === cols.length - 1) geoRow += '<th colspan="' + span + '"><span>' + esc(run) + '</span></th>';
      });
      geoRow += '</tr>';

      let head = '<tr><th class="ax-sticky ax-h-model" scope="col">Model</th>' +
        '<th class="ax-h-lc" scope="col">Lifecycle</th><th class="ax-h-n" scope="col" title="Regions matching the current filters">Regions</th>';
      cols.forEach(function (i) {
        const required = view.required.indexOf(i) >= 0;
        head += '<th class="ax-h-region' + (required ? ' is-required' : '') + '" scope="col" data-col="' + i +
          '" tabindex="0" data-tip-title="' + esc(data.regions[i].n) + '" data-tip="' +
          (required ? 'Required — click to remove.' : 'Click to show only models available here.') + '"><span>' +
          esc(data.regions[i].n) + '</span></th>';
      });
      head += '</tr>';

      let body = '';
      rows.forEach(function (m, r) {
        const badge = '<span class="lc-badge lc-badge--' + esc(m.lt) + '" data-tip-title="' + esc(m.ll) +
          '" data-tip="' + esc(m.tip || '') + '">' + esc(m.lb || m.ll) + '</span>';
        body += '<tr data-row="' + r + '"><th class="ax-sticky ax-model" scope="row"><div class="ax-model__id">' +
          providerLogo(m.f) + '<a href="' + esc(siteRoot + 'models/' + m.s + '/') + '">' + esc(m.n) + '</a><small>' +
          esc(m.f) + '</small></div></th>' +
          '<td class="ax-lc">' + badge + '</td><td class="ax-n">' + m._hits + '</td>';
        cols.forEach(function (i) { body += cellHtml(m.a[i] & mask, i); });
        body += '</tr>';
      });
      if (!rows.length) {
        body = '<tr><td class="ax-empty" colspan="' + (cols.length + 3) + '">No models match these filters. ' +
          '<button type="button" class="ax-btn" data-ax-action="reset">Reset filters</button></td></tr>';
      }
      grid.innerHTML = '<thead>' + geoRow + head + '</thead><tbody>' + body + '</tbody>';

      const typeLabel = state.t ? ' offering <strong>' + esc(typeByKey[state.t].label) + '</strong>' : '';
      summary.innerHTML = '<strong>' + rows.length + '</strong> of ' + data.models.length + ' models' + typeLabel +
        ' across <strong>' + cols.length + '</strong> regions';

      requiredHost.hidden = !state.rg.length;
      requiredHost.innerHTML = state.rg.length
        ? '<span>Must be in:</span>' + state.rg.map(function (name) {
          return '<button type="button" class="ax-req" data-remove-region="' + esc(name) + '">' + esc(name) + ' <b aria-label="remove">×</b></button>';
        }).join('')
        : '';

      root.querySelectorAll('.ax-types .ax-chip').forEach(function (chip) {
        chip.classList.toggle('is-active', chip.dataset.type === state.t);
      });
      writeHash();
    }

    function toggleRegion(name) {
      const idx = state.rg.indexOf(name);
      if (idx >= 0) state.rg.splice(idx, 1);
      else state.rg.push(name);
      render();
    }

    function reset() {
      Object.assign(state, { q: '', p: '', lc: '', g: '', s: 'name', t: '', rg: [], he: true });
      control('q').value = '';
      control('p').value = '';
      control('lc').value = '';
      control('g').value = '';
      control('s').value = 'name';
      control('he').checked = true;
      render();
    }

    function downloadCsv() {
      const quote = function (value) { return '"' + String(value).replace(/"/g, '""') + '"'; };
      const lines = [['Model', 'Provider', 'Lifecycle'].concat(view.cols.map(function (i) { return data.regions[i].n; })).map(quote).join(',')];
      view.rows.forEach(function (m) {
        lines.push([m.n, m.f, m.lb || m.ll].concat(view.cols.map(function (i) {
          return typeNames(m.a[i] & view.mask).join('; ');
        })).map(quote).join(','));
      });
      const blob = new Blob([lines.join('\r\n')], { type: 'text/csv' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = 'foundry-model-availability.csv';
      document.body.appendChild(link);
      link.click();
      setTimeout(function () { URL.revokeObjectURL(link.href); link.remove(); }, 0);
    }

    root.addEventListener('input', function (event) {
      const name = event.target.dataset.ax;
      if (!name) return;
      state[name] = name === 'he' ? event.target.checked : event.target.value;
      render();
    });
    root.addEventListener('change', function (event) {
      const name = event.target.dataset.ax;
      if (name === 'he') { state.he = event.target.checked; render(); }
    });
    root.addEventListener('click', function (event) {
      const chip = event.target.closest('.ax-types .ax-chip');
      if (chip) { state.t = chip.dataset.type === state.t ? '' : chip.dataset.type; render(); return; }
      const header = event.target.closest('.ax-h-region');
      if (header) { toggleRegion(data.regions[+header.dataset.col].n); return; }
      const remove = event.target.closest('[data-remove-region]');
      if (remove) { toggleRegion(remove.dataset.removeRegion); return; }
      const action = event.target.closest('[data-ax-action]');
      if (action) {
        if (action.dataset.axAction === 'reset') reset();
        if (action.dataset.axAction === 'csv') downloadCsv();
        if (action.dataset.axAction === 'expand') setExpanded(!state.x);
        return;
      }
      const cell = event.target.closest('td.ax-c:not(.ax-c--empty)');
      if (cell) {
        const link = cell.parentElement.querySelector('.ax-model a');
        if (link) link.click();
      }
    });
    root.addEventListener('keydown', function (event) {
      const header = event.target.closest && event.target.closest('.ax-h-region');
      if (header && (event.key === 'Enter' || event.key === ' ')) {
        event.preventDefault();
        toggleRegion(data.regions[+header.dataset.col].n);
      }
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && state.x && root.isConnected) setExpanded(false);
    });

    // Cell tooltips are computed on demand to keep the DOM light.
    grid.addEventListener('pointerover', function (event) {
      const cell = event.target.closest('td.ax-c');
      if (!cell || !window.FMTip) return;
      const row = view.rows[+cell.parentElement.dataset.row];
      const col = +cell.dataset.col;
      if (!row) return;
      const names = typeNames(row.a[col]);
      window.FMTip.show(cell, row.n + ' · ' + data.regions[col].n,
        names.length ? names.join(' · ') : 'Not available in this region.');
    });
    grid.addEventListener('pointerout', function (event) {
      const cell = event.target.closest('td.ax-c');
      if (cell && window.FMTip && !cell.contains(event.relatedTarget)) window.FMTip.hide(cell);
    });

    window.addEventListener('hashchange', function () {
      if (!data) return;
      applyHash();
      render();
    });

    load(root.dataset.src)
      .then(function (payload) {
        data = payload;
        data.types.forEach(function (type) {
          typeByKey[type.k] = type;
          allMask |= type.bit;
          groupBits[type.group] = (groupBits[type.group] || 0) | type.bit;
        });
        const families = {};
        data.models.forEach(function (m) { families[m.f] = (families[m.f] || 0) + 1; });
        control('p').insertAdjacentHTML('beforeend', Object.keys(families)
          .sort(function (a, b) { return families[b] - families[a] || a.localeCompare(b); })
          .map(function (f) { return '<option value="' + esc(f) + '">' + esc(f) + ' (' + families[f] + ')</option>'; })
          .join(''));
        applyHash();
        render();
      })
      .catch(function () {
        summary.textContent = 'The explorer could not load its data. Try reloading, or browse the model table instead.';
      });
  }

  function mountAll() {
    if (!document.querySelector('.ax.is-expanded')) document.documentElement.classList.remove('ax-lock');
    document.querySelectorAll('[data-explorer]').forEach(mount);
  }

  if (typeof window.document$ !== 'undefined' && window.document$.subscribe) {
    window.document$.subscribe(mountAll);
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mountAll);
  } else {
    mountAll();
  }
})();
