---
hide:
  - toc
---

# Deployment Types &amp; PTU Guide

<p class="page-lede">Every Foundry deployment answers two questions: <strong>where is inference processed</strong>, and <strong>how do you pay</strong>? Pick a cell to see which models and regions offer it.</p>

## Choose a deployment type

<div class="dmx" role="table" aria-label="Deployment types by billing model and data-processing location">
    <div class="dmx__corner"><span>Where inference runs →</span><span>How you pay ↓</span></div>
    <div class="dmx__col"><b>Global</b><small>Inference can run in any Azure region. Data at rest stays in your geography. Highest quota.</small><em>Not for strict data-residency rules.</em></div><div class="dmx__col"><b>Data Zone</b><small>Inference stays inside the US or EU data zone.</small><em>Fits most GDPR / EU residency needs.</em></div><div class="dmx__col"><b>Regional</b><small>Inference stays in the region you deploy to.</small><em>Strictest residency; lowest default quota.</em></div>
    <div class="dmx__row dmx__row--paygo"><b>Pay-as-you-go</b><small>Standard · billed per token · no commitment</small></div>
    <a class="dmx__cell dmx__cell--paygo" href="../explorer/#t=gs" tabindex="0" data-tip-title="Global Standard" data-tip="Pay per token. Requests can be processed in any Azure region worldwide. Highest default quota — the best place to start."><strong>Global Standard</strong><span><b>58</b> models · <b>29</b> regions</span></a><a class="dmx__cell dmx__cell--paygo" href="../explorer/#t=dz" tabindex="0" data-tip-title="Data Zone Standard" data-tip="Pay per token. Processing stays inside the Microsoft-defined data zone (US or EU)."><strong>Data Zone Standard</strong><span><b>28</b> models · <b>23</b> regions</span></a><a class="dmx__cell dmx__cell--paygo" href="../explorer/#t=rs" tabindex="0" data-tip-title="Regional Standard" data-tip="Pay per token. Processing stays in the region you deploy to."><strong>Regional Standard</strong><span><b>103</b> models · <b>34</b> regions</span></a>
    <div class="dmx__row dmx__row--ptu"><b>Provisioned (PTU)</b><small>Reserved throughput · hourly or with a reservation</small></div>
    <a class="dmx__cell dmx__cell--ptu" href="../explorer/#t=gp" tabindex="0" data-tip-title="Global Provisioned (PTU)" data-tip="Reserved throughput (PTUs) billed hourly or via reservation. Processing can happen in any Azure region."><strong>Global Provisioned</strong><span><b>18</b> models · <b>27</b> regions</span></a><a class="dmx__cell dmx__cell--ptu" href="../explorer/#t=dp" tabindex="0" data-tip-title="Data Zone Provisioned (PTU)" data-tip="Reserved throughput (PTUs) with processing kept inside the data zone (US or EU)."><strong>Data Zone Provisioned</strong><span><b>19</b> models · <b>14</b> regions</span></a><a class="dmx__cell dmx__cell--ptu" href="../explorer/#t=rp" tabindex="0" data-tip-title="Regional Provisioned (PTU)" data-tip="Reserved throughput (PTUs) with processing kept in the deployment region."><strong>Regional Provisioned</strong><span><b>27</b> models · <b>34</b> regions</span></a>
</div>
<div class="dmx-extra"><a class="dmx-extra__card dmx__cell--batch" href="../explorer/#t=bt"><strong>Batch</strong><small>Send large jobs asynchronously; results within 24 hours at a lower price than Standard. Good for evaluations, enrichment and offline scoring.</small><span><b>12</b> models · <b>22</b> regions</span></a><a class="dmx-extra__card dmx__cell--partner" href="../explorer/#t=mp"><strong>Partner / Marketplace</strong><small>Partner models (Mistral, Cohere, Meta…) deployed as a serverless API and usually billed through Azure Marketplace.</small><span><b>52</b> models · <b>31</b> regions</span></a></div>

<p class="diagram-note">Start with <strong>Global Standard</strong>. Move to Data Zone or Regional when data-residency rules require it, and to PTU when traffic is steady and latency matters.</p>

## Provisioned throughput (PTU)

<div class="ptu-hero">
    <p class="ptu-hero__lede"><strong>A PTU (provisioned throughput unit) is a slice of model capacity reserved only for you.</strong> You pay for it by the hour whether or not you send traffic. In return you get predictable latency, and when you hit 100% the service answers <code>429</code> immediately instead of slowing down.</p>
    <div class="ptu-hero__facts">
        <span tabindex="0" data-tip-title="Model-independent quota" data-tip="PTU quota is not tied to one model: the same quota can deploy any supported model."><b>Model-independent</b> quota</span>
        <span tabindex="0" data-tip-title="Region-specific" data-tip="Quota is granted per subscription, per region and per deployment type."><b>Per region</b> &amp; type</span>
        <span tabindex="0" data-tip-title="Throughput varies by model" data-tip="Each model gets a different number of tokens per minute from one PTU — see the sizing table."><b>Tokens/PTU</b> vary by model</span>
        <span tabindex="0" data-tip-title="Quota ≠ capacity" data-tip="Having PTU quota does not guarantee the capacity is free when you deploy."><b>Quota ≠</b> capacity</span>
    </div>
</div>

### 1 · Is PTU right for you?

<div class="ptu-fit">
    <div class="ptu-fit__col ptu-fit__col--yes">
        <h3>Choose PTU when…</h3>
        <ul>
            <li>Traffic is <strong>steady and predictable</strong></li>
            <li>You need <strong>consistent, low latency</strong> (real-time, interactive)</li>
            <li>Volume is <strong>production-scale</strong> and per-token bills are climbing</li>
        </ul>
    </div>
    <div class="ptu-fit__col ptu-fit__col--no">
        <h3>Stay on Standard when…</h3>
        <ul>
            <li>You're <strong>developing or testing</strong></li>
            <li>Usage is <strong>low</strong> or <strong>highly variable</strong></li>
            <li>You can't yet predict peak load well enough to size it</li>
        </ul>
    </div>
</div>

### 2 · Pick a provisioned deployment type

<div class="ptu-types">
<div class="ptu-type ptu-type--gp">
        <h3>Global Provisioned</h3>
        <code>GlobalProvisionedManaged</code>
        <dl>
            <dt>Data processing</dt><dd>Routed across Azure regions worldwide</dd>
            <dt>Best for</dt><dd>Highest availability and the most capacity</dd>
            <dt>Typical size</dt><dd>15 PTU min · +5</dd>
        </dl>
        <a class="ptu-type__link" href="../explorer/#t=gp">18 models · 27 regions →</a>
    </div>
<div class="ptu-type ptu-type--dp">
        <h3>Data Zone Provisioned</h3>
        <code>DataZoneProvisionedManaged</code>
        <dl>
            <dt>Data processing</dt><dd>Stays inside a data zone (US or EU)</dd>
            <dt>Best for</dt><dd>Zone-level data residency with better availability than regional</dd>
            <dt>Typical size</dt><dd>15 PTU min · +5</dd>
        </dl>
        <a class="ptu-type__link" href="../explorer/#t=dp">19 models · 14 regions →</a>
    </div>
<div class="ptu-type ptu-type--rp">
        <h3>Regional Provisioned</h3>
        <code>ProvisionedManaged</code>
        <dl>
            <dt>Data processing</dt><dd>Stays in the region you deploy to</dd>
            <dt>Best for</dt><dd>Strict single-region data residency</dd>
            <dt>Typical size</dt><dd>25–50 PTU min · +25/50</dd>
        </dl>
        <a class="ptu-type__link" href="../explorer/#t=rp">27 models · 34 regions →</a>
    </div>
</div>

<p class="diagram-note">Reservations are bought per deployment type and are not interchangeable — decide this before you buy.</p>

### 3 · Size it

<ol class="ptu-steps">
    <li><strong>Measure your peak.</strong> Peak requests per minute, average prompt tokens, average response tokens and expected cache-hit rate.</li>
    <li><strong>Run the Foundry capacity calculator.</strong> In the Foundry portal open <em>Quota → Provisioned throughput</em>, or go straight to the <a href="https://ai.azure.com/nextgen/goto/build/models/ptu-calculator">capacity calculator</a>. It rounds to the model's minimum and scale increment.</li>
    <li><strong>Benchmark it.</strong> Deploy the estimate and replay your traffic shape for 10+ minutes with the <a href="https://github.com/Azure/azure-openai-benchmark">Azure OpenAI benchmark tool</a>, then with your real client.</li>
    <li><strong>Adjust.</strong> Watch utilization and 429 rates in Azure Monitor and resize.</li>
</ol>

<p class="ptu-cost-link"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18v12H3zm9 3a3 3 0 1 1 0 6 3 3 0 0 1 0-6M7 8a2 2 0 0 1-2 2v4a2 2 0 0 1 2 2h10a2 2 0 0 1 2-2v-4a2 2 0 0 1-2-2z"/></svg><span><b>Is it cheaper?</b> The <a href="../cost/">cost planner</a> compares pay-as-you-go with hourly and reserved PTU at your volume and shows the break-even point.</span></p>

<div class="ptu-calc" data-ptu-calc data-models="[{&quot;m&quot;:&quot;gpt-5.6-luna&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:50,&quot;rinc&quot;:50,&quot;tpm&quot;:30000,&quot;ratio&quot;:6},{&quot;m&quot;:&quot;gpt-5.6-terra&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:50,&quot;rinc&quot;:50,&quot;tpm&quot;:3000,&quot;ratio&quot;:6},{&quot;m&quot;:&quot;gpt-5.6-sol&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:50,&quot;rinc&quot;:50,&quot;tpm&quot;:1200,&quot;ratio&quot;:6},{&quot;m&quot;:&quot;gpt-5.5&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:50,&quot;rinc&quot;:50,&quot;tpm&quot;:1200,&quot;ratio&quot;:6},{&quot;m&quot;:&quot;gpt-5.4&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:50,&quot;rinc&quot;:50,&quot;tpm&quot;:2400,&quot;ratio&quot;:6},{&quot;m&quot;:&quot;gpt-5.4-mini&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:25,&quot;rinc&quot;:25,&quot;tpm&quot;:7900,&quot;ratio&quot;:6},{&quot;m&quot;:&quot;gpt-5.3-codex&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:50,&quot;rinc&quot;:50,&quot;tpm&quot;:3400,&quot;ratio&quot;:8},{&quot;m&quot;:&quot;gpt-5.2&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:50,&quot;rinc&quot;:50,&quot;tpm&quot;:3400,&quot;ratio&quot;:8},{&quot;m&quot;:&quot;gpt-5.2-codex&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:50,&quot;rinc&quot;:50,&quot;tpm&quot;:3400,&quot;ratio&quot;:8},{&quot;m&quot;:&quot;gpt-5.1&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:50,&quot;rinc&quot;:50,&quot;tpm&quot;:4750,&quot;ratio&quot;:8},{&quot;m&quot;:&quot;gpt-5.1-codex&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:50,&quot;rinc&quot;:50,&quot;tpm&quot;:4750,&quot;ratio&quot;:8},{&quot;m&quot;:&quot;gpt-5&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:50,&quot;rinc&quot;:50,&quot;tpm&quot;:4750,&quot;ratio&quot;:8},{&quot;m&quot;:&quot;gpt-5-mini&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:50,&quot;rinc&quot;:50,&quot;tpm&quot;:4750,&quot;ratio&quot;:8},{&quot;m&quot;:&quot;gpt-4.1&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:25,&quot;rinc&quot;:25,&quot;tpm&quot;:23750,&quot;ratio&quot;:4},{&quot;m&quot;:&quot;gpt-4.1-mini&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:50,&quot;rinc&quot;:50,&quot;tpm&quot;:3000,&quot;ratio&quot;:4},{&quot;m&quot;:&quot;gpt-4.1-nano&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:25,&quot;rinc&quot;:25,&quot;tpm&quot;:14900,&quot;ratio&quot;:4},{&quot;m&quot;:&quot;o3&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:50,&quot;rinc&quot;:50,&quot;tpm&quot;:3000,&quot;ratio&quot;:4},{&quot;m&quot;:&quot;o4-mini&quot;,&quot;gmin&quot;:15,&quot;ginc&quot;:5,&quot;rmin&quot;:25,&quot;rinc&quot;:25,&quot;tpm&quot;:5400,&quot;ratio&quot;:4}]">
    <div class="ptu-calc__head">
        <h3>Quick estimate</h3>
        <p>Same formula as Microsoft's sizing guide. Always confirm in the <a href="https://ai.azure.com/nextgen/goto/build/models/ptu-calculator">Foundry capacity calculator</a>.</p>
    </div>
    <div class="ptu-calc__form">
        <label>Model<select data-calc="model"><option value="gpt-5.6-luna">gpt-5.6-luna</option><option value="gpt-5.6-terra">gpt-5.6-terra</option><option value="gpt-5.6-sol">gpt-5.6-sol</option><option value="gpt-5.5">gpt-5.5</option><option value="gpt-5.4">gpt-5.4</option><option value="gpt-5.4-mini">gpt-5.4-mini</option><option value="gpt-5.3-codex">gpt-5.3-codex</option><option value="gpt-5.2">gpt-5.2</option><option value="gpt-5.2-codex">gpt-5.2-codex</option><option value="gpt-5.1">gpt-5.1</option><option value="gpt-5.1-codex">gpt-5.1-codex</option><option value="gpt-5">gpt-5</option><option value="gpt-5-mini">gpt-5-mini</option><option value="gpt-4.1" selected>gpt-4.1</option><option value="gpt-4.1-mini">gpt-4.1-mini</option><option value="gpt-4.1-nano">gpt-4.1-nano</option><option value="o3">o3</option><option value="o4-mini">o4-mini</option></select></label>
        <label>Deployment type<select data-calc="type"><option value="g">Global / Data Zone</option><option value="r">Regional</option></select></label>
        <label>Peak requests / min<input type="number" min="0" step="1" value="1000" data-calc="rpm"></label>
        <label>Prompt tokens / call<input type="number" min="0" step="1" value="200" data-calc="prompt"></label>
        <label>Response tokens / call<input type="number" min="0" step="1" value="20" data-calc="response"></label>
        <label>Cache-hit rate %<input type="number" min="0" max="100" step="1" value="0" data-calc="cache"></label>
    </div>
    <div class="ptu-calc__result" aria-live="polite">
        <div class="ptu-calc__big"><strong data-calc-out="ptu">–</strong><span>PTUs to deploy</span></div>
        <div class="ptu-calc__detail" data-calc-out="detail"></div>
    </div>
</div>

??? info "The formula and per-model numbers"
    - Input TPM = peak RPM × prompt tokens
    - Output TPM = peak RPM × response tokens
    - **Normalized TPM** = Input TPM × (1 − cache rate) + output-to-input ratio × Output TPM
    - **PTUs** = Normalized TPM ÷ input TPM per PTU, rounded up to the minimum / increment

    Worked example from Microsoft (gpt-5.2, Data Zone): 1,000 RPM × 200 prompt + 20 response tokens → 360,000 normalized TPM → 105.9 → **110 PTUs**. With a 50% cache rate → **80 PTUs**.

    | Model | Global / Data Zone min (step) | Regional min (step) | Input TPM per PTU | Output : input ratio |
    |---|---|---|---|---|
    | `gpt-5.6-luna` | 15 (+5) | 50 (+50) | 30,000 | 6 |
    | `gpt-5.6-terra` | 15 (+5) | 50 (+50) | 3,000 | 6 |
    | `gpt-5.6-sol` | 15 (+5) | 50 (+50) | 1,200 | 6 |
    | `gpt-5.5` | 15 (+5) | 50 (+50) | 1,200 | 6 |
    | `gpt-5.4` | 15 (+5) | 50 (+50) | 2,400 | 6 |
    | `gpt-5.4-mini` | 15 (+5) | 25 (+25) | 7,900 | 6 |
    | `gpt-5.3-codex` | 15 (+5) | 50 (+50) | 3,400 | 8 |
    | `gpt-5.2` | 15 (+5) | 50 (+50) | 3,400 | 8 |
    | `gpt-5.2-codex` | 15 (+5) | 50 (+50) | 3,400 | 8 |
    | `gpt-5.1` | 15 (+5) | 50 (+50) | 4,750 | 8 |
    | `gpt-5.1-codex` | 15 (+5) | 50 (+50) | 4,750 | 8 |
    | `gpt-5` | 15 (+5) | 50 (+50) | 4,750 | 8 |
    | `gpt-5-mini` | 15 (+5) | 50 (+50) | 4,750 | 8 |
    | `gpt-4.1` | 15 (+5) | 25 (+25) | 23,750 | 4 |
    | `gpt-4.1-mini` | 15 (+5) | 50 (+50) | 3,000 | 4 |
    | `gpt-4.1-nano` | 15 (+5) | 25 (+25) | 14,900 | 4 |
    | `o3` | 15 (+5) | 50 (+50) | 3,000 | 4 |
    | `o4-mini` | 15 (+5) | 25 (+25) | 5,400 | 4 |

    GPT-6 family and image models use normalized token accounting — use the capacity calculator for those. Source: [PTU sizing](https://learn.microsoft.com/azure/foundry/openai/how-to/provisioned-throughput-sizing).

### 4 · Get capacity, then reserve

<ol class="ptu-flow">
    <li class="ptu-flow__step"><span>1</span><strong>Check quota</strong><small>Foundry → Manage → Quota → Provisioned throughput unit. <a href="https://aka.ms/oai/stuquotarequest">Request more</a> if needed.</small></li>
    <li class="ptu-flow__step"><span>2</span><strong>Deploy</strong><small>Creating the deployment is what actually claims capacity. The portal suggests other regions if yours is full.</small></li>
    <li class="ptu-flow__step"><span>3</span><strong>Reserve</strong><small>Only now buy a matching Azure Reservation (1 month or 1 year) to get the discounted rate.</small></li>
    <li class="ptu-flow__step"><span>4</span><strong>Go live</strong><small>Same API as Standard — call it with the deployment name.</small></li>
</ol>

!!! warning "Reservations don't guarantee capacity"
    Quota is just a limit, and a reservation is just a discount. Capacity is only held once a deployment exists. **Deploy first, then buy the reservation** — matching deployment type, region (Data Zone and Regional) and scope.

| | Hourly (no commitment) | Azure Reservation |
|---|---|---|
| Price | Full $/PTU/hour, prorated to the minute | Discounted $/PTU/hour |
| Term | None — stops only when you **delete** the deployment | 1 month or 1 year |
| Good for | Benchmarks, short events | Steady production |
| Watch out | Can't be paused; scaling down and back up risks losing capacity | Bought per deployment type; extra PTUs above the reservation bill hourly |

### 5 · Run it in production

<div class="ptu-ops">
    <div><h3>Monitor</h3><p>Azure Monitor metric <strong>Provisioned-managed utilization V2</strong> on the Foundry resource. Requests are rejected at 100%.</p></div>
    <div><h3>Handle 429s</h3><p>A 429 is a traffic signal, not an outage. Retry using the <code>retry-after-ms</code> header — SDK retries do this for you.</p></div>
    <div><h3>Spill over</h3><p>Send overflow to a Standard deployment in the same resource automatically with <a href="https://learn.microsoft.com/azure/foundry/openai/how-to/spillover-traffic-management">spillover</a> (not yet for DeepSeek or Llama).</p></div>
    <div><h3>Plan retirements</h3><p>Provisioned deployments are <strong>never auto-upgraded</strong>. Watch the <a href="../retirements/">retirement dates</a> and migrate yourself.</p></div>
</div>

!!! tip "Cleaning up"
    Delete the deployment before deleting the resource — billing continues until the resource is purged. Cancel or exchange the reservation separately.

<p class="dash-footnote">Summarised from Microsoft Learn: <a href="https://learn.microsoft.com/azure/foundry/openai/concepts/provisioned-throughput">What is provisioned throughput</a> · <a href="https://learn.microsoft.com/azure/foundry/openai/how-to/provisioned-throughput-sizing">PTU sizing</a> · <a href="https://learn.microsoft.com/azure/foundry/openai/concepts/provisioned-throughput-billing">Billing &amp; reservations</a> · <a href="https://learn.microsoft.com/azure/foundry/openai/how-to/provisioned-get-started">Operate in production</a>. Retrieved Oct 2026 — check the source pages for the latest numbers.</p>
