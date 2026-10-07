---
hide:
  - navigation
  - toc
---

# Availability Explorer

<p class="page-lede">Every model, every region, every deployment type — in one view. Filters update the grid instantly; the URL updates too, so you can share exactly what you see.</p>

<div class="ax" data-explorer data-src="../assets/model-index.json" data-root="../">
    <div class="ax-toolbar">
        <div class="ax-search">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9.5 3a6.5 6.5 0 0 1 5.25 10.33l5.46 5.46-1.42 1.42-5.46-5.46A6.5 6.5 0 1 1 9.5 3m0 2a4.5 4.5 0 1 0 0 9 4.5 4.5 0 0 0 0-9"/></svg>
            <input type="search" data-ax="q" placeholder="Filter 154 models — e.g. gpt-5, claude, embedding" aria-label="Filter models" autocomplete="off" spellcheck="false">
        </div>
        <label class="ax-select"><span>Provider</span><select data-ax="p"><option value="">All providers</option></select></label>
        <label class="ax-select"><span>Lifecycle</span><select data-ax="lc"><option value="">Any stage</option><option value="risk">Retiring ≤ 90 days</option><option value="deprecated">Deprecated</option><option value="preview">Preview</option><option value="ga">Generally available</option><option value="untracked">No date published</option><option value="retired">Retired</option></select></label>
        <label class="ax-select"><span>Geography</span><select data-ax="g"><option value="">All geographies</option><option value="Americas">Americas</option><option value="Europe">Europe</option><option value="Asia Pacific">Asia Pacific</option><option value="Middle East &amp; Africa">Middle East &amp; Africa</option><option value="US Government">US Government</option></select></label>
        <label class="ax-select"><span>Sort</span><select data-ax="s">
            <option value="name">Name</option>
            <option value="coverage">Most regions</option>
            <option value="retire">Retiring soonest</option>
        </select></label>
    </div>
    <div class="ax-types" role="group" aria-label="Deployment type">
        <span class="ax-types__label">Deployment type</span>
        <button type="button" class="ax-chip is-active" data-type="">Any</button>
        <button type="button" class="ax-chip ax-chip--paygo" data-type="gs" tabindex="0" data-tip-title="Global Standard" data-tip="Pay per token. Requests can be processed in any Azure region worldwide. Highest default quota — the best place to start."><i class="ax-dot ax-dot--paygo"></i>Global</button><button type="button" class="ax-chip ax-chip--paygo" data-type="dz" tabindex="0" data-tip-title="Data Zone Standard" data-tip="Pay per token. Processing stays inside the Microsoft-defined data zone (US or EU)."><i class="ax-dot ax-dot--paygo"></i>Data Zone</button><button type="button" class="ax-chip ax-chip--paygo" data-type="rs" tabindex="0" data-tip-title="Regional Standard" data-tip="Pay per token. Processing stays in the region you deploy to."><i class="ax-dot ax-dot--paygo"></i>Regional</button><button type="button" class="ax-chip ax-chip--ptu" data-type="gp" tabindex="0" data-tip-title="Global Provisioned (PTU)" data-tip="Reserved throughput (PTUs) billed hourly or via reservation. Processing can happen in any Azure region."><i class="ax-dot ax-dot--ptu"></i>Global PTU</button><button type="button" class="ax-chip ax-chip--ptu" data-type="dp" tabindex="0" data-tip-title="Data Zone Provisioned (PTU)" data-tip="Reserved throughput (PTUs) with processing kept inside the data zone (US or EU)."><i class="ax-dot ax-dot--ptu"></i>Data Zone PTU</button><button type="button" class="ax-chip ax-chip--ptu" data-type="rp" tabindex="0" data-tip-title="Regional Provisioned (PTU)" data-tip="Reserved throughput (PTUs) with processing kept in the deployment region."><i class="ax-dot ax-dot--ptu"></i>Regional PTU</button><button type="button" class="ax-chip ax-chip--batch" data-type="bt" tabindex="0" data-tip-title="Batch" data-tip="Asynchronous jobs with a 24-hour target turnaround at a lower price than Standard."><i class="ax-dot ax-dot--batch"></i>Batch</button><button type="button" class="ax-chip ax-chip--partner" data-type="mp" tabindex="0" data-tip-title="Partner / Marketplace" data-tip="Partner model deployed as a serverless API, typically billed through Azure Marketplace."><i class="ax-dot ax-dot--partner"></i>Partner</button>
    </div>
    <div class="ax-status">
        <p class="ax-summary" data-ax-summary aria-live="polite">Loading…</p>
        <div class="ax-required" data-ax-required hidden></div>
        <div class="ax-actions">
            <label class="ax-toggle"><input type="checkbox" data-ax="he" checked> Hide empty regions</label>
            <button type="button" class="ax-btn" data-ax-action="reset">Reset</button>
            <button type="button" class="ax-btn" data-ax-action="csv">Download CSV</button>
        </div>
    </div>
    <div class="ax-legend"><span tabindex="0" data-tip-title="Pay-as-you-go" data-tip="Global, Data Zone or Regional Standard — billed per token."><i class="ax-dot ax-dot--paygo"></i>Pay-as-you-go</span><span tabindex="0" data-tip-title="Provisioned (PTU)" data-tip="Reserved throughput. See the PTU guide for sizing and pricing."><i class="ax-dot ax-dot--ptu"></i>Provisioned (PTU)</span><span tabindex="0" data-tip-title="Batch" data-tip="Asynchronous 24-hour jobs at a discount."><i class="ax-dot ax-dot--batch"></i>Batch</span><span tabindex="0" data-tip-title="Partner" data-tip="Partner model via serverless API / Marketplace."><i class="ax-dot ax-dot--partner"></i>Partner</span><span tabindex="0" data-tip-title="Listed" data-tip="Available in the region; deployment type not published."><i class="ax-dot ax-dot--other"></i>Listed</span><em>Click a region header to require it.</em></div>
    <div class="ax-scroll" data-ax-scroll>
        <table class="ax-grid" data-ax-grid></table>
    </div>
</div>

<noscript>The explorer needs JavaScript. Browse the <a href="../models/">model table</a> instead.</noscript>
