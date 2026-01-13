# Models by Region

Find which AI models are available in your Azure region, including their deployment SKU options.

---

## Quick Stats

<div class="stats-cards">
  <div class="stat-card">
    <div class="stat-value">28</div>
    <div class="stat-label">Regions</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">58</div>
    <div class="stat-label">Models</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">652</div>
    <div class="stat-label">Deployments</div>
  </div>
</div>

---

## Region-Model Availability

<div class="filter-controls">
  <div class="filter-group">
    <label for="region-select">Region</label>
    <select id="region-select" onchange="filterRegionTable()">
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
    <label for="model-search">Model Name</label>
    <input type="text" id="model-search" placeholder="Search model..." oninput="filterRegionTable()">
  </div>
  <div class="filter-group">
    <label for="sku-category-filter">SKU Category</label>
    <select id="sku-category-filter" onchange="filterRegionTable()">
      <option value="">All Categories</option>
      <option value="Global">Global</option>
      <option value="Datazone">Datazone</option>
      <option value="Standard">Standard</option>
      <option value="Provisioned">Provisioned</option>
    </select>
  </div>
  <div class="filter-group">
    <label>&nbsp;</label>
    <button onclick="resetRegionFilters()" class="md-button">Reset</button>
  </div>
</div>

<div class="table-responsive">
<table id="region-table" class="filterable display">
  <thead>
    <tr>
      <th>Region</th>
      <th>Model</th>
      <th>Categories</th>
      <th>Available SKUs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/dall-e-3.md">dall-e-3</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard image generation</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/gpt-35-turbo-16k.md">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/gpt-5-1-chat.md">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/gpt-5-1-codex.md">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/gpt-5-1-codex-mini.md">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/gpt-35-turbo-16k.md">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/gpt-5-1-chat.md">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/gpt-5-1-codex.md">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/gpt-5-1-codex-mini.md">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/codex-mini.md">codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-5-chat.md">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-5-codex.md">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-5-pro.md">gpt-5-pro</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-5-1-codex.md">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-5-2.md">gpt-5.2</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-audio.md">gpt-audio</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-audio-mini.md">gpt-audio-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-realtime.md">gpt-realtime</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/gpt-realtime-mini.md">gpt-realtime-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/o3-pro.md">o3-pro</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/dall-e-3.md">dall-e-3</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard image generation</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/gpt-35-turbo-16k.md">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/gpt-35-turbo-instruct.md">gpt-35-turbo-instruct</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard GPT-3.5 Turbo, Standard completions</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-4, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/gpt-4o-mini-audio-preview.md">gpt-4o-mini-audio-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/gpt-image-1-mini.md">gpt-image-1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/o1-mini.md">o1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/o1-preview.md">o1-preview</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/codex-mini.md">codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/computer-use-preview.md">computer-use-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-35-turbo-16k.md">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-4, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-4o-audio-preview.md">gpt-4o-audio-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-4o-mini-audio-preview.md">gpt-4o-mini-audio-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-4o-mini-realtime-preview.md">gpt-4o-mini-realtime-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-4o-mini-transcribe.md">gpt-4o-mini-transcribe</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-4o-mini-tts.md">gpt-4o-mini-tts</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-4o-realtime-preview.md">gpt-4o-realtime-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-4o-transcribe.md">gpt-4o-transcribe</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-4o-transcribe-diarize.md">gpt-4o-transcribe-diarize</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-5-chat.md">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-5-codex.md">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-5-pro.md">gpt-5-pro</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-5-1-chat.md">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-5-1-codex.md">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-5-1-codex-max.md">gpt-5.1-codex-max</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-5-1-codex-mini.md">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-5-2.md">gpt-5.2</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-5-2-chat.md">gpt-5.2-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-audio.md">gpt-audio</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-audio-mini.md">gpt-audio-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-image-1.md">gpt-image-1</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-image-1-mini.md">gpt-image-1-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-image-1-5.md">gpt-image-1.5</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard global deployments, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-realtime.md">gpt-realtime</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/gpt-realtime-mini.md">gpt-realtime-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/model-router.md">model-router</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/o1-mini.md">o1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/o1-preview.md">o1-preview</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/o3-pro.md">o3-pro</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/sora.md">sora</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/sora-2.md">sora-2</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="models/whisper.md">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/gpt-35-turbo-16k.md">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/gpt-35-turbo-16k.md">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/gpt-5-1-chat.md">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/gpt-5-1-codex.md">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/gpt-5-1-codex-mini.md">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/gpt-5-1-chat.md">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/gpt-5-1-codex.md">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/gpt-5-1-codex-mini.md">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/gpt-35-turbo-16k.md">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-4, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/gpt-image-1-mini.md">gpt-image-1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/o1-mini.md">o1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/o1-preview.md">o1-preview</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/tts.md">tts</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/tts-hd.md">tts-hd</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="models/whisper.md">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/o3-deep-research.md">o3-deep-research</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="models/whisper.md">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/gpt-image-1.md">gpt-image-1</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/gpt-image-1-mini.md">gpt-image-1-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/gpt-image-1-5.md">gpt-image-1.5</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard global deployments, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-4, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/gpt-5-2.md">gpt-5.2</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/o1-mini.md">o1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/o1-preview.md">o1-preview</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/computer-use-preview.md">computer-use-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="models/whisper.md">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/codex-mini.md">codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/computer-use-preview.md">computer-use-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/dall-e-3.md">dall-e-3</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard image generation</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-35-turbo-16k.md">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-35-turbo-instruct.md">gpt-35-turbo-instruct</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-4, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-4o-audio-preview.md">gpt-4o-audio-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-4o-mini-realtime-preview.md">gpt-4o-mini-realtime-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-4o-mini-transcribe.md">gpt-4o-mini-transcribe</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-4o-realtime-preview.md">gpt-4o-realtime-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-4o-transcribe.md">gpt-4o-transcribe</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-4o-transcribe-diarize.md">gpt-4o-transcribe-diarize</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-5-chat.md">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-5-codex.md">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-5-pro.md">gpt-5-pro</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-5-1-chat.md">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-5-1-codex.md">gpt-5.1-codex</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-5-1-codex-max.md">gpt-5.1-codex-max</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-5-1-codex-mini.md">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-5-2.md">gpt-5.2</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-5-2-chat.md">gpt-5.2-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-audio.md">gpt-audio</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-audio-mini.md">gpt-audio-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-image-1.md">gpt-image-1</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-image-1-mini.md">gpt-image-1-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-image-1-5.md">gpt-image-1.5</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard global deployments, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-realtime.md">gpt-realtime</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/gpt-realtime-mini.md">gpt-realtime-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/model-router.md">model-router</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/o1-mini.md">o1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/o1-preview.md">o1-preview</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/o3-pro.md">o3-pro</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/sora.md">sora</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/sora-2.md">sora-2</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/tts.md">tts</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/tts-hd.md">tts-hd</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="models/whisper.md">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/gpt-35-turbo-16k.md">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/gpt-5-1-chat.md">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/gpt-5-1-codex.md">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/gpt-5-1-codex-mini.md">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="models/whisper.md">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/gpt-image-1.md">gpt-image-1</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard global deployments, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/gpt-image-1-mini.md">gpt-image-1-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/gpt-image-1-5.md">gpt-image-1.5</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard global deployments, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="models/whisper.md">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-35-turbo-16k.md">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-5-1-chat.md">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-5-1-codex.md">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-5-1-codex-mini.md">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/gpt-5-2.md">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/gpt-5-1-codex.md">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="models/whisper.md">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-4, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/o1-mini.md">o1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/o1-preview.md">o1-preview</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/o3-deep-research.md">o3-deep-research</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/gpt-35-turbo.md">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/gpt-4.md">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard (all), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/gpt-4-32k.md">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/gpt-4-1.md">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/gpt-4-1-mini.md">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/gpt-4-1-nano.md">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/gpt-4o.md">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/gpt-4o-mini.md">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/gpt-5.md">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/gpt-5-mini.md">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/gpt-5-nano.md">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/gpt-5-1.md">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/gpt-image-1.md">gpt-image-1</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard global deployments, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/gpt-image-1-mini.md">gpt-image-1-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/gpt-image-1-5.md">gpt-image-1.5</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard global deployments, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/o1.md">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/o1-mini.md">o1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all)</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/o3.md">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/o3-mini.md">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/o4-mini.md">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/text-embedding-3-large.md">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/text-embedding-3-small.md">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/text-embedding-ada-002.md">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/tts.md">tts</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all)</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="models/tts-hd.md">tts-hd</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all)</td>
    </tr>
  </tbody>
</table>
</div>

---

_Last updated: 2026-01-13 21:06 UTC_
