/* Retirement planner: horizon tabs, month calendar with deprecated-window spans, timeline and agenda. */
(function () {
  'use strict';

  var DAY = 86400000;
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  var MONTHS_LONG = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  var WEEKDAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  var MAX_LANES = 3;
  var MAX_CHIPS = 3;
  var HORIZONS = ['month', 'next', '3m', '6m', '12m', 'all'];

  function dn(y, m, d) { return Math.floor(Date.UTC(y, m, d) / DAY); }
  function parse(s) {
    if (!s) return null;
    var p = s.split('-');
    return dn(+p[0], +p[1] - 1, +p[2]);
  }
  function parts(n) {
    var d = new Date(n * DAY);
    return { y: d.getUTCFullYear(), m: d.getUTCMonth(), d: d.getUTCDate(), w: d.getUTCDay() };
  }
  function monthStart(n) { var p = parts(n); return dn(p.y, p.m, 1); }
  function monthEnd(n) { var p = parts(n); return dn(p.y, p.m + 1, 0); }
  function addMonths(n, k) { var p = parts(n); return dn(p.y, p.m + k, 1); }
  function fmt(n, year) { var p = parts(n); return MONTHS[p.m] + ' ' + p.d + (year ? ', ' + p.y : ''); }
  function esc(v) {
    return String(v == null ? '' : v).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function plural(n, one, many) { return n + ' ' + (n === 1 ? one : (many || one + 's')); }
  function rel(days) {
    if (days === 0) return 'today';
    if (days === 1) return 'tomorrow';
    if (days < 0) return plural(-days, 'day') + ' ago';
    if (days < 60) return 'in ' + plural(days, 'day');
    return 'in ~' + plural(Math.round(days / 30.4), 'month');
  }
  function span(days) {
    if (days < 60) return plural(days, 'day');
    return '~' + plural(Math.round(days / 30.4), 'month');
  }
  function tone(days) { return days <= 30 ? 'danger' : days <= 90 ? 'warning' : 'info'; }
  function todayDn() { var t = new Date(); return dn(t.getFullYear(), t.getMonth(), t.getDate()); }

  function mount(el) {
    if (el.getAttribute('data-rp-mounted')) return;
    el.setAttribute('data-rp-mounted', '1');

    var raw;
    try { raw = JSON.parse(el.getAttribute('data-rp') || '[]'); } catch (e) { raw = []; }
    var today = todayDn();
    var entries = raw.map(function (e, i) {
      return {
        id: i, m: e.m, v: e.v, c: e.c, s: e.s,
        d: parse(e.d), de: !!e.de, r: parse(e.r), re: !!e.re,
        rp: e.rp, rh: e.rh, h: e.h, n: e.n
      };
    });
    var lastDate = entries.reduce(function (acc, e) { return Math.max(acc, e.r || 0, e.d || 0); }, today);

    var state = { h: 'month', v: 'calendar', q: '', c: '', all: false, focus: null, zoom: null };
    readHash();

    var $ = function (sel) { return el.querySelector(sel); };
    var horizonsEl = $('[data-rp-horizons]');
    var summaryEl = $('[data-rp-summary]');
    var visualEl = $('[data-rp-visual]');
    var agendaEl = $('[data-rp-agenda]');
    var qInput = $('[data-rp-q]');
    var allInput = $('[data-rp-all]');
    qInput.value = state.q;
    allInput.checked = state.all;

    function readHash() {
      var h = (location.hash || '').replace(/^#/, '');
      if (h.indexOf('=') < 0) return;
      h.split('&').forEach(function (pair) {
        var kv = pair.split('=');
        var k = kv[0];
        var v = decodeURIComponent(kv[1] || '');
        if (k === 'h' && HORIZONS.indexOf(v) >= 0) state.h = v;
        else if (k === 'v' && (v === 'calendar' || v === 'timeline')) state.v = v;
        else if (k === 'q') state.q = v;
        else if (k === 'c') state.c = v;
        else if (k === 'w') state.all = v === '1';
      });
    }
    function writeHash() {
      var bits = [];
      if (state.h !== 'month') bits.push('h=' + state.h);
      if (state.v !== 'calendar') bits.push('v=' + state.v);
      if (state.q) bits.push('q=' + encodeURIComponent(state.q));
      if (state.c) bits.push('c=' + encodeURIComponent(state.c));
      if (state.all) bits.push('w=1');
      var next = bits.length ? '#' + bits.join('&') : location.pathname + location.search;
      if (bits.length ? location.hash !== next : location.hash.indexOf('=') >= 0) {
        history.replaceState(history.state, '', next);
      }
    }

    function filtered() {
      var q = state.q.trim().toLowerCase();
      return entries.filter(function (e) {
        if (state.c && e.c !== state.c) return false;
        if (q && (e.m + ' ' + e.v + ' ' + (e.rp || '')).toLowerCase().indexOf(q) < 0) return false;
        return true;
      });
    }

    function events(list) {
      var out = [];
      list.forEach(function (e) {
        if (e.r != null) out.push({ t: 'retire', date: e.r, est: e.re, e: e });
        if (e.d != null) out.push({ t: 'deprecate', date: e.d, est: e.de, e: e });
      });
      return out;
    }

    function range(h) {
      if (h === 'month') return [today, monthEnd(today)];
      if (h === 'next') { var s = addMonths(today, 1); return [s, monthEnd(s)]; }
      if (h === '3m') return [today, today + 91];
      if (h === '6m') return [today, today + 182];
      if (h === '12m') return [today, today + 365];
      return [today, Math.max(lastDate, today + 30)];
    }

    function horizonLabel(h) {
      var r = range(h);
      if (h === 'month') return ['This month', MONTHS_LONG[parts(today).m]];
      if (h === 'next') return ['Next month', MONTHS_LONG[parts(r[0]).m]];
      if (h === 'all') return ['All upcoming', 'to ' + MONTHS[parts(r[1]).m] + ' ’' + String(parts(r[1]).y).slice(2)];
      return [h.replace('m', '') + ' months', 'to ' + fmt(r[1])];
    }

    function groupEvents(evts) {
      var map = {};
      var groups = [];
      evts.forEach(function (ev) {
        var key = ev.t + '|' + ev.date + '|' + (ev.est ? 1 : 0);
        if (!map[key]) {
          map[key] = { key: key, t: ev.t, date: ev.date, est: ev.est, entries: [] };
          groups.push(map[key]);
        }
        map[key].entries.push(ev.e);
      });
      groups.sort(function (a, b) { return a.date - b.date || (a.t === 'retire' ? -1 : 1) - (b.t === 'retire' ? -1 : 1); });
      return groups;
    }

    function uniqueModels(list) {
      var seen = {};
      var out = [];
      list.forEach(function (e) {
        if (!seen[e.m]) { seen[e.m] = { m: e.m, h: e.h, versions: [] }; out.push(seen[e.m]); }
        seen[e.m].versions.push(e.v);
      });
      return out;
    }

    function focusModels() {
      if (!state.focus) return null;
      if (state.focus.model) return [state.focus.model];
      var g = state.focus.group;
      return g ? uniqueModels(g.entries).map(function (x) { return x.m; }) : null;
    }

    function typeLabel(g) {
      if (g.t === 'retire') return g.est ? 'Retires no earlier than' : 'Retires';
      return g.est ? 'Closes to new customers no earlier than' : 'Closes to new customers';
    }

    function meaning(g) {
      if (g.t === 'retire') {
        return g.est
          ? 'Earliest possible retirement. Microsoft may confirm a later date, but plan to migrate before this one.'
          : 'The version is removed: existing deployments stop responding and API calls return errors. Migrate before this date.';
      }
      var first = g.entries[0];
      var after = first.r != null ? ' Existing deployments keep working until it retires on ' + fmt(first.r, true) + ' (' + span(first.r - first.d) + ' later).' : ' Existing deployments keep working until a retirement date is announced.';
      return (g.est ? 'Expected to stop accepting new customers no earlier than this date.' : 'Subscriptions that have not used this version can no longer deploy it.') + after;
    }

    function replacementHtml(list) {
      var pairs = [];
      var seen = {};
      list.forEach(function (e) {
        if (!e.rp) return;
        var k = e.m + '>' + e.rp;
        if (seen[k]) return;
        seen[k] = 1;
        pairs.push(e);
      });
      if (!pairs.length) return '<span class="rp-norep">No replacement named yet</span>';
      var target = function (e) { return e.rh ? '<a href="' + esc(e.rh) + '">' + esc(e.rp) + '</a>' : '<span>' + esc(e.rp) + '</span>'; };
      var sameTarget = pairs.every(function (e) { return e.rp === pairs[0].rp; });
      if (sameTarget) return 'Move to ' + target(pairs[0]);
      return 'Move to ' + pairs.map(function (e) { return target(e) + ' <small>(from ' + esc(e.m) + ')</small>'; }).join(', ');
    }

    function chipTip(g, model) {
      var days = g.date - today;
      return ' tabindex="-1" data-tip-title="' + esc(model.m + ' · ' + typeLabel(g)) + '" data-tip="' +
        esc(fmt(g.date, true) + ' · ' + rel(days) + ' · ' + plural(model.versions.length, 'version') + ' (' + model.versions.join(', ') + ')') + '"';
    }

    /* ---------- horizon tabs + summary ---------- */
    function renderHorizons(evts) {
      horizonsEl.innerHTML = HORIZONS.map(function (h) {
        var r = range(h);
        var n = evts.filter(function (ev) { return ev.date >= r[0] && ev.date <= r[1]; }).length;
        var hot = evts.some(function (ev) { return ev.t === 'retire' && !ev.est && ev.date >= r[0] && ev.date <= r[1] && ev.date - today <= 30; });
        var label = horizonLabel(h);
        return '<button type="button" role="tab" class="rp-h' + (state.h === h ? ' is-on' : '') + '" aria-selected="' + (state.h === h) + '" data-h="' + h + '">' +
          '<small>' + esc(label[0]) + '</small><b>' + esc(label[1]) + '</b><em class="' + (hot ? 'is-hot' : '') + '">' + n + '</em></button>';
      }).join('');
    }

    function renderSummary(evts, list) {
      var r = range(state.h);
      var inRange = evts.filter(function (ev) { return ev.date >= r[0] && ev.date <= r[1]; });
      var retire = inRange.filter(function (ev) { return ev.t === 'retire'; });
      var firm = retire.filter(function (ev) { return !ev.est; }).length;
      var dep = inRange.filter(function (ev) { return ev.t === 'deprecate'; }).length;
      var active = list.filter(function (e) { return e.d != null && !e.de && e.d <= today && e.r != null && e.r > today; }).length;
      var next = evts.filter(function (ev) { return ev.t === 'retire' && ev.date >= today; }).sort(function (a, b) { return a.date - b.date; })[0];
      var nextHtml = next
        ? '<div class="rp-next"><span>Next retirement</span><b>' + esc(next.e.m) + '</b><em class="rp-tone--' + tone(next.date - today) + '">' + esc(rel(next.date - today)) + '</em></div>'
        : '';
      summaryEl.innerHTML =
        '<div class="rp-stat rp-stat--retire"><b>' + retire.length + '</b><span>version' + (retire.length === 1 ? '' : 's') + ' retire' + (retire.length === 1 ? 's' : '') +
        (retire.length - firm ? ' <small>' + (retire.length - firm) + ' no-earlier-than</small>' : '') + '</span></div>' +
        '<div class="rp-stat rp-stat--dep"><b>' + dep + '</b><span>close' + (dep === 1 ? 's' : '') + ' to new customers</span></div>' +
        '<div class="rp-stat rp-stat--window" tabindex="0" data-tip-title="Deprecated right now" data-tip="These versions no longer accept new customers. Existing deployments still work until their retirement date."><b>' + active + '</b><span>deprecated now, still running</span></div>' +
        nextHtml;
    }

    /* ---------- calendar ---------- */
    function windowsFor(list) {
      var map = {};
      var out = [];
      list.forEach(function (e) {
        if (e.d == null || e.r == null || e.d >= e.r) return;
        var key = e.d + '|' + e.r;
        if (!map[key]) { map[key] = { key: key, start: e.d, end: e.r, est: e.re, entries: [] }; out.push(map[key]); }
        map[key].entries.push(e);
      });
      return out;
    }

    function spanLabel(w) {
      var models = uniqueModels(w.entries);
      return models[0].m + (models.length > 1 ? ' +' + (models.length - 1) : '');
    }

    function renderMonth(ms, list, evts) {
      var me = monthEnd(ms);
      var gridStart = ms - parts(ms).w;
      var gridEnd = me + (6 - parts(me).w);
      var r = range(state.h);
      var fm = focusModels();
      var spans = windowsFor(list).filter(function (w) {
        if (w.end < gridStart || w.start > gridEnd) return false;
        var focused = fm && w.entries.some(function (e) { return fm.indexOf(e.m) >= 0; });
        w.focused = !!focused;
        return state.all || focused || (w.end >= ms && w.end <= me);
      }).sort(function (a, b) { return (b.focused - a.focused) || a.end - b.end || a.start - b.start; });
      var lanes = [];
      spans.forEach(function (w) {
        var s = Math.max(w.start, gridStart);
        var lane = 0;
        while (lane < lanes.length && lanes[lane] >= s) lane++;
        lanes[lane] = Math.min(w.end, gridEnd);
        w.lane = lane;
      });
      var hidden = spans.filter(function (w) { return w.lane >= MAX_LANES; }).length;

      var byDay = {};
      groupEvents(evts.filter(function (ev) { return ev.date >= gridStart && ev.date <= gridEnd; })).forEach(function (g) {
        (byDay[g.date] = byDay[g.date] || []).push(g);
      });

      var head = '<div class="rp-cal__head">' +
        '<button type="button" class="rp-nav" data-month="' + addMonths(ms, -1) + '" aria-label="Previous month">‹</button>' +
        '<h3>' + MONTHS_LONG[parts(ms).m] + ' <span>' + parts(ms).y + '</span></h3>' +
        '<button type="button" class="rp-nav" data-month="' + addMonths(ms, 1) + '" aria-label="Next month">›</button>' +
        (state.zoom != null && ['3m', '6m', '12m', 'all'].indexOf(state.h) >= 0 ? '<button type="button" class="rp-back" data-back>All months</button>' : '') +
        '</div>';
      var dow = '<div class="rp-dow">' + WEEKDAYS.map(function (d) { return '<span>' + d + '</span>'; }).join('') + '</div>';

      var weeks = '';
      for (var ws = gridStart; ws <= gridEnd; ws += 7) {
        var we = ws + 6;
        var segs = spans.filter(function (w) { return w.lane < MAX_LANES && w.start <= we && w.end >= ws; });
        var laneCount = segs.reduce(function (acc, w) { return Math.max(acc, w.lane + 1); }, 0);
        var rows = 'auto' + (laneCount ? ' repeat(' + laneCount + ', var(--rp-lane))' : '') + ' 1fr';
        var html = '';
        for (var i = 0; i < 7; i++) {
          var day = ws + i;
          var cls = 'rp-day';
          if (day < ms || day > me) cls += ' is-out';
          if (day < today) cls += ' is-past';
          if (day === today) cls += ' is-today';
          if (day >= r[0] && day <= r[1]) cls += ' is-range';
          html += '<div class="' + cls + '" style="grid-column:' + (i + 1) + ';grid-row:1/-1"></div>';
          html += '<span class="rp-dnum' + (day === today ? ' is-today' : '') + '" style="grid-column:' + (i + 1) + '">' + parts(day).d + '</span>';
        }
        segs.forEach(function (w) {
          var a = Math.max(w.start, ws);
          var b = Math.min(w.end, we);
          var isStart = a === w.start;
          var isEnd = b === w.end;
          var days = w.end - today;
          var models = uniqueModels(w.entries);
          var tip = models.map(function (m) { return m.m; }).join(', ');
          html += '<button type="button" class="rp-span rp-tone--' + tone(days) + (isStart ? ' is-start' : '') + (isEnd ? ' is-end' : '') + (w.focused ? ' is-focus' : '') + (fm && !w.focused ? ' is-dim' : '') +
            '" style="grid-column:' + (a - ws + 1) + '/' + (b - ws + 2) + ';grid-row:' + (w.lane + 2) + '" data-span="' + esc(w.key) + '" data-model="' + esc(models[0].m) + '"' +
            ' data-tip-title="' + esc('Deprecated · ' + tip) + '" data-tip="' + esc('Existing customers only from ' + fmt(w.start, true) + ' until it retires ' + fmt(w.end, true) + ' (' + rel(w.end - today) + ').') + '">' +
            '<span>' + (isStart ? 'Deprecated · ' : '') + esc(spanLabel(w)) + (isEnd ? '' : ' →') + '</span></button>';
        });
        for (var j = 0; j < 7; j++) {
          var d2 = ws + j;
          var chips = [];
          (byDay[d2] || []).forEach(function (g) {
            uniqueModels(g.entries).forEach(function (m) { chips.push({ g: g, m: m }); });
          });
          var visible = chips.length > MAX_CHIPS ? chips.slice(0, MAX_CHIPS - 1) : chips;
          var cell = visible.map(function (c) {
            var focused = state.focus && state.focus.group && state.focus.group.key === c.g.key && (!state.focus.model || state.focus.model === c.m.m);
            return '<button type="button" class="rp-chip rp-chip--' + c.g.t + ' rp-tone--' + tone(c.g.date - today) + (c.g.est ? ' is-est' : '') + (focused ? ' is-focus' : '') + (fm && fm.indexOf(c.m.m) < 0 ? ' is-dim' : '') +
              '" data-key="' + esc(c.g.key) + '" data-model="' + esc(c.m.m) + '"' + chipTip(c.g, c.m) + '><i></i><span>' + esc(c.m.m) + '</span>' +
              (c.m.versions.length > 1 ? '<small>×' + c.m.versions.length + '</small>' : '') + '</button>';
          }).join('');
          if (chips.length > visible.length) {
            cell += '<button type="button" class="rp-chip rp-chip--more" data-day="' + d2 + '">+' + (chips.length - visible.length) + ' more</button>';
          }
          html += '<div class="rp-cell" style="grid-column:' + (j + 1) + ';grid-row:' + (laneCount + 2) + '">' + cell + '</div>';
        }
        weeks += '<div class="rp-week" style="grid-template-rows:' + rows + '">' + html + '</div>';
      }
      var note = hidden ? '<p class="rp-hidden">' + plural(hidden, 'more deprecated window') + ' not shown. Switch to Timeline to see every window.</p>' : '';
      return '<div class="rp-cal">' + head + dow + '<div class="rp-weeks">' + weeks + '</div>' + note + '</div>';
    }

    function renderOverview(r, list, evts) {
      var fm = focusModels();
      var focusWindows = fm ? windowsFor(list).filter(function (w) { return w.entries.some(function (e) { return fm.indexOf(e.m) >= 0; }); }) : [];
      var months = [];
      for (var ms = monthStart(r[0]); ms <= r[1]; ms = addMonths(ms, 1)) months.push(ms);
      return '<div class="rp-months">' + months.map(function (ms) {
        var me = monthEnd(ms);
        var groups = groupEvents(evts.filter(function (ev) { return ev.date >= ms && ev.date <= me && ev.date >= r[0] && ev.date <= r[1]; }));
        var ret = groups.filter(function (g) { return g.t === 'retire'; }).reduce(function (acc, g) { return acc + g.entries.length; }, 0);
        var dep = groups.filter(function (g) { return g.t === 'deprecate'; }).reduce(function (acc, g) { return acc + g.entries.length; }, 0);
        var byDay = {};
        groups.forEach(function (g) { (byDay[g.date] = byDay[g.date] || []).push(g); });
        var lead = parts(ms).w;
        var cells = '';
        for (var k = 0; k < lead; k++) cells += '<span class="rp-mcell is-blank"></span>';
        for (var day = ms; day <= me; day++) {
          var gs = byDay[day] || [];
          var cls = 'rp-mcell';
          if (day < today) cls += ' is-past';
          if (day === today) cls += ' is-today';
          if (day < r[0] || day > r[1]) cls += ' is-outside';
          if (focusWindows.some(function (w) { return day >= w.start && day <= w.end; })) cls += ' is-window';
          var retG = gs.filter(function (g) { return g.t === 'retire'; });
          var depG = gs.filter(function (g) { return g.t === 'deprecate'; });
          if (retG.length) cls += ' has-retire rp-tone--' + tone(day - today) + (retG.every(function (g) { return g.est; }) ? ' is-est' : '');
          if (depG.length) cls += ' has-dep';
          if (gs.length) {
            var names = gs.map(function (g) { return typeLabel(g) + ': ' + uniqueModels(g.entries).map(function (m) { return m.m; }).join(', '); }).join(' · ');
            cells += '<button type="button" class="' + cls + '" data-day="' + day + '" data-tip-title="' + esc(fmt(day, true) + ' · ' + rel(day - today)) + '" data-tip="' + esc(names) + '">' + parts(day).d + '</button>';
          } else {
            cells += '<span class="' + cls + '">' + parts(day).d + '</span>';
          }
        }
        var items = groups.slice(0, 3).map(function (g) {
          var models = uniqueModels(g.entries);
          return '<li class="rp-mini__item rp-mini__item--' + g.t + ' rp-tone--' + tone(g.date - today) + (g.est ? ' is-est' : '') + '"><button type="button" data-key="' + esc(g.key) + '"><i></i><b>' + parts(g.date).d + '</b><span>' +
            esc(models[0].m) + (models.length > 1 ? ' +' + (models.length - 1) : '') + '</span></button></li>';
        }).join('');
        if (groups.length > 3) items += '<li class="rp-mini__more"><button type="button" data-month-zoom="' + ms + '">+' + (groups.length - 3) + ' more dates</button></li>';
        return '<section class="rp-mini' + (groups.length ? '' : ' is-empty') + '">' +
          '<button type="button" class="rp-mini__head" data-month-zoom="' + ms + '" aria-label="Open ' + MONTHS_LONG[parts(ms).m] + ' ' + parts(ms).y + '"><b>' + MONTHS[parts(ms).m] + '</b><span>' + parts(ms).y + '</span>' +
          '<em>' + (ret ? '<i class="rp-count rp-count--retire">' + ret + '</i>' : '') + (dep ? '<i class="rp-count rp-count--dep">' + dep + '</i>' : '') + '</em></button>' +
          '<div class="rp-mini__dow">' + WEEKDAYS.map(function (d) { return '<span>' + d.charAt(0) + '</span>'; }).join('') + '</div>' +
          '<div class="rp-mini__grid">' + cells + '</div>' +
          (items ? '<ul class="rp-mini__list">' + items + '</ul>' : '<p class="rp-mini__none">Nothing scheduled</p>') +
          '</section>';
      }).join('') + '</div>';
    }

    /* ---------- timeline ---------- */
    function renderTimeline(r, list) {
      var a = r[0];
      var b = r[1];
      var total = b - a + 1;
      var x = function (d) { return Math.max(0, Math.min(100, (d - a) / total * 100)); };
      var fm = focusModels();
      var map = {};
      var rows = [];
      list.forEach(function (e) {
        var key = e.m + '|' + e.d + '|' + e.r + '|' + e.re + '|' + e.de;
        if (!map[key]) { map[key] = { key: key, e: e, versions: [] }; rows.push(map[key]); }
        map[key].versions.push(e.v);
      });
      rows = rows.filter(function (row) {
        var e = row.e;
        var start = e.d != null ? e.d : e.r;
        var end = e.r != null ? e.r : e.d;
        return start <= b && end >= a;
      }).sort(function (p, q) {
        var pe = p.e.r != null ? p.e.r : p.e.d;
        var qe = q.e.r != null ? q.e.r : q.e.d;
        return pe - qe || p.e.m.localeCompare(q.e.m);
      });
      if (!rows.length) return '<p class="rp-empty">Nothing retires or closes in this window.</p>';

      var ticks = '';
      if (total <= 45) {
        for (var d = a; d <= b; d++) {
          var p = parts(d);
          if (p.w === 1 || d === a) ticks += '<span class="rp-tl__tick" style="left:' + x(d) + '%">' + MONTHS[p.m] + ' ' + p.d + '</span>';
        }
      } else {
        var step = total > 500 ? 3 : 1;
        for (var ms = addMonths(a, 1), n = 0; ms <= b; ms = addMonths(ms, 1), n++) {
          if (n % step) continue;
          var mp = parts(ms);
          ticks += '<span class="rp-tl__tick" style="left:' + x(ms) + '%">' + MONTHS[mp.m] + (mp.m === 0 ? ' ’' + String(mp.y).slice(2) : '') + '</span>';
        }
      }
      var todayLine = today >= a && today <= b ? '<span class="rp-tl__today" style="left:' + x(today) + '%"><em>Today</em></span>' : '';

      var body = rows.map(function (row) {
        var e = row.e;
        var segs = '';
        var liveEnd = e.d != null ? e.d : e.r;
        if (liveEnd != null && liveEnd > a) segs += '<span class="rp-tl__live" style="left:0;width:' + x(liveEnd) + '%"></span>';
        if (e.d != null && e.r != null && e.r > a && e.d <= b) {
          var l = x(Math.max(e.d, a));
          var w = x(Math.min(e.r, b + 1)) - l;
          segs += '<span class="rp-tl__dep' + (e.d < a ? ' is-clip-l' : '') + (e.r > b ? ' is-clip-r' : '') + '" style="left:' + l + '%;width:' + w + '%"><em>' + (w > 16 ? 'Deprecated · existing customers only' : '') + '</em></span>';
        }
        if (e.d != null && e.d >= a && e.d <= b) {
          segs += '<span class="rp-tl__mark rp-tl__mark--dep' + (e.de ? ' is-est' : '') + '" style="left:' + x(e.d) + '%" tabindex="-1" data-tip-title="' + esc(e.m + ' · ' + (e.de ? 'closes no earlier than' : 'closes to new customers')) + '" data-tip="' + esc(fmt(e.d, true) + ' · ' + rel(e.d - today)) + '"></span>';
        }
        if (e.r != null && e.r >= a && e.r <= b) {
          segs += '<span class="rp-tl__mark rp-tl__mark--ret rp-tone--' + tone(e.r - today) + (e.re ? ' is-est' : '') + '" style="left:' + x(e.r) + '%" tabindex="-1" data-tip-title="' + esc(e.m + ' · ' + (e.re ? 'retires no earlier than' : 'retires')) + '" data-tip="' + esc(fmt(e.r, true) + ' · ' + rel(e.r - today)) + '"></span>' +
            '<span class="rp-tl__date' + (x(e.r) > 82 ? ' is-left' : '') + '" style="left:' + x(e.r) + '%">' + (e.re ? '≥ ' : '') + fmt(e.r) + '</span>';
        } else if (e.r != null && e.r > b) {
          segs += '<span class="rp-tl__date is-out">' + (e.re ? '≥ ' : '') + fmt(e.r, true) + ' →</span>';
        }
        var focused = fm && fm.indexOf(e.m) >= 0;
        var name = e.h ? '<a href="' + esc(e.h) + '">' + esc(e.m) + '</a>' : '<span>' + esc(e.m) + '</span>';
        var rk = e.r != null ? 'retire|' + e.r + '|' + (e.re ? 1 : 0) : '';
        var dk = e.d != null ? 'deprecate|' + e.d + '|' + (e.de ? 1 : 0) : '';
        return '<div class="rp-tl__row' + (focused ? ' is-focus' : '') + (fm && !focused ? ' is-dim' : '') + '" data-model="' + esc(e.m) + '" data-key="' + (rk || dk) + '" data-key2="' + dk + '">' +
          '<div class="rp-tl__label">' + name + '<small>' + esc(row.versions.join(', ')) + (e.s === 'Preview' ? ' · preview' : '') + '</small></div>' +
          '<div class="rp-tl__track">' + segs + '</div></div>';
      }).join('');
      return '<div class="rp-tl"><div class="rp-tl__axis"><div></div><div class="rp-tl__ticks">' + ticks + '</div></div>' +
        '<div class="rp-tl__rows">' + body + '<div class="rp-tl__overlay"><div></div><div class="rp-tl__lines">' + todayLine + '</div></div></div></div>';
    }

    function legend() {
      return '<ul class="rp-legend">' +
        '<li><i class="rp-key rp-key--ret"></i>Retires</li>' +
        '<li><i class="rp-key rp-key--est"></i>No-earlier-than date</li>' +
        '<li><i class="rp-key rp-key--dep"></i>Closes to new customers</li>' +
        '<li><i class="rp-key rp-key--window"></i>Deprecated: existing customers only</li>' +
        '<li class="rp-legend__tones"><i class="rp-tone--danger"></i>≤ 30 days <i class="rp-tone--warning"></i>≤ 90 days <i class="rp-tone--info"></i>later</li>' +
        '</ul>';
    }

    /* ---------- agenda ---------- */
    function renderAgenda(evts) {
      var r = range(state.h);
      var groups = groupEvents(evts.filter(function (ev) { return ev.date >= r[0] && ev.date <= r[1]; }));
      var label = horizonLabel(state.h);
      if (!groups.length) {
        agendaEl.innerHTML = '<header class="rp-agenda__head"><b>' + esc(label[0]) + '</b><span>' + esc(label[1]) + '</span></header><p class="rp-empty">Nothing retires or closes to new customers in this window' + (state.q || state.c ? ' for the current filter' : '') + '.</p>';
        return;
      }
      var html = '<header class="rp-agenda__head"><b>' + esc(label[0]) + '</b><span>' + plural(groups.length, 'date') + '</span></header>';
      var month = null;
      groups.forEach(function (g) {
        var p = parts(g.date);
        var mKey = p.y * 12 + p.m;
        if (mKey !== month) {
          month = mKey;
          html += '<h4 class="rp-agenda__month">' + MONTHS_LONG[p.m] + ' ' + p.y + '</h4>';
        }
        var days = g.date - today;
        var focused = state.focus && ((state.focus.group && state.focus.group.key === g.key) || state.focus.day === g.date);
        var models = uniqueModels(g.entries).map(function (m) {
          var inner = esc(m.m) + '<small>' + esc(m.versions.join(', ')) + '</small>';
          return m.h ? '<a class="rp-model" href="' + esc(m.h) + '">' + inner + '</a>' : '<span class="rp-model">' + inner + '</span>';
        }).join('');
        var detail = '';
        if (focused) {
          var notes = {};
          g.entries.forEach(function (e) { if (e.n) notes[e.n] = 1; });
          detail = '<div class="rp-item__more">' + g.entries.map(function (e) {
            var bits = [e.s === 'Preview' ? 'Preview' : 'Generally available'];
            if (e.d != null) bits.push((e.d <= today ? 'deprecated ' : 'deprecates ') + (e.de ? '≥ ' : '') + fmt(e.d, true));
            if (e.r != null) bits.push((e.r <= today ? 'retired ' : 'retires ') + (e.re ? '≥ ' : '') + fmt(e.r, true));
            return '<div class="rp-ver"><code>' + esc(e.m) + ' ' + esc(e.v) + '</code><span>' + esc(bits.join(' · ')) + '</span></div>';
          }).join('') + Object.keys(notes).map(function (n) { return '<p class="rp-note">' + esc(n) + '</p>'; }).join('') + '</div>';
        }
        html += '<article class="rp-item rp-item--' + g.t + ' rp-tone--' + (g.t === 'retire' ? tone(days) : 'caution') + (g.est ? ' is-est' : '') + (focused ? ' is-focus' : '') + '" data-key="' + esc(g.key) + '" data-date="' + g.date + '" tabindex="0">' +
          '<div class="rp-item__date"><span>' + MONTHS[p.m] + '</span><b>' + p.d + '</b><small>' + WEEKDAYS[p.w] + '</small></div>' +
          '<div class="rp-item__body"><div class="rp-item__head"><span class="rp-type">' + esc(typeLabel(g)) + '</span><span class="rp-when">' + esc(rel(days)) + '</span></div>' +
          '<div class="rp-item__models">' + models + '</div>' +
          '<p class="rp-item__what">' + esc(meaning(g)) + '</p>' +
          (g.t === 'retire' ? '<p class="rp-item__rep">' + replacementHtml(g.entries) + '</p>' : '') +
          detail + '</div></article>';
      });
      agendaEl.innerHTML = html;
    }

    function scrollAgendaTo() {
      var item = agendaEl.querySelector('.rp-item.is-focus');
      if (!item) return;
      if (agendaEl.scrollHeight > agendaEl.clientHeight + 4) {
        agendaEl.scrollTo({ top: item.offsetTop - agendaEl.offsetTop - 8, behavior: 'smooth' });
      }
    }

    /* ---------- render ---------- */
    function render() {
      if (window.FMTip && window.FMTip.hide) window.FMTip.hide();
      var list = filtered();
      var evts = events(list).filter(function (ev) { return ev.date >= today; });
      var r = range(state.h);
      el.setAttribute('data-view', state.v);
      el.querySelectorAll('[data-view]').forEach(function (b) {
        if (b === el) return;
        var on = b.getAttribute('data-view') === state.v;
        b.classList.toggle('is-on', on);
        b.setAttribute('aria-pressed', on);
      });
      el.querySelectorAll('.rp-cat').forEach(function (b) { b.classList.toggle('is-on', b.getAttribute('data-cat') === state.c); });
      renderHorizons(evts);
      renderSummary(evts, list);
      var body;
      if (state.v === 'timeline') {
        body = renderTimeline(r, list);
      } else if (state.zoom != null) {
        body = renderMonth(state.zoom, list, evts);
      } else if (state.h === 'month' || state.h === 'next') {
        body = renderMonth(monthStart(r[0]), list, evts);
      } else {
        body = renderOverview(r, list, evts);
      }
      visualEl.innerHTML = body + legend();
      renderAgenda(evts);
      writeHash();
    }

    function findGroup(key) {
      var list = filtered();
      var groups = groupEvents(events(list));
      for (var i = 0; i < groups.length; i++) if (groups[i].key === key) return groups[i];
      return null;
    }

    function setFocus(next) {
      var same = state.focus && next && state.focus.group === next.group && state.focus.model === next.model && state.focus.day === next.day;
      if (state.focus && next && next.group && state.focus.group && state.focus.group.key === next.group.key && state.focus.model === next.model) same = true;
      state.focus = same ? null : next;
      render();
      scrollAgendaTo();
    }

    el.addEventListener('click', function (event) {
      var t = event.target;
      if (t.closest('a[href]')) return;
      var b;
      if ((b = t.closest('[data-h]'))) {
        state.h = b.getAttribute('data-h');
        state.zoom = null;
        state.focus = null;
        render();
      } else if ((b = t.closest('button[data-view]'))) {
        state.v = b.getAttribute('data-view');
        render();
      } else if ((b = t.closest('[data-cat]'))) {
        state.c = b.getAttribute('data-cat');
        state.focus = null;
        render();
      } else if ((b = t.closest('[data-month]'))) {
        state.zoom = +b.getAttribute('data-month');
        render();
      } else if ((b = t.closest('[data-month-zoom]'))) {
        state.zoom = +b.getAttribute('data-month-zoom');
        render();
      } else if ((b = t.closest('[data-back]'))) {
        state.zoom = null;
        render();
      } else if ((b = t.closest('[data-span]'))) {
        var model = b.getAttribute('data-model');
        var w = windowsFor(filtered()).filter(function (x) { return x.key === b.getAttribute('data-span'); })[0];
        var g = w ? findGroup('retire|' + w.end + '|' + (w.est ? 1 : 0)) : null;
        setFocus({ group: g, model: w && uniqueModels(w.entries).length > 1 ? null : model });
      } else if ((b = t.closest('[data-key]'))) {
        var group = findGroup(b.getAttribute('data-key')) || (b.getAttribute('data-key2') ? findGroup(b.getAttribute('data-key2')) : null);
        var byModel = b.classList.contains('rp-chip') || b.classList.contains('rp-tl__row');
        if (group) setFocus({ group: group, model: byModel ? b.getAttribute('data-model') : null });
      } else if ((b = t.closest('[data-day]'))) {
        var day = +b.getAttribute('data-day');
        var first = groupEvents(events(filtered())).filter(function (x) { return x.date === day; })[0];
        if (state.v === 'calendar' && state.zoom == null && ['3m', '6m', '12m', 'all'].indexOf(state.h) >= 0 && first) {
          setFocus({ group: first, model: null, day: day });
        } else {
          setFocus({ group: first || null, model: null, day: day });
        }
      }
    });
    el.addEventListener('keydown', function (event) {
      if ((event.key === 'Enter' || event.key === ' ') && event.target.classList && event.target.classList.contains('rp-item')) {
        event.preventDefault();
        event.target.click();
      }
    });
    qInput.addEventListener('input', function () { state.q = qInput.value; state.focus = null; render(); });
    allInput.addEventListener('change', function () { state.all = allInput.checked; render(); });

    render();
  }

  function mountAll() { document.querySelectorAll('[data-retire-planner]').forEach(mount); }
  if (typeof window.document$ !== 'undefined' && window.document$.subscribe) {
    window.document$.subscribe(mountAll);
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mountAll);
  } else {
    mountAll();
  }
})();
