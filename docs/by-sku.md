# Models by SKU Type

Explore every deployment SKU and discover which models and regions support it.

<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-value">20</div>
    <div class="stat-label">SKU Types</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">111</div>
    <div class="stat-label">Models</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">342</div>
    <div class="stat-label">Model × SKU Combinations</div>
  </div>
</div>

---

## :material-layers-outline: SKU Deployment Types Explained

<div class="grid cards sku-explainer-grid" markdown>

-   :material-earth:{ .lg .middle } **Global**

    ---

    Routes requests intelligently across Azure regions for maximum availability and throughput.
    Data may be processed in any region within the Azure geography.

    | | |
    |---|---|
    | :material-cube-outline: Models | **111** |
    | :material-map-marker-outline: Regions | **28** (100% coverage) |

    **SKU types:** `Global batch` · `Global batch datazone` · `Global coverage` · `Standard global deployments`

    **:material-check-circle-outline: Best for:** Applications needing worldwide reach, automatic
    failover, and maximum uptime across Azure's global network.

-   :material-shield-lock-outline:{ .lg .middle } **Datazone**

    ---

    Keeps data within a specified geographic zone to satisfy compliance and residency policies.
    Choose the zone; Azure handles routing within that boundary.

    | | |
    |---|---|
    | :material-cube-outline: Models | **19** |
    | :material-map-marker-outline: Regions | **14** (50% coverage) |

    **SKU types:** `Datazone provisioned managed` · `Datazone standard`

    **:material-check-circle-outline: Best for:** GDPR compliance, data sovereignty requirements,
    regulated industries (finance, healthcare, government).

-   :material-cash-multiple:{ .lg .middle } **Standard**

    ---

    Pay-as-you-go deployments in a single Azure region with flexible, on-demand scaling.
    No capacity reservation required — you pay only for what you use.

    | | |
    |---|---|
    | :material-cube-outline: Models | **25** |
    | :material-map-marker-outline: Regions | **25** (89% coverage) |

    **SKU types:** `Standard (all)` · `Standard GPT-3.5 Turbo` · `Standard GPT-4` · `Standard audio` · `Standard chat completions` · `Standard completions` · `Standard embeddings` · `Standard image generation`

    **:material-check-circle-outline: Best for:** Variable workloads, development and testing,
    cost-sensitive applications, or when you don't need guaranteed throughput.

-   :material-speedometer:{ .lg .middle } **Provisioned (PTU)**

    ---

    Reserved throughput units (PTUs) guarantee consistent, high-performance inference at scale.
    Capacity is pre-allocated, so latency and throughput are predictable regardless of platform load.

    | | |
    |---|---|
    | :material-cube-outline: Models | **17** |
    | :material-map-marker-outline: Regions | **28** (100% coverage) |

    **SKU types:** `Provisioned (PTU managed)` · `Provisioned global`

    **:material-check-circle-outline: Best for:** High-volume production workloads, latency-sensitive
    applications, or scenarios where consistent throughput is critical.

</div>

---

## :material-target: SKU Selection Guide

| Need | Recommended SKU | Why |
|------|-----------------|-----|
| Global reach with failover | **Global** | Automatic routing, high availability |
| Data residency compliance | **Datazone** | Data stays in specified regions |
| Cost-effective, variable load | **Standard** | Pay-as-you-go pricing |
| Predictable high throughput | **Provisioned (PTU)** | Reserved capacity, guaranteed performance |

---

## :material-format-list-bulleted-type: SKU Overview

| Category | SKU Type | Models | Regions | Coverage |
|----------|----------|--------|---------|----------|
| <span class="sku-badge sku-global">Global</span> | Global batch | 10 | 22 | 79% |
| <span class="sku-badge sku-global">Global</span> | Global batch datazone | 10 | 12 | 43% |
| <span class="sku-badge sku-global">Global</span> | Global coverage | 111 | 28 | 100% |
| <span class="sku-badge sku-global">Global</span> | Standard global deployments | 48 | 28 | 100% |
| <span class="sku-badge sku-datazone">Datazone</span> | Datazone provisioned managed | 13 | 13 | 46% |
| <span class="sku-badge sku-datazone">Datazone</span> | Datazone standard | 18 | 14 | 50% |
| <span class="sku-badge sku-standard">Standard</span> | Standard (all) | 15 | 25 | 89% |
| <span class="sku-badge sku-standard">Standard</span> | Standard GPT-3.5 Turbo | 3 | 15 | 54% |
| <span class="sku-badge sku-standard">Standard</span> | Standard GPT-4 | 4 | 15 | 54% |
| <span class="sku-badge sku-standard">Standard</span> | Standard audio | 3 | 8 | 29% |
| <span class="sku-badge sku-standard">Standard</span> | Standard chat completions | 6 | 15 | 54% |
| <span class="sku-badge sku-standard">Standard</span> | Standard completions | 1 | 1 | 4% |
| <span class="sku-badge sku-standard">Standard</span> | Standard embeddings | 3 | 21 | 75% |
| <span class="sku-badge sku-standard">Standard</span> | Standard image generation | 4 | 8 | 29% |
| <span class="sku-badge sku-provisioned">Provisioned</span> | Provisioned (PTU managed) | 14 | 27 | 96% |
| <span class="sku-badge sku-provisioned">Provisioned</span> | Provisioned global | 14 | 28 | 100% |
| <span class="sku-badge sku-other">Other</span> | Data Zone Standard | 5 | 16 | 57% |
| <span class="sku-badge sku-other">Other</span> | Global Provisioned Managed | 3 | 25 | 89% |
| <span class="sku-badge sku-other">Other</span> | Global Standard | 16 | 25 | 89% |
| <span class="sku-badge sku-other">Other</span> | Region Availability Maas | 41 | 7 | 25% |

---

## :material-table-search: Model–SKU Explorer

Filter by category, SKU type, or model to find exactly what you need.

<div class="filter-controls">
  <div class="filter-group">
    <label for="sku-cat-filter">SKU Category</label>
    <select id="sku-cat-filter" onchange="filterSkuTable()">
      <option value="">All Categories</option>
      <option value="Global">Global</option>
      <option value="Datazone">Datazone</option>
      <option value="Standard">Standard</option>
      <option value="Provisioned">Provisioned</option>
    </select>
  </div>
  <div class="filter-group">
    <label for="sku-type-filter">SKU Type</label>
    <select id="sku-type-filter" onchange="filterSkuTable()">
      <option value="">All SKU Types</option>
      <option value="Data Zone Standard">Data Zone Standard</option>
      <option value="Datazone provisioned managed">Datazone provisioned managed</option>
      <option value="Datazone standard">Datazone standard</option>
      <option value="Global Provisioned Managed">Global Provisioned Managed</option>
      <option value="Global Standard">Global Standard</option>
      <option value="Global batch">Global batch</option>
      <option value="Global batch datazone">Global batch datazone</option>
      <option value="Global coverage">Global coverage</option>
      <option value="Provisioned (PTU managed)">Provisioned (PTU managed)</option>
      <option value="Provisioned global">Provisioned global</option>
      <option value="Region Availability Maas">Region Availability Maas</option>
      <option value="Standard (all)">Standard (all)</option>
      <option value="Standard GPT-3.5 Turbo">Standard GPT-3.5 Turbo</option>
      <option value="Standard GPT-4">Standard GPT-4</option>
      <option value="Standard audio">Standard audio</option>
      <option value="Standard chat completions">Standard chat completions</option>
      <option value="Standard completions">Standard completions</option>
      <option value="Standard embeddings">Standard embeddings</option>
      <option value="Standard global deployments">Standard global deployments</option>
      <option value="Standard image generation">Standard image generation</option>
    </select>
  </div>
  <div class="filter-group">
    <label for="sku-model-search">Model Name</label>
    <input type="text" id="sku-model-search" placeholder="Search model..." oninput="filterSkuTable()">
  </div>
  <div class="filter-group">
    <label for="sku-coverage-filter">Coverage Level</label>
    <select id="sku-coverage-filter" onchange="filterSkuTable()">
      <option value="">All Levels</option>
      <option value="Broad">Broad (25+)</option>
      <option value="Strong">Strong (20-24)</option>
      <option value="Growing">Growing (15-19)</option>
      <option value="Emerging">Emerging (&lt;15)</option>
    </select>
  </div>
  <div class="filter-group">
    <label for="sku-region-filter">Region</label>
    <select id="sku-region-filter" onchange="filterSkuTable()">
      <option value="">All Regions</option>
      <option value="Australia East">Australia East</option>
      <option value="Brazil South">Brazil South</option>
      <option value="Canada Central">Canada Central</option>
      <option value="Canada East">Canada East</option>
      <option value="Central US">Central US</option>
      <option value="East US">East US</option>
      <option value="East US 2">East US 2</option>
      <option value="France Central">France Central</option>
      <option value="Germany West Central">Germany West Central</option>
      <option value="Italy North">Italy North</option>
      <option value="Japan East">Japan East</option>
      <option value="Korea Central">Korea Central</option>
      <option value="North Central US">North Central US</option>
      <option value="Norway East">Norway East</option>
      <option value="Poland Central">Poland Central</option>
      <option value="South Africa North">South Africa North</option>
      <option value="South Central US">South Central US</option>
      <option value="South India">South India</option>
      <option value="Southeast Asia">Southeast Asia</option>
      <option value="Spain Central">Spain Central</option>
      <option value="Sweden Central">Sweden Central</option>
      <option value="Switzerland North">Switzerland North</option>
      <option value="Switzerland West">Switzerland West</option>
      <option value="UAE North">UAE North</option>
      <option value="UK South">UK South</option>
      <option value="West Europe">West Europe</option>
      <option value="West US">West US</option>
      <option value="West US 3">West US 3</option>
    </select>
  </div>
  <div class="filter-group">
    <label>&nbsp;</label>
    <button onclick="resetSkuFilters()" class="md-button">Reset</button>
  </div>
</div>

<div class="table-responsive">
<table id="sku-table" class="display">
  <thead>
    <tr>
      <th>Model</th>
      <th>Category</th>
      <th>SKU Type</th>
      <th>Regions</th>
      <th>Coverage</th>
      <th>% of Regions</th>
      <th class="hidden-col">Region List</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="../models/claude-haiku-4-5-(preview)/"><strong>Claude Haiku 4.5 (preview)</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/claude-haiku-4-5-(preview)/"><strong>Claude Haiku 4.5 (preview)</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-4-1-(preview)/"><strong>Claude Opus 4.1 (preview)</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-4-1-(preview)/"><strong>Claude Opus 4.1 (preview)</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-4-5-(preview)/"><strong>Claude Opus 4.5 (preview)</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-4-5-(preview)/"><strong>Claude Opus 4.5 (preview)</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-4-6-(preview)/"><strong>Claude Opus 4.6 (preview)</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-4-6-(preview)/"><strong>Claude Opus 4.6 (preview)</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/claude-sonnet-4-5-(preview)/"><strong>Claude Sonnet 4.5 (preview)</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/claude-sonnet-4-5-(preview)/"><strong>Claude Sonnet 4.5 (preview)</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/claude-sonnet-4-6-(preview)/"><strong>Claude Sonnet 4.6 (preview)</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/claude-sonnet-4-6-(preview)/"><strong>Claude Sonnet 4.6 (preview)</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/codestral-2501/"><strong>Codestral-2501</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/codestral-2501/"><strong>Codestral-2501</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-command-r-08-2024/"><strong>Cohere Command R 08-2024</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-command-r-08-2024/"><strong>Cohere Command R 08-2024</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-command-r+-08-2024/"><strong>Cohere Command R+ 08-2024</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-command-r+-08-2024/"><strong>Cohere Command R+ 08-2024</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-embed-v3---english/"><strong>Cohere Embed v3 - English</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-embed-v3---english/"><strong>Cohere Embed v3 - English</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-embed-v3---multilingual/"><strong>Cohere Embed v3 - Multilingual</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-embed-v3---multilingual/"><strong>Cohere Embed v3 - Multilingual</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-rerank-v3-5/"><strong>Cohere Rerank v3.5</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-rerank-v3-5/"><strong>Cohere Rerank v3.5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-r1/"><strong>DeepSeek-R1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-r1/"><strong>DeepSeek-R1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Provisioned Managed</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-r1/"><strong>DeepSeek-R1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-r1/"><strong>DeepSeek-R1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-r1-0528/"><strong>DeepSeek-R1-0528</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-r1-0528/"><strong>DeepSeek-R1-0528</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Provisioned Managed</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-r1-0528/"><strong>DeepSeek-R1-0528</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v3-0324/"><strong>DeepSeek-V3-0324</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v3-0324/"><strong>DeepSeek-V3-0324</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Provisioned Managed</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v3-0324/"><strong>DeepSeek-V3-0324</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v3-0324/"><strong>DeepSeek-V3-0324</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v3-1/"><strong>DeepSeek-V3.1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v3-1/"><strong>DeepSeek-V3.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/flux-1-1-pro/"><strong>FLUX-1.1-pro</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/flux-1-1-pro/"><strong>FLUX-1.1-pro</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/flux-1-kontext-pro/"><strong>FLUX.1-Kontext-pro</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/flux-1-kontext-pro/"><strong>FLUX.1-Kontext-pro</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-1-405b-instruct/"><strong>Llama 3.1 405B Instruct</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-1-405b-instruct/"><strong>Llama 3.1 405B Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-1-8b-instruct/"><strong>Llama 3.1 8B Instruct</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-1-8b-instruct/"><strong>Llama 3.1 8B Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-3-70b-instruct/"><strong>Llama 3.3 70B Instruct</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-3-70b-instruct/"><strong>Llama 3.3 70B Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-11b-vision-instruct/"><strong>Llama-3.2-11B-Vision-Instruct</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-11b-vision-instruct/"><strong>Llama-3.2-11B-Vision-Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-1b/"><strong>Llama-3.2-1B</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-1b/"><strong>Llama-3.2-1B</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-1b-instruct/"><strong>Llama-3.2-1B-Instruct</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-1b-instruct/"><strong>Llama-3.2-1B-Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-3b/"><strong>Llama-3.2-3B</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-3b/"><strong>Llama-3.2-3B</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-3b-instruct/"><strong>Llama-3.2-3B-Instruct</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-3b-instruct/"><strong>Llama-3.2-3B-Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-90b-vision-instruct/"><strong>Llama-3.2-90B-Vision-Instruct</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-90b-vision-instruct/"><strong>Llama-3.2-90B-Vision-Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-3-70b-instruct/"><strong>Llama-3.3-70B-Instruct</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-3-70b-instruct/"><strong>Llama-3.3-70B-Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-3-70b-instruct/"><strong>Llama-3.3-70B-Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/"><strong>Llama-4-Maverick-17B-128E-Instruct-FP8</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/"><strong>Llama-4-Maverick-17B-128E-Instruct-FP8</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-guard-3-11b-vision/"><strong>Llama-Guard-3-11B-Vision</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-guard-3-11b-vision/"><strong>Llama-Guard-3-11B-Vision</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-guard-3-1b/"><strong>Llama-Guard-3-1B</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-guard-3-1b/"><strong>Llama-Guard-3-1B</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mai-ds-r1/"><strong>MAI-DS-R1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mai-ds-r1/"><strong>MAI-DS-R1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mai-ds-r1/"><strong>MAI-DS-R1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/ministral-3b/"><strong>Ministral-3B</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/ministral-3b/"><strong>Ministral-3B</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-medium-3-(25-05)/"><strong>Mistral Medium 3 (25.05)</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-medium-3-(25-05)/"><strong>Mistral Medium 3 (25.05)</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-small-25-03/"><strong>Mistral Small 25.03</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-small-25-03/"><strong>Mistral Small 25.03</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4/"><strong>Phi-4</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4/"><strong>Phi-4</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-mini-instruct/"><strong>Phi-4-mini-instruct</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-mini-instruct/"><strong>Phi-4-mini-instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-mini-reasoning/"><strong>Phi-4-mini-reasoning</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-mini-reasoning/"><strong>Phi-4-mini-reasoning</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-multimodal-instruct/"><strong>Phi-4-multimodal-instruct</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-multimodal-instruct/"><strong>Phi-4-multimodal-instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-reasoning/"><strong>Phi-4-reasoning</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-reasoning/"><strong>Phi-4-reasoning</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/stable-diffusion-3-5-large/"><strong>Stable Diffusion 3.5 Large</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/stable-diffusion-3-5-large/"><strong>Stable Diffusion 3.5 Large</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/stable-image-core/"><strong>Stable Image Core</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/stable-image-core/"><strong>Stable Image Core</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/stable-image-ultra/"><strong>Stable Image Ultra</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/stable-image-ultra/"><strong>Stable Image Ultra</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/timegen-1/"><strong>TimeGEN-1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/timegen-1/"><strong>TimeGEN-1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/codex-mini/"><strong>codex-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/codex-mini/"><strong>codex-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/computer-use-preview/"><strong>computer-use-preview</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">East US 2, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/computer-use-preview/"><strong>computer-use-preview</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">East US 2, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/dall-e-3/"><strong>dall-e-3</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Australia East, East US, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/dall-e-3/"><strong>dall-e-3</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard image generation</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Australia East, East US, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/dall-e-3/"><strong>dall-e-3</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard (all)</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Australia East, East US, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-35-turbo/"><strong>gpt-35-turbo</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-35-turbo/"><strong>gpt-35-turbo</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+21 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>86%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-35-turbo/"><strong>gpt-35-turbo</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard chat completions</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Japan East,North Central US,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Australia East, Canada East, East US, East US 2, France Central, Japan East, North Central US, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-35-turbo/"><strong>gpt-35-turbo</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard GPT-3.5 Turbo</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Japan East,North Central US,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+12 more</button></span></td>
      <td><span class="badge badge-growing">Growing</span></td>
      <td>54%</td>
      <td class="hidden-col">Australia East, Canada East, East US, East US 2, France Central, Japan East, North Central US, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-35-turbo-16k/"><strong>gpt-35-turbo-16k</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Japan East,North Central US,Sweden Central,Switzerland North,UK South"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+7 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>36%</td>
      <td class="hidden-col">Australia East, Canada East, East US, East US 2, France Central, Japan East, North Central US, Sweden Central, Switzerland North, UK South</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-35-turbo-16k/"><strong>gpt-35-turbo-16k</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard GPT-3.5 Turbo</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Japan East,North Central US,Sweden Central,Switzerland North,UK South"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+7 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>36%</td>
      <td class="hidden-col">Australia East, Canada East, East US, East US 2, France Central, Japan East, North Central US, Sweden Central, Switzerland North, UK South</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-35-turbo-instruct/"><strong>gpt-35-turbo-instruct</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-35-turbo-instruct/"><strong>gpt-35-turbo-instruct</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard completions</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>4%</td>
      <td class="hidden-col">East US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-35-turbo-instruct/"><strong>gpt-35-turbo-instruct</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard GPT-3.5 Turbo</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4/"><strong>gpt-4</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UAE North,UK South,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>79%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UAE North, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4/"><strong>gpt-4</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UAE North,UK South,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>79%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UAE North, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4/"><strong>gpt-4</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard chat completions</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4/"><strong>gpt-4</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard GPT-4</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Japan East,North Central US,Norway East,South Central US,South India,Sweden Central,Switzerland North,UK South,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+12 more</button></span></td>
      <td><span class="badge badge-growing">Growing</span></td>
      <td>54%</td>
      <td class="hidden-col">Australia East, Canada East, East US, East US 2, France Central, Japan East, North Central US, Norway East, South Central US, South India, Sweden Central, Switzerland North, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-32k/"><strong>gpt-4-32k</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+18 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>75%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-32k/"><strong>gpt-4-32k</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Central US,East US,East US 2,France Central,Germany West Central,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+17 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Central US, East US, East US 2, France Central, Germany West Central, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-32k/"><strong>gpt-4-32k</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard GPT-4</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,France Central" data-all-regions="Australia East,Canada East,France Central,Sweden Central,Switzerland North"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>18%</td>
      <td class="hidden-col">Australia East, Canada East, France Central, Sweden Central, Switzerland North</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>46%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>79%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>43%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Central US" data-all-regions="Australia East,Brazil South,Central US,East US,East US 2,Japan East,Korea Central,North Central US,South Central US,South India,Sweden Central,Switzerland North,UAE North,UK South,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+13 more</button></span></td>
      <td><span class="badge badge-growing">Growing</span></td>
      <td>57%</td>
      <td class="hidden-col">Australia East, Brazil South, Central US, East US, East US 2, Japan East, Korea Central, North Central US, South Central US, South India, Sweden Central, Switzerland North, UAE North, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard (all)</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,Switzerland North,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>29%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, Switzerland North, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>43%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>79%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>43%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,East US" data-all-regions="Australia East,Brazil South,East US,East US 2,Japan East,Korea Central,North Central US,South Central US,South India,Sweden Central,UK South,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>46%</td>
      <td class="hidden-col">Australia East, Brazil South, East US, East US 2, Japan East, Korea Central, North Central US, South Central US, South India, Sweden Central, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard (all)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Japan East,North Central US,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+12 more</button></span></td>
      <td><span class="badge badge-growing">Growing</span></td>
      <td>54%</td>
      <td class="hidden-col">Australia East, Canada East, East US, East US 2, France Central, Japan East, North Central US, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>46%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>79%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>43%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard (all)</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">North Central US, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>43%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>79%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>43%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>96%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard chat completions</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Japan East,North Central US,Norway East,South Central US,South India,Sweden Central,Switzerland North,UK South,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Australia East, Canada East, East US, East US 2, France Central, Japan East, North Central US, Norway East, South Central US, South India, Sweden Central, Switzerland North, UK South, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard GPT-4</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard (all)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,Central US" data-all-regions="Australia East,Canada East,Central US,East US,East US 2,France Central,Japan East,North Central US,Norway East,South Central US,South India,Sweden Central,Switzerland North,UK South,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+13 more</button></span></td>
      <td><span class="badge badge-growing">Growing</span></td>
      <td>57%</td>
      <td class="hidden-col">Australia East, Canada East, Central US, East US, East US 2, France Central, Japan East, North Central US, Norway East, South Central US, South India, Sweden Central, Switzerland North, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-audio-preview/"><strong>gpt-4o-audio-preview</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-audio-preview/"><strong>gpt-4o-audio-preview</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>43%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>79%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>43%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,East US,East US 2,France Central,Japan East,Korea Central,North Central US,Norway East,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UK South,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+18 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>75%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, East US, East US 2, France Central, Japan East, Korea Central, North Central US, Norway East, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard chat completions</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard GPT-4</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard (all)</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini-audio-preview/"><strong>gpt-4o-mini-audio-preview</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US, East US 2</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini-audio-preview/"><strong>gpt-4o-mini-audio-preview</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US, East US 2</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini-realtime-preview/"><strong>gpt-4o-mini-realtime-preview</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini-realtime-preview/"><strong>gpt-4o-mini-realtime-preview</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini-transcribe/"><strong>gpt-4o-mini-transcribe</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini-transcribe/"><strong>gpt-4o-mini-transcribe</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini-tts/"><strong>gpt-4o-mini-tts</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>4%</td>
      <td class="hidden-col">East US 2</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini-tts/"><strong>gpt-4o-mini-tts</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>4%</td>
      <td class="hidden-col">East US 2</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-realtime-preview/"><strong>gpt-4o-realtime-preview</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-realtime-preview/"><strong>gpt-4o-realtime-preview</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-transcribe/"><strong>gpt-4o-transcribe</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-transcribe/"><strong>gpt-4o-transcribe</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-transcribe-diarize/"><strong>gpt-4o-transcribe-diarize</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-transcribe-diarize/"><strong>gpt-4o-transcribe-diarize</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>46%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>79%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Canada East,East US,East US 2" data-all-regions="Canada East,East US,East US 2,Japan East,Korea Central,North Central US,South Central US,South India,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+7 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>36%</td>
      <td class="hidden-col">Canada East, East US, East US 2, Japan East, Korea Central, North Central US, South Central US, South India, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>93%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-chat/"><strong>gpt-5-chat</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-chat/"><strong>gpt-5-chat</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-codex/"><strong>gpt-5-codex</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-codex/"><strong>gpt-5-codex</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>46%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Korea Central')">Korea Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Korea Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>93%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-nano/"><strong>gpt-5-nano</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>93%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-nano/"><strong>gpt-5-nano</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-nano/"><strong>gpt-5-nano</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>93%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-pro/"><strong>gpt-5-pro</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-pro/"><strong>gpt-5-pro</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>46%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+1 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US, East US 2, France Central, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>79%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US 2" data-all-regions="Australia East,Canada East,East US 2,Japan East,Korea Central,Sweden Central,Switzerland North,UK South"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>29%</td>
      <td class="hidden-col">Australia East, Canada East, East US 2, Japan East, Korea Central, Sweden Central, Switzerland North, UK South</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-chat/"><strong>gpt-5.1-chat</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US 2" data-all-regions="Australia East,Canada East,East US 2,Japan East,Korea Central,Sweden Central,Switzerland North,UK South"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>29%</td>
      <td class="hidden-col">Australia East, Canada East, East US 2, Japan East, Korea Central, Sweden Central, Switzerland North, UK South</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-chat/"><strong>gpt-5.1-chat</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US 2" data-all-regions="Australia East,Canada East,East US 2,Japan East,Korea Central,Sweden Central,Switzerland North,UK South"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>29%</td>
      <td class="hidden-col">Australia East, Canada East, East US 2, Japan East, Korea Central, Sweden Central, Switzerland North, UK South</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex/"><strong>gpt-5.1-codex</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,Central US" data-all-regions="Australia East,Canada East,Central US,East US 2,Japan East,Korea Central,Sweden Central,Switzerland North,UK South,West Europe"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+7 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>36%</td>
      <td class="hidden-col">Australia East, Canada East, Central US, East US 2, Japan East, Korea Central, Sweden Central, Switzerland North, UK South, West Europe</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex/"><strong>gpt-5.1-codex</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('West Europe')">West Europe</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, West Europe</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex/"><strong>gpt-5.1-codex</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,Central US" data-all-regions="Australia East,Canada East,Central US,East US 2,Japan East,Korea Central,Switzerland North,UK South,West Europe"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>32%</td>
      <td class="hidden-col">Australia East, Canada East, Central US, East US 2, Japan East, Korea Central, Switzerland North, UK South, West Europe</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex/"><strong>gpt-5.1-codex</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US 2" data-all-regions="Australia East,Canada East,East US 2,Japan East,Korea Central,Sweden Central,Switzerland North,UK South"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>29%</td>
      <td class="hidden-col">Australia East, Canada East, East US 2, Japan East, Korea Central, Sweden Central, Switzerland North, UK South</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex-max/"><strong>gpt-5.1-codex-max</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex-max/"><strong>gpt-5.1-codex-max</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex-mini/"><strong>gpt-5.1-codex-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US 2" data-all-regions="Australia East,Canada East,East US 2,Japan East,Korea Central,Sweden Central,Switzerland North,UK South"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>29%</td>
      <td class="hidden-col">Australia East, Canada East, East US 2, Japan East, Korea Central, Sweden Central, Switzerland North, UK South</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex-mini/"><strong>gpt-5.1-codex-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US 2" data-all-regions="Australia East,Canada East,East US 2,Japan East,Korea Central,Sweden Central,Switzerland North,UK South"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>29%</td>
      <td class="hidden-col">Australia East, Canada East, East US 2, Japan East, Korea Central, Sweden Central, Switzerland North, UK South</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Central US,East US 2,South Central US" data-all-regions="Central US,East US 2,South Central US,Sweden Central,UK South"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('South Central US')">South Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>18%</td>
      <td class="hidden-col">Central US, East US 2, South Central US, Sweden Central, UK South</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">Central US, East US 2</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('UK South')">UK South</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, UK South</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('South Central US')">South Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">East US 2, South Central US, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2-chat/"><strong>gpt-5.2-chat</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2-chat/"><strong>gpt-5.2-chat</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2-codex/"><strong>gpt-5.2-codex</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2-codex/"><strong>gpt-5.2-codex</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-audio/"><strong>gpt-audio</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-audio/"><strong>gpt-audio</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-audio-mini/"><strong>gpt-audio-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-audio-mini/"><strong>gpt-audio-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1/"><strong>gpt-image-1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>18%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1/"><strong>gpt-image-1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>18%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1/"><strong>gpt-image-1</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard image generation</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('UAE North')">UAE North</span> <span class="region-badge" onclick="filterBySkuRegion('West US 3')">West US 3</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1-mini/"><strong>gpt-image-1-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1-mini/"><strong>gpt-image-1-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>18%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1-mini/"><strong>gpt-image-1-mini</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard image generation</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US, North Central US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1-5/"><strong>gpt-image-1.5</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>18%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1-5/"><strong>gpt-image-1.5</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>18%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1-5/"><strong>gpt-image-1.5</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard image generation</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>18%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime/"><strong>gpt-realtime</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime/"><strong>gpt-realtime</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-mini/"><strong>gpt-realtime-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-mini/"><strong>gpt-realtime-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/grok-3/"><strong>grok-3</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-3/"><strong>grok-3</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Data Zone Standard</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-3/"><strong>grok-3</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-3-mini/"><strong>grok-3-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-3-mini/"><strong>grok-3-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Data Zone Standard</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-3-mini/"><strong>grok-3-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4/"><strong>grok-4</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4/"><strong>grok-4</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-fast-non-reasoning/"><strong>grok-4-fast-non-reasoning</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-fast-non-reasoning/"><strong>grok-4-fast-non-reasoning</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Data Zone Standard</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-fast-non-reasoning/"><strong>grok-4-fast-non-reasoning</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-fast-reasoning/"><strong>grok-4-fast-reasoning</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-fast-reasoning/"><strong>grok-4-fast-reasoning</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Data Zone Standard</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-fast-reasoning/"><strong>grok-4-fast-reasoning</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-code-fast-1/"><strong>grok-code-fast-1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-code-fast-1/"><strong>grok-code-fast-1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-document-ai-2505/"><strong>mistral-document-ai-2505</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-document-ai-2505/"><strong>mistral-document-ai-2505</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Data Zone Standard</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Norway East,Poland Central,South Central US,Spain Central,Sweden Central,Switzerland North,Switzerland West,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+13 more</button></span></td>
      <td><span class="badge badge-growing">Growing</span></td>
      <td>57%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Norway East, Poland Central, South Central US, Spain Central, Sweden Central, Switzerland North, Switzerland West, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-document-ai-2505/"><strong>mistral-document-ai-2505</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-document-ai-2505/"><strong>mistral-document-ai-2505</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/model-router/"><strong>model-router</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/model-router/"><strong>model-router</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/model-router/"><strong>model-router</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>43%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Japan East')">Japan East</span> <span class="region-badge" onclick="filterBySkuRegion('UAE North')">UAE North</span> <span class="region-badge" onclick="filterBySkuRegion('UK South')">UK South</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Japan East, UAE North, UK South</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard (all)</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o1-mini/"><strong>o1-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US</td>
    </tr>
    <tr>
      <td><a href="../models/o1-mini/"><strong>o1-mini</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard chat completions</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US</td>
    </tr>
    <tr>
      <td><a href="../models/o1-preview/"><strong>o1-preview</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US</td>
    </tr>
    <tr>
      <td><a href="../models/o1-preview/"><strong>o1-preview</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard chat completions</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>46%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>79%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>43%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,East US,East US 2" data-all-regions="Australia East,East US,East US 2,North Central US,South Central US,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>29%</td>
      <td class="hidden-col">Australia East, East US, East US 2, North Central US, South Central US, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>93%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-deep-research/"><strong>o3-deep-research</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Norway East')">Norway East</span> <span class="region-badge" onclick="filterBySkuRegion('West US')">West US</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">Norway East, West US</td>
    </tr>
    <tr>
      <td><a href="../models/o3-deep-research/"><strong>o3-deep-research</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Norway East')">Norway East</span> <span class="region-badge" onclick="filterBySkuRegion('West US')">West US</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">Norway East, West US</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>43%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>79%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US 2" data-all-regions="Australia East,Canada East,East US 2,Japan East,Korea Central,South Central US,South India,Sweden Central,Switzerland North,UAE North"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+7 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>36%</td>
      <td class="hidden-col">Australia East, Canada East, East US 2, Japan East, Korea Central, South Central US, South India, Sweden Central, Switzerland North, UAE North</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-pro/"><strong>o3-pro</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/o3-pro/"><strong>o3-pro</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>46%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>79%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>43%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>100%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,Japan East,North Central US,South Central US,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>32%</td>
      <td class="hidden-col">Central US, East US, East US 2, Japan East, North Central US, South Central US, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>93%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard (all)</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>25%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/sora/"><strong>sora</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/sora/"><strong>sora</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/sora/"><strong>sora</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard (all)</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>4%</td>
      <td class="hidden-col">East US 2</td>
    </tr>
    <tr>
      <td><a href="../models/sora-2/"><strong>sora-2</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/sora-2/"><strong>sora-2</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-large/"><strong>text-embedding-3-large</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>93%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-large/"><strong>text-embedding-3-large</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-large/"><strong>text-embedding-3-large</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard embeddings</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Japan East,Norway East,Poland Central,South Africa North,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+13 more</button></span></td>
      <td><span class="badge badge-growing">Growing</span></td>
      <td>57%</td>
      <td class="hidden-col">Australia East, Canada East, East US, East US 2, France Central, Japan East, Norway East, Poland Central, South Africa North, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-large/"><strong>text-embedding-3-large</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-large/"><strong>text-embedding-3-large</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard (all)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,Norway East,Poland Central,South Africa North,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+16 more</button></span></td>
      <td><span class="badge badge-growing">Growing</span></td>
      <td>68%</td>
      <td class="hidden-col">Australia East, Canada East, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, Norway East, Poland Central, South Africa North, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-small/"><strong>text-embedding-3-small</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-small/"><strong>text-embedding-3-small</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-small/"><strong>text-embedding-3-small</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard embeddings</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,Japan East,Switzerland North,UAE North,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>29%</td>
      <td class="hidden-col">Australia East, Canada East, East US, East US 2, Japan East, Switzerland North, UAE North, West US</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-small/"><strong>text-embedding-3-small</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-small/"><strong>text-embedding-3-small</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard (all)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,Japan East,Switzerland North,UAE North,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>29%</td>
      <td class="hidden-col">Australia East, Canada East, East US, East US 2, Japan East, Switzerland North, UAE North, West US</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-ada-002/"><strong>text-embedding-ada-002</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-ada-002/"><strong>text-embedding-ada-002</strong></a></td>
      <td><span class="sku-badge sku-datazone">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>50%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-ada-002/"><strong>text-embedding-ada-002</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard embeddings</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Japan East,North Central US,Norway East,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+15 more</button></span></td>
      <td><span class="badge badge-growing">Growing</span></td>
      <td>64%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Japan East, North Central US, Norway East, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-ada-002/"><strong>text-embedding-ada-002</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Standard global deployments</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+21 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>86%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-ada-002/"><strong>text-embedding-ada-002</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard (all)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Japan East,North Central US,Norway East,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+16 more</button></span></td>
      <td><span class="badge badge-growing">Growing</span></td>
      <td>68%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Japan East, North Central US, Norway East, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/tsuzumi-7b/"><strong>tsuzumi-7b</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/tsuzumi-7b/"><strong>tsuzumi-7b</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>21%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/tts/"><strong>tts</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterBySkuRegion('West US 3')">West US 3</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">North Central US, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/tts/"><strong>tts</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard audio</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">North Central US, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/tts/"><strong>tts</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard (all)</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterBySkuRegion('West US 3')">West US 3</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">North Central US, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/tts-hd/"><strong>tts-hd</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterBySkuRegion('West US 3')">West US 3</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">North Central US, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/tts-hd/"><strong>tts-hd</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard audio</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>7%</td>
      <td class="hidden-col">North Central US, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/tts-hd/"><strong>tts-hd</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard (all)</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterBySkuRegion('West US 3')">West US 3</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">North Central US, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/whisper/"><strong>whisper</strong></a></td>
      <td><span class="sku-badge sku-global">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US 2,North Central US,Norway East" data-all-regions="East US 2,North Central US,Norway East,South India,Sweden Central,Switzerland North,UAE North,West Europe"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Norway East')">Norway East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>29%</td>
      <td class="hidden-col">East US 2, North Central US, Norway East, South India, Sweden Central, Switzerland North, UAE North, West Europe</td>
    </tr>
    <tr>
      <td><a href="../models/whisper/"><strong>whisper</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard audio</td>
      <td><span class="region-list" data-preview-regions="East US 2,North Central US,Norway East" data-all-regions="East US 2,North Central US,Norway East,South India,Sweden Central,Switzerland North,UAE North,West Europe"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Norway East')">Norway East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>29%</td>
      <td class="hidden-col">East US 2, North Central US, Norway East, South India, Sweden Central, Switzerland North, UAE North, West Europe</td>
    </tr>
    <tr>
      <td><a href="../models/whisper/"><strong>whisper</strong></a></td>
      <td><span class="sku-badge sku-standard">Standard</span></td>
      <td>Standard (all)</td>
      <td><span class="region-list" data-preview-regions="East US 2,North Central US,Norway East" data-all-regions="East US 2,North Central US,Norway East,South India,Sweden Central,Switzerland North,UAE North,West Europe"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Norway East')">Norway East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>29%</td>
      <td class="hidden-col">East US 2, North Central US, Norway East, South India, Sweden Central, Switzerland North, UAE North, West Europe</td>
    </tr>
  </tbody>
</table>
</div>

---

_Last updated: 2026-02-23 23:07 UTC_
