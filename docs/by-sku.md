# Models by SKU Type

Explore every deployment SKU and discover which models and regions support it.

<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-value">21</div>
    <div class="stat-label">SKU Types</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">154</div>
    <div class="stat-label">Models</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">606</div>
    <div class="stat-label">Model × SKU Combinations</div>
  </div>
</div>

---

## :material-layers-outline: SKU Deployment Types Explained

??? example ":material-earth: Global — Worldwide availability with intelligent routing"

    Routes requests intelligently across Azure regions for maximum availability and throughput.
    Data may be processed in any region within the Azure geography.

    | | |
    |---|---|
    | :material-cube-outline: Models | **154** |
    | :material-map-marker-outline: Regions | **35** (100% coverage) |

    **SKU types:** `Global Standard` · `Global batch` · `Global batch datazone` · `Global coverage`

    **:material-check-circle-outline: Best for:** Applications needing worldwide reach, automatic
    failover, and maximum uptime across Azure's global network.

    **:material-alert-outline: Compliance:** Data may cross region boundaries — not suitable for
    HIPAA, FedRAMP, or strict data-residency requirements.

??? example ":material-shield-lock-outline: Datazone — Data residency compliance deployments"

    Keeps data within a specified geographic zone to satisfy compliance and residency policies.
    Choose the zone; Azure handles routing within that boundary.

    | | |
    |---|---|
    | :material-cube-outline: Models | **25** |
    | :material-map-marker-outline: Regions | **21** (60% coverage) |

    **SKU types:** `Datazone provisioned managed` · `Datazone standard`

    **:material-check-circle-outline: Best for:** GDPR compliance, data sovereignty requirements,
    regulated industries (finance, healthcare, government).

    **:material-shield-check-outline: Compliance:** Data stays within the specified geographic zone —
    supports GDPR and regional data-residency policies.

??? example ":material-cash-multiple: Standard — Pay-as-you-go regional deployments"

    Pay-as-you-go deployments in a single Azure region with flexible, on-demand scaling.
    No capacity reservation required — you pay only for what you use.

    | | |
    |---|---|
    | :material-cube-outline: Models | **13** |
    | :material-map-marker-outline: Regions | **25** (71% coverage) |

    **SKU types:** `Standard`

    **:material-check-circle-outline: Best for:** Variable workloads, development and testing,
    cost-sensitive applications, or when you don't need guaranteed throughput.

    **:material-shield-check-outline: Compliance:** Single-region deployment — HIPAA-eligible in
    supported regions with a BAA from Microsoft.

??? example ":material-speedometer: Provisioned (PTU) — Reserved throughput capacity"

    Reserved throughput units (PTUs) guarantee consistent, high-performance inference at scale.
    Capacity is pre-allocated, so latency and throughput are predictable regardless of platform load.

    | | |
    |---|---|
    | :material-cube-outline: Models | **18** |
    | :material-map-marker-outline: Regions | **28** (80% coverage) |

    **SKU types:** `Provisioned (PTU managed)` · `Provisioned global`

    **:material-check-circle-outline: Best for:** High-volume production workloads, latency-sensitive
    applications, or scenarios where consistent throughput is critical.

    **:material-shield-check-outline: Compliance:** Single-region deployment — HIPAA-eligible in
    supported regions with a BAA from Microsoft.

---

??? tip ":material-target: SKU Selection Guide"

    | Need | Recommended SKU | Why |
    |------|-----------------|-----|
    | Global reach with failover | **Global** | Automatic routing, high availability |
    | Data residency compliance | **Datazone** | Data stays in specified regions |
    | Cost-effective, variable load | **Standard** | Pay-as-you-go pricing |
    | Predictable high throughput | **Provisioned (PTU)** | Reserved capacity, guaranteed performance |
    | HIPAA / regulated workloads | **Standard** or **Provisioned** | Single-region; HIPAA-eligible with a Microsoft BAA |
    | Avoid Global for compliance | ⚠ **Not Global** | Global data routing is incompatible with strict data-residency requirements |

??? note ":material-format-list-bulleted-type: SKU Overview"

    | Category | SKU Type | Models | Regions | Coverage |
    |----------|----------|--------|---------|----------|
    | <span class="sku-badge sku-global">Global</span> | Global Standard | 53 | 28 | 80% |
    | <span class="sku-badge sku-global">Global</span> | Global batch | 12 | 22 | 63% |
    | <span class="sku-badge sku-global">Global</span> | Global batch datazone | 12 | 12 | 34% |
    | <span class="sku-badge sku-global">Global</span> | Global coverage | 154 | 35 | 100% |
    | <span class="sku-badge sku-datazone">Datazone</span> | Datazone provisioned managed | 16 | 13 | 37% |
    | <span class="sku-badge sku-datazone">Datazone</span> | Datazone standard | 24 | 21 | 60% |
    | <span class="sku-badge sku-standard">Standard</span> | Standard | 13 | 25 | 71% |
    | <span class="sku-badge sku-provisioned">Provisioned</span> | Provisioned (PTU managed) | 15 | 27 | 77% |
    | <span class="sku-badge sku-provisioned">Provisioned</span> | Provisioned global | 18 | 27 | 77% |
    | <span class="sku-badge sku-other">Other</span> | Datazone Provisioned Managed Gov | 6 | 1 | 3% |
    | <span class="sku-badge sku-other">Other</span> | Datazone Standard Gov | 10 | 2 | 6% |
    | <span class="sku-badge sku-other">Other</span> | Datazone Standard Priority Processing | 7 | 7 | 20% |
    | <span class="sku-badge sku-other">Other</span> | Deployments Batch | 12 | 22 | 63% |
    | <span class="sku-badge sku-other">Other</span> | Deployments Provisioned | 27 | 33 | 94% |
    | <span class="sku-badge sku-other">Other</span> | Deployments Standard | 102 | 33 | 94% |
    | <span class="sku-badge sku-other">Other</span> | Marketplace Deployments Standard | 19 | 31 | 89% |
    | <span class="sku-badge sku-other">Other</span> | Provisioned Models Gov | 1 | 1 | 3% |
    | <span class="sku-badge sku-other">Other</span> | Region Availability Maas | 35 | 7 | 20% |
    | <span class="sku-badge sku-other">Other</span> | Standard Global By Capability | 55 | 28 | 80% |
    | <span class="sku-badge sku-other">Other</span> | Standard Global Priority Processing | 9 | 29 | 83% |
    | <span class="sku-badge sku-other">Other</span> | Standard Models Gov | 6 | 1 | 3% |

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
      <option value="Datazone Provisioned Managed Gov">Datazone Provisioned Managed Gov</option>
      <option value="Datazone Standard Gov">Datazone Standard Gov</option>
      <option value="Datazone Standard Priority Processing">Datazone Standard Priority Processing</option>
      <option value="Datazone provisioned managed">Datazone provisioned managed</option>
      <option value="Datazone standard">Datazone standard</option>
      <option value="Deployments Batch">Deployments Batch</option>
      <option value="Deployments Provisioned">Deployments Provisioned</option>
      <option value="Deployments Standard">Deployments Standard</option>
      <option value="Global Standard">Global Standard</option>
      <option value="Global batch">Global batch</option>
      <option value="Global batch datazone">Global batch datazone</option>
      <option value="Global coverage">Global coverage</option>
      <option value="Marketplace Deployments Standard">Marketplace Deployments Standard</option>
      <option value="Provisioned (PTU managed)">Provisioned (PTU managed)</option>
      <option value="Provisioned Models Gov">Provisioned Models Gov</option>
      <option value="Provisioned global">Provisioned global</option>
      <option value="Region Availability Maas">Region Availability Maas</option>
      <option value="Standard">Standard</option>
      <option value="Standard Global By Capability">Standard Global By Capability</option>
      <option value="Standard Global Priority Processing">Standard Global Priority Processing</option>
      <option value="Standard Models Gov">Standard Models Gov</option>
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
      <option value="Japan West">Japan West</option>
      <option value="Korea Central">Korea Central</option>
      <option value="North Central US">North Central US</option>
      <option value="North Europe">North Europe</option>
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
      <option value="UK West">UK West</option>
      <option value="West Central US">West Central US</option>
      <option value="West Europe">West Europe</option>
      <option value="West US">West US</option>
      <option value="West US 2">West US 2</option>
      <option value="West US 3">West US 3</option>
      <option value="usgovarizona">usgovarizona</option>
      <option value="usgovvirginia">usgovvirginia</option>
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
      <td><a href="../models/codestral-2501/"><strong>Codestral-2501</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/codestral-2501/"><strong>Codestral-2501</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/codestral-2501/"><strong>Codestral-2501</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-command-r-08-2024/"><strong>Cohere Command R 08-2024</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-command-r-08-2024/"><strong>Cohere Command R 08-2024</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-command-r+-08-2024/"><strong>Cohere Command R+ 08-2024</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-command-r+-08-2024/"><strong>Cohere Command R+ 08-2024</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-embed-v3---english/"><strong>Cohere Embed v3 - English</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-embed-v3---english/"><strong>Cohere Embed v3 - English</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-embed-v3---multilingual/"><strong>Cohere Embed v3 - Multilingual</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-embed-v3---multilingual/"><strong>Cohere Embed v3 - Multilingual</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-rerank-v3-5/"><strong>Cohere Rerank v3.5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-rerank-v3-5/"><strong>Cohere Rerank v3.5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-command-a-plus-05-2026/"><strong>Cohere-command-a-plus-05-2026</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-command-a-plus-05-2026/"><strong>Cohere-command-a-plus-05-2026</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-rerank-v4-0-fast/"><strong>Cohere-rerank-v4.0-fast</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-rerank-v4-0-fast/"><strong>Cohere-rerank-v4.0-fast</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-rerank-v4-0-pro/"><strong>Cohere-rerank-v4.0-pro</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-rerank-v4-0-pro/"><strong>Cohere-rerank-v4.0-pro</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-r1/"><strong>DeepSeek-R1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-r1/"><strong>DeepSeek-R1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v3-0324/"><strong>DeepSeek-V3-0324</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v3-0324/"><strong>DeepSeek-V3-0324</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v3-2/"><strong>DeepSeek-V3.2</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v3-2/"><strong>DeepSeek-V3.2</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v3-2/"><strong>DeepSeek-V3.2</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v3-2-speciale/"><strong>DeepSeek-V3.2-Speciale</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v3-2-speciale/"><strong>DeepSeek-V3.2-Speciale</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v4-flash/"><strong>DeepSeek-V4-Flash</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v4-flash/"><strong>DeepSeek-V4-Flash</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v4-flash-0731/"><strong>DeepSeek-V4-Flash-0731</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v4-flash-0731/"><strong>DeepSeek-V4-Flash-0731</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v4-pro/"><strong>DeepSeek-V4-Pro</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/deepseek-v4-pro/"><strong>DeepSeek-V4-Pro</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/flux-1-1-pro/"><strong>FLUX-1.1-pro</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/flux-1-1-pro/"><strong>FLUX-1.1-pro</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/flux-1-kontext-pro/"><strong>FLUX.1-Kontext-pro</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/flux-1-kontext-pro/"><strong>FLUX.1-Kontext-pro</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/flux-2-flex/"><strong>FLUX.2-flex</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/flux-2-flex/"><strong>FLUX.2-flex</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/flux-2-pro/"><strong>FLUX.2-pro</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/flux-2-pro/"><strong>FLUX.2-pro</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/kimi-k2-5/"><strong>Kimi-K2.5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/kimi-k2-5/"><strong>Kimi-K2.5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/kimi-k2-6/"><strong>Kimi-K2.6</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/kimi-k2-6/"><strong>Kimi-K2.6</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/kimi-k2-7-code/"><strong>Kimi-K2.7-Code</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/kimi-k2-7-code/"><strong>Kimi-K2.7-Code</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-1-405b-instruct/"><strong>Llama 3.1 405B Instruct</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-1-405b-instruct/"><strong>Llama 3.1 405B Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-1-8b-instruct/"><strong>Llama 3.1 8B Instruct</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-1-8b-instruct/"><strong>Llama 3.1 8B Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-3-70b-instruct/"><strong>Llama 3.3 70B Instruct</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-3-70b-instruct/"><strong>Llama 3.3 70B Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-11b-vision-instruct/"><strong>Llama-3.2-11B-Vision-Instruct</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-11b-vision-instruct/"><strong>Llama-3.2-11B-Vision-Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-1b/"><strong>Llama-3.2-1B</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-1b/"><strong>Llama-3.2-1B</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-1b-instruct/"><strong>Llama-3.2-1B-Instruct</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-1b-instruct/"><strong>Llama-3.2-1B-Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-3b/"><strong>Llama-3.2-3B</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-3b/"><strong>Llama-3.2-3B</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-3b-instruct/"><strong>Llama-3.2-3B-Instruct</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-3b-instruct/"><strong>Llama-3.2-3B-Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-90b-vision-instruct/"><strong>Llama-3.2-90B-Vision-Instruct</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-2-90b-vision-instruct/"><strong>Llama-3.2-90B-Vision-Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-3-70b-instruct/"><strong>Llama-3.3-70B-Instruct</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-3-70b-instruct/"><strong>Llama-3.3-70B-Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-3-70b-instruct/"><strong>Llama-3.3-70B-Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-3-3-70b-instruct/"><strong>Llama-3.3-70B-Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/"><strong>Llama-4-Maverick-17B-128E-Instruct-FP8</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/"><strong>Llama-4-Maverick-17B-128E-Instruct-FP8</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-4-scout-17b-16e-instruct/"><strong>Llama-4-Scout-17B-16E-Instruct</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-4-scout-17b-16e-instruct/"><strong>Llama-4-Scout-17B-16E-Instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-guard-3-11b-vision/"><strong>Llama-Guard-3-11B-Vision</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-guard-3-11b-vision/"><strong>Llama-Guard-3-11B-Vision</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-guard-3-1b/"><strong>Llama-Guard-3-1B</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/llama-guard-3-1b/"><strong>Llama-Guard-3-1B</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mai-ds-r1/"><strong>MAI-DS-R1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mai-ds-r1/"><strong>MAI-DS-R1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mai-image-2-5/"><strong>MAI-Image-2.5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,South India,Sweden Central" data-all-regions="East US,South India,Sweden Central,UAE North,West Central US,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, South India, Sweden Central, UAE North, West Central US, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/mai-image-2-5/"><strong>MAI-Image-2.5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="East US,South India,Sweden Central" data-all-regions="East US,South India,Sweden Central,UAE North,West Central US,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, South India, Sweden Central, UAE North, West Central US, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/mai-image-2-5-flash/"><strong>MAI-Image-2.5-Flash</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,South India,Sweden Central" data-all-regions="East US,South India,Sweden Central,UAE North,West Central US,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, South India, Sweden Central, UAE North, West Central US, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/mai-image-2-5-flash/"><strong>MAI-Image-2.5-Flash</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="East US,South India,Sweden Central" data-all-regions="East US,South India,Sweden Central,UAE North,West Central US,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, South India, Sweden Central, UAE North, West Central US, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/mai-image-2-5-pro/"><strong>MAI-Image-2.5-Pro</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,South India,Sweden Central" data-all-regions="East US,South India,Sweden Central,UAE North,West Central US,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, South India, Sweden Central, UAE North, West Central US, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/mai-image-2-5-pro/"><strong>MAI-Image-2.5-Pro</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="East US,South India,Sweden Central" data-all-regions="East US,South India,Sweden Central,UAE North,West Central US,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, South India, Sweden Central, UAE North, West Central US, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/mai-image-2-6/"><strong>MAI-Image-2.6</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,South India,Sweden Central" data-all-regions="East US,South India,Sweden Central,UAE North,West Central US,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, South India, Sweden Central, UAE North, West Central US, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/mai-image-2-6/"><strong>MAI-Image-2.6</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="East US,South India,Sweden Central" data-all-regions="East US,South India,Sweden Central,UAE North,West Central US,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, South India, Sweden Central, UAE North, West Central US, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/mai-image-2-6-flash/"><strong>MAI-Image-2.6-Flash</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,South India,Sweden Central" data-all-regions="East US,South India,Sweden Central,UAE North,West Central US,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, South India, Sweden Central, UAE North, West Central US, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/mai-image-2-6-flash/"><strong>MAI-Image-2.6-Flash</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="East US,South India,Sweden Central" data-all-regions="East US,South India,Sweden Central,UAE North,West Central US,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, South India, Sweden Central, UAE North, West Central US, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/mai-thinking-1/"><strong>MAI-Thinking-1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mai-thinking-1/"><strong>MAI-Thinking-1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/ministral-3b/"><strong>Ministral-3B</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/ministral-3b/"><strong>Ministral-3B</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/ministral-3b/"><strong>Ministral-3B</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-medium-3-(25-05)/"><strong>Mistral Medium 3 (25.05)</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-medium-3-(25-05)/"><strong>Mistral Medium 3 (25.05)</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-small-25-03/"><strong>Mistral Small 25.03</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-small-25-03/"><strong>Mistral Small 25.03</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-large-3/"><strong>Mistral-Large-3</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-large-3/"><strong>Mistral-Large-3</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-large/"><strong>Mistral-large</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-large/"><strong>Mistral-large</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4/"><strong>Phi-4</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4/"><strong>Phi-4</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4/"><strong>Phi-4</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-mini-instruct/"><strong>Phi-4-mini-instruct</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-mini-instruct/"><strong>Phi-4-mini-instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-mini-instruct/"><strong>Phi-4-mini-instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-mini-reasoning/"><strong>Phi-4-mini-reasoning</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-mini-reasoning/"><strong>Phi-4-mini-reasoning</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-mini-reasoning/"><strong>Phi-4-mini-reasoning</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-multimodal-instruct/"><strong>Phi-4-multimodal-instruct</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-multimodal-instruct/"><strong>Phi-4-multimodal-instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-multimodal-instruct/"><strong>Phi-4-multimodal-instruct</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-reasoning/"><strong>Phi-4-reasoning</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-reasoning/"><strong>Phi-4-reasoning</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/phi-4-reasoning/"><strong>Phi-4-reasoning</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/stable-diffusion-3-5-large/"><strong>Stable Diffusion 3.5 Large</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/stable-diffusion-3-5-large/"><strong>Stable Diffusion 3.5 Large</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/stable-image-core/"><strong>Stable Image Core</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/stable-image-core/"><strong>Stable Image Core</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/stable-image-ultra/"><strong>Stable Image Ultra</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/stable-image-ultra/"><strong>Stable Image Ultra</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/timegen-1/"><strong>TimeGEN-1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/timegen-1/"><strong>TimeGEN-1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-fable-5/"><strong>claude-fable-5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/claude-fable-5/"><strong>claude-fable-5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/claude-fable-5-1/"><strong>claude-fable-5-1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/claude-fable-5-1/"><strong>claude-fable-5-1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/claude-haiku-4-5/"><strong>claude-haiku-4-5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-haiku-4-5/"><strong>claude-haiku-4-5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-4-5/"><strong>claude-opus-4-5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-4-5/"><strong>claude-opus-4-5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-4-6/"><strong>claude-opus-4-6</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-4-6/"><strong>claude-opus-4-6</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-4-7/"><strong>claude-opus-4-7</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-4-7/"><strong>claude-opus-4-7</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-4-8/"><strong>claude-opus-4-8</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-4-8/"><strong>claude-opus-4-8</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-5/"><strong>claude-opus-5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-5/"><strong>claude-opus-5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-5-5/"><strong>claude-opus-5-5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-opus-5-5/"><strong>claude-opus-5-5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-sonnet-4-5/"><strong>claude-sonnet-4-5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-sonnet-4-5/"><strong>claude-sonnet-4-5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-sonnet-4-6/"><strong>claude-sonnet-4-6</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-sonnet-4-6/"><strong>claude-sonnet-4-6</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-sonnet-5/"><strong>claude-sonnet-5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-sonnet-5/"><strong>claude-sonnet-5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-sonnet-5-5/"><strong>claude-sonnet-5-5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/claude-sonnet-5-5/"><strong>claude-sonnet-5-5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/codex-mini/"><strong>codex-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/codex-mini/"><strong>codex-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/codex-mini/"><strong>codex-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/codex-mini/"><strong>codex-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-command-a/"><strong>cohere-command-a</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/cohere-command-a/"><strong>cohere-command-a</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/computer-use-preview/"><strong>computer-use-preview</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">East US 2, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/computer-use-preview/"><strong>computer-use-preview</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">East US 2, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/computer-use-preview/"><strong>computer-use-preview</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">East US 2, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/computer-use-preview/"><strong>computer-use-preview</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">East US 2, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>37%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>40%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span> <span class="region-badge" onclick="filterBySkuRegion('usgovvirginia')">usgovvirginia</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Priority Processing</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>34%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Central US" data-all-regions="Australia East,Brazil South,Central US,East US,East US 2,Germany West Central,Japan East,Korea Central,North Central US,South Central US,South India,Southeast Asia,Sweden Central,Switzerland North,UAE North,UK South,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+15 more</button></span></td>
      <td><span class="badge badge-growing">Growing</span></td>
      <td>51%</td>
      <td class="hidden-col">Australia East, Brazil South, Central US, East US, East US 2, Germany West Central, Japan East, Korea Central, North Central US, South Central US, South India, Southeast Asia, Sweden Central, Switzerland North, UAE North, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global Priority Processing</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td>Standard</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,Switzerland North,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>23%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, Switzerland North, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Models Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">usgovarizona</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>34%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Provisioned Managed Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">usgovarizona</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>40%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span> <span class="region-badge" onclick="filterBySkuRegion('usgovvirginia')">usgovvirginia</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>34%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,East US" data-all-regions="Australia East,Brazil South,East US,East US 2,Japan East,Korea Central,North Central US,South Central US,South India,Sweden Central,Switzerland North,UK South,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>40%</td>
      <td class="hidden-col">Australia East, Brazil South, East US, East US 2, Japan East, Korea Central, North Central US, South Central US, South India, Sweden Central, Switzerland North, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td>Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Japan East,North Central US,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+12 more</button></span></td>
      <td><span class="badge badge-growing">Growing</span></td>
      <td>43%</td>
      <td class="hidden-col">Australia East, Canada East, East US, East US 2, France Central, Japan East, North Central US, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Models Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">usgovarizona</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>37%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>40%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>34%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>34%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Provisioned Managed Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">usgovarizona</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>40%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span> <span class="region-badge" onclick="filterBySkuRegion('usgovvirginia')">usgovvirginia</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>34%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Provisioned Models Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">usgovarizona</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td>Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,Central US" data-all-regions="Australia East,Canada East,Central US,East US,East US 2,France Central,Japan East,North Central US,Norway East,South Central US,South India,Sweden Central,Switzerland North,UK South,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+13 more</button></span></td>
      <td><span class="badge badge-growing">Growing</span></td>
      <td>46%</td>
      <td class="hidden-col">Australia East, Canada East, Central US, East US, East US 2, France Central, Japan East, North Central US, Norway East, South Central US, South India, Sweden Central, Switzerland North, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Models Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">usgovarizona</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>34%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>40%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>34%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,East US,East US 2,France Central,Japan East,Korea Central,North Central US,Norway East,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UK South,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+18 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>60%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, East US, East US 2, France Central, Japan East, Korea Central, North Central US, Norway East, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td>Standard</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini-transcribe/"><strong>gpt-4o-mini-transcribe</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini-transcribe/"><strong>gpt-4o-mini-transcribe</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini-transcribe/"><strong>gpt-4o-mini-transcribe</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini-transcribe/"><strong>gpt-4o-mini-transcribe</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini-tts/"><strong>gpt-4o-mini-tts</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">East US 2</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini-tts/"><strong>gpt-4o-mini-tts</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">East US 2</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini-tts/"><strong>gpt-4o-mini-tts</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">East US 2</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-mini-tts/"><strong>gpt-4o-mini-tts</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">East US 2</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-transcribe/"><strong>gpt-4o-transcribe</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-transcribe/"><strong>gpt-4o-transcribe</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-transcribe/"><strong>gpt-4o-transcribe</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-transcribe/"><strong>gpt-4o-transcribe</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-transcribe-diarize/"><strong>gpt-4o-transcribe-diarize</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-transcribe-diarize/"><strong>gpt-4o-transcribe-diarize</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-transcribe-diarize/"><strong>gpt-4o-transcribe-diarize</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-4o-transcribe-diarize/"><strong>gpt-4o-transcribe-diarize</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>37%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>40%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,Central US" data-all-regions="Australia East,Canada East,Central US,East US,East US 2,Japan East,Korea Central,North Central US,South Central US,South India,UK South,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>37%</td>
      <td class="hidden-col">Australia East, Canada East, Central US, East US, East US 2, Japan East, Korea Central, North Central US, South Central US, South India, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-chat/"><strong>gpt-5-chat</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-chat/"><strong>gpt-5-chat</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-chat/"><strong>gpt-5-chat</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-codex/"><strong>gpt-5-codex</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-codex/"><strong>gpt-5-codex</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-codex/"><strong>gpt-5-codex</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-codex/"><strong>gpt-5-codex</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>37%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>40%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US 2" data-all-regions="Australia East,Canada East,East US 2,Japan East,Korea Central,South India,UK South,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>23%</td>
      <td class="hidden-col">Australia East, Canada East, East US 2, Japan East, Korea Central, South India, UK South, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-nano/"><strong>gpt-5-nano</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-nano/"><strong>gpt-5-nano</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>40%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-nano/"><strong>gpt-5-nano</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-nano/"><strong>gpt-5-nano</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-nano/"><strong>gpt-5-nano</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-pro/"><strong>gpt-5-pro</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-pro/"><strong>gpt-5-pro</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-pro/"><strong>gpt-5-pro</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-pro/"><strong>gpt-5-pro</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>37%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span> <span class="region-badge" onclick="filterBySkuRegion('usgovvirginia')">usgovvirginia</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Priority Processing</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,South India" data-all-regions="Australia East,Canada East,South India,Switzerland North,UAE North,UK South,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">Australia East, Canada East, South India, Switzerland North, UAE North, UK South, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global Priority Processing</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td>Standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>23%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-chat/"><strong>gpt-5.1-chat</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-chat/"><strong>gpt-5.1-chat</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-chat/"><strong>gpt-5.1-chat</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex/"><strong>gpt-5.1-codex</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex/"><strong>gpt-5.1-codex</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>37%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex/"><strong>gpt-5.1-codex</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex/"><strong>gpt-5.1-codex</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex/"><strong>gpt-5.1-codex</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex/"><strong>gpt-5.1-codex</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex/"><strong>gpt-5.1-codex</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex-max/"><strong>gpt-5.1-codex-max</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex-max/"><strong>gpt-5.1-codex-max</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex-max/"><strong>gpt-5.1-codex-max</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex-max/"><strong>gpt-5.1-codex-max</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex-mini/"><strong>gpt-5.1-codex-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex-mini/"><strong>gpt-5.1-codex-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex-mini/"><strong>gpt-5.1-codex-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-1-codex-mini/"><strong>gpt-5.1-codex-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>37%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Central US,East US" data-all-regions="Australia East,Central US,East US,East US 2,Japan East,Korea Central,North Central US,South Central US,South India,Southeast Asia,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>34%</td>
      <td class="hidden-col">Australia East, Central US, East US, East US 2, Japan East, Korea Central, North Central US, South Central US, South India, Southeast Asia, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Priority Processing</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,Japan East" data-all-regions="Australia East,Canada East,Japan East,Korea Central,UK South,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('Japan East')">Japan East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">Australia East, Canada East, Japan East, Korea Central, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global Priority Processing</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2-chat/"><strong>gpt-5.2-chat</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2-chat/"><strong>gpt-5.2-chat</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2-chat/"><strong>gpt-5.2-chat</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2-codex/"><strong>gpt-5.2-codex</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2-codex/"><strong>gpt-5.2-codex</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2-codex/"><strong>gpt-5.2-codex</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2-codex/"><strong>gpt-5.2-codex</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2-codex/"><strong>gpt-5.2-codex</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-2-codex/"><strong>gpt-5.2-codex</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-3-chat/"><strong>gpt-5.3-chat</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-3-chat/"><strong>gpt-5.3-chat</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-3-chat/"><strong>gpt-5.3-chat</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-3-codex/"><strong>gpt-5.3-codex</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-3-codex/"><strong>gpt-5.3-codex</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Central US,East US" data-all-regions="Australia East,Central US,East US,East US 2,Japan East,Korea Central,North Central US,South Central US,South India,Southeast Asia,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>34%</td>
      <td class="hidden-col">Australia East, Central US, East US, East US 2, Japan East, Korea Central, North Central US, South Central US, South India, Southeast Asia, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-3-codex/"><strong>gpt-5.3-codex</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-3-codex/"><strong>gpt-5.3-codex</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-3-codex/"><strong>gpt-5.3-codex</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-3-codex/"><strong>gpt-5.3-codex</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-3-codex/"><strong>gpt-5.3-codex</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4/"><strong>gpt-5.4</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4/"><strong>gpt-5.4</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>37%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4/"><strong>gpt-5.4</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Central US,East US" data-all-regions="Australia East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+18 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>60%</td>
      <td class="hidden-col">Australia East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4/"><strong>gpt-5.4</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Priority Processing</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4/"><strong>gpt-5.4</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4/"><strong>gpt-5.4</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4/"><strong>gpt-5.4</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4/"><strong>gpt-5.4</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4/"><strong>gpt-5.4</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4/"><strong>gpt-5.4</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4/"><strong>gpt-5.4</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Japan East')">Japan East</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">Australia East, Japan East</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4/"><strong>gpt-5.4</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4/"><strong>gpt-5.4</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4/"><strong>gpt-5.4</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global Priority Processing</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-mini/"><strong>gpt-5.4-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-mini/"><strong>gpt-5.4-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Central US,East US" data-all-regions="Australia East,Central US,East US,East US 2,Japan East,Korea Central,North Central US,South Central US,South India,Southeast Asia,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>34%</td>
      <td class="hidden-col">Australia East, Central US, East US, East US 2, Japan East, Korea Central, North Central US, South Central US, South India, Southeast Asia, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-mini/"><strong>gpt-5.4-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Priority Processing</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-mini/"><strong>gpt-5.4-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-mini/"><strong>gpt-5.4-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-mini/"><strong>gpt-5.4-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-mini/"><strong>gpt-5.4-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-mini/"><strong>gpt-5.4-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-mini/"><strong>gpt-5.4-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-mini/"><strong>gpt-5.4-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-mini/"><strong>gpt-5.4-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global Priority Processing</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-nano/"><strong>gpt-5.4-nano</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-nano/"><strong>gpt-5.4-nano</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-nano/"><strong>gpt-5.4-nano</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-nano/"><strong>gpt-5.4-nano</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-nano/"><strong>gpt-5.4-nano</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-pro/"><strong>gpt-5.4-pro</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-pro/"><strong>gpt-5.4-pro</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-pro/"><strong>gpt-5.4-pro</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,South Central US" data-all-regions="East US 2,Poland Central,South Central US,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('South Central US')">South Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+1 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">East US 2, Poland Central, South Central US, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-4-pro/"><strong>gpt-5.4-pro</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,South Central US" data-all-regions="East US 2,Poland Central,South Central US,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('South Central US')">South Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+1 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">East US 2, Poland Central, South Central US, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-5/"><strong>gpt-5.5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-5/"><strong>gpt-5.5</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">East US, North Central US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-5/"><strong>gpt-5.5</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Central US,East US" data-all-regions="Australia East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+18 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>60%</td>
      <td class="hidden-col">Australia East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-5/"><strong>gpt-5.5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Priority Processing</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-5/"><strong>gpt-5.5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-5/"><strong>gpt-5.5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-5/"><strong>gpt-5.5</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">East US, North Central US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-5/"><strong>gpt-5.5</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">East US</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-5/"><strong>gpt-5.5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,South Central US" data-all-regions="East US 2,Poland Central,South Central US,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('South Central US')">South Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+1 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">East US 2, Poland Central, South Central US, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-5/"><strong>gpt-5.5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-5/"><strong>gpt-5.5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global Priority Processing</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-luna/"><strong>gpt-5.6-luna</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+27 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>86%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-luna/"><strong>gpt-5.6-luna</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Provisioned Managed Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">usgovarizona</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-luna/"><strong>gpt-5.6-luna</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span> <span class="region-badge" onclick="filterBySkuRegion('usgovvirginia')">usgovvirginia</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-luna/"><strong>gpt-5.6-luna</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-luna/"><strong>gpt-5.6-luna</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-sol/"><strong>gpt-5.6-sol</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+27 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>86%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-sol/"><strong>gpt-5.6-sol</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Provisioned Managed Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">usgovarizona</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-sol/"><strong>gpt-5.6-sol</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span> <span class="region-badge" onclick="filterBySkuRegion('usgovvirginia')">usgovvirginia</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-sol/"><strong>gpt-5.6-sol</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,Central US" data-all-regions="Australia East,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Norway East,Poland Central,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+18 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>60%</td>
      <td class="hidden-col">Australia East, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Norway East, Poland Central, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-sol/"><strong>gpt-5.6-sol</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-sol/"><strong>gpt-5.6-sol</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global Priority Processing</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-terra/"><strong>gpt-5.6-terra</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+27 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>86%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-terra/"><strong>gpt-5.6-terra</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Provisioned Managed Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">usgovarizona</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-terra/"><strong>gpt-5.6-terra</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span> <span class="region-badge" onclick="filterBySkuRegion('usgovvirginia')">usgovvirginia</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-terra/"><strong>gpt-5.6-terra</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-terra/"><strong>gpt-5.6-terra</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-5-6-terra/"><strong>gpt-5.6-terra</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global Priority Processing</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-6-astra/"><strong>gpt-6-astra</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-6-astra/"><strong>gpt-6-astra</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-6-astra/"><strong>gpt-6-astra</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-6-luna/"><strong>gpt-6-luna</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-6-luna/"><strong>gpt-6-luna</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-6-sol/"><strong>gpt-6-sol</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-6-sol/"><strong>gpt-6-sol</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Priority Processing</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-6-sol/"><strong>gpt-6-sol</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-6-sol/"><strong>gpt-6-sol</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-6-sol/"><strong>gpt-6-sol</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global Priority Processing</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-6-1-sol/"><strong>gpt-6.1-sol</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-6-1-sol/"><strong>gpt-6.1-sol</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-6-1-sol/"><strong>gpt-6.1-sol</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-audio/"><strong>gpt-audio</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-audio/"><strong>gpt-audio</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-audio/"><strong>gpt-audio</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-audio/"><strong>gpt-audio</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-audio-1-5/"><strong>gpt-audio-1.5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Central US,East US 2,North Europe" data-all-regions="Central US,East US 2,North Europe,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Europe')">North Europe</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+1 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, North Europe, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-audio-1-5/"><strong>gpt-audio-1.5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US 2,North Europe" data-all-regions="Central US,East US 2,North Europe,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Europe')">North Europe</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+1 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">Central US, East US 2, North Europe, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-audio-1-5/"><strong>gpt-audio-1.5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-audio-1-5/"><strong>gpt-audio-1.5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-audio-mini/"><strong>gpt-audio-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-audio-mini/"><strong>gpt-audio-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-audio-mini/"><strong>gpt-audio-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-audio-mini/"><strong>gpt-audio-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-chat-latest/"><strong>gpt-chat-latest</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-chat-latest/"><strong>gpt-chat-latest</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1/"><strong>gpt-image-1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1/"><strong>gpt-image-1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1/"><strong>gpt-image-1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1/"><strong>gpt-image-1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1-mini/"><strong>gpt-image-1-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1-mini/"><strong>gpt-image-1-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1-mini/"><strong>gpt-image-1-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1-mini/"><strong>gpt-image-1-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1-5/"><strong>gpt-image-1.5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1-5/"><strong>gpt-image-1.5</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+1 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>11%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1-5/"><strong>gpt-image-1.5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1-5/"><strong>gpt-image-1.5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-1-5/"><strong>gpt-image-1.5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-2/"><strong>gpt-image-2</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-2/"><strong>gpt-image-2</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-2/"><strong>gpt-image-2</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-2/"><strong>gpt-image-2</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-2-5-flare/"><strong>gpt-image-2.5-flare</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-2-5-flare/"><strong>gpt-image-2.5-flare</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-2-5-sunburst/"><strong>gpt-image-2.5-sunburst</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-image-2-5-sunburst/"><strong>gpt-image-2.5-sunburst</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime/"><strong>gpt-realtime</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime/"><strong>gpt-realtime</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime/"><strong>gpt-realtime</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime/"><strong>gpt-realtime</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-1-5/"><strong>gpt-realtime-1.5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-1-5/"><strong>gpt-realtime-1.5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-1-5/"><strong>gpt-realtime-1.5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-1-5/"><strong>gpt-realtime-1.5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-2/"><strong>gpt-realtime-2</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-2/"><strong>gpt-realtime-2</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-2-1/"><strong>gpt-realtime-2.1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-2-1/"><strong>gpt-realtime-2.1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-2-1-mini/"><strong>gpt-realtime-2.1-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-2-1-mini/"><strong>gpt-realtime-2.1-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-mini/"><strong>gpt-realtime-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-mini/"><strong>gpt-realtime-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-mini/"><strong>gpt-realtime-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-mini/"><strong>gpt-realtime-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-translate/"><strong>gpt-realtime-translate</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-translate/"><strong>gpt-realtime-translate</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-whisper/"><strong>gpt-realtime-whisper</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/gpt-realtime-whisper/"><strong>gpt-realtime-whisper</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-1-fast-non-reasoning/"><strong>grok-4-1-fast-non-reasoning</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-1-fast-non-reasoning/"><strong>grok-4-1-fast-non-reasoning</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-1-fast-reasoning/"><strong>grok-4-1-fast-reasoning</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-1-fast-reasoning/"><strong>grok-4-1-fast-reasoning</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-20-non-reasoning/"><strong>grok-4-20-non-reasoning</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-20-non-reasoning/"><strong>grok-4-20-non-reasoning</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-20-reasoning/"><strong>grok-4-20-reasoning</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-20-reasoning/"><strong>grok-4-20-reasoning</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-3/"><strong>grok-4.3</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-3/"><strong>grok-4.3</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-6/"><strong>grok-4.6</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/grok-4-6/"><strong>grok-4.6</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-document-ai-2505/"><strong>mistral-document-ai-2505</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-document-ai-2505/"><strong>mistral-document-ai-2505</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-medium-2505/"><strong>mistral-medium-2505</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-medium-2505/"><strong>mistral-medium-2505</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-medium-3-5/"><strong>mistral-medium-3-5</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-medium-3-5/"><strong>mistral-medium-3-5</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-small-2503/"><strong>mistral-small-2503</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/mistral-small-2503/"><strong>mistral-small-2503</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Marketplace Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/model-router/"><strong>model-router</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,East US 2,North Europe" data-all-regions="Australia East,East US 2,North Europe,South India,Sweden Central,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Europe')">North Europe</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Australia East, East US 2, North Europe, South India, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/model-router/"><strong>model-router</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,East US 2,South India" data-all-regions="Australia East,East US 2,South India,Sweden Central,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">Australia East, East US 2, South India, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/model-router/"><strong>model-router</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,East US 2,North Europe" data-all-regions="Australia East,East US 2,North Europe,South India,Sweden Central,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Europe')">North Europe</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">Australia East, East US 2, North Europe, South India, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/model-router/"><strong>model-router</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,East US 2,South India" data-all-regions="Australia East,East US 2,South India,Sweden Central,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">Australia East, East US 2, South India, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/model-router/"><strong>model-router</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,East US 2,South India" data-all-regions="Australia East,East US 2,South India,Sweden Central,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('South India')">South India</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+2 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>14%</td>
      <td class="hidden-col">Australia East, East US 2, South India, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>34%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>40%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Japan East')">Japan East</span> <span class="region-badge" onclick="filterBySkuRegion('UAE North')">UAE North</span> <span class="region-badge" onclick="filterBySkuRegion('UK South')">UK South</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Japan East, UAE North, UK South</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o1/"><strong>o1</strong></a></td>
      <td><span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td>Standard</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>37%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>40%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>34%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,East US,East US 2" data-all-regions="Australia East,East US,East US 2,North Central US,South Central US,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>23%</td>
      <td class="hidden-col">Australia East, East US, East US 2, North Central US, South Central US, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3/"><strong>o3</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-deep-research/"><strong>o3-deep-research</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Norway East')">Norway East</span> <span class="region-badge" onclick="filterBySkuRegion('West US')">West US</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">Norway East, West US</td>
    </tr>
    <tr>
      <td><a href="../models/o3-deep-research/"><strong>o3-deep-research</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Norway East')">Norway East</span> <span class="region-badge" onclick="filterBySkuRegion('West US')">West US</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">Norway East, West US</td>
    </tr>
    <tr>
      <td><a href="../models/o3-deep-research/"><strong>o3-deep-research</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Norway East')">Norway East</span> <span class="region-badge" onclick="filterBySkuRegion('West US')">West US</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">Norway East, West US</td>
    </tr>
    <tr>
      <td><a href="../models/o3-deep-research/"><strong>o3-deep-research</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Norway East')">Norway East</span> <span class="region-badge" onclick="filterBySkuRegion('West US')">West US</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">Norway East, West US</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>34%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Provisioned Managed Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">usgovarizona</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>40%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span> <span class="region-badge" onclick="filterBySkuRegion('usgovvirginia')">usgovvirginia</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US 2" data-all-regions="Australia East,Canada East,East US 2,Japan East,Korea Central,South Central US,South India,Sweden Central,Switzerland North,UAE North"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+7 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>29%</td>
      <td class="hidden-col">Australia East, Canada East, East US 2, Japan East, Korea Central, South Central US, South India, Sweden Central, Switzerland North, UAE North</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o3-pro/"><strong>o3-pro</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/o3-pro/"><strong>o3-pro</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/o3-pro/"><strong>o3-pro</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/o3-pro/"><strong>o3-pro</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone provisioned managed</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+10 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>37%</td>
      <td class="hidden-col">East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>40%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Provisioned</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+19 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>63%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global batch datazone</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,North Central US,Poland Central,South Central US,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+9 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>34%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, North Central US, Poland Central, South Central US, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned global</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+24 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>77%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-provisioned" data-tooltip="Reserved throughput capacity (PTU) | Best for predictable, high-volume production workloads | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Provisioned</span></td>
      <td>Provisioned (PTU managed)</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,Japan East,North Central US,South Central US,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+6 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>26%</td>
      <td class="hidden-col">Central US, East US, East US 2, Japan East, North Central US, South Central US, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+23 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>74%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td>Standard</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+4 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>20%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/sora-2/"><strong>sora-2</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/sora-2/"><strong>sora-2</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/sora-2/"><strong>sora-2</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/sora-2/"><strong>sora-2</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-large/"><strong>text-embedding-3-large</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-large/"><strong>text-embedding-3-large</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>40%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-large/"><strong>text-embedding-3-large</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span> <span class="region-badge" onclick="filterBySkuRegion('usgovvirginia')">usgovvirginia</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-large/"><strong>text-embedding-3-large</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-large/"><strong>text-embedding-3-large</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-large/"><strong>text-embedding-3-large</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-large/"><strong>text-embedding-3-large</strong></a></td>
      <td><span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td>Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,Norway East,Poland Central,South Africa North,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+16 more</button></span></td>
      <td><span class="badge badge-growing">Growing</span></td>
      <td>54%</td>
      <td class="hidden-col">Australia East, Canada East, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, Norway East, Poland Central, South Africa North, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-large/"><strong>text-embedding-3-large</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Models Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">usgovarizona</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-small/"><strong>text-embedding-3-small</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+28 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>89%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-small/"><strong>text-embedding-3-small</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>40%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-small/"><strong>text-embedding-3-small</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Datazone Standard Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span> <span class="region-badge" onclick="filterBySkuRegion('usgovvirginia')">usgovvirginia</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>6%</td>
      <td class="hidden-col">usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-small/"><strong>text-embedding-3-small</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-small/"><strong>text-embedding-3-small</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-small/"><strong>text-embedding-3-small</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+22 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>71%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-small/"><strong>text-embedding-3-small</strong></a></td>
      <td><span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td>Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,Japan East,Switzerland North,UAE North,West US"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>23%</td>
      <td class="hidden-col">Australia East, Canada East, East US, East US 2, Japan East, Switzerland North, UAE North, West US</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-3-small/"><strong>text-embedding-3-small</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Models Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">usgovarizona</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-ada-002/"><strong>text-embedding-ada-002</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+26 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>83%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-ada-002/"><strong>text-embedding-ada-002</strong></a></td>
      <td><span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td>Datazone standard</td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+11 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>40%</td>
      <td class="hidden-col">Central US, East US, East US 2, France Central, Germany West Central, Italy North, North Central US, Poland Central, South Central US, Spain Central, Sweden Central, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-ada-002/"><strong>text-embedding-ada-002</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+25 more</button></span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td>80%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-ada-002/"><strong>text-embedding-ada-002</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+21 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>69%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-ada-002/"><strong>text-embedding-ada-002</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Global By Capability</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+21 more</button></span></td>
      <td><span class="badge badge-strong">Strong</span></td>
      <td>69%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-ada-002/"><strong>text-embedding-ada-002</strong></a></td>
      <td><span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td>Standard</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Japan East,North Central US,Norway East,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterBySkuRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterBySkuRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+16 more</button></span></td>
      <td><span class="badge badge-growing">Growing</span></td>
      <td>54%</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Japan East, North Central US, Norway East, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/text-embedding-ada-002/"><strong>text-embedding-ada-002</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Standard Models Gov</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('usgovarizona')">usgovarizona</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>3%</td>
      <td class="hidden-col">usgovarizona</td>
    </tr>
    <tr>
      <td><a href="../models/tsuzumi-7b/"><strong>tsuzumi-7b</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/tsuzumi-7b/"><strong>tsuzumi-7b</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Region Availability Maas</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterBySkuRegion('East US')">East US</span> <span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+3 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>17%</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/tts/"><strong>tts</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterBySkuRegion('West US 3')">West US 3</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">North Central US, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/tts/"><strong>tts</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterBySkuRegion('West US 3')">West US 3</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">North Central US, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/tts/"><strong>tts</strong></a></td>
      <td><span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td>Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterBySkuRegion('West US 3')">West US 3</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">North Central US, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/tts-hd/"><strong>tts-hd</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterBySkuRegion('West US 3')">West US 3</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">North Central US, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/tts-hd/"><strong>tts-hd</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterBySkuRegion('West US 3')">West US 3</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">North Central US, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/tts-hd/"><strong>tts-hd</strong></a></td>
      <td><span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td>Standard</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterBySkuRegion('West US 3')">West US 3</span></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>9%</td>
      <td class="hidden-col">North Central US, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="../models/whisper/"><strong>whisper</strong></a></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td>Global coverage</td>
      <td><span class="region-list" data-preview-regions="East US 2,North Central US,Norway East" data-all-regions="East US 2,North Central US,Norway East,South India,Sweden Central,Switzerland North,UAE North,West Europe"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Norway East')">Norway East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>23%</td>
      <td class="hidden-col">East US 2, North Central US, Norway East, South India, Sweden Central, Switzerland North, UAE North, West Europe</td>
    </tr>
    <tr>
      <td><a href="../models/whisper/"><strong>whisper</strong></a></td>
      <td><span class="sku-badge sku-other">Other</span></td>
      <td>Deployments Standard</td>
      <td><span class="region-list" data-preview-regions="East US 2,North Central US,Norway East" data-all-regions="East US 2,North Central US,Norway East,South India,Sweden Central,Switzerland North,UAE North,West Europe"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Norway East')">Norway East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>23%</td>
      <td class="hidden-col">East US 2, North Central US, Norway East, South India, Sweden Central, Switzerland North, UAE North, West Europe</td>
    </tr>
    <tr>
      <td><a href="../models/whisper/"><strong>whisper</strong></a></td>
      <td><span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td>Standard</td>
      <td><span class="region-list" data-preview-regions="East US 2,North Central US,Norway East" data-all-regions="East US 2,North Central US,Norway East,South India,Sweden Central,Switzerland North,UAE North,West Europe"><span class="region-badge" onclick="filterBySkuRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterBySkuRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterBySkuRegion('Norway East')">Norway East</span> <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">+5 more</button></span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td>23%</td>
      <td class="hidden-col">East US 2, North Central US, Norway East, South India, Sweden Central, Switzerland North, UAE North, West Europe</td>
    </tr>
  </tbody>
</table>
</div>

---

_Last updated: 2026-10-07 14:13 UTC_
