---
hide:
  - navigation
  - toc
---

<section class="dash-hero">
    <div class="dash-hero__head">
        <div>
            <p class="dash-eyebrow">Azure AI Foundry · model tracker</p>
            <h1 class="dash-title">Foundry Model Availability</h1>
            <p class="dash-lede">Where every model runs, how you can deploy it, and when it retires.</p>
        </div>
        <span class="dash-freshness"><span class="dash-freshness__dot"></span>Updated Oct 5, 2026</span>
    </div>
    <div class="model-finder" data-model-finder data-src="assets/model-index.json" data-root="">
    <div class="model-finder__field">
        <svg class="model-finder__icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M9.5 3a6.5 6.5 0 0 1 5.25 10.33l5.46 5.46-1.42 1.42-5.46-5.46A6.5 6.5 0 1 1 9.5 3m0 2a4.5 4.5 0 1 0 0 9 4.5 4.5 0 0 0 0-9"/></svg>
        <input type="search" class="model-finder__input" placeholder="Search models — e.g. gpt-5, o4-mini, claude, embedding" autocomplete="off" spellcheck="false" aria-label="Find a model" aria-controls="model-finder-results">
        <kbd class="model-finder__kbd">Ctrl K</kbd>
    </div>
    <div class="model-finder__chips" role="group" aria-label="Quick filters">
        <button type="button" class="finder-chip is-active" data-filter="all">All</button>
        <button type="button" class="finder-chip" data-filter="risk">Retiring soon</button>
        <button type="button" class="finder-chip" data-filter="preview">Preview</button>
        <button type="button" class="finder-chip" data-filter="Provisioned">Provisioned (PTU)</button>
        <button type="button" class="finder-chip" data-filter="Datazone">Data Zone</button>
        <span class="model-finder__families" data-family-chips></span>
    </div>
    <div class="model-finder__results" id="model-finder-results" role="listbox" aria-live="polite" hidden></div>
</div>
    <div class="quick-picks"><span>Widest availability</span><a class="quick-pick" href="models/codestral-2501/">Codestral-2501 <small>31</small></a> <a class="quick-pick" href="models/cohere-command-a/">cohere-command-a <small>31</small></a> <a class="quick-pick" href="models/cohere-command-a-plus-05-2026/">Cohere-command-a-plus-05-2026 <small>31</small></a> <a class="quick-pick" href="models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast <small>31</small></a> <a class="quick-pick" href="models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro <small>31</small></a> <a class="quick-pick" href="models/deepseek-v3-2/">DeepSeek-V3.2 <small>31</small></a></div>
</section>

<div class="kpi-grid">
    <a class="kpi kpi--accent" href="models/">
        <span class="kpi__label">Models tracked</span>
        <strong class="kpi__value">154</strong>
        <span class="kpi__hint">from 12 providers</span>
    </a>
    <a class="kpi kpi--info" href="by-region/">
        <span class="kpi__label">Azure regions</span>
        <strong class="kpi__value">35</strong>
        <span class="kpi__hint">with at least one model</span>
    </a>
    <a class="kpi kpi--danger" href="retirements/">
        <span class="kpi__label">Retiring in 90 days</span>
        <strong class="kpi__value">16</strong>
        <span class="kpi__hint">9 within 30 days</span>
    </a>
    <a class="kpi kpi--success" href="history/?date=2026-10-01">
        <span class="kpi__label">Latest change run</span>
        <strong class="kpi__value"><span class="kpi__plus">+28</span> <span class="kpi__minus">−0</span></strong>
        <span class="kpi__hint">Oct 1, 2026 · 1 model</span>
    </a>
</div>

<div class="dash-grid">
    <section class="dash-panel" aria-labelledby="watchlist-title">
        <header class="dash-panel__head">
            <h2 id="watchlist-title">Retirement watchlist</h2>
            <a href="retirements/">All retirements</a>
        </header>
        <p class="dash-panel__sub">Next scheduled retirements by version. 12 versions already retired.</p>
        <ul class="watchlist"><li class="watch-item watch-item--danger">
        <div class="watch-item__main">
            <div class="watch-item__title"><a href="models/gpt-4-1/">gpt-4.1</a> <code>2025-04-14</code></div>
            <div class="watch-item__meta">Oct 14, 2026 <span class="watch-item__replacement">→ <a href="models/gpt-5/">gpt-5</a></span></div>
            <div class="watch-item__meter" aria-hidden="true"><span style="width:95%"></span></div>
        </div>
        <span class="watch-item__countdown">8<small>days</small></span>
    </li>
<li class="watch-item watch-item--danger">
        <div class="watch-item__main">
            <div class="watch-item__title"><a href="models/gpt-4-1-mini/">gpt-4.1-mini</a> <code>2025-04-14</code></div>
            <div class="watch-item__meta">Oct 14, 2026 <span class="watch-item__replacement">→ <a href="models/gpt-5-mini/">gpt-5-mini</a></span></div>
            <div class="watch-item__meter" aria-hidden="true"><span style="width:95%"></span></div>
        </div>
        <span class="watch-item__countdown">8<small>days</small></span>
    </li>
<li class="watch-item watch-item--danger">
        <div class="watch-item__main">
            <div class="watch-item__title"><a href="models/gpt-4-1-nano/">gpt-4.1-nano</a> <code>2025-04-14</code></div>
            <div class="watch-item__meta">Oct 14, 2026 <span class="watch-item__replacement">→ <a href="models/gpt-5-nano/">gpt-5-nano</a></span></div>
            <div class="watch-item__meter" aria-hidden="true"><span style="width:95%"></span></div>
        </div>
        <span class="watch-item__countdown">8<small>days</small></span>
    </li>
<li class="watch-item watch-item--danger">
        <div class="watch-item__main">
            <div class="watch-item__title"><a href="models/o3/">o3</a> <code>2025-04-16</code></div>
            <div class="watch-item__meta">Oct 16, 2026 </div>
            <div class="watch-item__meter" aria-hidden="true"><span style="width:94%"></span></div>
        </div>
        <span class="watch-item__countdown">10<small>days</small></span>
    </li>
<li class="watch-item watch-item--danger">
        <div class="watch-item__main">
            <div class="watch-item__title"><a href="models/o4-mini/">o4-mini</a> <code>2025-04-16</code></div>
            <div class="watch-item__meta">Oct 16, 2026 </div>
            <div class="watch-item__meter" aria-hidden="true"><span style="width:94%"></span></div>
        </div>
        <span class="watch-item__countdown">10<small>days</small></span>
    </li>
<li class="watch-item watch-item--danger">
        <div class="watch-item__main">
            <div class="watch-item__title"><a href="models/text-embedding-3-large/">text-embedding-3-large</a> <code>1</code></div>
            <div class="watch-item__meta">≥ Oct 30, 2026 </div>
            <div class="watch-item__meter" aria-hidden="true"><span style="width:86%"></span></div>
        </div>
        <span class="watch-item__countdown">≥ 24<small>days</small></span>
    </li>
<li class="watch-item watch-item--danger">
        <div class="watch-item__main">
            <div class="watch-item__title"><a href="models/text-embedding-3-small/">text-embedding-3-small</a> <code>1</code></div>
            <div class="watch-item__meta">≥ Oct 30, 2026 </div>
            <div class="watch-item__meter" aria-hidden="true"><span style="width:86%"></span></div>
        </div>
        <span class="watch-item__countdown">≥ 24<small>days</small></span>
    </li>
<li class="watch-item watch-item--danger">
        <div class="watch-item__main">
            <div class="watch-item__title"><a href="models/text-embedding-ada-002/">text-embedding-ada-002</a> <code>2</code></div>
            <div class="watch-item__meta">≥ Oct 30, 2026 </div>
            <div class="watch-item__meter" aria-hidden="true"><span style="width:86%"></span></div>
        </div>
        <span class="watch-item__countdown">≥ 24<small>days</small></span>
    </li></ul><a class="dash-panel__more" href="retirements/">22 more scheduled retirements →</a>
    </section>
    <section class="dash-panel" aria-labelledby="changes-title">
        <header class="dash-panel__head">
            <h2 id="changes-title">Latest availability changes</h2>
            <a href="history/">Full history</a>
        </header>
        <p class="dash-panel__sub">Regional SKU additions and removals detected by the watcher.</p>
        <ul class="feed"><li class="feed-item feed-item--added">
        <span class="feed-item__icon" aria-label="Added">+</span>
        <div class="feed-item__body">
            <div class="feed-item__title"><a href="models/gpt-6-1-sol/">gpt-6.1-sol</a> <a class="feed-sku" href="by-sku/?sku=Deployments%20Provisioned">Deployments Provisioned</a></div>
            <div class="feed-item__meta"><time datetime="2026-10-01">Oct 1</time> · <a class="feed-region" href="by-region/?region=Australia%20East">Australia East</a> <span class="feed-more">+27</span></div>
        </div>
    </li>
<li class="feed-item feed-item--added">
        <span class="feed-item__icon" aria-label="Added">+</span>
        <div class="feed-item__body">
            <div class="feed-item__title"><a href="models/gpt-6-1-sol/">gpt-6.1-sol</a> <a class="feed-sku" href="by-sku/?sku=Deployments%20Standard">Deployments Standard</a></div>
            <div class="feed-item__meta"><time datetime="2026-09-30">Sep 30</time> · <a class="feed-region" href="by-region/?region=Australia%20East">Australia East</a> <span class="feed-more">+27</span></div>
        </div>
    </li>
<li class="feed-item feed-item--added">
        <span class="feed-item__icon" aria-label="Added">+</span>
        <div class="feed-item__body">
            <div class="feed-item__title"><a href="models/claude-sonnet-5-5/">claude-sonnet-5-5</a> <a class="feed-sku" href="by-sku/?sku=Marketplace%20Deployments%20Standard">Marketplace Deployments Standard</a></div>
            <div class="feed-item__meta"><time datetime="2026-09-29">Sep 29</time> · <a class="feed-region" href="by-region/?region=Central%20US">Central US</a> <span class="feed-more">+8</span></div>
        </div>
    </li>
<li class="feed-item feed-item--added">
        <span class="feed-item__icon" aria-label="Added">+</span>
        <div class="feed-item__body">
            <div class="feed-item__title"><a href="models/gpt-4-1/">gpt-4.1</a> <a class="feed-sku" href="by-sku/?sku=Deployments%20Provisioned">Deployments Provisioned</a></div>
            <div class="feed-item__meta"><time datetime="2026-09-26">Sep 26</time> · <a class="feed-region" href="by-region/?region=North%20Europe">North Europe</a></div>
        </div>
    </li>
<li class="feed-item feed-item--added">
        <span class="feed-item__icon" aria-label="Added">+</span>
        <div class="feed-item__body">
            <div class="feed-item__title"><a href="models/gpt-4-1-mini/">gpt-4.1-mini</a> <a class="feed-sku" href="by-sku/?sku=Deployments%20Provisioned">Deployments Provisioned</a></div>
            <div class="feed-item__meta"><time datetime="2026-09-26">Sep 26</time> · <a class="feed-region" href="by-region/?region=North%20Europe">North Europe</a></div>
        </div>
    </li>
<li class="feed-item feed-item--added">
        <span class="feed-item__icon" aria-label="Added">+</span>
        <div class="feed-item__body">
            <div class="feed-item__title"><a href="models/gpt-4-1-nano/">gpt-4.1-nano</a> <a class="feed-sku" href="by-sku/?sku=Deployments%20Provisioned">Deployments Provisioned</a></div>
            <div class="feed-item__meta"><time datetime="2026-09-26">Sep 26</time> · <a class="feed-region" href="by-region/?region=North%20Europe">North Europe</a></div>
        </div>
    </li>
<li class="feed-item feed-item--added">
        <span class="feed-item__icon" aria-label="Added">+</span>
        <div class="feed-item__body">
            <div class="feed-item__title"><a href="models/gpt-4o/">gpt-4o</a> <a class="feed-sku" href="by-sku/?sku=Deployments%20Provisioned">Deployments Provisioned</a></div>
            <div class="feed-item__meta"><time datetime="2026-09-26">Sep 26</time> · <a class="feed-region" href="by-region/?region=North%20Europe">North Europe</a></div>
        </div>
    </li>
<li class="feed-item feed-item--added">
        <span class="feed-item__icon" aria-label="Added">+</span>
        <div class="feed-item__body">
            <div class="feed-item__title"><a href="models/gpt-4o-mini/">gpt-4o-mini</a> <a class="feed-sku" href="by-sku/?sku=Deployments%20Provisioned">Deployments Provisioned</a></div>
            <div class="feed-item__meta"><time datetime="2026-09-26">Sep 26</time> · <a class="feed-region" href="by-region/?region=North%20Europe">North Europe</a></div>
        </div>
    </li></ul><a class="dash-panel__more" href="history/">57 more changes in history →</a>
    </section>
</div>

<section class="dash-panel dash-panel--wide" aria-labelledby="lifecycle-title">
    <header class="dash-panel__head">
        <h2 id="lifecycle-title">How model lifecycles work</h2>
        <a href="lifecycle/">Lifecycle guide</a>
    </header>
    <ol class="stage-flow" aria-label="Model lifecycle stages">
    <li class="stage-node stage-node--preview">
        <span class="stage-node__dot" aria-hidden="true"></span>
        <strong>Preview</strong>
        <span class="stage-node__access">Evaluation only</span>
        <small>No SLA · can change or be force-upgraded</small>
    </li>
<li class="stage-node stage-node--ga">
        <span class="stage-node__dot" aria-hidden="true"></span>
        <strong>Generally available</strong><span class="stage-node__count" title="Models tracked in this stage">12</span>
        <span class="stage-node__access">All customers</span>
        <small>Production-ready · retirement date set at launch</small>
    </li>
<li class="stage-node stage-node--legacy">
        <span class="stage-node__dot" aria-hidden="true"></span>
        <strong>Legacy</strong>
        <span class="stage-node__access">All customers</span>
        <small>Newer model exists · start evaluating</small>
    </li>
<li class="stage-node stage-node--deprecated">
        <span class="stage-node__dot" aria-hidden="true"></span>
        <strong>Deprecated</strong><span class="stage-node__count" title="Models tracked in this stage">26</span>
        <span class="stage-node__access">Existing customers</span>
        <small>No new customers · migrate now</small>
    </li>
<li class="stage-node stage-node--retired">
        <span class="stage-node__dot" aria-hidden="true"></span>
        <strong>Retired</strong><span class="stage-node__count" title="Models tracked in this stage">5</span>
        <span class="stage-node__access">Nobody</span>
        <small>Removed · inference returns errors</small>
    </li>
</ol>
    <figure class="lc-diagram lc-diagram--compact">
    <figcaption><strong>GA model</strong> · about 18 months from launch to retirement</figcaption>
    <div class="lc-track">
        <div class="lc-phase lc-phase--ga" style="--w:66.67%"><span>Generally available · all customers</span></div>
        <div class="lc-phase lc-phase--deprecated" style="--w:33.33%"><span>Deprecated · existing customers</span></div>
        <div class="lc-zoom-bracket" style="--x:83.33%; --w:16.67%"></div>
    </div>
    <div class="lc-scale" aria-hidden="true"><span style="--x:0.00%">0</span><span style="--x:16.67%">3</span><span style="--x:33.33%">6</span><span style="--x:50.00%">9</span><span style="--x:66.67%">12</span><span style="--x:83.33%">15</span><span style="--x:100.00%">18</span><em>months</em></div>
    <ol class="lc-marks">
        <li class="lc-mark lc-mark--start" style="--x:0%"><b>Launch</b><span>Retirement date published</span></li>
        <li class="lc-mark" style="--x:66.67%"><b>12 mo · Deprecated</b><span>New customers blocked</span></li>
        <li class="lc-mark lc-mark--end lc-mark--danger" style="--x:100%"><b>18 mo · Retired</b><span>410 / errors</span></li>
    </ol>
    <div class="lc-zoom" aria-label="Final 90 days before retirement">
        <div class="lc-zoom__title">Final 90 days</div>
        <div class="lc-track lc-track--zoom">
            <div class="lc-phase lc-phase--eval" style="--w:33.33%"><span>Evaluate replacement</span></div>
            <div class="lc-phase lc-phase--notice" style="--w:33.33%"><span>Notifications</span></div>
            <div class="lc-phase lc-phase--ptu" style="--w:33.34%"><span>PTU migration</span></div>
        </div>
        <ol class="lc-marks">
            <li class="lc-mark lc-mark--start" style="--x:0%"><b>−90 d</b><span>Replacement named</span></li>
            <li class="lc-mark" style="--x:33.33%"><b>−60 d</b><span>Active notice</span></li>
            <li class="lc-mark" style="--x:66.67%"><b>−30 d</b><span>PTU migration window</span></li>
            <li class="lc-mark lc-mark--end lc-mark--danger" style="--x:100%"><b>Retire</b><span>Requests fail</span></li>
        </ol>
    </div>
</figure>
</section>

<nav class="explore-row" aria-label="Explore">
    <a href="models/"><strong>All models</strong><span>Filterable catalog</span></a>
    <a href="by-region/"><strong>By region</strong><span>What runs where</span></a>
    <a href="by-sku/"><strong>By deployment type</strong><span>Global, Data Zone, PTU</span></a>
    <a href="lifecycle/"><strong>Lifecycle guide</strong><span>Dates &amp; what to do</span></a>
</nav>

<p class="dash-footnote">Snapshot generated 2026-10-05 15:23 UTC · retirement data as of 2026-01-23. Validate active deployments with the Models API and Azure Service Health.</p>
