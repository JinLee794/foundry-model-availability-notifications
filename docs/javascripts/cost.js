/* Cost planner: projects monthly pay-as-you-go spend across models and compares it with PTU. */
(function () {
  'use strict';

  var DEPS = { global: 'Global', datazone: 'Data Zone', regional: 'Regional' };
  var POPULAR = ['gpt-5', 'gpt-5-mini', 'gpt-4-1', 'gpt-4-1-mini', 'gpt-4o', 'o4-mini', 'deepseek-v3-2', 'grok-4-1-fast-reasoning', 'mistral-large-3', 'llama-3-3-70b-instruct'];
  var ALERT = { soon: 1, retiring: 1, deprecated: 1, retired: 1 };
  var MAX_MODELS = 20;
  var MEDIA_TABS = { image: 1, audio: 1, video: 1, docs: 1 };
  var DEFAULTS = { rpd: 3000, in: 1500, out: 400, cache: 30, batch: 0, dep: 'global', peak: 2 };

  function esc(value) {
    return String(value == null ? '' : value)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }
  function providerLogo(family) {
    var slug = String(family || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    return '<span class="pv pv--' + slug + '" aria-hidden="true" title="' + esc(family) + '"></span>';
  }
  function money(v) {
    if (v == null || isNaN(v)) return '—';
    if (v === 0) return '$0';
    if (v < 0.01) return '<$0.01';
    if (v >= 100) return '$' + Math.round(v).toLocaleString('en-US');
    return '$' + v.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }
  function unitPrice(v) {
    if (v == null) return '—';
    if (v >= 1) return '$' + v.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    var s = v.toFixed(4).replace(/0+$/, '');
    if (s.split('.')[1].length < 2) s = v.toFixed(2);
    return '$' + s;
  }
  function compact(v, cur) {
    var p = cur ? '$' : '';
    var a = Math.abs(v);
    if (a >= 1e9) return p + (v / 1e9).toFixed(a >= 1e10 ? 0 : 1).replace(/\.0$/, '') + 'B';
    if (a >= 1e6) return p + (v / 1e6).toFixed(a >= 1e7 ? 0 : 1).replace(/\.0$/, '') + 'M';
    if (a >= 1e3) return p + (v / 1e3).toFixed(a >= 1e4 ? 0 : 1).replace(/\.0$/, '') + 'K';
    return p + (cur && a < 10 && a > 0 ? v.toFixed(2) : Math.round(v));
  }
  function niceCeil(v) {
    if (v <= 0) return 1;
    var e = Math.pow(10, Math.floor(Math.log10(v)));
    var steps = [1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10];
    for (var i = 0; i < steps.length; i++) if (steps[i] * e >= v) return steps[i] * e;
    return 10 * e;
  }
  function num(v, fallback) {
    var n = parseFloat(v);
    return isFinite(n) && n >= 0 ? n : fallback;
  }

  function mount(root) {
    if (root.dataset.mounted) return;
    root.dataset.mounted = 'true';
    var load = window.FMLoadData || function (src) { return fetch(src).then(function (r) { return r.json(); }); };
    load(root.getAttribute('data-src')).then(function (data) { init(root, data); }).catch(function () {
      root.querySelector('[data-cp-bars]').innerHTML = '<p class="cp-empty">Price data could not be loaded.</p>';
    });
  }

  function init(root, data) {
    var siteRoot = root.getAttribute('data-root') || '../';
    var bySlug = {};
    data.models.forEach(function (m) { bySlug[m.s] = m; });
    var hours = data.hours || 730;
    var ptuPrices = data.ptu || {};

    var q = new URLSearchParams(window.location.search);
    var state = {
      rpd: num(q.get('rpd'), DEFAULTS.rpd),
      in: num(q.get('in'), DEFAULTS.in),
      out: num(q.get('out'), DEFAULTS.out),
      cache: Math.min(90, num(q.get('c'), DEFAULTS.cache)),
      batch: Math.min(100, num(q.get('b'), DEFAULTS.batch)),
      dep: DEPS[q.get('d')] ? q.get('d') : DEFAULTS.dep,
      peak: num(q.get('pk'), DEFAULTS.peak) || DEFAULTS.peak,
      models: [],
      ptuModel: q.get('p') || '',
    };
    var initial = (q.get('m') || '').split(',').filter(function (s) { return bySlug[s]; });
    state.models = initial.length ? initial : modelSet('popular');
    var stashedModels = null;
    function isEmbed(s) { return !!bySlug[s] && /embed/i.test(bySlug[s].n); }

    var $ = function (sel) { return root.querySelector(sel); };
    var fields = {};
    root.querySelectorAll('[data-cp]').forEach(function (el) { fields[el.getAttribute('data-cp')] = el; });
    var selectedEl = $('[data-cp-selected]');
    var searchEl = $('[data-cp-search]');
    var suggestEl = $('[data-cp-suggest]');
    var ptuSelect = $('[data-cp-ptu-model]');

    function tierFor(m) {
      if (m.p[state.dep] && m.p[state.dep].in != null) return { t: m.p[state.dep], dep: state.dep, fallback: false };
      var keys = ['global', 'datazone', 'regional'];
      for (var i = 0; i < keys.length; i++) {
        if (m.p[keys[i]] && m.p[keys[i]].in != null) return { t: m.p[keys[i]], dep: keys[i], fallback: true };
      }
      return { t: {}, dep: state.dep, fallback: true };
    }
    function blended(t) {
      if (t.in == null) return null;
      return t.out == null ? t.in : (3 * t.in + t.out) / 4;
    }

    function costFor(m, rpd, batchShare) {
      var tier = tierFor(m);
      var t = tier.t;
      var reqs = rpd * hours / 24;
      var inM = reqs * state.in / 1e6;
      var outM = reqs * state.out / 1e6;
      var c = state.cache / 100;
      var b = batchShare == null ? state.batch / 100 : batchShare;
      var pIn = t.in || 0;
      var pCached = t.cached != null ? t.cached : pIn;
      var pBatchIn = t.batch_in != null ? t.batch_in : pIn;
      var pOut = t.out || 0;
      var pBatchOut = t.batch_out != null ? t.batch_out : pOut;
      var input = (1 - b) * inM * (1 - c) * pIn + b * inM * pBatchIn;
      var cached = (1 - b) * inM * c * pCached;
      var output = (1 - b) * outM * pOut + b * outM * pBatchOut;
      return {
        input: input, cached: cached, output: output, total: input + cached + output,
        dep: tier.dep, fallback: tier.fallback, noOut: t.out == null && state.out > 0,
        noBatch: b > 0 && t.batch_in == null, t: t,
      };
    }

    function modelSet(name) {
      var deps = state ? state.dep : DEFAULTS.dep;
      if (name === 'popular') {
        var picks = POPULAR.filter(function (s) { return bySlug[s]; });
        return picks.length ? picks : data.models.slice(0, 8).map(function (m) { return m.s; });
      }
      if (name === 'retiring') {
        var out = [];
        data.models.forEach(function (m) {
          if (ALERT[m.lk] && m.lk !== 'retired' && m.rs && out.length < MAX_MODELS - 1) {
            if (out.indexOf(m.s) < 0) out.push(m.s);
            if (out.indexOf(m.rs) < 0) out.push(m.rs);
          }
        });
        return out;
      }
      if (name === 'budget') {
        return data.models
          .map(function (m) { var t = m.p[deps] || m.p.global || {}; return { s: m.s, b: blended(t), lk: m.lk }; })
          .filter(function (x) { return x.b != null && x.b < 1 && x.lk !== 'retired'; })
          .sort(function (a, b) { return a.b - b.b; })
          .slice(0, 12).map(function (x) { return x.s; });
      }
      if (name === 'partner') {
        // Round-robin across providers so no single family fills the set; the last name
        // alphabetically is usually the newest version.
        var pool = data.models.filter(function (m) {
          var t = m.p.global || m.p.datazone || m.p.regional || {};
          return m.f !== 'OpenAI' && m.lk !== 'retired' && !ALERT[m.lk] && t.in != null && t.out != null;
        });
        var byFam = {};
        pool.forEach(function (m) { (byFam[m.f] = byFam[m.f] || []).push(m.s); });
        var picks2 = [], round = 0, added = true;
        while (picks2.length < 12 && added) {
          added = false;
          Object.keys(byFam).forEach(function (f) {
            var list = byFam[f];
            var s = list[list.length - 1 - round];
            if (s && picks2.length < 12) { picks2.push(s); added = true; }
          });
          round++;
        }
        return picks2;
      }
      return [];
    }

    function syncUrl() {
      var p = new URLSearchParams();
      p.set('m', state.models.join(','));
      p.set('rpd', state.rpd); p.set('in', state.in); p.set('out', state.out);
      p.set('c', state.cache); p.set('b', state.batch); p.set('d', state.dep);
      if (state.peak !== DEFAULTS.peak) p.set('pk', state.peak);
      if (state.ptuModel) p.set('p', state.ptuModel);
      if (media && media.touched) {
        p.set('media', media.tab);
        if (media.hl) p.set('hl', media.hl);
      }
      try { window.history.replaceState(window.history.state, '', window.location.pathname + '?' + p.toString() + window.location.hash); } catch (e) { /* file:// */ }
    }

    function syncInputs() {
      ['rpd', 'in', 'out', 'cache', 'batch'].forEach(function (k) {
        if (fields[k] && document.activeElement !== fields[k]) fields[k].value = state[k];
      });
      if (fields.peak) fields.peak.value = String(state.peak);
      root.querySelector('[data-cp-out="cache"]').textContent = state.cache + '%';
      root.querySelector('[data-cp-out="batch"]').textContent = state.batch + '%';
      root.querySelectorAll('[data-dep]').forEach(function (b) {
        var on = b.getAttribute('data-dep') === state.dep;
        b.classList.toggle('is-active', on);
        b.setAttribute('aria-checked', on ? 'true' : 'false');
      });
      root.querySelectorAll('[data-workload]').forEach(function (b) {
        var on = +b.dataset.rpd === state.rpd && +b.dataset.in === state.in && +b.dataset.out === state.out &&
          +b.dataset.cache === state.cache && +b.dataset.batch === state.batch;
        b.classList.toggle('is-active', on);
      });
    }

    function badge(m) {
      if (!ALERT[m.lk]) return '';
      return '<span class="lc-badge lc-badge--' + esc(m.lt) + '">' + esc(m.ll) + '</span>';
    }

    function renderSelected() {
      selectedEl.innerHTML = state.models.map(function (s) {
        var m = bySlug[s];
        return '<span class="cp-pick">' + providerLogo(m.f) + esc(m.n) +
          '<button type="button" data-remove="' + esc(s) + '" aria-label="Remove ' + esc(m.n) + '">×</button></span>';
      }).join('') || '<span class="cp-hint">Pick a set above or search to add models.</span>';
      searchEl.disabled = state.models.length >= MAX_MODELS;
      searchEl.placeholder = state.models.length >= MAX_MODELS ? 'Up to ' + MAX_MODELS + ' models' : 'Add a model — ' + data.models.length + ' priced';
    }

    function renderKpis(rows) {
      var kp = $('[data-cp-kpis]');
      var reqs = state.rpd * hours / 24;
      var tokIn = reqs * state.in, tokOut = reqs * state.out;
      var priced = rows.filter(function (r) { return r.c.total > 0; });
      var cheap = priced[0], dear = priced[priced.length - 1];
      var spread = cheap && dear && cheap.c.total > 0 ? dear.c.total / cheap.c.total : null;
      kp.innerHTML = [
        ['Monthly volume', compact(reqs) + ' requests', compact(tokIn) + ' in · ' + compact(tokOut) + ' out tokens'],
        ['Lowest', cheap ? money(cheap.c.total) : '—', cheap ? esc(cheap.m.n) + ' / month' : 'Add models to compare'],
        ['Highest', dear ? money(dear.c.total) : '—', dear ? esc(dear.m.n) + ' / month' : ''],
        ['Spread', spread ? (spread >= 10 ? Math.round(spread) : spread.toFixed(1)) + '×' : '—', spread ? 'between highest and lowest' : ''],
      ].map(function (k) {
        return '<div class="cp-kpi"><span>' + k[0] + '</span><strong>' + k[1] + '</strong><small>' + k[2] + '</small></div>';
      }).join('');
    }

    function renderBars(rows) {
      var el = $('[data-cp-bars]');
      $('[data-cp-basis]').textContent = 'List price · ' + DEPS[state.dep] + ' deployment · ' + data.region + ' · USD per month';
      if (!rows.length) { el.innerHTML = '<p class="cp-empty">No models selected.</p>'; return; }
      var max = Math.max.apply(null, rows.map(function (r) { return r.c.total; })) || 1;
      el.innerHTML = rows.map(function (r) {
        var c = r.c, m = r.m;
        var w = function (v) { return (v / max * 100).toFixed(2) + '%'; };
        var notes = [];
        if (c.fallback) notes.push('<span class="cp-note"' + tip('Deployment type', 'No ' + DEPS[state.dep] + ' price is published, so this uses the ' + DEPS[c.dep] + ' price.') + '>' + DEPS[c.dep] + ' price</span>');
        if (c.noOut) notes.push('<span class="cp-note"' + tip('Input only', 'This model has no output-token price (e.g. embeddings), so output tokens are free.') + '>input only</span>');
        if (c.noBatch) notes.push('<span class="cp-note"' + tip('No batch price', 'No Global Batch price is published, so batch traffic uses the standard price.') + '>no batch rate</span>');
        if (m.src === 'mp') notes.push('<span class="cp-note"' + tip('Azure Marketplace', 'Billed through Azure Marketplace. The price comes from the Marketplace catalog; deployment types are not priced separately.') + '>Marketplace</span>');
        var rep = m.rs && ALERT[m.lk] ? '<a class="cp-rep" href="#" data-add="' + esc(m.rs) + '"' + tip('Replacement', 'Add ' + m.rep + ' to compare the cost of switching.') + '>→ ' + esc(m.rep) + '</a>' : '';
        var perK = state.rpd > 0 ? money(c.total / (state.rpd * hours / 24) * 1000) + ' per 1K requests' : '';
        var segTip = 'Input ' + money(c.input) + ' · Cached ' + money(c.cached) + ' · Output ' + money(c.output);
        return '<div class="cp-bar">' +
          '<div class="cp-bar__label">' + providerLogo(m.f) +
          '<a href="' + esc(siteRoot + 'models/' + m.s + '/') + '">' + esc(m.n) + '</a>' + badge(m) + rep + notes.join('') + '</div>' +
          '<div class="cp-bar__track"' + tip(m.n + ' · ' + money(c.total) + '/month', segTip) + '>' +
          '<span class="cp-part cp-part--in" style="width:' + w(c.input) + '"></span>' +
          '<span class="cp-part cp-part--cached" style="width:' + w(c.cached) + '"></span>' +
          '<span class="cp-part cp-part--out" style="width:' + w(c.output) + '"></span></div>' +
          '<div class="cp-bar__value"><strong>' + money(c.total) + '</strong><small>' + perK + '</small></div>' +
          '</div>';
      }).join('');
    }

    function tip(title, body) {
      return ' tabindex="0" data-tip-title="' + esc(title) + '" data-tip="' + esc(body) + '"';
    }

    function renderTable(rows) {
      var t = $('[data-cp-table]');
      var head = '<thead><tr><th>Model</th><th>Input</th><th>Cached</th><th>Output</th><th>Batch in</th><th>Batch out</th><th>Blended</th><th>Monthly</th></tr></thead>';
      var body = rows.map(function (r) {
        var p = r.c.t;
        return '<tr><th scope="row">' + providerLogo(r.m.f) + '<a href="' + esc(siteRoot + 'models/' + r.m.s + '/') + '">' + esc(r.m.n) + '</a>' +
          (r.c.fallback ? ' <small>(' + DEPS[r.c.dep] + ')</small>' : '') + '</th>' +
          ['in', 'cached', 'out', 'batch_in', 'batch_out'].map(function (k) { return '<td>' + unitPrice(p[k]) + '</td>'; }).join('') +
          '<td>' + unitPrice(blended(p)) + '</td><td><strong>' + money(r.c.total) + '</strong></td></tr>';
      }).join('');
      t.innerHTML = head + '<tbody>' + (body || '<tr><td colspan="8">No models selected.</td></tr>') + '</tbody>';
    }

    function csv(rows) {
      var lines = [['Model', 'Deployment', 'Input/1M', 'Cached/1M', 'Output/1M', 'Batch in/1M', 'Batch out/1M', 'Monthly USD'].join(',')];
      rows.forEach(function (r) {
        var p = r.c.t;
        lines.push(['"' + r.m.n + '"', DEPS[r.c.dep], p.in, p.cached, p.out, p.batch_in, p.batch_out, r.c.total.toFixed(2)]
          .map(function (v) { return v == null ? '' : v; }).join(','));
      });
      lines.push('');
      lines.push('"Workload: ' + state.rpd + ' requests/day, ' + state.in + ' in / ' + state.out + ' out tokens, ' + state.cache + '% cached, ' + state.batch + '% batch. List price ' + data.region + ', ' + (data.fetched || '').slice(0, 10) + '"');
      var blob = new Blob([lines.join('\n')], { type: 'text/csv' });
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'foundry-cost-plan.csv';
      document.body.appendChild(a);
      a.click();
      setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 0);
    }

    // ----- PTU break-even -----
    function ptuCandidates() {
      return data.models.filter(function (m) { return m.ptu; });
    }
    function ptuDep() { return ptuPrices.hourly && ptuPrices.hourly[state.dep] != null ? state.dep : 'global'; }
    function ptusNeeded(m, rpd) {
      var s = m.ptu;
      var regional = ptuDep() === 'regional';
      var min = regional ? s[2] : s[0], inc = regional ? s[3] : s[1];
      var rpm = rpd / 1440 * state.peak;
      var tpm = rpm * state.in * (1 - state.cache / 100) + s[5] * rpm * state.out;
      var raw = Math.ceil(tpm / s[4]);
      if (raw <= min) return min;
      return min + Math.ceil((raw - min) / inc) * inc;
    }
    function ptuCosts(m, rpd) {
      var d = ptuDep();
      var n = ptusNeeded(m, rpd);
      var hourly = (ptuPrices.hourly || {})[d];
      var month = ((ptuPrices.reservation || {}).month || {})[d];
      var year = ((ptuPrices.reservation || {}).year || {})[d];
      return {
        n: n,
        hourly: hourly != null ? n * hourly * hours : null,
        month: month != null ? n * month : null,
        year: year != null ? n * year / 12 : null,
      };
    }

    function renderPtuSelect() {
      var cands = ptuCandidates();
      if (!state.ptuModel || !bySlug[state.ptuModel] || !bySlug[state.ptuModel].ptu) {
        var sel = state.models.filter(function (s) { return bySlug[s].ptu; })[0];
        state.ptuModel = sel || (bySlug['gpt-4-1'] && bySlug['gpt-4-1'].ptu ? 'gpt-4-1' : (cands[0] && cands[0].s));
      }
      ptuSelect.innerHTML = cands.map(function (m) {
        return '<option value="' + esc(m.s) + '"' + (m.s === state.ptuModel ? ' selected' : '') + '>' + esc(m.n) + '</option>';
      }).join('');
    }

    function renderPtu() {
      var chart = $('[data-cp-ptu-chart]');
      var verdict = $('[data-cp-ptu-verdict]');
      var m = bySlug[state.ptuModel];
      if (!m || !m.ptu || !ptuPrices.hourly) {
        chart.innerHTML = '';
        verdict.innerHTML = '<p class="cp-empty">No PTU sizing data for this model.</p>';
        return;
      }
      var paygo = function (rpd) { return costFor(m, rpd, 0).total; };
      var slope = paygo(1);
      var cur = state.rpd;
      var now = ptuCosts(m, cur);
      var nowPay = paygo(cur);

      // Scan upward until pay-as-you-go overtakes the 1-year reserved price.
      var breakeven = null;
      if (slope > 0 && now.year != null) {
        var r = Math.max(1, ptuCosts(m, 1).year / slope * 0.9);
        for (var i = 0; i < 600 && r < 1e10; i++) {
          if (paygo(r) >= ptuCosts(m, r).year) { breakeven = r; break; }
          r *= 1.025;
        }
      }
      var xMax = niceCeil(Math.max(cur * 2, breakeven ? breakeven * 1.5 : cur * 4, 100));
      var W = 640, H = 260, L = 58, R = 16, T = 14, B = 34;
      var pw = W - L - R, ph = H - T - B;
      var N = 160;
      var pts = [];
      var yMax = 0;
      for (var k = 0; k <= N; k++) {
        var x = xMax * k / N;
        var pc = ptuCosts(m, x);
        var row = { x: x, pay: paygo(x), hourly: pc.hourly, year: pc.year };
        pts.push(row);
        yMax = Math.max(yMax, row.pay, row.year || 0);
      }
      yMax = niceCeil(Math.max(yMax, now.hourly || 0) * 1.05);
      var sx = function (x) { return L + x / xMax * pw; };
      var sy = function (y) { return T + ph - Math.min(y, yMax) / yMax * ph; };
      var path = function (key, step) {
        var d = '';
        pts.forEach(function (p, idx) {
          if (p[key] == null) return;
          var X = sx(p.x).toFixed(1), Y = sy(p[key]).toFixed(1);
          if (!idx) d += 'M' + X + ' ' + Y;
          else if (step) d += 'H' + X + 'V' + Y;
          else d += 'L' + X + ' ' + Y;
        });
        return d;
      };
      var grid = '';
      for (var g = 0; g <= 4; g++) {
        var gy = yMax * g / 4;
        grid += '<line x1="' + L + '" x2="' + (W - R) + '" y1="' + sy(gy).toFixed(1) + '" y2="' + sy(gy).toFixed(1) + '" class="cp-grid"/>' +
          '<text x="' + (L - 8) + '" y="' + (sy(gy) + 4).toFixed(1) + '" text-anchor="end" class="cp-axis">' + compact(gy, true) + '</text>';
        var gx = xMax * g / 4;
        grid += '<text x="' + sx(gx).toFixed(1) + '" y="' + (H - 12) + '" text-anchor="' + (g === 0 ? 'start' : g === 4 ? 'end' : 'middle') + '" class="cp-axis">' + compact(gx) + '</text>';
      }
      var marker = '<line x1="' + sx(cur).toFixed(1) + '" x2="' + sx(cur).toFixed(1) + '" y1="' + T + '" y2="' + (T + ph) + '" class="cp-now"/>' +
        '<text x="' + (sx(cur) + 5).toFixed(1) + '" y="' + (T + 11) + '" class="cp-now-label">You</text>';
      var be = breakeven && breakeven <= xMax
        ? '<circle cx="' + sx(breakeven).toFixed(1) + '" cy="' + sy(paygo(breakeven)).toFixed(1) + '" r="5" class="cp-be"/>' : '';
      chart.innerHTML = '<svg viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="Monthly cost versus requests per day for ' + esc(m.n) + '">' +
        grid + '<text x="' + (L + pw / 2) + '" y="' + (H - 1) + '" text-anchor="middle" class="cp-axis cp-axis--title">requests per day</text>' +
        '<path d="' + path('hourly', true) + '" class="cp-line cp-line--hourly"/>' +
        '<path d="' + path('year', true) + '" class="cp-line cp-line--year"/>' +
        '<path d="' + path('pay', false) + '" class="cp-line cp-line--pay"/>' + marker + be + '</svg>' +
        '<div class="cp-legend cp-legend--lines"><span class="cp-key cp-key--pay">Pay-as-you-go</span><span class="cp-key cp-key--hourly">PTU hourly</span><span class="cp-key cp-key--year">PTU 1-year reserved</span></div>';

      var best = Math.min(nowPay, now.hourly == null ? Infinity : now.hourly, now.year == null ? Infinity : now.year);
      var head, tone;
      if (best === nowPay) {
        tone = 'pay';
        head = breakeven
          ? 'Pay-as-you-go is cheaper today. A 1-year PTU reservation breaks even near <b>' + compact(breakeven) + ' requests/day</b> (' + (breakeven / Math.max(cur, 1)).toFixed(breakeven / Math.max(cur, 1) >= 10 ? 0 : 1) + '× your volume).'
          : 'Pay-as-you-go is cheaper at any realistic volume for this prompt shape.';
      } else {
        tone = 'ptu';
        var save = nowPay - best;
        head = 'A ' + (best === now.year ? '1-year reserved' : 'hourly') + ' PTU deployment saves about <b>' + money(save) + '/month</b> (' + Math.round(save / nowPay * 100) + '%) at your volume.';
      }
      var line = function (label, v, extra) {
        return '<li><span>' + label + '</span><strong>' + money(v) + '</strong>' + (extra ? '<small>' + extra + '</small>' : '') + '</li>';
      };
      verdict.innerHTML = '<p class="cp-verdict cp-verdict--' + tone + '">' + head + '</p><ul class="cp-compare">' +
        line('Pay-as-you-go', nowPay, 'no batch, ' + DEPS[costFor(m, cur, 0).dep]) +
        line('PTU hourly', now.hourly, now.n + ' PTUs × ' + money((ptuPrices.hourly || {})[ptuDep()]) + '/hr') +
        line('PTU 1-month reserved', now.month, '') +
        line('PTU 1-year reserved', now.year, 'per month') +
        '</ul><p class="cp-fine">Sized for ' + state.peak + '× average traffic at peak (' + compact(state.rpd / 1440 * state.peak) + ' requests/min) on ' + DEPS[ptuDep()] +
        ' provisioned, using ' + m.ptu[4].toLocaleString('en-US') + ' input tokens/min per PTU. PTU also buys predictable latency. Confirm sizing in the Foundry capacity calculator.</p>';
    }

    function renderUnpriced() {
      var groups = {};
      (data.unpriced || []).forEach(function (u) { (groups[u.why] = groups[u.why] || []).push(u); });
      $('[data-cp-unpriced]').innerHTML = Object.keys(groups).map(function (why) {
        return '<div class="cp-unpriced__group"><p>' + esc(why) + '</p><div class="cp-unpriced__list">' +
          groups[why].map(function (u) {
            return '<a href="' + esc(siteRoot + 'models/' + u.s + '/') + '">' + providerLogo(u.f) + esc(u.n) + '</a>';
          }).join('') + '</div></div>';
      }).join('');
    }

    function render() {
      var rows = state.models.map(function (s) { return { m: bySlug[s], c: costFor(bySlug[s], state.rpd) }; })
        .sort(function (a, b) { return a.c.total - b.c.total; });
      syncInputs();
      renderSelected();
      renderKpis(rows);
      renderBars(rows);
      renderTable(rows);
      renderPtuSelect();
      renderPtu();
      syncUrl();
      root._rows = rows;
    }

    // ----- search -----
    var active = -1;
    function suggestions() {
      var term = searchEl.value.trim().toLowerCase();
      if (!term) return [];
      return data.models.filter(function (m) {
        return state.models.indexOf(m.s) < 0 && (m.n.toLowerCase().indexOf(term) >= 0 || m.f.toLowerCase().indexOf(term) >= 0);
      }).slice(0, 8);
    }
    function renderSuggest() {
      var list = suggestions();
      if (!list.length) { suggestEl.hidden = true; suggestEl.innerHTML = ''; return; }
      if (active >= list.length) active = list.length - 1;
      suggestEl.innerHTML = list.map(function (m, i) {
        var t = tierFor(m).t;
        return '<li role="option" data-add="' + esc(m.s) + '" class="' + (i === active ? 'is-active' : '') + '">' + providerLogo(m.f) +
          '<span>' + esc(m.n) + '</span>' + badge(m) + '<small>' + unitPrice(blended(t)) + ' / 1M</small></li>';
      }).join('');
      suggestEl.hidden = false;
    }
    function add(slug) {
      if (!bySlug[slug] || state.models.indexOf(slug) >= 0 || state.models.length >= MAX_MODELS) return;
      state.models.push(slug);
      searchEl.value = '';
      active = -1;
      renderSuggest();
      render();
    }

    searchEl.addEventListener('input', function () { active = 0; renderSuggest(); });
    searchEl.addEventListener('keydown', function (e) {
      var list = suggestions();
      if (e.key === 'ArrowDown') { e.preventDefault(); active = Math.min(list.length - 1, active + 1); renderSuggest(); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); active = Math.max(0, active - 1); renderSuggest(); }
      else if (e.key === 'Enter') { e.preventDefault(); if (list[Math.max(0, active)]) add(list[Math.max(0, active)].s); }
      else if (e.key === 'Escape') { suggestEl.hidden = true; }
    });
    searchEl.addEventListener('blur', function () { setTimeout(function () { suggestEl.hidden = true; }, 150); });
    searchEl.addEventListener('focus', renderSuggest);

    root.addEventListener('mousedown', function (e) {
      var opt = e.target.closest('.cp-suggest [data-add]');
      if (opt) { e.preventDefault(); add(opt.getAttribute('data-add')); }
    });
    root.addEventListener('click', function (e) {
      var t = e.target.closest('button, a[data-add]');
      if (!t || !root.contains(t)) return;
      if (t.hasAttribute('data-remove')) {
        state.models = state.models.filter(function (s) { return s !== t.getAttribute('data-remove'); });
        render();
      } else if (t.matches('a[data-add]')) {
        e.preventDefault();
        add(t.getAttribute('data-add'));
      } else if (t.hasAttribute('data-set')) {
        state.models = modelSet(t.getAttribute('data-set')).slice(0, MAX_MODELS);
        render();
      } else if (t.hasAttribute('data-workload')) {
        ['rpd', 'in', 'out', 'cache', 'batch'].forEach(function (k) { state[k] = +t.dataset[k]; });
        // Embedding models only make sense for the Embeddings preset: swap them in and out
        // so they don't linger in chat/agent comparisons.
        if (t.dataset.workload === 'embed') {
          var embeds = data.models.filter(function (m) { return isEmbed(m.s) && m.lk !== 'retired'; }).map(function (m) { return m.s; });
          if (embeds.length) {
            var rest = state.models.filter(function (s) { return !isEmbed(s); });
            if (rest.length) stashedModels = rest;
            state.models = embeds.slice(0, MAX_MODELS);
          }
        } else if (state.models.some(isEmbed) || !state.models.length) {
          var kept = state.models.filter(function (s) { return !isEmbed(s); });
          var restored = (stashedModels || []).concat(kept).filter(function (s, i, a) { return bySlug[s] && a.indexOf(s) === i; });
          state.models = (restored.length ? restored : modelSet('popular')).slice(0, MAX_MODELS);
          stashedModels = null;
        }
        render();
      } else if (t.hasAttribute('data-dep')) {
        state.dep = t.getAttribute('data-dep');
        render();
      } else if (t.getAttribute('data-cp-action') === 'csv') {
        csv(root._rows || []);
      }
    });
    ['rpd', 'in', 'out', 'cache', 'batch'].forEach(function (k) {
      if (!fields[k]) return;
      fields[k].addEventListener('input', function () {
        var v = num(fields[k].value, null);
        if (v == null) return;
        state[k] = k === 'cache' ? Math.min(90, v) : k === 'batch' ? Math.min(100, v) : Math.round(v);
        render();
      });
    });
    fields.peak.addEventListener('change', function () { state.peak = num(fields.peak.value, 2) || 2; render(); });
    ptuSelect.addEventListener('change', function () { state.ptuModel = ptuSelect.value; renderPtu(); syncUrl(); });

    // ----- media & audio estimator -----
    var mediaEl = $('[data-cpm]');
    var media = mediaEl ? initMedia() : null;

    function initMedia() {
      var defaults = data.media_defaults || {};
      var tabParam = q.get('media');
      var tab = MEDIA_TABS[tabParam] ? tabParam : (tabParam === 'search' ? 'docs' : 'image');
      var st = {
        tab: tab,
        hl: q.get('hl') || '',
        touched: !!MEDIA_TABS[tabParam] || tabParam === 'search',
        quality: 'medium',
        mode: 'transcribe',
        vol: { image: 10000, audio: 10000, video: 600, docs: 10000, search: 100000 },
        a: JSON.parse(JSON.stringify(defaults)),
      };
      var hlModel = (data.media || []).filter(function (m) { return m.s === st.hl; })[0];
      if (hlModel && hlModel.c === 'audio') st.mode = hlModel.am;
      return st;
    }

    function mediaTab(m) { return m.c === 'search' ? 'docs' : m.c; }

    function mediaUnit(m) {
      var p = m.p, a = media.a;
      if (m.c === 'video') return { cost: p.per_second, unit: 'per second', vol: 'video' };
      if (m.c === 'docs') return { cost: p.per_page, unit: 'per page', vol: 'docs' };
      if (m.c === 'search') return { cost: p.per_query, unit: 'per query', vol: 'search' };
      if (m.c === 'image') {
        if (p.per_image != null) return { cost: p.per_image, unit: 'per image', vol: 'image' };
        if (p.per_megapixel != null) {
          var mp = a.megapixels;
          var cost = p.per_megapixel_first != null ? p.per_megapixel_first + p.per_megapixel * Math.max(mp - 1, 0) : p.per_megapixel * mp;
          return { cost: cost, unit: 'per image', vol: 'image', est: 'megapixel' };
        }
        var tokens = (a.image_tokens || {})[media.quality] || 0;
        return { cost: (p.image_out || 0) * tokens / 1e6 + (p.text_in || 0) * a.prompt_tokens / 1e6, unit: 'per image', vol: 'image', est: 'token' };
      }
      if (p.per_hour != null) return { cost: p.per_hour / 60, unit: 'per minute', vol: 'audio' };
      if (p.per_1m_chars != null) return { cost: p.per_1m_chars * a.speech_chars_pm / 1e6, unit: 'per minute', vol: 'audio', est: 'chars' };
      if (media.mode === 'transcribe') {
        return { cost: (p.audio_in || 0) * a.transcribe_audio_tpm / 1e6 + (p.text_out || 0) * a.transcript_tpm / 1e6, unit: 'per minute', vol: 'audio', est: 'token' };
      }
      if (media.mode === 'speech') {
        return { cost: (p.audio_out || 0) * a.speech_audio_tpm / 1e6 + (p.text_in || 0) * a.transcript_tpm / 1e6, unit: 'per minute', vol: 'audio', est: 'token' };
      }
      return { cost: 0.5 * (p.audio_in || 0) * a.voice_in_tpm / 1e6 + 0.5 * (p.audio_out || 0) * a.voice_out_tpm / 1e6, unit: 'per minute', vol: 'audio', est: 'token' };
    }

    function mediaModels() {
      return (data.media || []).filter(function (m) {
        if (mediaTab(m) !== media.tab) return false;
        if (media.tab === 'audio') return m.am === media.mode || (media.mode === 'voice' && m.am === 'voice');
        return true;
      });
    }

    function mediaControls() {
      var v = media.vol;
      var field = function (key, label, step) {
        return '<label class="cp-field"><span>' + label + '</span><input type="number" min="0" step="' + step + '" data-cpm-vol="' + key + '" value="' + v[key] + '" inputmode="numeric"></label>';
      };
      var seg = function (attr, current, opts) {
        return '<div class="cp-seg" role="radiogroup">' + opts.map(function (o) {
          var on = o[0] === current;
          return '<button type="button" role="radio" ' + attr + '="' + o[0] + '" aria-checked="' + on + '" class="' + (on ? 'is-active' : '') + '">' + o[1] + '</button>';
        }).join('') + '</div>';
      };
      if (media.tab === 'image') {
        return field('image', 'Images per month', 1000) +
          '<div class="cp-field"><span>Quality (token-billed models)</span>' + seg('data-cpm-quality', media.quality, [['low', 'Low'], ['medium', 'Medium'], ['high', 'High']]) + '</div>';
      }
      if (media.tab === 'audio') {
        var counts = { transcribe: 0, speech: 0, voice: 0 };
        (data.media || []).forEach(function (m) { if (m.c === 'audio') counts[m.am] = (counts[m.am] || 0) + 1; });
        return '<div class="cp-field"><span>What the model does</span>' + seg('data-cpm-mode', media.mode, [
          ['transcribe', 'Speech → text <small>' + counts.transcribe + '</small>'],
          ['speech', 'Text → speech <small>' + counts.speech + '</small>'],
          ['voice', 'Voice chat <small>' + counts.voice + '</small>']]) + '</div>' +
          field('audio', media.mode === 'transcribe' ? 'Audio minutes per month' : media.mode === 'speech' ? 'Minutes of speech per month' : 'Conversation minutes per month', 500);
      }
      if (media.tab === 'video') return field('video', 'Seconds of video per month', 60);
      return field('docs', 'Document pages per month', 1000) + field('search', 'Search queries per month', 10000);
    }

    var ASSUME = {
      image: [
        ['image_tokens.low', 'Output tokens per image — low quality'],
        ['image_tokens.medium', 'Output tokens per image — medium quality'],
        ['image_tokens.high', 'Output tokens per image — high quality'],
        ['prompt_tokens', 'Prompt tokens per image'],
        ['megapixels', 'Megapixels per image (megapixel-billed models)'],
      ],
      audio: {
        transcribe: [['transcribe_audio_tpm', 'Audio tokens per minute of input'], ['transcript_tpm', 'Transcript text tokens per minute']],
        speech: [['speech_audio_tpm', 'Audio tokens per minute of speech'], ['transcript_tpm', 'Input text tokens per minute'], ['speech_chars_pm', 'Characters per minute (character-billed models)']],
        voice: [['voice_in_tpm', 'Audio tokens per minute while the user talks'], ['voice_out_tpm', 'Audio tokens per minute while the model talks']],
      },
    };
    function getA(path) { return path.split('.').reduce(function (o, k) { return o ? o[k] : undefined; }, media.a); }
    function setA(path, value) {
      var keys = path.split('.'), o = media.a;
      for (var i = 0; i < keys.length - 1; i++) o = o[keys[i]];
      o[keys[keys.length - 1]] = value;
    }

    function renderMediaAssumptions() {
      var list = media.tab === 'image' ? ASSUME.image : media.tab === 'audio' ? ASSUME.audio[media.mode] : null;
      var box = mediaEl.querySelector('[data-cpm-assume]');
      if (!list) {
        box.innerHTML = '<p class="cp-fine">These models are billed directly per ' + (media.tab === 'video' ? 'second of video' : 'page or query') + ', so the estimate needs no conversion.</p>';
        return;
      }
      box.innerHTML = '<p class="cp-fine">Token-billed models are converted to a per-' + (media.tab === 'image' ? 'image' : 'minute') +
        ' cost with these figures. They are typical values, not guarantees — change them to match your content.' +
        (media.tab === 'audio' && media.mode === 'voice' ? ' Each side is assumed to talk half the time; re-sent conversation context is not included.' : '') + '</p>' +
        '<div class="cp-fields cpm-assume__fields">' + list.map(function (it) {
          return '<label class="cp-field"><span>' + it[1] + '</span><input type="number" min="0" step="any" data-cpm-a="' + it[0] + '" value="' + getA(it[0]) + '"></label>';
        }).join('') + '</div><button type="button" class="ax-btn" data-cpm-reset>Reset to defaults</button>';
    }

    function renderMedia(rebuildControls) {
      if (!media) return;
      mediaEl.querySelectorAll('[data-cpm-tab]').forEach(function (b) {
        var on = b.getAttribute('data-cpm-tab') === media.tab;
        b.classList.toggle('is-active', on);
        b.setAttribute('aria-selected', on ? 'true' : 'false');
      });
      if (rebuildControls) {
        mediaEl.querySelector('[data-cpm-controls]').innerHTML = mediaControls();
        renderMediaAssumptions();
      }
      var rows = mediaModels().map(function (m) {
        var u = mediaUnit(m);
        return { m: m, u: u, total: (u.cost || 0) * (media.vol[u.vol] || 0) };
      }).sort(function (a, b) { return a.total - b.total; });
      var el = mediaEl.querySelector('[data-cpm-bars]');
      if (!rows.length) { el.innerHTML = '<p class="cp-empty">No priced models in this group.</p>'; return; }
      var max = Math.max.apply(null, rows.map(function (r) { return r.total; })) || 1;
      var EST = {
        token: 'Converted from per-token prices using the assumptions below.',
        megapixel: 'Billed per megapixel; uses the image size in the assumptions below.',
        chars: 'Billed per character; uses the characters-per-minute assumption below.',
      };
      el.innerHTML = rows.map(function (r) {
        var m = r.m;
        var notes = [];
        if (r.u.est) notes.push('<span class="cp-note"' + tip('Estimate', EST[r.u.est]) + '>estimate</span>');
        if (m.src === 'mp') notes.push('<span class="cp-note"' + tip('Azure Marketplace', 'Billed through Azure Marketplace. The price comes from the Marketplace catalog.') + '>Marketplace</span>');
        var rep = m.rs && ALERT[m.lk] ? '<span class="cp-rep">→ ' + esc(m.rep) + '</span>' : '';
        return '<div class="cp-bar' + (m.s === media.hl ? ' is-hl' : '') + '" data-cpm-row="' + esc(m.s) + '">' +
          '<div class="cp-bar__label">' + providerLogo(m.f) +
          '<a href="' + esc(siteRoot + 'models/' + m.s + '/') + '">' + esc(m.n) + '</a>' + badge(m) + rep + notes.join('') + '</div>' +
          '<div class="cp-bar__track"' + tip(m.n + ' · ' + money(r.total) + '/month', unitPrice(r.u.cost) + ' ' + r.u.unit) + '>' +
          '<span class="cp-part cp-part--media" style="width:' + (r.total / max * 100).toFixed(2) + '%"></span></div>' +
          '<div class="cp-bar__value"><strong>' + money(r.total) + '</strong><small>' + unitPrice(r.u.cost) + ' ' + r.u.unit + '</small></div>' +
          '</div>';
      }).join('');
    }

    if (media) {
      mediaEl.querySelectorAll('[data-cpm-count]').forEach(function (s) {
        var k = s.getAttribute('data-cpm-count');
        s.textContent = (data.media || []).filter(function (m) { return mediaTab(m) === k; }).length;
      });
      mediaEl.addEventListener('click', function (e) {
        var b = e.target.closest('button');
        if (!b || !mediaEl.contains(b)) return;
        if (b.hasAttribute('data-cpm-tab')) { media.tab = b.getAttribute('data-cpm-tab'); media.hl = ''; }
        else if (b.hasAttribute('data-cpm-quality')) media.quality = b.getAttribute('data-cpm-quality');
        else if (b.hasAttribute('data-cpm-mode')) { media.mode = b.getAttribute('data-cpm-mode'); media.hl = ''; }
        else if (b.hasAttribute('data-cpm-reset')) media.a = JSON.parse(JSON.stringify(data.media_defaults || {}));
        else return;
        media.touched = true;
        renderMedia(true);
        syncUrl();
      });
      mediaEl.addEventListener('input', function (e) {
        var t = e.target;
        var v = num(t.value, null);
        if (v == null) return;
        if (t.hasAttribute('data-cpm-vol')) media.vol[t.getAttribute('data-cpm-vol')] = v;
        else if (t.hasAttribute('data-cpm-a')) setA(t.getAttribute('data-cpm-a'), v);
        else return;
        renderMedia(false);
      });
      renderMedia(true);
      if (media.hl && media.touched) {
        var row = mediaEl.querySelector('[data-cpm-row="' + media.hl + '"]');
        setTimeout(function () { (row || mediaEl).scrollIntoView({ block: 'center' }); }, 50);
      }
    }

    renderUnpriced();
    render();
  }

  function mountAll() { document.querySelectorAll('[data-cost-planner]').forEach(mount); }
  if (typeof window.document$ !== 'undefined' && window.document$.subscribe) {
    window.document$.subscribe(mountAll);
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mountAll);
  } else {
    mountAll();
  }
})();
