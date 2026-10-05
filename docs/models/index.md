---
hide:
  - toc
---

# All Models

<p class="page-lede">Jump straight to a model, or use the table below to compare deployment coverage across the full catalog.</p>

<div class="model-finder" data-model-finder data-src="../assets/model-index.json" data-root="../">
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

<div class="filter-controls">
  <div class="filter-group">
    <label for="lifecycle-filter">Lifecycle</label>
    <select id="lifecycle-filter" onchange="filterModelsTable()">
      <option value="">All Stages</option>
      <option value="Retiring ≤30d">Retiring ≤30d</option>
      <option value="Retiring ≤90d">Retiring ≤90d</option>
      <option value="Retirement due">Retirement due</option>
      <option value="Deprecated">Deprecated</option>
      <option value="Generally available">Generally available</option>
      <option value="Retired">Retired</option>
      <option value="No date announced">No date announced</option>
    </select>
  </div>
  <div class="filter-group">
    <label for="coverage-filter">Coverage Level</label>
    <select id="coverage-filter" onchange="filterModelsTable()">
      <option value="">All Levels</option>
      <option value="Broad">Broad (25+)</option>
      <option value="Strong">Strong (20-24)</option>
      <option value="Growing">Growing (15-19)</option>
      <option value="Emerging">Emerging (&lt;15)</option>
    </select>
  </div>
  <div class="filter-group">
    <label for="category-filter">SKU Category</label>
    <select id="category-filter" onchange="filterModelsTable()">
      <option value="">All Categories</option>
      <option value="Global">Global</option>
      <option value="Datazone">Datazone</option>
      <option value="Standard">Standard</option>
      <option value="Provisioned">Provisioned</option>
    </select>
  </div>
  <div class="filter-group">
    <label for="region-filter">Available In Region</label>
    <select id="region-filter" onchange="filterModelsTable()">
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
    <button onclick="resetModelsFilters()" class="md-button">Reset</button>
  </div>
</div>

<div class="table-responsive">
<table id="models-table" class="filterable display">
  <thead>
    <tr>
      <th>Model</th>
      <th>Lifecycle</th>
      <th>Coverage</th>
      <th>SKU Types</th>
      <th>Global Regions</th>
      <th>Datazone Regions</th>
      <th>Standard Regions</th>
      <th>Prov. PTU Regions</th>
      <th>Prov. Global Regions</th>
      <th class="hidden-col">Categories</th>
      <th class="hidden-col">Region List</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="codestral-2501/"><strong>Codestral-2501</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="cohere-command-r-08-2024/"><strong>Cohere Command R 08-2024</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="cohere-command-r+-08-2024/"><strong>Cohere Command R+ 08-2024</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="cohere-embed-v3---english/"><strong>Cohere Embed v3 - English</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="cohere-embed-v3---multilingual/"><strong>Cohere Embed v3 - Multilingual</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="cohere-rerank-v3-5/"><strong>Cohere Rerank v3.5</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="cohere-command-a-plus-05-2026/"><strong>Cohere-command-a-plus-05-2026</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="cohere-rerank-v4-0-fast/"><strong>Cohere-rerank-v4.0-fast</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="cohere-rerank-v4-0-pro/"><strong>Cohere-rerank-v4.0-pro</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="deepseek-r1/"><strong>DeepSeek-R1</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="deepseek-v3-0324/"><strong>DeepSeek-V3-0324</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="deepseek-v3-2/"><strong>DeepSeek-V3.2</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="deepseek-v3-2-speciale/"><strong>DeepSeek-V3.2-Speciale</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="deepseek-v4-flash/"><strong>DeepSeek-V4-Flash</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="deepseek-v4-flash-0731/"><strong>DeepSeek-V4-Flash-0731</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="deepseek-v4-pro/"><strong>DeepSeek-V4-Pro</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="flux-1-1-pro/"><strong>FLUX-1.1-pro</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="flux-1-kontext-pro/"><strong>FLUX.1-Kontext-pro</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="flux-2-flex/"><strong>FLUX.2-flex</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="flux-2-pro/"><strong>FLUX.2-pro</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="kimi-k2-5/"><strong>Kimi-K2.5</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="kimi-k2-6/"><strong>Kimi-K2.6</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="kimi-k2-7-code/"><strong>Kimi-K2.7-Code</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="llama-3-1-405b-instruct/"><strong>Llama 3.1 405B Instruct</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="llama-3-1-8b-instruct/"><strong>Llama 3.1 8B Instruct</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="llama-3-3-70b-instruct/"><strong>Llama 3.3 70B Instruct</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="llama-3-2-11b-vision-instruct/"><strong>Llama-3.2-11B-Vision-Instruct</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="llama-3-2-1b/"><strong>Llama-3.2-1B</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="llama-3-2-1b-instruct/"><strong>Llama-3.2-1B-Instruct</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="llama-3-2-3b/"><strong>Llama-3.2-3B</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="llama-3-2-3b-instruct/"><strong>Llama-3.2-3B-Instruct</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="llama-3-2-90b-vision-instruct/"><strong>Llama-3.2-90B-Vision-Instruct</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="llama-3-3-70b-instruct/"><strong>Llama-3.3-70B-Instruct</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="llama-4-maverick-17b-128e-instruct-fp8/"><strong>Llama-4-Maverick-17B-128E-Instruct-FP8</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="llama-4-scout-17b-16e-instruct/"><strong>Llama-4-Scout-17B-16E-Instruct</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="llama-guard-3-11b-vision/"><strong>Llama-Guard-3-11B-Vision</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="llama-guard-3-1b/"><strong>Llama-Guard-3-1B</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="mai-ds-r1/"><strong>MAI-DS-R1</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="mai-image-2-5/"><strong>MAI-Image-2.5</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,South India,Sweden Central" data-all-regions="East US,South India,Sweden Central,UAE North,West Central US,West Europe,West US"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('South India')">South India</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, South India, Sweden Central, UAE North, West Central US, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="mai-image-2-5-flash/"><strong>MAI-Image-2.5-Flash</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,South India,Sweden Central" data-all-regions="East US,South India,Sweden Central,UAE North,West Central US,West Europe,West US"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('South India')">South India</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, South India, Sweden Central, UAE North, West Central US, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="mai-image-2-5-pro/"><strong>MAI-Image-2.5-Pro</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,South India,Sweden Central" data-all-regions="East US,South India,Sweden Central,UAE North,West Central US,West Europe,West US"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('South India')">South India</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, South India, Sweden Central, UAE North, West Central US, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="mai-image-2-6/"><strong>MAI-Image-2.6</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,South India,Sweden Central" data-all-regions="East US,South India,Sweden Central,UAE North,West Central US,West Europe,West US"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('South India')">South India</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, South India, Sweden Central, UAE North, West Central US, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="mai-image-2-6-flash/"><strong>MAI-Image-2.6-Flash</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,South India,Sweden Central" data-all-regions="East US,South India,Sweden Central,UAE North,West Central US,West Europe,West US"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('South India')">South India</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, South India, Sweden Central, UAE North, West Central US, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="mai-thinking-1/"><strong>MAI-Thinking-1</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="ministral-3b/"><strong>Ministral-3B</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="mistral-medium-3-(25-05)/"><strong>Mistral Medium 3 (25.05)</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="mistral-small-25-03/"><strong>Mistral Small 25.03</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="mistral-large-3/"><strong>Mistral-Large-3</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="mistral-large/"><strong>Mistral-large</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="phi-4/"><strong>Phi-4</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="phi-4-mini-instruct/"><strong>Phi-4-mini-instruct</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="phi-4-mini-reasoning/"><strong>Phi-4-mini-reasoning</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="phi-4-multimodal-instruct/"><strong>Phi-4-multimodal-instruct</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="phi-4-reasoning/"><strong>Phi-4-reasoning</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="stable-diffusion-3-5-large/"><strong>Stable Diffusion 3.5 Large</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="stable-image-core/"><strong>Stable Image Core</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="stable-image-ultra/"><strong>Stable Image Ultra</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="timegen-1/"><strong>TimeGEN-1</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="claude-fable-5/"><strong>claude-fable-5</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="claude-fable-5-1/"><strong>claude-fable-5-1</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="claude-haiku-4-5/"><strong>claude-haiku-4-5</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+6 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="claude-opus-4-5/"><strong>claude-opus-4-5</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+6 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="claude-opus-4-6/"><strong>claude-opus-4-6</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+6 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="claude-opus-4-7/"><strong>claude-opus-4-7</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+6 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="claude-opus-4-8/"><strong>claude-opus-4-8</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+6 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="claude-opus-5/"><strong>claude-opus-5</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+6 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="claude-opus-5-5/"><strong>claude-opus-5-5</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+6 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="claude-sonnet-4-5/"><strong>claude-sonnet-4-5</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+6 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="claude-sonnet-4-6/"><strong>claude-sonnet-4-6</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+6 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="claude-sonnet-5/"><strong>claude-sonnet-5</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+6 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="claude-sonnet-5-5/"><strong>claude-sonnet-5-5</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+6 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Central US, East US, East US 2, North Central US, South Central US, Sweden Central, West Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="codex-mini/"><strong>codex-mini</strong></a></td>
      <td data-search="Retiring ≤90d"><span class="lc-badge lc-badge--warning">Retiring ≤90d</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="cohere-command-a/"><strong>cohere-command-a</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="computer-use-preview/"><strong>computer-use-preview</strong></a></td>
      <td data-search="Retirement due"><span class="lc-badge lc-badge--warning">Retirement due</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('South India')">South India</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US 2, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td data-search="Retiring ≤30d"><span class="lc-badge lc-badge--danger">Retiring ≤30d</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span> <span class="sku-badge sku-provisioned" title="18 regions">Prov.PTU</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,Switzerland North,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+5 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Central US" data-all-regions="Australia East,Brazil South,Central US,East US,East US 2,Germany West Central,Japan East,Korea Central,North Central US,South Central US,South India,Southeast Asia,Sweden Central,Switzerland North,UAE North,UK South,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+15 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td data-search="Retiring ≤30d"><span class="lc-badge lc-badge--danger">Retiring ≤30d</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span> <span class="sku-badge sku-provisioned" title="14 regions">Prov.PTU</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Japan East,North Central US,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+12 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,East US" data-all-regions="Australia East,Brazil South,East US,East US 2,Japan East,Korea Central,North Central US,South Central US,South India,Sweden Central,Switzerland North,UK South,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td data-search="Retiring ≤30d"><span class="lc-badge lc-badge--danger">Retiring ≤30d</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-provisioned" title="7 regions">Prov.PTU</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td data-search="Retired"><span class="lc-badge lc-badge--muted">Retired</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span> <span class="sku-badge sku-provisioned" title="27 regions">Prov.PTU</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,Central US" data-all-regions="Australia East,Canada East,Central US,East US,East US 2,France Central,Japan East,North Central US,Norway East,South Central US,South India,Sweden Central,Switzerland North,UK South,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+13 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td data-search="Retired"><span class="lc-badge lc-badge--muted">Retired</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span> <span class="sku-badge sku-provisioned" title="21 regions">Prov.PTU</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,East US,East US 2,France Central,Japan East,Korea Central,North Central US,Norway East,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UK South,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+18 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-4o-mini-transcribe/"><strong>gpt-4o-mini-transcribe</strong></a></td>
      <td data-search="Retiring ≤90d"><span class="lc-badge lc-badge--warning">Retiring ≤90d</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-4o-mini-tts/"><strong>gpt-4o-mini-tts</strong></a></td>
      <td data-search="Retiring ≤90d"><span class="lc-badge lc-badge--warning">Retiring ≤90d</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US 2</td>
    </tr>
    <tr>
      <td><a href="gpt-4o-transcribe/"><strong>gpt-4o-transcribe</strong></a></td>
      <td data-search="Retirement due"><span class="lc-badge lc-badge--warning">Retirement due</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-4o-transcribe-diarize/"><strong>gpt-4o-transcribe-diarize</strong></a></td>
      <td data-search="Generally available"><span class="lc-badge lc-badge--success">Generally available</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-5/"><strong>gpt-5</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-provisioned" title="13 regions">Prov.PTU</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,Central US" data-all-regions="Australia East,Canada East,Central US,East US,East US 2,Japan East,Korea Central,North Central US,South Central US,South India,UK South,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+10 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-chat/"><strong>gpt-5-chat</strong></a></td>
      <td data-search="Retired"><span class="lc-badge lc-badge--muted">Retired</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US</td>
    </tr>
    <tr>
      <td><a href="gpt-5-codex/"><strong>gpt-5-codex</strong></a></td>
      <td data-search="Deprecated"><span class="lc-badge lc-badge--caution">Deprecated</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td data-search="Deprecated"><span class="lc-badge lc-badge--caution">Deprecated</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-provisioned" title="8 regions">Prov.PTU</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US 2" data-all-regions="Australia East,Canada East,East US 2,Japan East,Korea Central,South India,UK South,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+5 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-nano/"><strong>gpt-5-nano</strong></a></td>
      <td data-search="Deprecated"><span class="lc-badge lc-badge--caution">Deprecated</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+23 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Datazone, Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-pro/"><strong>gpt-5-pro</strong></a></td>
      <td data-search="Generally available"><span class="lc-badge lc-badge--success">Generally available</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td data-search="Generally available"><span class="lc-badge lc-badge--success">Generally available</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span> <span class="sku-badge sku-provisioned" title="7 regions">Prov.PTU</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+5 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,South India" data-all-regions="Australia East,Canada East,South India,Switzerland North,UAE North,UK South,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('South India')">South India</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="gpt-5-1-chat/"><strong>gpt-5.1-chat</strong></a></td>
      <td data-search="Retirement due"><span class="lc-badge lc-badge--warning">Retirement due</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-1-codex/"><strong>gpt-5.1-codex</strong></a></td>
      <td data-search="Generally available"><span class="lc-badge lc-badge--success">Generally available</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+10 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-1-codex-max/"><strong>gpt-5.1-codex-max</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-1-codex-mini/"><strong>gpt-5.1-codex-mini</strong></a></td>
      <td data-search="Generally available"><span class="lc-badge lc-badge--success">Generally available</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td data-search="Generally available"><span class="lc-badge lc-badge--success">Generally available</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-provisioned" title="7 regions">Prov.PTU</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Central US,East US" data-all-regions="Australia East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Poland Central,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+16 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,Japan East" data-all-regions="Australia East,Canada East,Japan East,Korea Central,UK South,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('Japan East')">Japan East</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-2-chat/"><strong>gpt-5.2-chat</strong></a></td>
      <td data-search="Retirement due"><span class="lc-badge lc-badge--warning">Retirement due</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-2-codex/"><strong>gpt-5.2-codex</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Global, Other, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-3-chat/"><strong>gpt-5.3-chat</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-3-codex/"><strong>gpt-5.3-codex</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Central US,East US" data-all-regions="Australia East,Central US,East US,East US 2,Japan East,Korea Central,North Central US,South Central US,South India,Southeast Asia,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+9 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-4/"><strong>gpt-5.4</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-provisioned" title="2 regions">Prov.PTU</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Central US,East US" data-all-regions="Australia East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+18 more</button></span></td>
      <td>-</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Japan East')">Japan East</span></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-4-mini/"><strong>gpt-5.4-mini</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Central US,East US" data-all-regions="Australia East,Central US,East US,East US 2,Japan East,Korea Central,North Central US,South Central US,South India,Southeast Asia,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+9 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Datazone, Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-4-nano/"><strong>gpt-5.4-nano</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Datazone, Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-4-pro/"><strong>gpt-5.4-pro</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-5/"><strong>gpt-5.5</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-provisioned" title="1 regions">Prov.PTU</span> <span class="sku-badge sku-provisioned-global" title="2 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Central US,East US" data-all-regions="Australia East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+18 more</button></span></td>
      <td>-</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US')">East US</span></span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-6-luna/"><strong>gpt-5.6-luna</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+27 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="gpt-5-6-sol/"><strong>gpt-5.6-sol</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+27 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="gpt-5-6-terra/"><strong>gpt-5.6-terra</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+27 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="gpt-6-astra/"><strong>gpt-6-astra</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-6-luna/"><strong>gpt-6-luna</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-6-sol/"><strong>gpt-6-sol</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-6-1-sol/"><strong>gpt-6.1-sol</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-audio/"><strong>gpt-audio</strong></a></td>
      <td data-search="Deprecated"><span class="lc-badge lc-badge--caution">Deprecated</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-audio-1-5/"><strong>gpt-audio-1.5</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US 2,North Europe" data-all-regions="Central US,East US 2,North Europe,Sweden Central"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Europe')">North Europe</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+1 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Central US, East US 2, North Europe, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-audio-mini/"><strong>gpt-audio-mini</strong></a></td>
      <td data-search="Generally available"><span class="lc-badge lc-badge--success">Generally available</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-chat-latest/"><strong>gpt-chat-latest</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-image-1/"><strong>gpt-image-1</strong></a></td>
      <td data-search="Retirement due"><span class="lc-badge lc-badge--warning">Retirement due</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+2 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-image-1-mini/"><strong>gpt-image-1-mini</strong></a></td>
      <td data-search="Generally available"><span class="lc-badge lc-badge--success">Generally available</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+2 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-image-1-5/"><strong>gpt-image-1.5</strong></a></td>
      <td data-search="Retiring ≤90d"><span class="lc-badge lc-badge--warning">Retiring ≤90d</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+2 more</button></span></td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,West US 3"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+1 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Datazone, Global, Other</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-image-2/"><strong>gpt-image-2</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+2 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-image-2-5-flare/"><strong>gpt-image-2.5-flare</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-image-2-5-sunburst/"><strong>gpt-image-2.5-sunburst</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-realtime/"><strong>gpt-realtime</strong></a></td>
      <td data-search="Deprecated"><span class="lc-badge lc-badge--caution">Deprecated</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-realtime-1-5/"><strong>gpt-realtime-1.5</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-realtime-2/"><strong>gpt-realtime-2</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-realtime-2-1/"><strong>gpt-realtime-2.1</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-realtime-2-1-mini/"><strong>gpt-realtime-2.1-mini</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-realtime-mini/"><strong>gpt-realtime-mini</strong></a></td>
      <td data-search="Retiring ≤90d"><span class="lc-badge lc-badge--warning">Retiring ≤90d</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-realtime-translate/"><strong>gpt-realtime-translate</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-realtime-whisper/"><strong>gpt-realtime-whisper</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Canada Central,Central US,East US 2" data-all-regions="Canada Central,Central US,East US 2,France Central,South India,Sweden Central"><span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Canada Central, Central US, East US 2, France Central, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="grok-4-1-fast-non-reasoning/"><strong>grok-4-1-fast-non-reasoning</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="grok-4-1-fast-reasoning/"><strong>grok-4-1-fast-reasoning</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="grok-4-20-non-reasoning/"><strong>grok-4-20-non-reasoning</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="grok-4-20-reasoning/"><strong>grok-4-20-reasoning</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="grok-4-3/"><strong>grok-4.3</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="grok-4-6/"><strong>grok-4.6</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="mistral-document-ai-2505/"><strong>mistral-document-ai-2505</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="mistral-medium-2505/"><strong>mistral-medium-2505</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="mistral-medium-3-5/"><strong>mistral-medium-3-5</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="mistral-small-2503/"><strong>mistral-small-2503</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Japan West,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,UK West,West Central US,West Europe,West US,West US 2,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Japan West, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, UK West, West Central US, West Europe, West US, West US 2, West US 3</td>
    </tr>
    <tr>
      <td><a href="model-router/"><strong>model-router</strong></a></td>
      <td data-search="Generally available"><span class="lc-badge lc-badge--success">Generally available</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,East US 2,North Europe" data-all-regions="Australia East,East US 2,North Europe,South India,Sweden Central,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Europe')">North Europe</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,East US 2,South India" data-all-regions="Australia East,East US 2,South India,Sweden Central,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('South India')">South India</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+2 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Datazone, Global, Other</td>
      <td class="hidden-col">Australia East, East US 2, North Europe, South India, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="o1/"><strong>o1</strong></a></td>
      <td data-search="Retired"><span class="lc-badge lc-badge--muted">Retired</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span> <span class="sku-badge sku-provisioned" title="3 regions">Prov.PTU</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Japan East')">Japan East</span> <span class="region-badge" onclick="filterByRegion('UAE North')">UAE North</span> <span class="region-badge" onclick="filterByRegion('UK South')">UK South</span></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="o3/"><strong>o3</strong></a></td>
      <td data-search="Retiring ≤30d"><span class="lc-badge lc-badge--danger">Retiring ≤30d</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-provisioned" title="8 regions">Prov.PTU</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,East US,East US 2" data-all-regions="Australia East,East US,East US 2,North Central US,South Central US,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+5 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="o3-deep-research/"><strong>o3-deep-research</strong></a></td>
      <td data-search="Retiring ≤90d"><span class="lc-badge lc-badge--warning">Retiring ≤90d</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Norway East')">Norway East</span> <span class="region-badge" onclick="filterByRegion('West US')">West US</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Norway East, West US</td>
    </tr>
    <tr>
      <td><a href="o3-mini/"><strong>o3-mini</strong></a></td>
      <td data-search="Retired"><span class="lc-badge lc-badge--muted">Retired</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-provisioned" title="10 regions">Prov.PTU</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US 2" data-all-regions="Australia East,Canada East,East US 2,Japan East,Korea Central,South Central US,South India,Sweden Central,Switzerland North,UAE North"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+7 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="o3-pro/"><strong>o3-pro</strong></a></td>
      <td data-search="Retiring ≤90d"><span class="lc-badge lc-badge--warning">Retiring ≤90d</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="o4-mini/"><strong>o4-mini</strong></a></td>
      <td data-search="Retiring ≤30d"><span class="lc-badge lc-badge--danger">Retiring ≤30d</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span> <span class="sku-badge sku-provisioned" title="9 regions">Prov.PTU</span> <span class="sku-badge sku-provisioned-global" title="27 regions">Prov.Global</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,Japan East,North Central US,South Central US,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+6 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+24 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Other, Provisioned, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="sora-2/"><strong>sora-2</strong></a></td>
      <td data-search="Retirement due"><span class="lc-badge lc-badge--warning">Retirement due</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="text-embedding-3-large/"><strong>text-embedding-3-large</strong></a></td>
      <td data-search="Retiring ≤30d"><span class="lc-badge lc-badge--danger">Retiring ≤30d</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,Norway East,Poland Central,South Africa North,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+16 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Datazone, Global, Other, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="text-embedding-3-small/"><strong>text-embedding-3-small</strong></a></td>
      <td data-search="Retiring ≤30d"><span class="lc-badge lc-badge--danger">Retiring ≤30d</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,North Europe,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona,usgovvirginia"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+28 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,Japan East,Switzerland North,UAE North,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+5 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Datazone, Global, Other, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, North Europe, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona, usgovvirginia</td>
    </tr>
    <tr>
      <td><a href="text-embedding-ada-002/"><strong>text-embedding-ada-002</strong></a></td>
      <td data-search="Retiring ≤30d"><span class="lc-badge lc-badge--danger">Retiring ≤30d</span></td>
      <td><span class="badge badge-broad">Broad</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-datazone" data-tooltip="Data residency compliance deployments | Required for data sovereignty and compliance requirements (GDPR, etc.) | ✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies">Datazone</span> <span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3,usgovarizona"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+26 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Japan East,North Central US,Norway East,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+16 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Datazone, Global, Other, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3, usgovarizona</td>
    </tr>
    <tr>
      <td><a href="tsuzumi-7b/"><strong>tsuzumi-7b</strong></a></td>
      <td data-search="No date announced"><span class="lc-badge lc-badge--neutral">No date announced</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="tts/"><strong>tts</strong></a></td>
      <td data-search="Generally available"><span class="lc-badge lc-badge--success">Generally available</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterByRegion('West US 3')">West US 3</span></span></td>
      <td>-</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterByRegion('West US 3')">West US 3</span></span></td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other, Standard</td>
      <td class="hidden-col">North Central US, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="tts-hd/"><strong>tts-hd</strong></a></td>
      <td data-search="Generally available"><span class="lc-badge lc-badge--success">Generally available</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterByRegion('West US 3')">West US 3</span></span></td>
      <td>-</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterByRegion('West US 3')">West US 3</span></span></td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other, Standard</td>
      <td class="hidden-col">North Central US, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="whisper/"><strong>whisper</strong></a></td>
      <td data-search="Generally available"><span class="lc-badge lc-badge--success">Generally available</span></td>
      <td><span class="badge badge-emerging">Emerging</span></td>
      <td><span class="sku-badge sku-global" data-tooltip="Worldwide availability with intelligent routing | Best for applications needing global reach with automatic failover | ⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements">Global</span> <span class="sku-badge sku-standard" data-tooltip="Pay-as-you-go regional deployments | Best for variable workloads and cost-sensitive applications | ✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft">Standard</span></td>
      <td><span class="region-list" data-preview-regions="East US 2,North Central US,Norway East" data-all-regions="East US 2,North Central US,Norway East,South India,Sweden Central,Switzerland North,UAE North,West Europe"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterByRegion('Norway East')">Norway East</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+5 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="East US 2,North Central US,Norway East" data-all-regions="East US 2,North Central US,Norway East,South India,Sweden Central,Switzerland North,UAE North,West Europe"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterByRegion('Norway East')">Norway East</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+5 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global, Other, Standard</td>
      <td class="hidden-col">East US 2, North Central US, Norway East, South India, Sweden Central, Switzerland North, UAE North, West Europe</td>
    </tr>
  </tbody>
</table>
</div>

---

## SKU Category Reference

| Category | Description | Best For |
|----------|-------------|----------|
| **Global** | Worldwide availability with intelligent routing | Apps needing global reach with automatic failover |
| **Datazone** | Data residency compliance deployments | GDPR, sovereignty, compliance requirements |
| **Standard** | Pay-as-you-go regional deployments | Variable workloads, cost-sensitive apps |
| **Prov. PTU** | Regional reserved throughput capacity (PTU) | High-volume workloads in a specific region |
| **Prov. Global** | Global reserved throughput capacity (PTU) | High-volume workloads with global routing |

---

_Last updated: 2026-10-05 15:23 UTC_
