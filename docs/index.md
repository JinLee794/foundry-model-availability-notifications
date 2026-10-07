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
        <span class="dash-freshness"><span class="dash-freshness__dot"></span>Updated Oct 7, 2026</span>
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

<section class="insights" aria-labelledby="insights-title">
    <header class="insights__head">
        <h2 id="insights-title">At a glance</h2>
        <a class="md-button md-button--primary insights__cta" href="explorer/">Open the availability explorer →</a>
    </header>
    <div class="chart-grid">
        <div class="chart-card">
            <h3>Lifecycle mix</h3>
            <p>Most urgent stage of each model. Click to filter.</p>
            <div class="donut">
        <svg viewBox="0 0 42 42" role="img" aria-label="Models by lifecycle stage">
            <circle class="donut__ring" r="15.9155" cx="21" cy="21"></circle>
            <circle class="donut__seg donut__seg--danger" r="15.9155" cx="21" cy="21" stroke-dasharray="13.636 86.364" stroke-dashoffset="25.000"><title>Retiring ≤ 90 days: 21</title></circle><circle class="donut__seg donut__seg--caution" r="15.9155" cx="21" cy="21" stroke-dasharray="5.195 94.805" stroke-dashoffset="11.364"><title>Deprecated: 8</title></circle><circle class="donut__seg donut__seg--success" r="15.9155" cx="21" cy="21" stroke-dasharray="5.844 94.156" stroke-dashoffset="6.169"><title>Generally available: 9</title></circle><circle class="donut__seg donut__seg--neutral" r="15.9155" cx="21" cy="21" stroke-dasharray="72.078 27.922" stroke-dashoffset="0.325"><title>No date published: 111</title></circle><circle class="donut__seg donut__seg--muted" r="15.9155" cx="21" cy="21" stroke-dasharray="3.247 96.753" stroke-dashoffset="-71.753"><title>Retired: 5</title></circle>
            <text x="21" y="20.5" class="donut__value">154</text>
            <text x="21" y="26" class="donut__label">models</text>
        </svg>
        <ul class="chart-legend"><li><a href="explorer/#lc=risk"><span class="chart-swatch chart-swatch--danger"></span>Retiring ≤ 90 days<b>21</b></a></li><li><a href="explorer/#lc=deprecated"><span class="chart-swatch chart-swatch--caution"></span>Deprecated<b>8</b></a></li><li><a href="explorer/#lc=ga"><span class="chart-swatch chart-swatch--success"></span>Generally available<b>9</b></a></li><li><a href="explorer/#lc=untracked"><span class="chart-swatch chart-swatch--neutral"></span>No date published<b>111</b></a></li><li><a href="explorer/#lc=retired"><span class="chart-swatch chart-swatch--muted"></span>Retired<b>5</b></a></li></ul>
    </div>
        </div>
        <div class="chart-card">
            <h3>Deployment options</h3>
            <p>Models offering each deployment type somewhere.</p>
            <ul class="hbars"><li><a class="hbar" href="explorer/#t=gs" title="58 of 154 models"><span class="hbar__label">Global</span><span class="hbar__track"><span class="hbar__fill hbar__fill--paygo" style="width:56.9%"></span></span><span class="hbar__value">58</span></a></li><li><a class="hbar" href="explorer/#t=dz" title="28 of 154 models"><span class="hbar__label">Data Zone</span><span class="hbar__track"><span class="hbar__fill hbar__fill--paygo" style="width:27.5%"></span></span><span class="hbar__value">28</span></a></li><li><a class="hbar" href="explorer/#t=rs" title="102 of 154 models"><span class="hbar__label">Regional</span><span class="hbar__track"><span class="hbar__fill hbar__fill--paygo" style="width:100.0%"></span></span><span class="hbar__value">102</span></a></li><li><a class="hbar" href="explorer/#t=gp" title="18 of 154 models"><span class="hbar__label">Global PTU</span><span class="hbar__track"><span class="hbar__fill hbar__fill--ptu" style="width:17.6%"></span></span><span class="hbar__value">18</span></a></li><li><a class="hbar" href="explorer/#t=dp" title="19 of 154 models"><span class="hbar__label">Data Zone PTU</span><span class="hbar__track"><span class="hbar__fill hbar__fill--ptu" style="width:18.6%"></span></span><span class="hbar__value">19</span></a></li><li><a class="hbar" href="explorer/#t=rp" title="27 of 154 models"><span class="hbar__label">Regional PTU</span><span class="hbar__track"><span class="hbar__fill hbar__fill--ptu" style="width:26.5%"></span></span><span class="hbar__value">27</span></a></li><li><a class="hbar" href="explorer/#t=bt" title="12 of 154 models"><span class="hbar__label">Batch</span><span class="hbar__track"><span class="hbar__fill hbar__fill--batch" style="width:11.8%"></span></span><span class="hbar__value">12</span></a></li><li><a class="hbar" href="explorer/#t=mp" title="52 of 154 models"><span class="hbar__label">Partner</span><span class="hbar__track"><span class="hbar__fill hbar__fill--partner" style="width:51.0%"></span></span><span class="hbar__value">52</span></a></li></ul>
        </div>
        <div class="chart-card">
            <h3>Providers</h3>
            <p>Models tracked per provider.</p>
            <ul class="hbars"><li><a class="hbar" href="explorer/#p=OpenAI" title="71 of 154 models"><span class="hbar__label">OpenAI</span><span class="hbar__track"><span class="hbar__fill hbar__fill--accent" style="width:100.0%"></span></span><span class="hbar__value">71</span></a></li><li><a class="hbar" href="explorer/#p=Meta" title="14 of 154 models"><span class="hbar__label">Meta</span><span class="hbar__track"><span class="hbar__fill hbar__fill--accent" style="width:19.7%"></span></span><span class="hbar__value">14</span></a></li><li><a class="hbar" href="explorer/#p=Anthropic" title="13 of 154 models"><span class="hbar__label">Anthropic</span><span class="hbar__track"><span class="hbar__fill hbar__fill--accent" style="width:18.3%"></span></span><span class="hbar__value">13</span></a></li><li><a class="hbar" href="explorer/#p=Microsoft" title="12 of 154 models"><span class="hbar__label">Microsoft</span><span class="hbar__track"><span class="hbar__fill hbar__fill--accent" style="width:16.9%"></span></span><span class="hbar__value">12</span></a></li><li><a class="hbar" href="explorer/#p=Mistral%20AI" title="10 of 154 models"><span class="hbar__label">Mistral AI</span><span class="hbar__track"><span class="hbar__fill hbar__fill--accent" style="width:14.1%"></span></span><span class="hbar__value">10</span></a></li><li><a class="hbar" href="explorer/#p=Cohere" title="9 of 154 models"><span class="hbar__label">Cohere</span><span class="hbar__track"><span class="hbar__fill hbar__fill--accent" style="width:12.7%"></span></span><span class="hbar__value">9</span></a></li><li><a class="hbar" href="explorer/#p=DeepSeek" title="7 of 154 models"><span class="hbar__label">DeepSeek</span><span class="hbar__track"><span class="hbar__fill hbar__fill--accent" style="width:9.9%"></span></span><span class="hbar__value">7</span></a></li><li><a class="hbar" href="explorer/#p=xAI" title="6 of 154 models"><span class="hbar__label">xAI</span><span class="hbar__track"><span class="hbar__fill hbar__fill--accent" style="width:8.5%"></span></span><span class="hbar__value">6</span></a></li><li><a class="hbar" href="explorer/" title="12 of 154 models"><span class="hbar__label">Other providers</span><span class="hbar__track"><span class="hbar__fill hbar__fill--muted" style="width:16.9%"></span></span><span class="hbar__value">12</span></a></li></ul>
        </div>
        <div class="chart-card chart-card--wide">
            <h3>Retirements ahead</h3>
            <p>Model versions retiring per month over the next 12 months.</p>
            <ol class="vcols" aria-label="Retirements per month"><li class="vcol" tabindex="0" data-tip-title="October 2026: 9 versions retiring (4 no-earlier-than)" data-tip="gpt-4.1 2025-04-14, gpt-4.1-mini 2025-04-14, gpt-4.1-nano 2025-04-14, o3 2025-04-16, o4-mini 2025-04-16, text-embedding-3-large 1, text-embedding-3-small 1, text-embedding-ada-002 2 +1 more"><span class="vcol__bar" style="--h:100.0%"><span class="vcol__firm" style="--h:55.6%"></span></span><b>9</b><small>Oct</small></li><li class="vcol" tabindex="0" data-tip-title="November 2026: 1 version retiring" data-tip="codex-mini 2025-05-16"><span class="vcol__bar" style="--h:11.1%"><span class="vcol__firm" style="--h:100.0%"></span></span><b>1</b><small>Nov</small></li><li class="vcol" tabindex="0" data-tip-title="December 2026: 6 versions retiring (4 no-earlier-than)" data-tip="o3-pro 2025-06-10, o3-deep-research 2025-06-26, gpt-realtime-mini 2025-12-15, gpt-4o-mini-transcribe 2025-12-15, gpt-4o-mini-tts 2025-12-15, gpt-image-1.5 2025-12-16"><span class="vcol__bar" style="--h:66.7%"><span class="vcol__firm" style="--h:33.3%"></span></span><b>6</b><small>Dec</small></li><li class="vcol vcol--empty" tabindex="0" data-tip-title="January 2027: 0 versions retiring" data-tip="Nothing scheduled."><span class="vcol__bar" style="--h:0.0%"><span class="vcol__firm" style="--h:0.0%"></span></span><b></b><small>Jan</small></li><li class="vcol" tabindex="0" data-tip-title="February 2027: 4 versions retiring" data-tip="gpt-5-mini 2025-08-07, gpt-5-nano 2025-08-07, gpt-audio 2025-08-28, gpt-realtime 2025-08-28"><span class="vcol__bar" style="--h:44.4%"><span class="vcol__firm" style="--h:100.0%"></span></span><b>4</b><small>Feb</small></li><li class="vcol" tabindex="0" data-tip-title="March 2027: 1 version retiring" data-tip="gpt-5-codex 2025-09-15"><span class="vcol__bar" style="--h:11.1%"><span class="vcol__firm" style="--h:100.0%"></span></span><b>1</b><small>Mar</small></li><li class="vcol" tabindex="0" data-tip-title="April 2027: 4 versions retiring" data-tip="gpt-5-pro 2025-10-06, gpt-4o-transcribe-diarize 2025-10-15, gpt-audio-mini 2025-10-06, gpt-image-1-mini 2025-10-06"><span class="vcol__bar" style="--h:44.4%"><span class="vcol__firm" style="--h:100.0%"></span></span><b>4</b><small>Apr</small></li><li class="vcol" tabindex="0" data-tip-title="May 2027: 5 versions retiring (1 no-earlier-than)" data-tip="model-router 2025-11-18, gpt-5.1 2025-11-13, gpt-5.1-codex 2025-11-13, gpt-5.1-codex-mini 2025-11-13, gpt-5.2 2025-12-11"><span class="vcol__bar" style="--h:55.6%"><span class="vcol__firm" style="--h:80.0%"></span></span><b>5</b><small>May</small></li><li class="vcol vcol--empty" tabindex="0" data-tip-title="June 2027: 0 versions retiring" data-tip="Nothing scheduled."><span class="vcol__bar" style="--h:0.0%"><span class="vcol__firm" style="--h:0.0%"></span></span><b></b><small>Jun</small></li><li class="vcol vcol--empty" tabindex="0" data-tip-title="July 2027: 0 versions retiring" data-tip="Nothing scheduled."><span class="vcol__bar" style="--h:0.0%"><span class="vcol__firm" style="--h:0.0%"></span></span><b></b><small>Jul</small></li><li class="vcol vcol--empty" tabindex="0" data-tip-title="August 2027: 0 versions retiring" data-tip="Nothing scheduled."><span class="vcol__bar" style="--h:0.0%"><span class="vcol__firm" style="--h:0.0%"></span></span><b></b><small>Aug</small></li><li class="vcol vcol--empty" tabindex="0" data-tip-title="September 2027: 0 versions retiring" data-tip="Nothing scheduled."><span class="vcol__bar" style="--h:0.0%"><span class="vcol__firm" style="--h:0.0%"></span></span><b></b><small>Sep</small></li></ol>
    <p class="chart-note"><span class="chart-swatch chart-swatch--danger"></span>Firm date <span class="chart-swatch chart-swatch--warning"></span>No-earlier-than date</p>
        </div>
        <div class="chart-card chart-card--full">
            <h3>Where models run</h3>
            <p>Models available per region, grouped by geography. Darker means more models.</p>
            <div class="heatmap"><div class="heat-group"><h4>Americas</h4><div class="heat-tiles"><a class="heat-tile" href="explorer/#rg=East%20US%202" style="--i:1.00" tabindex="0" data-tip-title="East US 2" data-tip="146 of 154 models available here. Click to see which."><span>East US 2</span><b>146</b></a><a class="heat-tile" href="explorer/#rg=West%20US" style="--i:0.85" tabindex="0" data-tip-title="West US" data-tip="124 of 154 models available here. Click to see which."><span>West US</span><b>124</b></a><a class="heat-tile" href="explorer/#rg=West%20US%203" style="--i:0.85" tabindex="0" data-tip-title="West US 3" data-tip="124 of 154 models available here. Click to see which."><span>West US 3</span><b>124</b></a><a class="heat-tile" href="explorer/#rg=East%20US" style="--i:0.84" tabindex="0" data-tip-title="East US" data-tip="123 of 154 models available here. Click to see which."><span>East US</span><b>123</b></a><a class="heat-tile" href="explorer/#rg=North%20Central%20US" style="--i:0.83" tabindex="0" data-tip-title="North Central US" data-tip="121 of 154 models available here. Click to see which."><span>North Central US</span><b>121</b></a><a class="heat-tile" href="explorer/#rg=South%20Central%20US" style="--i:0.81" tabindex="0" data-tip-title="South Central US" data-tip="118 of 154 models available here. Click to see which."><span>South Central US</span><b>118</b></a><a class="heat-tile" href="explorer/#rg=Central%20US" style="--i:0.74" tabindex="0" data-tip-title="Central US" data-tip="108 of 154 models available here. Click to see which."><span>Central US</span><b>108</b></a><a class="heat-tile" href="explorer/#rg=Canada%20Central" style="--i:0.62" tabindex="0" data-tip-title="Canada Central" data-tip="91 of 154 models available here. Click to see which."><span>Canada Central</span><b>91</b></a><a class="heat-tile" href="explorer/#rg=Brazil%20South" style="--i:0.55" tabindex="0" data-tip-title="Brazil South" data-tip="81 of 154 models available here. Click to see which."><span>Brazil South</span><b>81</b></a><a class="heat-tile" href="explorer/#rg=Canada%20East" style="--i:0.55" tabindex="0" data-tip-title="Canada East" data-tip="81 of 154 models available here. Click to see which."><span>Canada East</span><b>81</b></a><a class="heat-tile" href="explorer/#rg=West%20Central%20US" style="--i:0.37" tabindex="0" data-tip-title="West Central US" data-tip="54 of 154 models available here. Click to see which."><span>West Central US</span><b>54</b></a><a class="heat-tile" href="explorer/#rg=West%20US%202" style="--i:0.26" tabindex="0" data-tip-title="West US 2" data-tip="38 of 154 models available here. Click to see which."><span>West US 2</span><b>38</b></a></div></div><div class="heat-group"><h4>Europe</h4><div class="heat-tiles"><a class="heat-tile" href="explorer/#rg=Sweden%20Central" style="--i:0.99" tabindex="0" data-tip-title="Sweden Central" data-tip="144 of 154 models available here. Click to see which."><span>Sweden Central</span><b>144</b></a><a class="heat-tile" href="explorer/#rg=France%20Central" style="--i:0.63" tabindex="0" data-tip-title="France Central" data-tip="92 of 154 models available here. Click to see which."><span>France Central</span><b>92</b></a><a class="heat-tile" href="explorer/#rg=West%20Europe" style="--i:0.60" tabindex="0" data-tip-title="West Europe" data-tip="87 of 154 models available here. Click to see which."><span>West Europe</span><b>87</b></a><a class="heat-tile" href="explorer/#rg=Poland%20Central" style="--i:0.58" tabindex="0" data-tip-title="Poland Central" data-tip="85 of 154 models available here. Click to see which."><span>Poland Central</span><b>85</b></a><a class="heat-tile" href="explorer/#rg=Norway%20East" style="--i:0.57" tabindex="0" data-tip-title="Norway East" data-tip="83 of 154 models available here. Click to see which."><span>Norway East</span><b>83</b></a><a class="heat-tile" href="explorer/#rg=Switzerland%20North" style="--i:0.56" tabindex="0" data-tip-title="Switzerland North" data-tip="82 of 154 models available here. Click to see which."><span>Switzerland North</span><b>82</b></a><a class="heat-tile" href="explorer/#rg=Germany%20West%20Central" style="--i:0.55" tabindex="0" data-tip-title="Germany West Central" data-tip="81 of 154 models available here. Click to see which."><span>Germany West Central</span><b>81</b></a><a class="heat-tile" href="explorer/#rg=Italy%20North" style="--i:0.55" tabindex="0" data-tip-title="Italy North" data-tip="81 of 154 models available here. Click to see which."><span>Italy North</span><b>81</b></a><a class="heat-tile" href="explorer/#rg=Spain%20Central" style="--i:0.55" tabindex="0" data-tip-title="Spain Central" data-tip="81 of 154 models available here. Click to see which."><span>Spain Central</span><b>81</b></a><a class="heat-tile" href="explorer/#rg=UK%20South" style="--i:0.55" tabindex="0" data-tip-title="UK South" data-tip="81 of 154 models available here. Click to see which."><span>UK South</span><b>81</b></a><a class="heat-tile" href="explorer/#rg=Switzerland%20West" style="--i:0.55" tabindex="0" data-tip-title="Switzerland West" data-tip="80 of 154 models available here. Click to see which."><span>Switzerland West</span><b>80</b></a><a class="heat-tile" href="explorer/#rg=UK%20West" style="--i:0.26" tabindex="0" data-tip-title="UK West" data-tip="38 of 154 models available here. Click to see which."><span>UK West</span><b>38</b></a><a class="heat-tile" href="explorer/#rg=North%20Europe" style="--i:0.18" tabindex="0" data-tip-title="North Europe" data-tip="26 of 154 models available here. Click to see which."><span>North Europe</span><b>26</b></a></div></div><div class="heat-group"><h4>Asia Pacific</h4><div class="heat-tiles"><a class="heat-tile" href="explorer/#rg=South%20India" style="--i:0.68" tabindex="0" data-tip-title="South India" data-tip="100 of 154 models available here. Click to see which."><span>South India</span><b>100</b></a><a class="heat-tile" href="explorer/#rg=Australia%20East" style="--i:0.56" tabindex="0" data-tip-title="Australia East" data-tip="82 of 154 models available here. Click to see which."><span>Australia East</span><b>82</b></a><a class="heat-tile" href="explorer/#rg=Japan%20East" style="--i:0.55" tabindex="0" data-tip-title="Japan East" data-tip="81 of 154 models available here. Click to see which."><span>Japan East</span><b>81</b></a><a class="heat-tile" href="explorer/#rg=Korea%20Central" style="--i:0.55" tabindex="0" data-tip-title="Korea Central" data-tip="81 of 154 models available here. Click to see which."><span>Korea Central</span><b>81</b></a><a class="heat-tile" href="explorer/#rg=Southeast%20Asia" style="--i:0.29" tabindex="0" data-tip-title="Southeast Asia" data-tip="43 of 154 models available here. Click to see which."><span>Southeast Asia</span><b>43</b></a><a class="heat-tile" href="explorer/#rg=Japan%20West" style="--i:0.26" tabindex="0" data-tip-title="Japan West" data-tip="38 of 154 models available here. Click to see which."><span>Japan West</span><b>38</b></a></div></div><div class="heat-group"><h4>Middle East & Africa</h4><div class="heat-tiles"><a class="heat-tile" href="explorer/#rg=UAE%20North" style="--i:0.62" tabindex="0" data-tip-title="UAE North" data-tip="91 of 154 models available here. Click to see which."><span>UAE North</span><b>91</b></a><a class="heat-tile" href="explorer/#rg=South%20Africa%20North" style="--i:0.55" tabindex="0" data-tip-title="South Africa North" data-tip="81 of 154 models available here. Click to see which."><span>South Africa North</span><b>81</b></a></div></div><div class="heat-group"><h4>US Government</h4><div class="heat-tiles"><a class="heat-tile" href="explorer/#rg=usgovarizona" style="--i:0.08" tabindex="0" data-tip-title="usgovarizona" data-tip="11 of 154 models available here. Click to see which."><span>usgovarizona</span><b>11</b></a><a class="heat-tile" href="explorer/#rg=usgovvirginia" style="--i:0.07" tabindex="0" data-tip-title="usgovvirginia" data-tip="10 of 154 models available here. Click to see which."><span>usgovvirginia</span><b>10</b></a></div></div></div>
        </div>
    </div>
</section>

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
            <div class="watch-item__meter" aria-hidden="true"><span style="width:96%"></span></div>
        </div>
        <span class="watch-item__countdown">6<small>days</small></span>
    </li>
<li class="watch-item watch-item--danger">
        <div class="watch-item__main">
            <div class="watch-item__title"><a href="models/gpt-4-1-mini/">gpt-4.1-mini</a> <code>2025-04-14</code></div>
            <div class="watch-item__meta">Oct 14, 2026 <span class="watch-item__replacement">→ <a href="models/gpt-5-mini/">gpt-5-mini</a></span></div>
            <div class="watch-item__meter" aria-hidden="true"><span style="width:96%"></span></div>
        </div>
        <span class="watch-item__countdown">6<small>days</small></span>
    </li>
<li class="watch-item watch-item--danger">
        <div class="watch-item__main">
            <div class="watch-item__title"><a href="models/gpt-4-1-nano/">gpt-4.1-nano</a> <code>2025-04-14</code></div>
            <div class="watch-item__meta">Oct 14, 2026 <span class="watch-item__replacement">→ <a href="models/gpt-5-nano/">gpt-5-nano</a></span></div>
            <div class="watch-item__meter" aria-hidden="true"><span style="width:96%"></span></div>
        </div>
        <span class="watch-item__countdown">6<small>days</small></span>
    </li>
<li class="watch-item watch-item--danger">
        <div class="watch-item__main">
            <div class="watch-item__title"><a href="models/o3/">o3</a> <code>2025-04-16</code></div>
            <div class="watch-item__meta">Oct 16, 2026 </div>
            <div class="watch-item__meter" aria-hidden="true"><span style="width:95%"></span></div>
        </div>
        <span class="watch-item__countdown">8<small>days</small></span>
    </li>
<li class="watch-item watch-item--danger">
        <div class="watch-item__main">
            <div class="watch-item__title"><a href="models/o4-mini/">o4-mini</a> <code>2025-04-16</code></div>
            <div class="watch-item__meta">Oct 16, 2026 </div>
            <div class="watch-item__meter" aria-hidden="true"><span style="width:95%"></span></div>
        </div>
        <span class="watch-item__countdown">8<small>days</small></span>
    </li>
<li class="watch-item watch-item--danger">
        <div class="watch-item__main">
            <div class="watch-item__title"><a href="models/text-embedding-3-large/">text-embedding-3-large</a> <code>1</code></div>
            <div class="watch-item__meta">≥ Oct 30, 2026 </div>
            <div class="watch-item__meter" aria-hidden="true"><span style="width:87%"></span></div>
        </div>
        <span class="watch-item__countdown">≥ 22<small>days</small></span>
    </li>
<li class="watch-item watch-item--danger">
        <div class="watch-item__main">
            <div class="watch-item__title"><a href="models/text-embedding-3-small/">text-embedding-3-small</a> <code>1</code></div>
            <div class="watch-item__meta">≥ Oct 30, 2026 </div>
            <div class="watch-item__meter" aria-hidden="true"><span style="width:87%"></span></div>
        </div>
        <span class="watch-item__countdown">≥ 22<small>days</small></span>
    </li>
<li class="watch-item watch-item--danger">
        <div class="watch-item__main">
            <div class="watch-item__title"><a href="models/text-embedding-ada-002/">text-embedding-ada-002</a> <code>2</code></div>
            <div class="watch-item__meta">≥ Oct 30, 2026 </div>
            <div class="watch-item__meter" aria-hidden="true"><span style="width:87%"></span></div>
        </div>
        <span class="watch-item__countdown">≥ 22<small>days</small></span>
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

<nav class="explore-row" aria-label="Explore">
    <a href="explorer/"><strong>Availability explorer</strong><span>Every model × region in one grid</span></a>
    <a href="ptu/"><strong>PTU guide</strong><span>Is provisioned right for you?</span></a>
    <a href="lifecycle/"><strong>Lifecycle guide</strong><span>What each badge means</span></a>
    <a href="models/"><strong>All models</strong><span>Sortable catalog table</span></a>
</nav>

<p class="dash-footnote">Snapshot generated 2026-10-07 14:13 UTC · retirement data as of 2026-01-23. Validate active deployments with the Models API and Azure Service Health.</p>
