# AI Foundry Model Availability

Real-time tracking of Azure AI Foundry model availability across regions and deployment types.

<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-value">111</div>
    <div class="stat-label">Models Tracked</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">28</div>
    <div class="stat-label">Azure Regions</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">8</div>
    <div class="stat-label">Action Needed</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">45</div>
    <div class="stat-label">Scheduled Retirements</div>
  </div>
</div>

---

???+ tip "Recent Availability Changes"
    | Date | Change | Model | Region | SKU Type |
    |------|--------|-------|--------|----------|
    | 2026-02-18 | <span class="badge-added">Added</span> | [Claude Sonnet 4.6 (preview)](models/claude-sonnet-4-6-(preview)/) | East US 2 | Region Availability Maas |
    | 2026-02-18 | <span class="badge-added">Added</span> | [Claude Sonnet 4.6 (preview)](models/claude-sonnet-4-6-(preview)/) | Sweden Central | Region Availability Maas |
    | 2026-02-12 | <span class="badge-added">Added</span> | [text-embedding-3-large](models/text-embedding-3-large/) | France Central | Datazone standard |
    | 2026-02-12 | <span class="badge-added">Added</span> | [text-embedding-3-large](models/text-embedding-3-large/) | Germany West Central | Datazone standard |
    | 2026-02-12 | <span class="badge-added">Added</span> | [text-embedding-3-large](models/text-embedding-3-large/) | Italy North | Datazone standard |
    | 2026-02-12 | <span class="badge-added">Added</span> | [text-embedding-3-large](models/text-embedding-3-large/) | Poland Central | Datazone standard |
    | 2026-02-12 | <span class="badge-added">Added</span> | [text-embedding-3-large](models/text-embedding-3-large/) | Spain Central | Datazone standard |
    | 2026-02-12 | <span class="badge-added">Added</span> | [text-embedding-3-large](models/text-embedding-3-large/) | Sweden Central | Datazone standard |
    | 2026-02-12 | <span class="badge-added">Added</span> | [text-embedding-3-large](models/text-embedding-3-large/) | West Europe | Datazone standard |
    | 2026-02-12 | <span class="badge-added">Added</span> | [text-embedding-3-small](models/text-embedding-3-small/) | France Central | Datazone standard |

    *… and 965 more — see [full change history](history.md)*


---

## :material-alert-circle: Deprecation & Retirement Notices

!!! danger "Retiring Within 30 Days — 2 model versions"
    These models require **immediate migration**. After the retirement date, API calls will return errors.

    | Model | Version | Category | Retirement Date | Status | Replacement |
    |-------|---------|----------|-----------------|--------|-------------|
    | [gpt-5-chat](models/gpt-5-chat/) | 2025-08-07 | Text Generation | 2026-03-01 | <span class="badge badge-retiring-soon">Retiring Soon</span> | [gpt-5.2-chat](models/gpt-5-2-chat/) |
    | [gpt-5-chat](models/gpt-5-chat/) | 2025-10-03 | Text Generation | 2026-03-01 | <span class="badge badge-retiring-soon">Retiring Soon</span> | [gpt-5.2-chat](models/gpt-5-2-chat/) |

!!! warning "Upcoming Retirements (31-90 Days) — 3 model versions"
    Plan and test your migration to the replacement model.

    | Model | Version | Category | Retirement Date | Status | Replacement |
    |-------|---------|----------|-----------------|--------|-------------|
    | [gpt-4o](models/gpt-4o/) | 2024-05-13 | Text Generation | 2026-03-31 | <span class="badge badge-retiring">Retiring</span> | [gpt-5.1](models/gpt-5-1/) |
    | [gpt-4o](models/gpt-4o/) | 2024-08-06 | Text Generation | 2026-03-31 | <span class="badge badge-retiring">Retiring</span> | [gpt-5.1](models/gpt-5-1/) |
    | [gpt-4o-mini](models/gpt-4o-mini/) | 2024-07-18 | Text Generation | 2026-03-31 | <span class="badge badge-retiring">Retiring</span> | [gpt-4.1-mini](models/gpt-4-1-mini/) |

!!! failure "Already Retired — 3 model versions"
    These models are no longer available. Migrate to the listed replacement.

    | Model | Version | Category | Retirement Date | Status | Replacement |
    |-------|---------|----------|-----------------|--------|-------------|
    | [gpt-4o-audio-preview](models/gpt-4o-audio-preview/) | 2024-12-17 | Audio | 2026-02-02 | <span class="badge badge-retired">Retired</span> | [gpt-audio](models/gpt-audio/) |
    | [gpt-4o-realtime-preview](models/gpt-4o-realtime-preview/) | 2024-12-17 | Audio | 2026-02-02 | <span class="badge badge-retired">Retired</span> | [gpt-realtime](models/gpt-realtime/) |
    | [dall-e-3](models/dall-e-3/) | 3 | Image And Video | 2026-02-18 | <span class="badge badge-retired">Retired</span> | [gpt-image-1-mini](models/gpt-image-1-mini/) |


??? info "Deprecation vs Retirement — What's the Difference?"
    **Deprecation** marks a model version as no longer recommended. It still works, but no new deployments can be created.
    After deprecation you should begin migrating to the replacement model.

    **Retirement** means the model version is fully removed. API calls will return errors after the retirement date.
    Always migrate **before** the retirement date.

    | Phase | New Deployments | Existing Deployments | API Calls |
    |-------|-----------------|----------------------|-----------|
    | **Active** | :material-check: Allowed | :material-check: Running | :material-check: Working |
    | **Deprecated** | :material-close: Blocked | :material-check: Running | :material-check: Working |
    | **Retired** | :material-close: Blocked | :material-close: Removed | :material-close: Errors |

    See [full retirement details](retirements.md) and [Microsoft's model lifecycle docs](https://learn.microsoft.com/azure/ai-services/openai/concepts/model-retirements).

---

## :material-book-open-variant: Browse By

| View | Description |
|------|-------------|
| [**All Models**](models/index.md) | Complete model catalog with SKU details |
| [**By Region**](by-region.md) | Find what's available in your region |
| [**By SKU Type**](by-sku.md) | Filter by deployment type |
| [**Change History**](history.md) | Recent availability changes |

---

_Last updated: 2026-02-24 00:17 UTC_
