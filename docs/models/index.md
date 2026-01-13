# All Models

Complete catalog of AI Foundry models with availability details. Each SKU column shows the regions where that deployment type is available.

<div class="filter-controls">
  <div class="filter-group">
    <label for="coverage-filter">Coverage Level</label>
    <select id="coverage-filter" onchange="filterModelsTable()">
      <option value="">All Levels</option>
      <option value="Broad">🟢 Broad (25+)</option>
      <option value="Strong">🟡 Strong (20-24)</option>
      <option value="Growing">🟠 Growing (15-19)</option>
      <option value="Emerging">🔴 Emerging (&lt;15)</option>
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
    <button onclick="resetModelsFilters()" class="md-button">Reset</button>
  </div>
</div>

<div class="table-responsive">
<table id="models-table" class="filterable display">
  <thead>
    <tr>
      <th>Model</th>
      <th>Coverage</th>
      <th>Global Regions</th>
      <th>Datazone Regions</th>
      <th>Standard Regions</th>
      <th>Provisioned Regions</th>
      <th class="hidden-col">Categories</th>
      <th class="hidden-col">Region List</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="codex-mini/"><strong>codex-mini</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="computer-use-preview/"><strong>computer-use-preview</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('South India')">South India</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">East US 2, South India, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="dall-e-3/"><strong>dall-e-3</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td class="hidden-col">Global, Standard</td>
      <td class="hidden-col">Australia East, East US, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-35-turbo/"><strong>gpt-35-turbo</strong></a></td>
      <td><span class="badge badge-broad">🟢 Broad</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+22 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Japan East,North Central US,South Central US,South India,Sweden Central,Switzerland North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+12 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+21 more</button></span></td>
      <td class="hidden-col">Global, Provisioned, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-35-turbo-16k/"><strong>gpt-35-turbo-16k</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Japan East,North Central US,Sweden Central,Switzerland North,UK South"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+7 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Japan East,North Central US,Sweden Central,Switzerland North,UK South"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+7 more</button></span></td>
      <td>-</td>
      <td class="hidden-col">Global, Standard</td>
      <td class="hidden-col">Australia East, Canada East, East US, East US 2, France Central, Japan East, North Central US, Sweden Central, Switzerland North, UK South</td>
    </tr>
    <tr>
      <td><a href="gpt-35-turbo-instruct/"><strong>gpt-35-turbo-instruct</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td class="hidden-col">Global, Standard</td>
      <td class="hidden-col">East US, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-4/"><strong>gpt-4</strong></a></td>
      <td><span class="badge badge-strong">🟡 Strong</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UAE North,UK South,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+19 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Japan East,North Central US,Norway East,South Central US,South India,Sweden Central,Switzerland North,UK South,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+12 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UAE North,UK South,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+19 more</button></span></td>
      <td class="hidden-col">Global, Provisioned, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, East US, East US 2, France Central, Germany West Central, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UAE North, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-4-32k/"><strong>gpt-4-32k</strong></a></td>
      <td><span class="badge badge-strong">🟡 Strong</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+18 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,France Central" data-all-regions="Australia East,Canada East,France Central,Sweden Central,Switzerland North"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+2 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Central US,East US,East US 2,France Central,Germany West Central,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UK South,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+17 more</button></span></td>
      <td class="hidden-col">Global, Provisioned, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Sweden Central, Switzerland North, UK South, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-4-1/"><strong>gpt-4.1</strong></a></td>
      <td><span class="badge badge-broad">🟢 Broad</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-4-1-mini/"><strong>gpt-4.1-mini</strong></a></td>
      <td><span class="badge badge-broad">🟢 Broad</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-4-1-nano/"><strong>gpt-4.1-nano</strong></a></td>
      <td><span class="badge badge-broad">🟢 Broad</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-4o/"><strong>gpt-4o</strong></a></td>
      <td><span class="badge badge-broad">🟢 Broad</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Japan East,North Central US,Norway East,South Central US,South India,Sweden Central,Switzerland North,UK South,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+12 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Provisioned, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-4o-audio-preview/"><strong>gpt-4o-audio-preview</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-4o-mini/"><strong>gpt-4o-mini</strong></a></td>
      <td><span class="badge badge-broad">🟢 Broad</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Provisioned, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-4o-mini-audio-preview/"><strong>gpt-4o-mini-audio-preview</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">East US, East US 2</td>
    </tr>
    <tr>
      <td><a href="gpt-4o-mini-realtime-preview/"><strong>gpt-4o-mini-realtime-preview</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-4o-mini-transcribe/"><strong>gpt-4o-mini-transcribe</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-4o-mini-tts/"><strong>gpt-4o-mini-tts</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">East US 2</td>
    </tr>
    <tr>
      <td><a href="gpt-4o-realtime-preview/"><strong>gpt-4o-realtime-preview</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-4o-transcribe/"><strong>gpt-4o-transcribe</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-4o-transcribe-diarize/"><strong>gpt-4o-transcribe-diarize</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-5/"><strong>gpt-5</strong></a></td>
      <td><span class="badge badge-broad">🟢 Broad</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-chat/"><strong>gpt-5-chat</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-5-codex/"><strong>gpt-5-codex</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-5-mini/"><strong>gpt-5-mini</strong></a></td>
      <td><span class="badge badge-broad">🟢 Broad</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-nano/"><strong>gpt-5-nano</strong></a></td>
      <td><span class="badge badge-broad">🟢 Broad</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+23 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Datazone, Global</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-pro/"><strong>gpt-5-pro</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-5-1/"><strong>gpt-5.1</strong></a></td>
      <td><span class="badge badge-broad">🟢 Broad</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,France Central" data-all-regions="East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('France Central')">France Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+10 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-5-1-chat/"><strong>gpt-5.1-chat</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US 2" data-all-regions="Australia East,Canada East,East US 2,Japan East,Korea Central,Sweden Central,Switzerland North,UK South"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+5 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">Australia East, Canada East, East US 2, Japan East, Korea Central, Sweden Central, Switzerland North, UK South</td>
    </tr>
    <tr>
      <td><a href="gpt-5-1-codex/"><strong>gpt-5.1-codex</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,Central US" data-all-regions="Australia East,Canada East,Central US,East US 2,Japan East,Korea Central,Sweden Central,Switzerland North,UK South,West Europe"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+7 more</button></span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('West Europe')">West Europe</span></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,Central US" data-all-regions="Australia East,Canada East,Central US,East US 2,Japan East,Korea Central,Switzerland North,UK South,West Europe"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+6 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Provisioned</td>
      <td class="hidden-col">Australia East, Canada East, Central US, East US 2, Japan East, Korea Central, Sweden Central, Switzerland North, UK South, West Europe</td>
    </tr>
    <tr>
      <td><a href="gpt-5-1-codex-max/"><strong>gpt-5.1-codex-max</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-5-1-codex-mini/"><strong>gpt-5.1-codex-mini</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US 2" data-all-regions="Australia East,Canada East,East US 2,Japan East,Korea Central,Sweden Central,Switzerland North,UK South"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+5 more</button></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">Australia East, Canada East, East US 2, Japan East, Korea Central, Sweden Central, Switzerland North, UK South</td>
    </tr>
    <tr>
      <td><a href="gpt-5-2/"><strong>gpt-5.2</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US 2,South Central US" data-all-regions="Central US,East US 2,South Central US,Sweden Central,UK South"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('South Central US')">South Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+2 more</button></span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span></span></td>
      <td>-</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('UK South')">UK South</span></span></td>
      <td class="hidden-col">Datazone, Global, Provisioned</td>
      <td class="hidden-col">Central US, East US 2, South Central US, Sweden Central, UK South</td>
    </tr>
    <tr>
      <td><a href="gpt-5-2-chat/"><strong>gpt-5.2-chat</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-audio/"><strong>gpt-audio</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-audio-mini/"><strong>gpt-audio-mini</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-image-1/"><strong>gpt-image-1</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+2 more</button></span></td>
      <td>-</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('UAE North')">UAE North</span> <span class="region-badge" onclick="filterByRegion('West US 3')">West US 3</span></span></td>
      <td>-</td>
      <td class="hidden-col">Global, Standard</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-image-1-mini/"><strong>gpt-image-1-mini</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span></span></td>
      <td>-</td>
      <td class="hidden-col">Global, Standard</td>
      <td class="hidden-col">East US, East US 2, North Central US, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-image-1-5/"><strong>gpt-image-1.5</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+2 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="East US 2,Poland Central,Sweden Central" data-all-regions="East US 2,Poland Central,Sweden Central,UAE North,West US 3"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Poland Central')">Poland Central</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+2 more</button></span></td>
      <td>-</td>
      <td class="hidden-col">Global, Standard</td>
      <td class="hidden-col">East US 2, Poland Central, Sweden Central, UAE North, West US 3</td>
    </tr>
    <tr>
      <td><a href="gpt-realtime/"><strong>gpt-realtime</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="gpt-realtime-mini/"><strong>gpt-realtime-mini</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="model-router/"><strong>model-router</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Datazone, Global</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="o1/"><strong>o1</strong></a></td>
      <td><span class="badge badge-broad">🟢 Broad</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Provisioned, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="o1-mini/"><strong>o1-mini</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US,West US 3"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+4 more</button></span></td>
      <td>-</td>
      <td class="hidden-col">Global, Standard</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="o1-preview/"><strong>o1-preview</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="East US,East US 2,North Central US" data-all-regions="East US,East US 2,North Central US,South Central US,Sweden Central,West US"><span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+3 more</button></span></td>
      <td>-</td>
      <td class="hidden-col">Global, Standard</td>
      <td class="hidden-col">East US, East US 2, North Central US, South Central US, Sweden Central, West US</td>
    </tr>
    <tr>
      <td><a href="o3/"><strong>o3</strong></a></td>
      <td><span class="badge badge-broad">🟢 Broad</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="o3-deep-research/"><strong>o3-deep-research</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Norway East')">Norway East</span> <span class="region-badge" onclick="filterByRegion('West US')">West US</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">Norway East, West US</td>
    </tr>
    <tr>
      <td><a href="o3-mini/"><strong>o3-mini</strong></a></td>
      <td><span class="badge badge-broad">🟢 Broad</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="o3-pro/"><strong>o3-pro</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">Central US, East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="o4-mini/"><strong>o4-mini</strong></a></td>
      <td><span class="badge badge-broad">🟢 Broad</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td><span class="region-list" data-preview-regions="Central US,East US,East US 2" data-all-regions="Central US,East US,East US 2,France Central,Germany West Central,Italy North,North Central US,Poland Central,South Central US,Spain Central,Sweden Central,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Central US')">Central US</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+11 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada Central" data-all-regions="Australia East,Brazil South,Canada Central,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,Switzerland West,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada Central')">Canada Central</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+25 more</button></span></td>
      <td class="hidden-col">Datazone, Global, Provisioned</td>
      <td class="hidden-col">Australia East, Brazil South, Canada Central, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, Switzerland West, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="sora/"><strong>sora</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span></span></td>
      <td>-</td>
      <td class="hidden-col">Global, Standard</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="sora-2/"><strong>sora-2</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span></span></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td class="hidden-col">Global</td>
      <td class="hidden-col">East US 2, Sweden Central</td>
    </tr>
    <tr>
      <td><a href="text-embedding-3-large/"><strong>text-embedding-3-large</strong></a></td>
      <td><span class="badge badge-broad">🟢 Broad</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+23 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,France Central,Germany West Central,Japan East,Korea Central,Norway East,Poland Central,South Africa North,South India,Southeast Asia,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+16 more</button></span></td>
      <td>-</td>
      <td class="hidden-col">Global, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Southeast Asia, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="text-embedding-3-small/"><strong>text-embedding-3-small</strong></a></td>
      <td><span class="badge badge-broad">🟢 Broad</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,Central US,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+22 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Canada East,East US" data-all-regions="Australia East,Canada East,East US,East US 2,Japan East,Switzerland North,UAE North,West US"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <span class="region-badge" onclick="filterByRegion('East US')">East US</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+5 more</button></span></td>
      <td>-</td>
      <td class="hidden-col">Global, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, Central US, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="text-embedding-ada-002/"><strong>text-embedding-ada-002</strong></a></td>
      <td><span class="badge badge-strong">🟡 Strong</span></td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Germany West Central,Italy North,Japan East,Korea Central,North Central US,Norway East,Poland Central,South Africa North,South Central US,South India,Spain Central,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+21 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="Australia East,Brazil South,Canada East" data-all-regions="Australia East,Brazil South,Canada East,East US,East US 2,France Central,Japan East,North Central US,Norway East,South Africa North,South Central US,South India,Sweden Central,Switzerland North,UAE North,UK South,West Europe,West US,West US 3"><span class="region-badge" onclick="filterByRegion('Australia East')">Australia East</span> <span class="region-badge" onclick="filterByRegion('Brazil South')">Brazil South</span> <span class="region-badge" onclick="filterByRegion('Canada East')">Canada East</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+16 more</button></span></td>
      <td>-</td>
      <td class="hidden-col">Global, Standard</td>
      <td class="hidden-col">Australia East, Brazil South, Canada East, East US, East US 2, France Central, Germany West Central, Italy North, Japan East, Korea Central, North Central US, Norway East, Poland Central, South Africa North, South Central US, South India, Spain Central, Sweden Central, Switzerland North, UAE North, UK South, West Europe, West US, West US 3</td>
    </tr>
    <tr>
      <td><a href="tts/"><strong>tts</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterByRegion('West US 3')">West US 3</span></span></td>
      <td>-</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterByRegion('West US 3')">West US 3</span></span></td>
      <td>-</td>
      <td class="hidden-col">Global, Standard</td>
      <td class="hidden-col">North Central US, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="tts-hd/"><strong>tts-hd</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterByRegion('West US 3')">West US 3</span></span></td>
      <td>-</td>
      <td><span class="region-list"><span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterByRegion('Sweden Central')">Sweden Central</span> <span class="region-badge" onclick="filterByRegion('West US 3')">West US 3</span></span></td>
      <td>-</td>
      <td class="hidden-col">Global, Standard</td>
      <td class="hidden-col">North Central US, Sweden Central, West US 3</td>
    </tr>
    <tr>
      <td><a href="whisper/"><strong>whisper</strong></a></td>
      <td><span class="badge badge-emerging">🔴 Emerging</span></td>
      <td><span class="region-list" data-preview-regions="East US 2,North Central US,Norway East" data-all-regions="East US 2,North Central US,Norway East,South India,Sweden Central,Switzerland North,UAE North,West Europe"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterByRegion('Norway East')">Norway East</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+5 more</button></span></td>
      <td>-</td>
      <td><span class="region-list" data-preview-regions="East US 2,North Central US,Norway East" data-all-regions="East US 2,North Central US,Norway East,South India,Sweden Central,Switzerland North,UAE North,West Europe"><span class="region-badge" onclick="filterByRegion('East US 2')">East US 2</span> <span class="region-badge" onclick="filterByRegion('North Central US')">North Central US</span> <span class="region-badge" onclick="filterByRegion('Norway East')">Norway East</span> <button class="expand-btn" onclick="toggleRegionBadges(this)">+5 more</button></span></td>
      <td>-</td>
      <td class="hidden-col">Global, Standard</td>
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
| **Provisioned** | Reserved throughput capacity (PTU) | Predictable, high-volume production workloads |

---

_Last updated: 2026-01-13 17:29 UTC_
