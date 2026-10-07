# Model Lifecycle

<p class="page-lede">Every Foundry model version moves through the same stages. Knowing where a model sits tells you whether to build on it, plan a migration, or move now.</p>

## Stages

<ol class="stage-flow" aria-label="Model lifecycle stages">
    <li class="stage-node stage-node--preview">
        <span class="stage-node__dot" aria-hidden="true"></span>
        <strong>Preview</strong>
        <span class="stage-node__access">Evaluation only</span>
        <small>No SLA · can change or be force-upgraded</small>
    </li>
<li class="stage-node stage-node--ga">
        <span class="stage-node__dot" aria-hidden="true"></span>
        <strong>Generally available</strong><span class="stage-node__count" title="Models tracked in this stage">9</span>
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
        <strong>Deprecated</strong><span class="stage-node__count" title="Models tracked in this stage">29</span>
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

<p class="diagram-note">Counts group tracked models by their most urgent active version; Deprecated also includes versions with a retirement due. Legacy has no published date, so it is not counted.</p>

## Retirement timelines

<figure class="lc-diagram">
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

<figure class="lc-diagram">
    <figcaption><strong>Preview model</strong> · not-sooner-than date, often ~90 days out</figcaption>
    <div class="lc-track">
        <div class="lc-phase lc-phase--preview" style="--w:66.67%"><span>Preview · evaluation only</span></div>
        <div class="lc-phase lc-phase--notice" style="--w:33.33%"><span>≥30 d notice</span></div>
    </div>
    <ol class="lc-marks">
        <li class="lc-mark lc-mark--start" style="--x:0%"><b>Launch</b><span>Not-sooner-than date set</span></li>
        <li class="lc-mark" style="--x:66.67%"><b>Notice</b><span>≥30 days warning</span></li>
        <li class="lc-mark lc-mark--end lc-mark--danger" style="--x:100%"><b>Upgrade or retire</b><span>Newer version or ends</span></li>
    </ol>
</figure>

## When to act

<div class="act-grid">
    <div class="act-card act-card--watch"><span>1</span><strong>Start watching</strong><p>The model shows as Deprecated, Legacy, or has a scheduled retirement on its model page.</p></div>
    <div class="act-card act-card--test"><span>2</span><strong>Start testing</strong><p>A replacement is named — usually 90–120 days before retirement. Evaluate it in Global Standard.</p></div>
    <div class="act-card act-card--notify"><span>3</span><strong>Expect notices</strong><p>GA retirements get at least 60 days active notice; preview models at least 30 days.</p></div>
    <div class="act-card act-card--manual"><span>4</span><strong>Migrate PTU yourself</strong><p>Provisioned deployments never auto-upgrade. Plan capacity in the replacement before the 30-day window.</p></div>
</div>

## Upgrade behavior by deployment type

| Deployment type | At retirement | What you should do |
|---|---|---|
| <span class="sku-badge sku-global">Global</span> Global Standard / Batch | Auto-upgraded to the replacement when an upgrade policy allows it | Pin a version and test the replacement before the date |
| <span class="sku-badge sku-datazone">Datazone</span> Data Zone Standard | Auto-upgraded within the data zone | Confirm the replacement is available in your data zone |
| <span class="sku-badge sku-standard">Standard</span> Regional Standard | Auto-upgraded when available in the region | Check regional availability of the replacement |
| <span class="sku-badge sku-provisioned">Provisioned</span> Provisioned (PTU) | **Not upgraded** — requests fail after retirement | Create a new PTU deployment on the replacement and move traffic |

## What each stage lets you do

| Stage | Meaning | New deployments | Existing deployments |
|---|---|---|---|
| <span class="lc-badge lc-badge--info">Preview</span> | Experimental — weights, runtime and API might change; not guaranteed to reach GA | Yes | Yes |
| <span class="lc-badge lc-badge--success">Generally available</span> | Production-ready — weights and APIs are fixed | Yes | Yes |
| Legacy | Newer, more capable models exist (optional stage) | Yes, until deprecated | Yes |
| <span class="lc-badge lc-badge--caution">Deprecated</span> | No longer available to new customers | Only subscriptions that already used this version | Yes |
| <span class="lc-badge lc-badge--muted">Retired</span> | Removed from service — every request returns `410 Gone` | No | No |

!!! info "Key timings"
    - GA models get **about 18 months** from launch to retirement and become Deprecated at **12 months**. GA models from Anthropic, DeepSeek, Fireworks and Mistral AI follow a **12-month** lifecycle.
    - A replacement is named **90–120 days** before retirement — in Global Standard about 90 days out, and in provisioned regions about 30 days out.
    - Preview models launch with a *not-sooner-than* date (typically ~90 days) and are force-upgraded or removed with **at least 30 days** notice.
    - Standard deployment types can be auto-upgraded. **Provisioned (PTU) deployments are never auto-upgraded** — you must migrate them yourself.

## How this site labels models

Hover or tap any lifecycle badge on this site for a plain-language explanation of what it means for you.

| Badge | What it means | What to do |
|---|---|---|
| <span class="lc-badge lc-badge--danger">Retires in 12 days</span> | Firm retirement date within 30 days | Move traffic to the replacement now |
| <span class="lc-badge lc-badge--warning">Retires in 60 days</span> | Firm retirement date within 90 days | Test the replacement and plan the cut-over |
| <span class="lc-badge lc-badge--warning">Retirement imminent</span> | A *no-earlier-than* date has passed — it can retire any time after notice | Treat as retiring now |
| <span class="lc-badge lc-badge--caution">Deprecated</span> | Closed to new customers | Don't start new work on it |
| <span class="lc-badge lc-badge--success">GA · until Jun 2027</span> | Generally available, with its next retirement month | Safe to build on |
| <span class="lc-badge lc-badge--neutral">No retirement date</span> | Not in Microsoft's retirement tables yet (common for new and partner models) | Check the model card in Foundry |

## Reading the Models API

| API `lifecycleStatus` | Means | Badge on this site |
|---|---|---|
| `Preview` | Preview, not for production | <span class="lc-badge lc-badge--info">Preview</span> |
| `GenerallyAvailable` | GA and open to new customers | <span class="lc-badge lc-badge--success">Generally available</span> |
| `Deprecating` | Deprecated — existing customers only | <span class="lc-badge lc-badge--caution">Deprecated</span> |
| `Deprecated` | Retired — no longer served | <span class="lc-badge lc-badge--muted">Retired</span> |

Adapted from [Foundry Models lifecycle and support policy](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirements). See [Retirements](../retirements/) for every model-specific date.
