# <span class="pv pv--openai pv--xl" aria-hidden="true" title="OpenAI"></span> model-router

<div class="swap swap--scheduled swap--none" aria-label="Replacement model">
    <div class="swap__side swap__side--from">
        <span class="swap__eyebrow">Retirement scheduled</span>
        <span class="swap__model"><span class="pv pv--openai pv--sm" aria-hidden="true" title="OpenAI"></span><b>model-router</b></span>
        <small>Retires May 20, 2027 · in 7 months</small>
    </div>
    <span class="swap__arrow" aria-hidden="true"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 11h11.17l-4.88-4.88L12.7 4.7 20 12l-7.3 7.3-1.41-1.42L16.17 13H5z"/></svg></span>
    <div class="swap__side swap__side--to">
        <span class="swap__eyebrow">Replacement</span>
        <span class="swap__model"><b>Not named yet</b></span>
        <small>Microsoft usually names one before retirement. <a href="../../lifecycle/">How retirement works</a></small>
    </div>
</div>

<div class="model-profile" aria-label="Model availability profile">
    <div class="model-profile__main">
        <div class="model-profile__badges">
            <span class="badge badge-emerging">Emerging</span>
            <span class="lc-badge lc-badge--success" tabindex="0" data-tip-title="Generally available" data-tip="Production-ready: weights and APIs are fixed and new deployments are allowed. Most GA models get about 18 months before retirement (12 for some partner models). Next retirement: May 20, 2027 (version 2025-11-18). Safe to build on — note the retirement date in your roadmap.">GA · until May 2027</span>
            <span class="model-profile__family"><span class="pv pv--openai pv--sm" aria-hidden="true" title="OpenAI"></span>OpenAI</span>
            <span class="model-profile__coverage-note">Under 15 regions tracked</span>
        </div>
        <p class="model-profile__lead">Available in <strong>6</strong> of <strong>35</strong> tracked regions with <strong>5</strong> deployment SKU types.</p>
        <div class="model-profile__chips" aria-label="Deployment categories"><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-other">Other</span></div>
        <div class="model-profile__actions">
            <a class="md-button md-button--primary" href="#deployment-options">Deployment options</a>
            <a class="md-button" href="#lifecycle">Lifecycle</a>
            <a class="md-button" href="#full-availability-matrix">Availability matrix</a>
        </div>
    </div>
    <div class="model-profile__metrics" aria-label="Model availability metrics">
    <div class="model-metric">
        <span>Total regions</span>
        <strong>6</strong>
    </div>
    <div class="model-metric">
        <span>Coverage</span>
        <strong>17%</strong>
    </div>
    <div class="model-metric">
        <span>SKU types</span>
        <strong>5</strong>
    </div>
    <div class="model-metric model-metric--success">
        <span>Next retirement</span>
        <strong>in 7 months</strong>
    </div>
</div>
    <div class="model-profile__insight">
        <span>Widest SKU footprint</span>
        <strong><a href="../../explorer/#t=gs">Global coverage</a></strong>
        <small>6 regions · 17% coverage · Global</small>
    </div>
</div>
## :material-clock-alert: Lifecycle

<div class="lc-versions">
<div class="lc-version lc-version--success">
    <div class="lc-version__head">
        <code>2025-11-18</code>
        <span class="lc-badge lc-badge--success" tabindex="0" data-tip-title="Generally available" data-tip="Production-ready: weights and APIs are fixed and new deployments are allowed. Most GA models get about 18 months before retirement (12 for some partner models). Safe to build on — note the retirement date in your roadmap.">Generally available</span>
        <span class="lc-version__countdown lc-version__countdown--success">in 7 months</span>
    </div>
    <div class="lc-bar" aria-hidden="true"><span class="lc-seg lc-seg--ga" style="left:0;width:66.61%"></span><span class="lc-seg lc-seg--deprecated" style="left:66.61%;width:33.39%"></span><span class="lc-today" style="left:59.12%"><em>Today</em></span></div>
    <div class="lc-version__dates"><span><b>Released</b> Nov 18, 2025</span><span><b>Deprecates</b> Nov 18, 2026</span><span><b>Retires</b> May 20, 2027</span></div>
    
</div>
</div>



## :material-cash-multiple: Pricing

<div class="price-card price-card--empty">
    <p><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18v12H3zm9 3a3 3 0 1 1 0 6 3 3 0 0 1 0-6M7 8a2 2 0 0 1-2 2v4a2 2 0 0 1 2 2h10a2 2 0 0 1 2-2v-4a2 2 0 0 1-2-2z"/></svg><span>The router bills at the price of whichever model it picks for each request.</span></p>
    <p class="price-card__foot">See <a href="https://azure.microsoft.com/pricing/details/ai-foundry-models/">Foundry Models pricing</a> for current rates.</p>
</div>


## :material-target: Deployment Options

<div class="deployment-lanes">
<section class="deployment-lane deployment-lane--global" aria-labelledby="global-deployments">
    <div class="deployment-lane__header">
        <div>
            <div class="deployment-lane__badge"><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></div>
            <h3 id="global-deployments">Global deployments</h3>
            <p>Worldwide availability with intelligent routing</p>
        </div>
        <p class="deployment-lane__use-case">Best for applications needing global reach with automatic failover</p>
    </div>
    <div class="deployment-lane__body">
        <div class="deployment-sku-list">
        <div class="deployment-sku-row">
            <div class="deployment-sku-row__copy">
                <a class="deployment-sku-row__name" href="../../explorer/#t=gs">Global Standard</a>
                <span>5 regions · 14% coverage</span>
            </div>
            <div class="availability-meter" aria-hidden="true"><span style="width: 14%;"></span></div>
        </div>
        <div class="deployment-sku-row">
            <div class="deployment-sku-row__copy">
                <a class="deployment-sku-row__name" href="../../explorer/#t=gs">Global coverage</a>
                <span>6 regions · 17% coverage</span>
            </div>
            <div class="availability-meter" aria-hidden="true"><span style="width: 17%;"></span></div>
        </div>
        </div>
        <div class="deployment-lane__regions" aria-label="Global deployment regions">
            <a class="region-badge model-region-chip" href="../../explorer/#rg=Australia%20East">Australia East</a> <a class="region-badge model-region-chip" href="../../explorer/#rg=East%20US%202">East US 2</a> <a class="region-badge model-region-chip" href="../../explorer/#rg=North%20Europe">North Europe</a> <a class="region-badge model-region-chip" href="../../explorer/#rg=South%20India">South India</a> <a class="region-badge model-region-chip" href="../../explorer/#rg=Sweden%20Central">Sweden Central</a> <a class="region-badge model-region-chip" href="../../explorer/#rg=West%20US%203">West US 3</a>
        </div>
        <p class="deployment-lane__compliance">⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements</p>
    </div>
</section>
<section class="deployment-lane deployment-lane--datazone" aria-labelledby="datazone-deployments">
    <div class="deployment-lane__header">
        <div>
            <div class="deployment-lane__badge"><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></div>
            <h3 id="datazone-deployments">Datazone deployments</h3>
            <p>Data residency compliance deployments</p>
        </div>
        <p class="deployment-lane__use-case">Required for data sovereignty and compliance requirements (GDPR, etc.)</p>
    </div>
    <div class="deployment-lane__body">
        <div class="deployment-sku-list">
        <div class="deployment-sku-row">
            <div class="deployment-sku-row__copy">
                <a class="deployment-sku-row__name" href="../../explorer/#t=dz">Datazone standard</a>
                <span>5 regions · 14% coverage</span>
            </div>
            <div class="availability-meter" aria-hidden="true"><span style="width: 14%;"></span></div>
        </div>
        </div>
        <div class="deployment-lane__regions" aria-label="Datazone deployment regions">
            <a class="region-badge model-region-chip" href="../../explorer/#rg=Australia%20East">Australia East</a> <a class="region-badge model-region-chip" href="../../explorer/#rg=East%20US%202">East US 2</a> <a class="region-badge model-region-chip" href="../../explorer/#rg=South%20India">South India</a> <a class="region-badge model-region-chip" href="../../explorer/#rg=Sweden%20Central">Sweden Central</a> <a class="region-badge model-region-chip" href="../../explorer/#rg=West%20US%203">West US 3</a>
        </div>
        <p class="deployment-lane__compliance">✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies</p>
    </div>
</section>
<section class="deployment-lane deployment-lane--other" aria-labelledby="other-deployments">
    <div class="deployment-lane__header">
        <div>
            <div class="deployment-lane__badge"><span class="sku-badge sku-other">Other</span></div>
            <h3 id="other-deployments">Other deployments</h3>
            <p>Deployment labels outside the canonical SKU groups</p>
        </div>
        <p class="deployment-lane__use-case">Review individual SKU labels for deployment behavior.</p>
    </div>
    <div class="deployment-lane__body">
        <div class="deployment-sku-list">
        <div class="deployment-sku-row">
            <div class="deployment-sku-row__copy">
                <a class="deployment-sku-row__name" href="../../explorer/#t=rs">Deployments Standard</a>
                <span>6 regions · 17% coverage</span>
            </div>
            <div class="availability-meter" aria-hidden="true"><span style="width: 17%;"></span></div>
        </div>
        <div class="deployment-sku-row">
            <div class="deployment-sku-row__copy">
                <a class="deployment-sku-row__name" href="../../explorer/#t=gs">Standard Global By Capability</a>
                <span>5 regions · 14% coverage</span>
            </div>
            <div class="availability-meter" aria-hidden="true"><span style="width: 14%;"></span></div>
        </div>
        </div>
        <div class="deployment-lane__regions" aria-label="Other deployment regions">
            <a class="region-badge model-region-chip" href="../../explorer/#rg=Australia%20East">Australia East</a> <a class="region-badge model-region-chip" href="../../explorer/#rg=East%20US%202">East US 2</a> <a class="region-badge model-region-chip" href="../../explorer/#rg=North%20Europe">North Europe</a> <a class="region-badge model-region-chip" href="../../explorer/#rg=South%20India">South India</a> <a class="region-badge model-region-chip" href="../../explorer/#rg=Sweden%20Central">Sweden Central</a> <a class="region-badge model-region-chip" href="../../explorer/#rg=West%20US%203">West US 3</a>
        </div>
        
    </div>
</section>
</div>

## :material-clipboard-list: Full Availability Matrix

<div class="matrix-tools">
    <input type="search" class="matrix-filter" data-matrix-filter placeholder="Filter 6 regions…" aria-label="Filter regions">
    <span class="matrix-count" data-matrix-count>6 regions</span>
</div>
<div class="table-responsive">
<table class="matrix-table">
<thead>
<tr><th>Region</th><th>Datazone standard</th><th>Deployments Standard</th><th>Global Standard</th><th>Global coverage</th><th>Standard Global By Capability</th></tr>
</thead>
<tbody>
<tr data-region="Australia East"><td><strong>Australia East</strong></td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td></tr>
<tr data-region="East US 2"><td><strong>East US 2</strong></td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td></tr>
<tr data-region="North Europe"><td><strong>North Europe</strong></td><td class="matrix-no">&mdash;</td><td class="matrix-yes">&#10003;</td><td class="matrix-no">&mdash;</td><td class="matrix-yes">&#10003;</td><td class="matrix-no">&mdash;</td></tr>
<tr data-region="South India"><td><strong>South India</strong></td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td></tr>
<tr data-region="Sweden Central"><td><strong>Sweden Central</strong></td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td></tr>
<tr data-region="West US 3"><td><strong>West US 3</strong></td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td><td class="matrix-yes">&#10003;</td></tr>
</tbody>
</table>
</div>

[← Back to All Models](index.md)

_Last updated: 2026-10-08 14:41 UTC_
