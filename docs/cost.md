---
hide:
  - navigation
  - toc
---

# Cost planner

<p class="page-lede">Describe your traffic once and compare the projected monthly bill across models, side by side. Then see at what volume a provisioned (PTU) reservation becomes cheaper than pay-as-you-go.</p>

<div class="cp" data-cost-planner data-src="../assets/pricing.json" data-root="../">
    <section class="cp-panel cp-inputs" aria-label="Workload">
        <div class="cp-row">
            <span class="cp-label">Workload</span>
            <div class="cp-chips" role="group" aria-label="Workload presets">
<button type="button" class="cp-chip" data-workload="chat" data-rpd="3000" data-in="1500" data-out="400" data-cache="30" data-batch="0">Chat assistant</button>
<button type="button" class="cp-chip" data-workload="rag" data-rpd="3000" data-in="6000" data-out="500" data-cache="50" data-batch="0">RAG Q&amp;A</button>
<button type="button" class="cp-chip" data-workload="agent" data-rpd="1000" data-in="20000" data-out="1500" data-cache="70" data-batch="0">Coding agent</button>
<button type="button" class="cp-chip" data-workload="batch" data-rpd="20000" data-in="3000" data-out="300" data-cache="0" data-batch="100">Batch summaries</button>
<button type="button" class="cp-chip" data-workload="embed" data-rpd="50000" data-in="500" data-out="0" data-cache="0" data-batch="0">Embeddings</button>
            </div>
        </div>
        <div class="cp-fields">
            <label class="cp-field"><span>Requests per day</span><input type="number" min="0" step="100" data-cp="rpd" inputmode="numeric"></label>
            <label class="cp-field"><span>Input tokens / request</span><input type="number" min="0" step="100" data-cp="in" inputmode="numeric"></label>
            <label class="cp-field"><span>Output tokens / request</span><input type="number" min="0" step="50" data-cp="out" inputmode="numeric"></label>
            <label class="cp-field cp-field--range"><span>Cached input <output data-cp-out="cache"></output></span><input type="range" min="0" max="90" step="5" data-cp="cache"></label>
            <label class="cp-field cp-field--range"><span>Sent as batch <output data-cp-out="batch"></output></span><input type="range" min="0" max="100" step="5" data-cp="batch"></label>
            <div class="cp-field"><span>Deployment type</span>
                <div class="cp-seg" role="radiogroup" aria-label="Deployment type">
                    <button type="button" data-dep="global" role="radio">Global</button>
                    <button type="button" data-dep="datazone" role="radio">Data Zone</button>
                    <button type="button" data-dep="regional" role="radio">Regional</button>
                </div>
            </div>
        </div>
    </section>

    <section class="cp-panel cp-models" aria-label="Models to compare">
        <div class="cp-row">
            <span class="cp-label">Compare</span>
            <div class="cp-chips" role="group" aria-label="Model sets">
                <button type="button" class="cp-chip" data-set="popular">Popular</button>
                <button type="button" class="cp-chip" data-set="retiring">Retiring → replacements</button>
                <button type="button" class="cp-chip" data-set="budget">Under $1 / 1M</button>
                <button type="button" class="cp-chip" data-set="partner">Partner models</button>
                <button type="button" class="cp-chip cp-chip--ghost" data-set="clear">Clear</button>
            </div>
        </div>
        <div class="cp-picker">
            <div class="cp-selected" data-cp-selected></div>
            <div class="cp-search">
                <input type="search" data-cp-search placeholder="Add a model — 138 priced" aria-label="Add a model" autocomplete="off" spellcheck="false">
                <ul class="cp-suggest" data-cp-suggest role="listbox" hidden></ul>
            </div>
        </div>
    </section>

    <div class="cp-kpis" data-cp-kpis aria-live="polite"></div>

    <section class="cp-panel cp-chart">
        <header class="cp-head">
            <div><h2>Projected monthly cost</h2><p data-cp-basis></p></div>
            <div class="cp-legend"><span class="cp-key cp-key--in">Input</span><span class="cp-key cp-key--cached">Cached input</span><span class="cp-key cp-key--out">Output</span></div>
        </header>
        <div class="cp-bars" data-cp-bars></div>
    </section>

    <section class="cp-panel cp-ptu">
        <header class="cp-head">
            <div><h2>Pay-as-you-go vs PTU</h2><p>Monthly cost as daily volume grows, for the same prompt shape.</p></div>
            <div class="cp-ptu-controls">
                <label class="cp-select"><span>Model</span><select data-cp-ptu-model></select></label>
                <label class="cp-select"><span>Peak ÷ average</span><select data-cp="peak"><option value="1">1× (flat)</option><option value="2">2×</option><option value="3">3×</option><option value="5">5×</option></select></label>
            </div>
        </header>
        <div class="cp-ptu-body">
            <div class="cp-ptu-chart" data-cp-ptu-chart></div>
            <div class="cp-ptu-verdict" data-cp-ptu-verdict></div>
        </div>
    </section>

    <section class="cp-panel cp-table-wrap">
        <header class="cp-head"><div><h2>Price sheet</h2><p>List price per 1M tokens for the selected deployment type.</p></div>
            <button type="button" class="ax-btn" data-cp-action="csv">Download CSV</button></header>
        <div class="table-responsive"><table class="cp-table" data-cp-table></table></div>
    </section>

    <section class="cp-panel cp-media" id="media" data-cpm aria-label="Media and audio estimator">
        <header class="cp-head">
            <div><h2>Media &amp; audio estimator</h2><p>Image, speech, video, document and search models are billed per image, minute, second, page or query rather than per chat request. Pick a group and enter your monthly volume.</p></div>
        </header>
        <div class="cpm-tabs" role="tablist" aria-label="Media type">
            <button type="button" role="tab" data-cpm-tab="image">Images <small data-cpm-count="image"></small></button>
            <button type="button" role="tab" data-cpm-tab="audio">Audio &amp; speech <small data-cpm-count="audio"></small></button>
            <button type="button" role="tab" data-cpm-tab="video">Video <small data-cpm-count="video"></small></button>
            <button type="button" role="tab" data-cpm-tab="docs">Documents &amp; search <small data-cpm-count="docs"></small></button>
        </div>
        <div class="cp-fields cpm-controls" data-cpm-controls></div>
        <div class="cp-bars" data-cpm-bars aria-live="polite"></div>
        <details class="cpm-assume">
            <summary>Assumptions</summary>
            <div data-cpm-assume></div>
        </details>
    </section>

    <details class="cp-unpriced">
        <summary>Why some models aren't here</summary>
        <div data-cp-unpriced></div>
    </details>
</div>

<p class="dash-footnote">138 of 155 tracked models have pay-as-you-go prices (97 per token, 41 per image, minute, second, page or query). List prices are in USD from the <a href="https://learn.microsoft.com/rest/api/cost-management/retail-prices/azure-retail-prices">Azure Retail Prices API</a> for East US 2 (North Central US for classic speech and Whisper, which East US 2 does not sell), and from the public <a href="https://azuremarketplace.microsoft.com/">Azure Marketplace</a> catalog for 27 partner models billed through Marketplace. Prices are checked daily, last updated 2026-10-08. They exclude tax, negotiated discounts and fine-tuning or hosting fees. A month is 730 hours. Per-image and per-minute figures for token-billed media models are estimates based on the editable assumptions. PTU sizing uses Microsoft's published tokens-per-minute figures and is an estimate: confirm it with the <a href="https://ai.azure.com/nextgen/goto/build/models/ptu-calculator">Foundry capacity calculator</a> before you buy.</p>

<noscript>The cost planner needs JavaScript. Each <a href="../models/">model page</a> lists its prices.</noscript>
