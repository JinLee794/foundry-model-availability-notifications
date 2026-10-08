# Model Lifecycle

<p class="page-lede">Every model in Foundry eventually retires. This page explains, in plain terms, what that means for your deployments — what happens on the day, what stays the same, and what you need to do.</p>

<div class="lcx-tldr"><div class="lcx-tldr__card lcx-tldr__card--1"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2zM5 22h14a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-2V2h-2v2H9V2H7v2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2M19 8v12H5V8z"/></svg><div><strong>Every model has an end date</strong><p>GA models get about <b>18 months</b> — 12 for Anthropic, DeepSeek, Fireworks and Mistral AI. The date is published on day one and can't be extended.</p></div></div><div class="lcx-tldr__card lcx-tldr__card--2"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6v3l4-4-4-4v3a8 8 0 0 0-8 8c0 1.57.46 3.03 1.24 4.26L6.7 14.8A5.9 5.9 0 0 1 6 12a6 6 0 0 1 6-6m6.76 1.74L17.3 9.2c.44.84.7 1.8.7 2.8a6 6 0 0 1-6 6v-3l-4 4 4 4v-3a8 8 0 0 0 8-8c0-1.57-.46-3.03-1.24-4.26"/></svg><div><strong>Pay-as-you-go upgrades itself</strong><p>Global, Data Zone and regional Standard deployments are switched to the replacement <b>in place</b>: same name, endpoint, location and quota.</p></div></div><div class="lcx-tldr__card lcx-tldr__card--3"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 7a2.5 2.5 0 0 0-2.5-2.5c-.17 0-.34 0-.5.05V4a2.5 2.5 0 0 0-3.17-2.41A2.51 2.51 0 0 0 12.5 0c-1.23 0-2.25.89-2.46 2.06C9.87 2 9.69 2 9.5 2A2.5 2.5 0 0 0 7 4.5v5.89c-.34-.31-.76-.54-1.22-.66L5 9.5c-.82-.21-1.69.11-2.18.85-.38.57-.4 1.31-.15 1.95l2.56 6.43A8.36 8.36 0 0 0 13 24c4.42 0 8-3.58 8-8zm-2 9c0 3.31-2.69 6-6 6a6.36 6.36 0 0 1-5.91-4L4.5 11.45l.5.14c.5.12.85.46 1 .91L7 15h2V4.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V2.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V4c0-.28.22-.5.5-.5s.5.22.5.5v8h2V7c0-.28.22-.5.5-.5s.5.22.5.5z"/></svg><div><strong>PTU and Batch don't</strong><p>Provisioned and Batch deployments must be moved by you. If they aren't, every request fails with <code>410 Gone</code>.</p></div></div></div>

## The five stages

<ol class="stage-flow" aria-label="Model lifecycle stages">
    <li class="stage-node stage-node--preview">
        <span class="stage-node__dot" aria-hidden="true"></span>
        <strong>Preview</strong>
        <span class="stage-node__access">Try it out</span>
        <small>May change or disappear · not for production</small>
    </li>
<li class="stage-node stage-node--ga">
        <span class="stage-node__dot" aria-hidden="true"></span>
        <strong>Generally available</strong><span class="stage-node__count" title="Models tracked in this stage">9</span>
        <span class="stage-node__access">Build on it</span>
        <small>Stable · end date known from day one</small>
    </li>
<li class="stage-node stage-node--legacy">
        <span class="stage-node__dot" aria-hidden="true"></span>
        <strong>Legacy</strong>
        <span class="stage-node__access">Something better exists</span>
        <small>Still works · start looking at newer models</small>
    </li>
<li class="stage-node stage-node--deprecated">
        <span class="stage-node__dot" aria-hidden="true"></span>
        <strong>Deprecated</strong><span class="stage-node__count" title="Models tracked in this stage">29</span>
        <span class="stage-node__access">Existing users only</span>
        <small>Nobody new can start · plan your move</small>
    </li>
<li class="stage-node stage-node--retired">
        <span class="stage-node__dot" aria-hidden="true"></span>
        <strong>Retired</strong><span class="stage-node__count" title="Models tracked in this stage">5</span>
        <span class="stage-node__access">Switched off</span>
        <small>Every request fails with 410 Gone</small>
    </li>
</ol>

<p class="diagram-note">Counts group tracked models by their most urgent active version; Deprecated also includes versions with a retirement due. Legacy is optional and has no published date, so it isn't counted.</p>

<figure class="lc-diagram">
    <figcaption><strong>A GA model's life</strong> · about 18 months from launch to switch-off</figcaption>
    <div class="lc-track">
        <div class="lc-phase lc-phase--ga" style="--w:66.67%"><span>Generally available · anyone can deploy</span></div>
        <div class="lc-phase lc-phase--deprecated" style="--w:33.33%"><span>Deprecated · existing users only</span></div>
        
    </div>
    <div class="lc-scale" aria-hidden="true"><span style="--x:0.00%">0</span><span style="--x:16.67%">3</span><span style="--x:33.33%">6</span><span style="--x:50.00%">9</span><span style="--x:66.67%">12</span><span style="--x:83.33%">15</span><span style="--x:100.00%">18</span><em>months</em></div>
    <ol class="lc-marks">
        <li class="lc-mark lc-mark--start" style="--x:0%"><b>Launch</b><span>End date published on day one</span></li>
        <li class="lc-mark" style="--x:66.67%"><b>12 mo · Deprecated</b><span>Closed to new users</span></li>
        <li class="lc-mark lc-mark--end lc-mark--danger" style="--x:100%"><b>18 mo · Retired</b><span>Switched off · 410 Gone</span></li>
    </ol>
</figure>

## What happens on retirement day

<p class="lcx-intro">It depends on <b>how you deployed</b> the model. Pick your deployment type:</p>

<div class="lcx-tabs">
    <input type="radio" name="lcx-tab" id="lcx-tab-paygo" class="lcx-tabs__input" checked><label for="lcx-tab-paygo" class="lcx-tabs__tab lcx-tabs__tab--paygo"><strong>Pay-as-you-go</strong><small>Global · Data Zone · Standard</small></label><input type="radio" name="lcx-tab" id="lcx-tab-ptu" class="lcx-tabs__input"><label for="lcx-tab-ptu" class="lcx-tabs__tab lcx-tabs__tab--ptu"><strong>Provisioned (PTU)</strong><small>Global · Data Zone · Regional</small></label><input type="radio" name="lcx-tab" id="lcx-tab-batch" class="lcx-tabs__input"><label for="lcx-tab-batch" class="lcx-tabs__tab lcx-tabs__tab--batch"><strong>Batch</strong><small>Global · Data Zone</small></label><input type="radio" name="lcx-tab" id="lcx-tab-preview" class="lcx-tabs__input"><label for="lcx-tab-preview" class="lcx-tabs__tab lcx-tabs__tab--preview"><strong>Preview models</strong><small>Any deployment type</small></label><input type="radio" name="lcx-tab" id="lcx-tab-tuned" class="lcx-tabs__input"><label for="lcx-tab-tuned" class="lcx-tabs__tab lcx-tabs__tab--tuned"><strong>Fine-tuned</strong><small>Custom models</small></label>
    <div class="lcx-panels"><section class="lcx-panel lcx-panel--paygo"><div class="lcx-story">
        <div class="lcx-frame"><span class="lcx-frame__when">Before</span>
            <div class="lcx-dep lcx-dep--ok">
        <div class="lcx-dep__top"><strong>chat-prod</strong><span class="lcx-dep__state">Running</span></div>
        <dl><div class="lcx-dep__field"><dt>Model</dt><dd><span class="pv pv--openai pv--xs" aria-hidden="true" title="OpenAI"></span><span>gpt-4.1</span> <small>2025-04-14</small></dd></div><div class="lcx-dep__field"><dt>Type</dt><dd>Data Zone Standard</dd></div><div class="lcx-dep__field"><dt>Location</dt><dd>East US 2</dd></div><div class="lcx-dep__field"><dt>Endpoint</dt><dd><code>/deployments/chat-prod</code></dd></div></dl>
    </div>
        </div>
        <div class="lcx-event lcx-event--auto"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6v3l4-4-4-4v3a8 8 0 0 0-8 8c0 1.57.46 3.03 1.24 4.26L6.7 14.8A5.9 5.9 0 0 1 6 12a6 6 0 0 1 6-6m6.76 1.74L17.3 9.2c.44.84.7 1.8.7 2.8a6 6 0 0 1-6 6v-3l-4 4 4 4v-3a8 8 0 0 0 8-8c0-1.57-.46-3.03-1.24-4.26"/></svg><strong>Retirement day</strong><span>Microsoft swaps the model behind your deployment, region by region</span></div>
        <div class="lcx-frame"><span class="lcx-frame__when">After</span>
            <div class="lcx-dep lcx-dep--ok">
        <div class="lcx-dep__top"><strong>chat-prod</strong><span class="lcx-dep__state">Running · upgraded</span></div>
        <dl><div class="lcx-dep__field is-changed"><dt>Model</dt><dd><span class="pv pv--openai pv--xs" aria-hidden="true" title="OpenAI"></span><span>gpt-5</span></dd></div><div class="lcx-dep__field is-same"><dt>Type</dt><dd>Data Zone Standard</dd></div><div class="lcx-dep__field is-same"><dt>Location</dt><dd>East US 2</dd></div><div class="lcx-dep__field is-same"><dt>Endpoint</dt><dd><code>/deployments/chat-prod</code></dd></div></dl>
    </div>
        </div>
    </div>
    <div class="lcx-diff">
        <div class="lcx-diff__col lcx-diff__col--same">
            <h4><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8m4.59-12.42L10 14.17l-2.59-2.58L6 13l4 4 8-8z"/></svg> Stays the same</h4>
            <ul>
                <li><b>Deployment name and endpoint</b> — your app calls the same URL</li>
                <li><b>Region or data zone</b> — requests are processed where they were before</li>
                <li><b>Deployment type and quota</b> — your tokens-per-minute limit carries over</li>
            </ul>
        </div>
        <div class="lcx-diff__col lcx-diff__col--change">
            <h4><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 19a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1c0-.21-.07-.41-.18-.57L13 8.35V4h-2v4.35L5.18 18.43c-.11.16-.18.36-.18.57m1 3a3 3 0 0 1-3-3c0-.6.18-1.16.5-1.63L9 7.81V6a1 1 0 0 1-1-1V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v1a1 1 0 0 1-1 1v1.81l5.5 9.56c.32.47.5 1.03.5 1.63a3 3 0 0 1-3 3zm7-6 1.34-1.34L16.27 18H7.73l2.66-4.61zm-.5-4a.5.5 0 0 1 .5.5.5.5 0 0 1-.5.5.5.5 0 0 1-.5-.5.5.5 0 0 1 .5-.5"/></svg> Can change — test first</h4>
            <ul>
                <li><b>The answers</b> — it's a different model, so prompts can behave differently</li>
                <li><b>Price</b> — tokens are billed at the new model's rate</li>
                <li><b>API features</b> — check that the parameters and tools you use are supported</li>
                <li><b>Speed and token usage</b> per request</li>
            </ul>
        </div>
    </div>
    <h4 class="lcx-subhead">Your deployment's upgrade setting decides when the swap happens</h4>
    <figure class="lcx-policy" aria-label="How each upgrade setting behaves">
    <div class="lcx-policy__axis"><span style="--x:30%">New default version set</span><span style="--x:76%">Retirement date</span></div>
    <div class="lcx-policy__row">
        <div class="lcx-policy__label"><strong>Early</strong><code>OnceNewDefaultVersionAvailable</code><small>Switches within two weeks of a new default version.</small></div>
        <div class="lcx-policy__track"><i class="lcx-seg lcx-seg--old" style="left:0%;width:38%"><span>gpt-4.1</span></i><i class="lcx-seg lcx-seg--new" style="left:38%;width:62%"><span>gpt-5</span></i></div>
    </div><div class="lcx-policy__row">
        <div class="lcx-policy__label"><strong>On the date</strong><code>OnceCurrentVersionExpired</code><small>Keeps the old model until retirement day, then switches.</small></div>
        <div class="lcx-policy__track"><i class="lcx-seg lcx-seg--old" style="left:0%;width:76%"><span>gpt-4.1</span></i><i class="lcx-seg lcx-seg--new" style="left:76%;width:24%"><span>gpt-5</span></i></div>
    </div><div class="lcx-policy__row">
        <div class="lcx-policy__label"><strong>Never</strong><code>NoAutoUpgrade</code><small>Keeps the old model — and stops working on retirement day.</small></div>
        <div class="lcx-policy__track"><i class="lcx-seg lcx-seg--old" style="left:0%;width:76%"><span>gpt-4.1</span></i><i class="lcx-seg lcx-seg--fail" style="left:76%;width:24%"><span>410 Gone</span></i></div>
    </div>
</figure>
    <p class="lcx-note">Find the setting under the deployment's details in the Foundry portal, or read <code>versionUpgradeOption</code> from the REST API, PowerShell or <code>az cognitiveservices account deployment show</code>. You can change it with REST, PowerShell or the portal — not with the Azure CLI. Priority Processing deployments follow the same rules.</p></section><section class="lcx-panel lcx-panel--ptu"><div class="lcx-story">
        <div class="lcx-frame"><span class="lcx-frame__when">Before</span>
            <div class="lcx-dep lcx-dep--ok">
        <div class="lcx-dep__top"><strong>ptu-prod</strong><span class="lcx-dep__state">Running</span></div>
        <dl><div class="lcx-dep__field"><dt>Model</dt><dd><span class="pv pv--openai pv--xs" aria-hidden="true" title="OpenAI"></span><span>gpt-4.1</span> <small>2025-04-14</small></dd></div><div class="lcx-dep__field"><dt>Type</dt><dd>Data Zone Provisioned</dd></div><div class="lcx-dep__field"><dt>Location</dt><dd>Sweden Central</dd></div><div class="lcx-dep__field"><dt>Capacity</dt><dd>100 PTU</dd></div><div class="lcx-dep__field"><dt>Endpoint</dt><dd><code>/deployments/ptu-prod</code></dd></div></dl>
    </div>
        </div>
        <div class="lcx-event lcx-event--manual"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 7a2.5 2.5 0 0 0-2.5-2.5c-.17 0-.34 0-.5.05V4a2.5 2.5 0 0 0-3.17-2.41A2.51 2.51 0 0 0 12.5 0c-1.23 0-2.25.89-2.46 2.06C9.87 2 9.69 2 9.5 2A2.5 2.5 0 0 0 7 4.5v5.89c-.34-.31-.76-.54-1.22-.66L5 9.5c-.82-.21-1.69.11-2.18.85-.38.57-.4 1.31-.15 1.95l2.56 6.43A8.36 8.36 0 0 0 13 24c4.42 0 8-3.58 8-8zm-2 9c0 3.31-2.69 6-6 6a6.36 6.36 0 0 1-5.91-4L4.5 11.45l.5.14c.5.12.85.46 1 .91L7 15h2V4.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V2.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V4c0-.28.22-.5.5-.5s.5.22.5.5v8h2V7c0-.28.22-.5.5-.5s.5.22.5.5z"/></svg><strong>Retirement day</strong><span>Nothing is upgraded for you — provisioned deployments are never auto-upgraded</span></div>
        <div class="lcx-frame lcx-frame--split"><span class="lcx-frame__when">After</span>
            <div class="lcx-outcome lcx-outcome--fail"><span><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8m0-18C6.47 2 2 6.47 2 12s4.47 10 10 10 10-4.47 10-10S17.53 2 12 2m2.59 6L12 10.59 9.41 8 8 9.41 10.59 12 8 14.59 9.41 16 12 13.41 14.59 16 16 14.59 13.41 12 16 9.41z"/></svg> If you didn't migrate</span>
                <div class="lcx-dep lcx-dep--fail">
        <div class="lcx-dep__top"><strong>ptu-prod</strong><span class="lcx-dep__state">410 Gone</span></div>
        <dl><div class="lcx-dep__field"><dt>Model</dt><dd><span class="pv pv--openai pv--xs" aria-hidden="true" title="OpenAI"></span><span>gpt-4.1</span> <small>2025-04-14</small></dd></div><div class="lcx-dep__field"><dt>Type</dt><dd>Data Zone Provisioned</dd></div><div class="lcx-dep__field"><dt>Location</dt><dd>Sweden Central</dd></div><div class="lcx-dep__field"><dt>Endpoint</dt><dd><code>/deployments/ptu-prod</code></dd></div></dl>
    </div>
            </div>
            <div class="lcx-outcome lcx-outcome--ok"><span><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8m4.59-12.42L10 14.17l-2.59-2.58L6 13l4 4 8-8z"/></svg> If you migrated</span>
                <div class="lcx-dep lcx-dep--ok">
        <div class="lcx-dep__top"><strong>ptu-prod</strong><span class="lcx-dep__state">Running</span></div>
        <dl><div class="lcx-dep__field is-changed"><dt>Model</dt><dd><span class="pv pv--openai pv--xs" aria-hidden="true" title="OpenAI"></span><span>gpt-5</span></dd></div><div class="lcx-dep__field is-same"><dt>Type</dt><dd>Data Zone Provisioned</dd></div><div class="lcx-dep__field is-same"><dt>Location</dt><dd>Sweden Central</dd></div><div class="lcx-dep__field is-same"><dt>Endpoint</dt><dd><code>/deployments/ptu-prod</code></dd></div></dl>
    </div>
            </div>
        </div>
    </div>
    <div class="lcx-ways">
        <div class="lcx-way"><h4><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6v3l4-4-4-4v3a8 8 0 0 0-8 8c0 1.57.46 3.03 1.24 4.26L6.7 14.8A5.9 5.9 0 0 1 6 12a6 6 0 0 1 6-6m6.76 1.74L17.3 9.2c.44.84.7 1.8.7 2.8a6 6 0 0 1-6 6v-3l-4 4 4 4v-3a8 8 0 0 0 8-8c0-1.57-.46-3.03-1.24-4.26"/></svg> In place</h4><p>Change the model version on the existing deployment. Azure moves traffic over a <b>20–30 minute</b> window with no downtime.</p></div>
        <div class="lcx-way"><h4><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="m21 9-4-4v3h-7v2h7v3M7 11l-4 4 4 4v-3h7v-2H7z"/></svg> Side by side</h4><p>Create a new deployment on the replacement, test it, shift traffic, then delete the old one. Safest when you want a rollback path.</p></div>
    </div>
    <ul class="lcx-points">
        <li><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2zM5 22h14a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-2V2h-2v2H9V2H7v2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2M19 8v12H5V8z"/></svg> The replacement becomes available in the provisioned regions where the old model is retiring about <b>30 days</b> before retirement.</li>
        <li><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4a10 10 0 0 0-8.66 15h17.32A10 10 0 0 0 12 4m0 2a8 8 0 0 1 7.42 11H4.58A8 8 0 0 1 12 6m4.24 2.34-5.66 4.24a1.5 1.5 0 1 0 1.84 1.84z"/></svg> PTU quota isn't tied to one model, but each model delivers different throughput per PTU — re-size with the <a href="../ptu/">PTU guide</a> and make sure you have quota for the target model.</li>
    </ul></section><section class="lcx-panel lcx-panel--batch"><div class="lcx-story">
        <div class="lcx-frame"><span class="lcx-frame__when">Before</span>
            <div class="lcx-dep lcx-dep--ok">
        <div class="lcx-dep__top"><strong>batch-nightly</strong><span class="lcx-dep__state">Running</span></div>
        <dl><div class="lcx-dep__field"><dt>Model</dt><dd><span class="pv pv--openai pv--xs" aria-hidden="true" title="OpenAI"></span><span>gpt-4.1</span> <small>2025-04-14</small></dd></div><div class="lcx-dep__field"><dt>Type</dt><dd>Global Batch</dd></div><div class="lcx-dep__field"><dt>Location</dt><dd>East US</dd></div><div class="lcx-dep__field"><dt>Endpoint</dt><dd><code>/deployments/batch-nightly</code></dd></div></dl>
    </div>
        </div>
        <div class="lcx-event lcx-event--manual"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 7a2.5 2.5 0 0 0-2.5-2.5c-.17 0-.34 0-.5.05V4a2.5 2.5 0 0 0-3.17-2.41A2.51 2.51 0 0 0 12.5 0c-1.23 0-2.25.89-2.46 2.06C9.87 2 9.69 2 9.5 2A2.5 2.5 0 0 0 7 4.5v5.89c-.34-.31-.76-.54-1.22-.66L5 9.5c-.82-.21-1.69.11-2.18.85-.38.57-.4 1.31-.15 1.95l2.56 6.43A8.36 8.36 0 0 0 13 24c4.42 0 8-3.58 8-8zm-2 9c0 3.31-2.69 6-6 6a6.36 6.36 0 0 1-5.91-4L4.5 11.45l.5.14c.5.12.85.46 1 .91L7 15h2V4.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V2.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V4c0-.28.22-.5.5-.5s.5.22.5.5v8h2V7c0-.28.22-.5.5-.5s.5.22.5.5z"/></svg><strong>Retirement day</strong><span>Batch deployments aren't upgraded — new jobs on the old model fail</span></div>
        <div class="lcx-frame"><span class="lcx-frame__when">What you do</span>
            <ol class="lcx-steps">
                <li><b>Deploy</b> the replacement as a new batch deployment</li>
                <li><b>Resubmit</b> your jobs against the new deployment</li>
                <li><b>Delete</b> the old deployment once jobs succeed</li>
            </ol>
        </div>
    </div></section><section class="lcx-panel lcx-panel--preview"><figure class="lc-diagram">
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
    <div class="lcx-ways lcx-ways--3">
        <div class="lcx-way"><h4><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6v3l4-4-4-4v3a8 8 0 0 0-8 8c0 1.57.46 3.03 1.24 4.26L6.7 14.8A5.9 5.9 0 0 1 6 12a6 6 0 0 1 6-6m6.76 1.74L17.3 9.2c.44.84.7 1.8.7 2.8a6 6 0 0 1-6 6v-3l-4 4 4 4v-3a8 8 0 0 0 8-8c0-1.57-.46-3.03-1.24-4.26"/></svg> Upgraded to a newer preview</h4><p>Your deployment is moved to the next preview version. This can repeat until a GA version exists.</p></div>
        <div class="lcx-way"><h4><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8m4.59-12.42L10 14.17l-2.59-2.58L6 13l4 4 8-8z"/></svg> Upgraded to GA</h4><p>When the GA model launches, preview deployments are moved to it and follow the GA lifecycle from then on.</p></div>
        <div class="lcx-way lcx-way--fail"><h4><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8m0-18C6.47 2 2 6.47 2 12s4.47 10 10 10 10-4.47 10-10S17.53 2 12 2m2.59 6L12 10.59 9.41 8 8 9.41 10.59 12 8 14.59 9.41 16 12 13.41 14.59 16 16 14.59 13.41 12 16 9.41z"/></svg> Removed (rare)</h4><p>If there's no replacement, the model is switched off and requests return <code>410 Gone</code>.</p></div>
    </div>
    <p class="lcx-note">Every outcome comes with at least <b>30 days</b> notice. There's no option to stay on a retiring preview model, so keep previews out of critical production.</p></section><section class="lcx-panel lcx-panel--tuned"><ol class="lcx-phases">
        <li class="lcx-phase"><span class="lcx-phase__n">1</span><div><strong>Training retires</strong><p>You can no longer start new fine-tuning jobs on the base model. Models you already trained can still be deployed. This happens no earlier than the base model's retirement.</p></div></li>
        <li class="lcx-phase lcx-phase--end"><span class="lcx-phase__n">2</span><div><strong>Deployment retires</strong><p>Inference and new deployments of the fine-tuned model return errors. Re-train on a newer base model before this date.</p></div></li>
    </ol>
    <p class="lcx-note">Fine-tuned models have their own dates — see the fine-tuned section of the <a href="../retirements/">retirement schedule</a>.</p></section></div>
</div>

## Will the replacement run in my region?

<p class="lcx-intro"><b>For pay-as-you-go deployments, yes.</b> Upgrades keep the same deployment type in the same place — and if the replacement isn't offered there yet, Microsoft adds it as part of the upgrade.</p>

<div class="lcx-where"><div class="lcx-where__card"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20m6.93 6h-2.95a15.7 15.7 0 0 0-1.38-3.56A8 8 0 0 1 18.93 8M12 4.04c.83 1.2 1.48 2.53 1.91 3.96h-3.82c.43-1.43 1.08-2.76 1.91-3.96M4.26 14a8 8 0 0 1 0-4h3.38a16 16 0 0 0 0 4zm.82 2h2.95c.32 1.25.78 2.45 1.38 3.56A8 8 0 0 1 5.08 16m2.95-8H5.08a8 8 0 0 1 4.33-3.56A15.7 15.7 0 0 0 8.03 8M12 19.96c-.83-1.2-1.48-2.53-1.91-3.96h3.82c-.43 1.43-1.08 2.76-1.91 3.96M14.34 14H9.66a14 14 0 0 1 0-4h4.68a14 14 0 0 1 0 4m.25 5.56c.6-1.11 1.06-2.31 1.38-3.56h2.95a8 8 0 0 1-4.33 3.56M16.36 14a16 16 0 0 0 0-4h3.38a8 8 0 0 1 0 4z"/></svg><strong>Global Standard</strong><p>Stays global — requests can be processed in any Azure region, before and after the upgrade.</p></div><div class="lcx-where__card"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 11c0 5.55-3.84 10.74-9 12-5.16-1.26-9-6.45-9-12V5l9-4 9 4zm-9 10c3.75-1 7-5.46 7-9.78V6.3l-7-3.12L5 6.3v4.92C5 15.54 8.25 20 12 21M11 7h2v6h-2zm0 8h2v2h-2z"/></svg><strong>Data Zone Standard</strong><p>Stays in your data zone (for example the EU or the US). Same deployment type, so the same boundary applies.</p></div><div class="lcx-where__card"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6.5A2.5 2.5 0 0 1 14.5 9a2.5 2.5 0 0 1-2.5 2.5A2.5 2.5 0 0 1 9.5 9 2.5 2.5 0 0 1 12 6.5M12 2a7 7 0 0 1 7 7c0 5.25-7 13-7 13S5 14.25 5 9a7 7 0 0 1 7-7m0 2a5 5 0 0 0-5 5c0 1 0 3 5 9.71C17 12 17 10 17 9a5 5 0 0 0-5-5"/></svg><strong>Regional Standard</strong><p>Stays in the same region. If the replacement isn't offered there yet, the upgrade adds it.</p></div></div>

<div class="lcx-callout"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 19a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1c0-.21-.07-.41-.18-.57L13 8.35V4h-2v4.35L5.18 18.43c-.11.16-.18.36-.18.57m1 3a3 3 0 0 1-3-3c0-.6.18-1.16.5-1.63L9 7.81V6a1 1 0 0 1-1-1V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v1a1 1 0 0 1-1 1v1.81l5.5 9.56c.32.47.5 1.03.5 1.63a3 3 0 0 1-3 3zm7-6 1.34-1.34L16.27 18H7.73l2.66-4.61zm-.5-4a.5.5 0 0 1 .5.5.5.5 0 0 1-.5.5.5.5 0 0 1-.5-.5.5.5 0 0 1 .5-.5"/></svg><p><b>Where location matters is testing early.</b> New models arrive in Global Standard first, then Global Provisioned, then Data Zone, and regional deployments last. If your data must stay in a region or data zone, test with non-sensitive data in Global Standard — or wait until the replacement is offered where you run. <b>Provisioned</b> customers need the replacement to be offered in their region before they can migrate.</p></div>

### Is the replacement already where the old model runs?

<p class="lcx-intro">For each upcoming retirement with a named replacement: of the regions where the retiring model runs today, how many already offer the replacement with the <b>same deployment type</b>.</p>

<div class="lcx-cov-grid">
    <article class="lcx-cov lcx-cov--danger">
        <header class="lcx-cov__head">
            <div class="lcx-cov__pair">
                <a href="../models/gpt-4-1/"><span class="pv pv--openai pv--sm" aria-hidden="true" title="OpenAI"></span><span>gpt-4.1</span></a>
                <svg class="fm-icon lcx-cov__arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 11h11.17l-4.88-4.88L12.7 4.7 20 12l-7.3 7.3-1.41-1.42L16.17 13H5z"/></svg>
                <a href="../models/gpt-5/"><span class="pv pv--openai pv--sm" aria-hidden="true" title="OpenAI"></span><span>gpt-5</span></a>
            </div>
            <span class="lc-badge lc-badge--danger">Retires in 6 days</span>
        </header>
        <p class="lcx-cov__meta">Oct 14, 2026 · version 2025-04-14</p>
        <ul class="lcx-cov__rows">
        <li class="lcx-cov__row lcx-cov__row--auto">
            <span class="lcx-cov__type">Global Standard<small>Upgraded for you</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 26 of 28 regions"><i style="--p:92.9%"></i></span>
            <span class="lcx-cov__num"><b>26</b>/28</span>
            <span class="lcx-cov__note lcx-cov__note--auto" title="Canada Central, Switzerland West"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6v3l4-4-4-4v3a8 8 0 0 0-8 8c0 1.57.46 3.03 1.24 4.26L6.7 14.8A5.9 5.9 0 0 1 6 12a6 6 0 0 1 6-6m6.76 1.74L17.3 9.2c.44.84.7 1.8.7 2.8a6 6 0 0 1-6 6v-3l-4 4 4 4v-3a8 8 0 0 0 8-8c0-1.57-.46-3.03-1.24-4.26"/></svg> Auto-upgrade adds it in Canada Central, Switzerland West</span>
        </li><li class="lcx-cov__row lcx-cov__row--auto">
            <span class="lcx-cov__type">Data Zone Standard<small>Upgraded for you</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 14 of 16 regions"><i style="--p:87.5%"></i></span>
            <span class="lcx-cov__num"><b>14</b>/16</span>
            <span class="lcx-cov__note lcx-cov__note--auto" title="US Gov Arizona, US Gov Virginia"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6v3l4-4-4-4v3a8 8 0 0 0-8 8c0 1.57.46 3.03 1.24 4.26L6.7 14.8A5.9 5.9 0 0 1 6 12a6 6 0 0 1 6-6m6.76 1.74L17.3 9.2c.44.84.7 1.8.7 2.8a6 6 0 0 1-6 6v-3l-4 4 4 4v-3a8 8 0 0 0 8-8c0-1.57-.46-3.03-1.24-4.26"/></svg> Auto-upgrade adds it in US Gov Arizona, US Gov Virginia</span>
        </li><li class="lcx-cov__row lcx-cov__row--auto">
            <span class="lcx-cov__type">Regional Standard<small>Upgraded for you</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 26 of 27 regions"><i style="--p:96.3%"></i></span>
            <span class="lcx-cov__num"><b>26</b>/27</span>
            <span class="lcx-cov__note lcx-cov__note--auto" title="US Gov Arizona"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6v3l4-4-4-4v3a8 8 0 0 0-8 8c0 1.57.46 3.03 1.24 4.26L6.7 14.8A5.9 5.9 0 0 1 6 12a6 6 0 0 1 6-6m6.76 1.74L17.3 9.2c.44.84.7 1.8.7 2.8a6 6 0 0 1-6 6v-3l-4 4 4 4v-3a8 8 0 0 0 8-8c0-1.57-.46-3.03-1.24-4.26"/></svg> Auto-upgrade adds it in US Gov Arizona</span>
        </li><li class="lcx-cov__row lcx-cov__row--manual">
            <span class="lcx-cov__type">Global Provisioned<small>You migrate</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 27 of 27 regions"><i style="--p:100.0%"></i></span>
            <span class="lcx-cov__num"><b>27</b>/27</span>
            <span class="lcx-cov__note lcx-cov__note--ok"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8m4.59-12.42L10 14.17l-2.59-2.58L6 13l4 4 8-8z"/></svg> Already offered in all 27 regions</span>
        </li><li class="lcx-cov__row lcx-cov__row--manual">
            <span class="lcx-cov__type">Data Zone Provisioned<small>You migrate</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 13 of 13 regions"><i style="--p:100.0%"></i></span>
            <span class="lcx-cov__num"><b>13</b>/13</span>
            <span class="lcx-cov__note lcx-cov__note--ok"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8m4.59-12.42L10 14.17l-2.59-2.58L6 13l4 4 8-8z"/></svg> Already offered in all 13 regions</span>
        </li><li class="lcx-cov__row lcx-cov__row--manual">
            <span class="lcx-cov__type">Regional Provisioned<small>You migrate</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 29 of 29 regions"><i style="--p:100.0%"></i></span>
            <span class="lcx-cov__num"><b>29</b>/29</span>
            <span class="lcx-cov__note lcx-cov__note--ok"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8m4.59-12.42L10 14.17l-2.59-2.58L6 13l4 4 8-8z"/></svg> Already offered in all 29 regions</span>
        </li><li class="lcx-cov__row lcx-cov__row--manual">
            <span class="lcx-cov__type">Batch<small>You migrate</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 22 of 22 regions"><i style="--p:100.0%"></i></span>
            <span class="lcx-cov__num"><b>22</b>/22</span>
            <span class="lcx-cov__note lcx-cov__note--ok"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8m4.59-12.42L10 14.17l-2.59-2.58L6 13l4 4 8-8z"/></svg> Already offered in all 22 regions</span>
        </li>
        </ul>
    </article><article class="lcx-cov lcx-cov--danger">
        <header class="lcx-cov__head">
            <div class="lcx-cov__pair">
                <a href="../models/gpt-4-1-mini/"><span class="pv pv--openai pv--sm" aria-hidden="true" title="OpenAI"></span><span>gpt-4.1-mini</span></a>
                <svg class="fm-icon lcx-cov__arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 11h11.17l-4.88-4.88L12.7 4.7 20 12l-7.3 7.3-1.41-1.42L16.17 13H5z"/></svg>
                <a href="../models/gpt-5-mini/"><span class="pv pv--openai pv--sm" aria-hidden="true" title="OpenAI"></span><span>gpt-5-mini</span></a>
            </div>
            <span class="lc-badge lc-badge--danger">Retires in 6 days</span>
        </header>
        <p class="lcx-cov__meta">Oct 14, 2026 · version 2025-04-14</p>
        <ul class="lcx-cov__rows">
        <li class="lcx-cov__row lcx-cov__row--auto">
            <span class="lcx-cov__type">Global Standard<small>Upgraded for you</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 26 of 26 regions"><i style="--p:100.0%"></i></span>
            <span class="lcx-cov__num"><b>26</b>/26</span>
            <span class="lcx-cov__note lcx-cov__note--ok"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8m4.59-12.42L10 14.17l-2.59-2.58L6 13l4 4 8-8z"/></svg> Already offered in all 26 regions</span>
        </li><li class="lcx-cov__row lcx-cov__row--auto">
            <span class="lcx-cov__type">Data Zone Standard<small>Upgraded for you</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 14 of 16 regions"><i style="--p:87.5%"></i></span>
            <span class="lcx-cov__num"><b>14</b>/16</span>
            <span class="lcx-cov__note lcx-cov__note--auto" title="US Gov Arizona, US Gov Virginia"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6v3l4-4-4-4v3a8 8 0 0 0-8 8c0 1.57.46 3.03 1.24 4.26L6.7 14.8A5.9 5.9 0 0 1 6 12a6 6 0 0 1 6-6m6.76 1.74L17.3 9.2c.44.84.7 1.8.7 2.8a6 6 0 0 1-6 6v-3l-4 4 4 4v-3a8 8 0 0 0 8-8c0-1.57-.46-3.03-1.24-4.26"/></svg> Auto-upgrade adds it in US Gov Arizona, US Gov Virginia</span>
        </li><li class="lcx-cov__row lcx-cov__row--auto">
            <span class="lcx-cov__type">Regional Standard<small>Upgraded for you</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 26 of 27 regions"><i style="--p:96.3%"></i></span>
            <span class="lcx-cov__num"><b>26</b>/27</span>
            <span class="lcx-cov__note lcx-cov__note--auto" title="US Gov Arizona"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6v3l4-4-4-4v3a8 8 0 0 0-8 8c0 1.57.46 3.03 1.24 4.26L6.7 14.8A5.9 5.9 0 0 1 6 12a6 6 0 0 1 6-6m6.76 1.74L17.3 9.2c.44.84.7 1.8.7 2.8a6 6 0 0 1-6 6v-3l-4 4 4 4v-3a8 8 0 0 0 8-8c0-1.57-.46-3.03-1.24-4.26"/></svg> Auto-upgrade adds it in US Gov Arizona</span>
        </li><li class="lcx-cov__row lcx-cov__row--manual">
            <span class="lcx-cov__type">Global Provisioned<small>You migrate</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 27 of 27 regions"><i style="--p:100.0%"></i></span>
            <span class="lcx-cov__num"><b>27</b>/27</span>
            <span class="lcx-cov__note lcx-cov__note--ok"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8m4.59-12.42L10 14.17l-2.59-2.58L6 13l4 4 8-8z"/></svg> Already offered in all 27 regions</span>
        </li><li class="lcx-cov__row lcx-cov__row--manual">
            <span class="lcx-cov__type">Data Zone Provisioned<small>You migrate</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 12 of 13 regions"><i style="--p:92.3%"></i></span>
            <span class="lcx-cov__num"><b>12</b>/13</span>
            <span class="lcx-cov__note lcx-cov__note--manual" title="US Gov Arizona"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 7a2.5 2.5 0 0 0-2.5-2.5c-.17 0-.34 0-.5.05V4a2.5 2.5 0 0 0-3.17-2.41A2.51 2.51 0 0 0 12.5 0c-1.23 0-2.25.89-2.46 2.06C9.87 2 9.69 2 9.5 2A2.5 2.5 0 0 0 7 4.5v5.89c-.34-.31-.76-.54-1.22-.66L5 9.5c-.82-.21-1.69.11-2.18.85-.38.57-.4 1.31-.15 1.95l2.56 6.43A8.36 8.36 0 0 0 13 24c4.42 0 8-3.58 8-8zm-2 9c0 3.31-2.69 6-6 6a6.36 6.36 0 0 1-5.91-4L4.5 11.45l.5.14c.5.12.85.46 1 .91L7 15h2V4.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V2.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V4c0-.28.22-.5.5-.5s.5.22.5.5v8h2V7c0-.28.22-.5.5-.5s.5.22.5.5z"/></svg> Not offered yet in US Gov Arizona</span>
        </li><li class="lcx-cov__row lcx-cov__row--manual">
            <span class="lcx-cov__type">Regional Provisioned<small>You migrate</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 29 of 29 regions"><i style="--p:100.0%"></i></span>
            <span class="lcx-cov__num"><b>29</b>/29</span>
            <span class="lcx-cov__note lcx-cov__note--ok"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8m4.59-12.42L10 14.17l-2.59-2.58L6 13l4 4 8-8z"/></svg> Already offered in all 29 regions</span>
        </li><li class="lcx-cov__row lcx-cov__row--manual">
            <span class="lcx-cov__type">Batch<small>You migrate</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 0 of 22 regions"><i style="--p:0.0%"></i></span>
            <span class="lcx-cov__num"><b>0</b>/22</span>
            <span class="lcx-cov__note lcx-cov__note--manual" title="Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 7a2.5 2.5 0 0 0-2.5-2.5c-.17 0-.34 0-.5.05V4a2.5 2.5 0 0 0-3.17-2.41A2.51 2.51 0 0 0 12.5 0c-1.23 0-2.25.89-2.46 2.06C9.87 2 9.69 2 9.5 2A2.5 2.5 0 0 0 7 4.5v5.89c-.34-.31-.76-.54-1.22-.66L5 9.5c-.82-.21-1.69.11-2.18.85-.38.57-.4 1.31-.15 1.95l2.56 6.43A8.36 8.36 0 0 0 13 24c4.42 0 8-3.58 8-8zm-2 9c0 3.31-2.69 6-6 6a6.36 6.36 0 0 1-5.91-4L4.5 11.45l.5.14c.5.12.85.46 1 .91L7 15h2V4.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V2.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V4c0-.28.22-.5.5-.5s.5.22.5.5v8h2V7c0-.28.22-.5.5-.5s.5.22.5.5z"/></svg> Not offered yet in Australia East, Brazil South, Canada East +19 more</span>
        </li>
        </ul>
    </article><article class="lcx-cov lcx-cov--danger">
        <header class="lcx-cov__head">
            <div class="lcx-cov__pair">
                <a href="../models/gpt-4-1-nano/"><span class="pv pv--openai pv--sm" aria-hidden="true" title="OpenAI"></span><span>gpt-4.1-nano</span></a>
                <svg class="fm-icon lcx-cov__arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 11h11.17l-4.88-4.88L12.7 4.7 20 12l-7.3 7.3-1.41-1.42L16.17 13H5z"/></svg>
                <a href="../models/gpt-5-nano/"><span class="pv pv--openai pv--sm" aria-hidden="true" title="OpenAI"></span><span>gpt-5-nano</span></a>
            </div>
            <span class="lc-badge lc-badge--danger">Retires in 6 days</span>
        </header>
        <p class="lcx-cov__meta">Oct 14, 2026 · version 2025-04-14</p>
        <ul class="lcx-cov__rows">
        <li class="lcx-cov__row lcx-cov__row--auto">
            <span class="lcx-cov__type">Global Standard<small>Upgraded for you</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 26 of 26 regions"><i style="--p:100.0%"></i></span>
            <span class="lcx-cov__num"><b>26</b>/26</span>
            <span class="lcx-cov__note lcx-cov__note--ok"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8m4.59-12.42L10 14.17l-2.59-2.58L6 13l4 4 8-8z"/></svg> Already offered in all 26 regions</span>
        </li><li class="lcx-cov__row lcx-cov__row--auto">
            <span class="lcx-cov__type">Data Zone Standard<small>Upgraded for you</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 14 of 14 regions"><i style="--p:100.0%"></i></span>
            <span class="lcx-cov__num"><b>14</b>/14</span>
            <span class="lcx-cov__note lcx-cov__note--ok"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8m4.59-12.42L10 14.17l-2.59-2.58L6 13l4 4 8-8z"/></svg> Already offered in all 14 regions</span>
        </li><li class="lcx-cov__row lcx-cov__row--auto">
            <span class="lcx-cov__type">Regional Standard<small>Upgraded for you</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 26 of 26 regions"><i style="--p:100.0%"></i></span>
            <span class="lcx-cov__num"><b>26</b>/26</span>
            <span class="lcx-cov__note lcx-cov__note--ok"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8m4.59-12.42L10 14.17l-2.59-2.58L6 13l4 4 8-8z"/></svg> Already offered in all 26 regions</span>
        </li><li class="lcx-cov__row lcx-cov__row--manual">
            <span class="lcx-cov__type">Global Provisioned<small>You migrate</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 0 of 27 regions"><i style="--p:0.0%"></i></span>
            <span class="lcx-cov__num"><b>0</b>/27</span>
            <span class="lcx-cov__note lcx-cov__note--manual" title="Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 7a2.5 2.5 0 0 0-2.5-2.5c-.17 0-.34 0-.5.05V4a2.5 2.5 0 0 0-3.17-2.41A2.51 2.51 0 0 0 12.5 0c-1.23 0-2.25.89-2.46 2.06C9.87 2 9.69 2 9.5 2A2.5 2.5 0 0 0 7 4.5v5.89c-.34-.31-.76-.54-1.22-.66L5 9.5c-.82-.21-1.69.11-2.18.85-.38.57-.4 1.31-.15 1.95l2.56 6.43A8.36 8.36 0 0 0 13 24c4.42 0 8-3.58 8-8zm-2 9c0 3.31-2.69 6-6 6a6.36 6.36 0 0 1-5.91-4L4.5 11.45l.5.14c.5.12.85.46 1 .91L7 15h2V4.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V2.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V4c0-.28.22-.5.5-.5s.5.22.5.5v8h2V7c0-.28.22-.5.5-.5s.5.22.5.5z"/></svg> Not offered yet in Australia East, Brazil South, Canada Central +24 more</span>
        </li><li class="lcx-cov__row lcx-cov__row--manual">
            <span class="lcx-cov__type">Data Zone Provisioned<small>You migrate</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 0 of 13 regions"><i style="--p:0.0%"></i></span>
            <span class="lcx-cov__num"><b>0</b>/13</span>
            <span class="lcx-cov__note lcx-cov__note--manual" title="East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 7a2.5 2.5 0 0 0-2.5-2.5c-.17 0-.34 0-.5.05V4a2.5 2.5 0 0 0-3.17-2.41A2.51 2.51 0 0 0 12.5 0c-1.23 0-2.25.89-2.46 2.06C9.87 2 9.69 2 9.5 2A2.5 2.5 0 0 0 7 4.5v5.89c-.34-.31-.76-.54-1.22-.66L5 9.5c-.82-.21-1.69.11-2.18.85-.38.57-.4 1.31-.15 1.95l2.56 6.43A8.36 8.36 0 0 0 13 24c4.42 0 8-3.58 8-8zm-2 9c0 3.31-2.69 6-6 6a6.36 6.36 0 0 1-5.91-4L4.5 11.45l.5.14c.5.12.85.46 1 .91L7 15h2V4.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V2.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V4c0-.28.22-.5.5-.5s.5.22.5.5v8h2V7c0-.28.22-.5.5-.5s.5.22.5.5z"/></svg> Not offered yet in East US, East US 2, France Central +10 more</span>
        </li><li class="lcx-cov__row lcx-cov__row--manual">
            <span class="lcx-cov__type">Regional Provisioned<small>You migrate</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 0 of 29 regions"><i style="--p:0.0%"></i></span>
            <span class="lcx-cov__num"><b>0</b>/29</span>
            <span class="lcx-cov__note lcx-cov__note--manual" title="Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 7a2.5 2.5 0 0 0-2.5-2.5c-.17 0-.34 0-.5.05V4a2.5 2.5 0 0 0-3.17-2.41A2.51 2.51 0 0 0 12.5 0c-1.23 0-2.25.89-2.46 2.06C9.87 2 9.69 2 9.5 2A2.5 2.5 0 0 0 7 4.5v5.89c-.34-.31-.76-.54-1.22-.66L5 9.5c-.82-.21-1.69.11-2.18.85-.38.57-.4 1.31-.15 1.95l2.56 6.43A8.36 8.36 0 0 0 13 24c4.42 0 8-3.58 8-8zm-2 9c0 3.31-2.69 6-6 6a6.36 6.36 0 0 1-5.91-4L4.5 11.45l.5.14c.5.12.85.46 1 .91L7 15h2V4.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V2.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V4c0-.28.22-.5.5-.5s.5.22.5.5v8h2V7c0-.28.22-.5.5-.5s.5.22.5.5z"/></svg> Not offered yet in Australia East, Brazil South, Canada Central +26 more</span>
        </li><li class="lcx-cov__row lcx-cov__row--manual">
            <span class="lcx-cov__type">Batch<small>You migrate</small></span>
            <span class="lcx-cov__bar" role="img" aria-label="Replacement offered in 0 of 22 regions"><i style="--p:0.0%"></i></span>
            <span class="lcx-cov__num"><b>0</b>/22</span>
            <span class="lcx-cov__note lcx-cov__note--manual" title="Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3"><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 7a2.5 2.5 0 0 0-2.5-2.5c-.17 0-.34 0-.5.05V4a2.5 2.5 0 0 0-3.17-2.41A2.51 2.51 0 0 0 12.5 0c-1.23 0-2.25.89-2.46 2.06C9.87 2 9.69 2 9.5 2A2.5 2.5 0 0 0 7 4.5v5.89c-.34-.31-.76-.54-1.22-.66L5 9.5c-.82-.21-1.69.11-2.18.85-.38.57-.4 1.31-.15 1.95l2.56 6.43A8.36 8.36 0 0 0 13 24c4.42 0 8-3.58 8-8zm-2 9c0 3.31-2.69 6-6 6a6.36 6.36 0 0 1-5.91-4L4.5 11.45l.5.14c.5.12.85.46 1 .91L7 15h2V4.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V2.5c0-.28.22-.5.5-.5s.5.22.5.5V12h2V4c0-.28.22-.5.5-.5s.5.22.5.5v8h2V7c0-.28.22-.5.5-.5s.5.22.5.5z"/></svg> Not offered yet in Australia East, Brazil South, Canada East +19 more</span>
        </li>
        </ul>
    </article>
</div>
<p class="lcx-cov-foot">26 other models retire later without a named replacement yet — Microsoft names one 90–120 days before the date. Track them in the <a href="../retirements/">retirement planner</a>.</p>

<p class="diagram-note">From the latest availability snapshot. Regions are compared by model name, not by individual version. Gaps in pay-as-you-go rows are filled by the upgrade itself; gaps in provisioned or batch rows mean you can't migrate there yet.</p>

## Countdown to a retirement

<ol class="lcx-count" aria-label="Countdown to a GA model retirement"><li class="lcx-count__step lcx-count__step--info">
        <span class="lcx-count__when">−120 to −90 days</span>
        <strong>Replacement named</strong>
        <p>Microsoft picks the recommended replacement and lists it in the retirement schedule.</p>
        <p class="lcx-count__you"><b>You:</b> Start testing newer models — you don't have to wait for this.</p>
    </li><li class="lcx-count__step lcx-count__step--info">
        <span class="lcx-count__when">≈ −90 days</span>
        <strong>Testable in Global Standard</strong>
        <p>The replacement can be deployed in Global Standard.</p>
        <p class="lcx-count__you"><b>You:</b> Run your own prompts and evaluations against it.</p>
    </li><li class="lcx-count__step lcx-count__step--warning">
        <span class="lcx-count__when">≥ −60 days</span>
        <strong>You get told</strong>
        <p>Email to subscription owners and an Azure Service Health advisory.</p>
        <p class="lcx-count__you"><b>You:</b> Set a Service Health alert so the right people see it.</p>
    </li><li class="lcx-count__step lcx-count__step--warning">
        <span class="lcx-count__when">≈ −30 days</span>
        <strong>PTU window opens</strong>
        <p>The replacement appears in the provisioned regions where the old model retires.</p>
        <p class="lcx-count__you"><b>You:</b> Migrate provisioned deployments in place or side by side.</p>
    </li><li class="lcx-count__step lcx-count__step--danger">
        <span class="lcx-count__when">Day 0</span>
        <strong>Retirement</strong>
        <p>Pay-as-you-go deployments are upgraded region by region. Anything not moved returns 410 Gone.</p>
        <p class="lcx-count__you"><b>You:</b> Dates can't be extended.</p>
    </li></ol>

<div class="lcx-notify">
    <div><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M10 21h4a2 2 0 0 1-2 2 2 2 0 0 1-2-2m11-2v1H3v-1l2-2v-6c0-3.1 2.03-5.83 5-6.71V4a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.29c2.97.88 5 3.61 5 6.71v6zm-4-8a5 5 0 0 0-5-5 5 5 0 0 0-5 5v7h10zm2.75-7.81-1.42 1.42A8.98 8.98 0 0 1 21 11h2c0-2.93-1.16-5.75-3.25-7.81M1 11h2c0-2.4.96-4.7 2.67-6.39L4.25 3.19A10.96 10.96 0 0 0 1 11"/></svg><strong>Email</strong><p>Sent automatically to subscription owners with active deployments.</p></div>
    <div><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 13h3.28l2.5-6.24 4.04 12.12L16.2 11H21V9h-6.2l-1.96 4.6L8.86 1.62 4.92 11H3z"/></svg><strong>Azure Service Health</strong><p>Health advisories under <em>Azure OpenAI Service</em> — create an alert rule for email, SMS or a webhook.</p></div>
    <div><svg class="fm-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 4h18v16H3zm2 2v3h14V6zm0 5v3h6v-3zm8 0v3h6v-3zm-8 5v2h6v-2zm8 0v2h6v-2z"/></svg><strong>Models API</strong><p>Check <code>lifecycleStatus</code> and <code>deprecation</code> dates for any model, any time.</p></div>
</div>

## Common questions

??? question "Can I get more time before a model retires?"
    No. Retirement dates can't be extended. In rare cases a model with a security or compliance problem can be retired early with shorter notice.

??? question "Do I have to use the replacement Microsoft names?"
    No. It's Microsoft's recommendation and the model used for automatic upgrades, but you can migrate to any model that suits you. Compare quality, speed and cost on your own prompts rather than public benchmarks.

??? question "Will my code need to change?"
    Usually not to keep calling the deployment — the name and endpoint stay the same. But check that the API parameters, tools and output format you rely on still behave the same with the new model.

??? question "What does 'existing customer' mean for deprecated models?"
    It's decided per **Azure subscription**: a subscription that has ever deployed that exact model version can keep creating deployments until retirement. A new subscription in the same tenant doesn't inherit that access.

??? question "Is Azure Government different?"
    Yes. Global Standard isn't available, not every model is offered, and usually only one version of a model is available at a time, with a **30-day overlap** when a new version arrives.

## Reference

??? info "What each badge on this site means"
    Hover or tap any lifecycle badge on the site for this explanation in place.

    | Badge | What it means | What to do |
    |---|---|---|
    | <span class="lc-badge lc-badge--danger">Retires in 12 days</span> | Firm retirement date within 30 days | Move traffic to the replacement now |
    | <span class="lc-badge lc-badge--warning">Retires in 60 days</span> | Firm retirement date within 90 days | Test the replacement and plan the cut-over |
    | <span class="lc-badge lc-badge--warning">Retirement imminent</span> | A *no-earlier-than* date has passed — it can retire any time after notice | Treat as retiring now |
    | <span class="lc-badge lc-badge--caution">Deprecated</span> | Closed to new customers | Don't start new work on it |
    | <span class="lc-badge lc-badge--success">GA · until Jun 2027</span> | Generally available, with its next retirement month | Safe to build on |
    | <span class="lc-badge lc-badge--neutral">No retirement date</span> | Not in Microsoft's retirement tables yet (common for new and partner models) | Check the model card in Foundry |

??? info "Who can deploy at each stage"
    | Stage | Meaning | New deployments | Existing deployments |
    |---|---|---|---|
    | <span class="lc-badge lc-badge--info">Preview</span> | Experimental — weights, runtime and API might change; not guaranteed to reach GA | Yes | Yes |
    | <span class="lc-badge lc-badge--success">Generally available</span> | Production-ready — weights and APIs are fixed | Yes | Yes |
    | Legacy | Newer, more capable models exist (optional stage) | Yes, until deprecated | Yes |
    | <span class="lc-badge lc-badge--caution">Deprecated</span> | No longer available to new customers | Only subscriptions that already used this version | Yes |
    | <span class="lc-badge lc-badge--muted">Retired</span> | Removed from service — every request returns `410 Gone` | No | No |

??? info "Reading the Models API (the names don't match the portal)"
    The API's `Deprecated` means **retired**, not deprecated — watch out for this when scripting checks.

    | API `lifecycleStatus` | Means | Badge on this site |
    |---|---|---|
    | `Preview` | Preview, not for production | <span class="lc-badge lc-badge--info">Preview</span> |
    | `GenerallyAvailable` | GA and open to new customers | <span class="lc-badge lc-badge--success">Generally available</span> |
    | `Deprecating` | Deprecated — existing customers only | <span class="lc-badge lc-badge--caution">Deprecated</span> |
    | `Deprecated` | Retired — no longer served | <span class="lc-badge lc-badge--muted">Retired</span> |

    If `deprecation.inference` is in the past, treat the model as retired even if `lifecycleStatus` hasn't caught up yet.

Adapted from Microsoft Learn: [Foundry Models lifecycle and support policy](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirements), [Working with models](https://learn.microsoft.com/azure/foundry/openai/how-to/working-with-models#model-deployment-upgrade-configuration) and [Model migration process](https://learn.microsoft.com/azure/foundry/foundry-models/concepts/model-migration). See [Retirements](../retirements/) for every model-specific date.
