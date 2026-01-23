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
    <div class="stat-value">114</div>
    <div class="stat-label">Models</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">1294</div>
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
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/dall-e-3/">dall-e-3</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard image generation</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-35-turbo-16k/">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-35-turbo-16k/">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/codex-mini/">codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-audio/">gpt-audio</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-audio-mini/">gpt-audio-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-realtime-mini/">gpt-realtime-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/o3-pro/">o3-pro</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/codestral-2501/">Codestral-2501</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/cohere-command-r-08-2024/">Cohere Command R 08-2024</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/cohere-command-r+-08-2024/">Cohere Command R+ 08-2024</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/cohere-embed-v3---english/">Cohere Embed v3 - English</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/cohere-embed-v3---multilingual/">Cohere Embed v3 - Multilingual</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/cohere-rerank-v3-5/">Cohere Rerank v3.5</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/llama-3-1-405b-instruct/">Llama 3.1 405B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/llama-3-1-8b-instruct/">Llama 3.1 8B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama 3.3 70B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/llama-3-2-11b-vision-instruct/">Llama-3.2-11B-Vision-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/llama-3-2-1b/">Llama-3.2-1B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/llama-3-2-1b-instruct/">Llama-3.2-1B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/llama-3-2-3b/">Llama-3.2-3B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/llama-3-2-3b-instruct/">Llama-3.2-3B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/llama-3-2-90b-vision-instruct/">Llama-3.2-90B-Vision-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/llama-guard-3-11b-vision/">Llama-Guard-3-11B-Vision</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/llama-guard-3-1b/">Llama-Guard-3-1B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/ministral-3b/">Ministral-3B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/mistral-medium-3-(25-05)/">Mistral Medium 3 (25.05)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/mistral-small-25-03/">Mistral Small 25.03</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/phi-4/">Phi-4</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/phi-4-mini-instruct/">Phi-4-mini-instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/phi-4-mini-reasoning/">Phi-4-mini-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/phi-4-multimodal-instruct/">Phi-4-multimodal-instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/phi-4-reasoning/">Phi-4-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/stable-diffusion-3-5-large/">Stable Diffusion 3.5 Large</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/stable-image-core/">Stable Image Core</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/stable-image-ultra/">Stable Image Ultra</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/timegen-1/">TimeGEN-1</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/dall-e-3/">dall-e-3</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard image generation</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-35-turbo-16k/">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-35-turbo-instruct/">gpt-35-turbo-instruct</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo, Standard completions</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-4o-mini-audio-preview/">gpt-4o-mini-audio-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/o1-preview/">o1-preview</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/tsuzumi-7b/">tsuzumi-7b</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/claude-haiku-4-5-(preview)/">Claude Haiku 4.5 (preview)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/claude-opus-4-1-(preview)/">Claude Opus 4.1 (preview)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/claude-opus-4-5-(preview)/">Claude Opus 4.5 (preview)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/claude-sonnet-4-5-(preview)/">Claude Sonnet 4.5 (preview)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/codestral-2501/">Codestral-2501</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/cohere-command-r-08-2024/">Cohere Command R 08-2024</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/cohere-command-r+-08-2024/">Cohere Command R+ 08-2024</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/cohere-embed-v3---english/">Cohere Embed v3 - English</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/cohere-embed-v3---multilingual/">Cohere Embed v3 - Multilingual</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/cohere-rerank-v3-5/">Cohere Rerank v3.5</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gretel-navigator/">Gretel-Navigator</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/llama-3-1-405b-instruct/">Llama 3.1 405B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/llama-3-1-8b-instruct/">Llama 3.1 8B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama 3.3 70B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/llama-3-2-11b-vision-instruct/">Llama-3.2-11B-Vision-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/llama-3-2-1b/">Llama-3.2-1B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/llama-3-2-1b-instruct/">Llama-3.2-1B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/llama-3-2-3b/">Llama-3.2-3B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/llama-3-2-3b-instruct/">Llama-3.2-3B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/llama-3-2-90b-vision-instruct/">Llama-3.2-90B-Vision-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/llama-guard-3-11b-vision/">Llama-Guard-3-11B-Vision</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/llama-guard-3-1b/">Llama-Guard-3-1B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/ministral-3b/">Ministral-3B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/mistral-medium-3-(25-05)/">Mistral Medium 3 (25.05)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/mistral-small-25-03/">Mistral Small 25.03</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/phi-4/">Phi-4</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/phi-4-mini-instruct/">Phi-4-mini-instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/phi-4-mini-reasoning/">Phi-4-mini-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/phi-4-multimodal-instruct/">Phi-4-multimodal-instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/phi-4-reasoning/">Phi-4-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/stable-diffusion-3-5-large/">Stable Diffusion 3.5 Large</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/stable-image-core/">Stable Image Core</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/stable-image-ultra/">Stable Image Ultra</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/timegen-1/">TimeGEN-1</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/codex-mini/">codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-35-turbo-16k/">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-audio-preview/">gpt-4o-audio-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-mini-audio-preview/">gpt-4o-mini-audio-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-mini-realtime-preview/">gpt-4o-mini-realtime-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-mini-transcribe/">gpt-4o-mini-transcribe</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-mini-tts/">gpt-4o-mini-tts</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-realtime-preview/">gpt-4o-realtime-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-transcribe/">gpt-4o-transcribe</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-transcribe-diarize/">gpt-4o-transcribe-diarize</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-1-codex-max/">gpt-5.1-codex-max</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-2-chat/">gpt-5.2-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-audio/">gpt-audio</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-audio-mini/">gpt-audio-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard global deployments, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-realtime-mini/">gpt-realtime-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/o1-preview/">o1-preview</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/o3-pro/">o3-pro</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/sora/">sora</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/sora-2/">sora-2</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/tsuzumi-7b/">tsuzumi-7b</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/whisper/">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-35-turbo-16k/">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-35-turbo-16k/">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/codestral-2501/">Codestral-2501</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/cohere-command-r-08-2024/">Cohere Command R 08-2024</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/cohere-command-r+-08-2024/">Cohere Command R+ 08-2024</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/cohere-embed-v3---english/">Cohere Embed v3 - English</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/cohere-embed-v3---multilingual/">Cohere Embed v3 - Multilingual</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/cohere-rerank-v3-5/">Cohere Rerank v3.5</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/llama-3-1-405b-instruct/">Llama 3.1 405B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/llama-3-1-8b-instruct/">Llama 3.1 8B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama 3.3 70B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/llama-3-2-11b-vision-instruct/">Llama-3.2-11B-Vision-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/llama-3-2-1b/">Llama-3.2-1B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/llama-3-2-1b-instruct/">Llama-3.2-1B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/llama-3-2-3b/">Llama-3.2-3B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/llama-3-2-3b-instruct/">Llama-3.2-3B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/llama-3-2-90b-vision-instruct/">Llama-3.2-90B-Vision-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/llama-guard-3-11b-vision/">Llama-Guard-3-11B-Vision</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/llama-guard-3-1b/">Llama-Guard-3-1B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/ministral-3b/">Ministral-3B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/mistral-medium-3-(25-05)/">Mistral Medium 3 (25.05)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/mistral-small-25-03/">Mistral Small 25.03</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/phi-4/">Phi-4</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/phi-4-mini-instruct/">Phi-4-mini-instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/phi-4-mini-reasoning/">Phi-4-mini-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/phi-4-multimodal-instruct/">Phi-4-multimodal-instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/phi-4-reasoning/">Phi-4-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/stable-diffusion-3-5-large/">Stable Diffusion 3.5 Large</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/stable-image-core/">Stable Image Core</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/stable-image-ultra/">Stable Image Ultra</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/timegen-1/">TimeGEN-1</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-35-turbo-16k/">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/o1-preview/">o1-preview</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/tsuzumi-7b/">tsuzumi-7b</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/tts/">tts</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/tts-hd/">tts-hd</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/whisper/">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/o3-deep-research/">o3-deep-research</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/whisper/">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard global deployments, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/codestral-2501/">Codestral-2501</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/cohere-command-r-08-2024/">Cohere Command R 08-2024</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/cohere-command-r+-08-2024/">Cohere Command R+ 08-2024</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/cohere-embed-v3---english/">Cohere Embed v3 - English</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/cohere-embed-v3---multilingual/">Cohere Embed v3 - Multilingual</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/cohere-rerank-v3-5/">Cohere Rerank v3.5</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/llama-3-1-405b-instruct/">Llama 3.1 405B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/llama-3-1-8b-instruct/">Llama 3.1 8B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama 3.3 70B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/llama-3-2-11b-vision-instruct/">Llama-3.2-11B-Vision-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/llama-3-2-1b/">Llama-3.2-1B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/llama-3-2-1b-instruct/">Llama-3.2-1B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/llama-3-2-3b/">Llama-3.2-3B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/llama-3-2-3b-instruct/">Llama-3.2-3B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/llama-3-2-90b-vision-instruct/">Llama-3.2-90B-Vision-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/llama-guard-3-11b-vision/">Llama-Guard-3-11B-Vision</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/llama-guard-3-1b/">Llama-Guard-3-1B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/ministral-3b/">Ministral-3B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/mistral-medium-3-(25-05)/">Mistral Medium 3 (25.05)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/mistral-small-25-03/">Mistral Small 25.03</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/phi-4/">Phi-4</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/phi-4-mini-instruct/">Phi-4-mini-instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/phi-4-mini-reasoning/">Phi-4-mini-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/phi-4-multimodal-instruct/">Phi-4-multimodal-instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/phi-4-reasoning/">Phi-4-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/stable-diffusion-3-5-large/">Stable Diffusion 3.5 Large</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/stable-image-core/">Stable Image Core</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/stable-image-ultra/">Stable Image Ultra</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/timegen-1/">TimeGEN-1</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/o1-preview/">o1-preview</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/tsuzumi-7b/">tsuzumi-7b</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/whisper/">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/claude-haiku-4-5-(preview)/">Claude Haiku 4.5 (preview)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/claude-opus-4-1-(preview)/">Claude Opus 4.1 (preview)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/claude-opus-4-5-(preview)/">Claude Opus 4.5 (preview)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/claude-sonnet-4-5-(preview)/">Claude Sonnet 4.5 (preview)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/codestral-2501/">Codestral-2501</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/cohere-command-r-08-2024/">Cohere Command R 08-2024</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/cohere-command-r+-08-2024/">Cohere Command R+ 08-2024</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/cohere-embed-v3---english/">Cohere Embed v3 - English</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/cohere-embed-v3---multilingual/">Cohere Embed v3 - Multilingual</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/cohere-rerank-v3-5/">Cohere Rerank v3.5</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/llama-3-1-8b-instruct/">Llama 3.1 8B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama 3.3 70B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/llama-3-2-11b-vision-instruct/">Llama-3.2-11B-Vision-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/llama-3-2-1b/">Llama-3.2-1B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/llama-3-2-1b-instruct/">Llama-3.2-1B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/llama-3-2-3b/">Llama-3.2-3B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/llama-3-2-3b-instruct/">Llama-3.2-3B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/llama-3-2-90b-vision-instruct/">Llama-3.2-90B-Vision-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/llama-guard-3-11b-vision/">Llama-Guard-3-11B-Vision</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/llama-guard-3-1b/">Llama-Guard-3-1B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/ministral-3b/">Ministral-3B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/mistral-medium-3-(25-05)/">Mistral Medium 3 (25.05)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/mistral-small-25-03/">Mistral Small 25.03</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/phi-4/">Phi-4</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/phi-4-mini-instruct/">Phi-4-mini-instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/phi-4-multimodal-instruct/">Phi-4-multimodal-instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/timegen-1/">TimeGEN-1</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/codex-mini/">codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/dall-e-3/">dall-e-3</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard image generation</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-35-turbo-16k/">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-35-turbo-instruct/">gpt-35-turbo-instruct</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4o-audio-preview/">gpt-4o-audio-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4o-mini-realtime-preview/">gpt-4o-mini-realtime-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4o-mini-transcribe/">gpt-4o-mini-transcribe</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4o-realtime-preview/">gpt-4o-realtime-preview</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4o-transcribe/">gpt-4o-transcribe</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4o-transcribe-diarize/">gpt-4o-transcribe-diarize</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-1-codex-max/">gpt-5.1-codex-max</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-2-chat/">gpt-5.2-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-audio/">gpt-audio</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-audio-mini/">gpt-audio-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard global deployments, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-realtime-mini/">gpt-realtime-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/o1-preview/">o1-preview</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/o3-pro/">o3-pro</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/sora/">sora</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/sora-2/">sora-2</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/tts/">tts</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/tts-hd/">tts-hd</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/whisper/">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-35-turbo-16k/">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/whisper/">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard global deployments, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard global deployments, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/whisper/">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-35-turbo-16k/">gpt-35-turbo-16k</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/whisper/">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all), Standard audio</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/codestral-2501/">Codestral-2501</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/cohere-command-r-08-2024/">Cohere Command R 08-2024</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/cohere-command-r+-08-2024/">Cohere Command R+ 08-2024</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/cohere-embed-v3---english/">Cohere Embed v3 - English</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/cohere-embed-v3---multilingual/">Cohere Embed v3 - Multilingual</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/cohere-rerank-v3-5/">Cohere Rerank v3.5</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/llama-3-1-405b-instruct/">Llama 3.1 405B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/llama-3-1-8b-instruct/">Llama 3.1 8B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama 3.3 70B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/llama-3-2-11b-vision-instruct/">Llama-3.2-11B-Vision-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/llama-3-2-1b/">Llama-3.2-1B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/llama-3-2-1b-instruct/">Llama-3.2-1B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/llama-3-2-3b/">Llama-3.2-3B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/llama-3-2-3b-instruct/">Llama-3.2-3B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/llama-3-2-90b-vision-instruct/">Llama-3.2-90B-Vision-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/llama-guard-3-11b-vision/">Llama-Guard-3-11B-Vision</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/llama-guard-3-1b/">Llama-Guard-3-1B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/ministral-3b/">Ministral-3B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/mistral-medium-3-(25-05)/">Mistral Medium 3 (25.05)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/mistral-small-25-03/">Mistral Small 25.03</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/phi-4/">Phi-4</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/phi-4-mini-instruct/">Phi-4-mini-instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/phi-4-mini-reasoning/">Phi-4-mini-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/phi-4-multimodal-instruct/">Phi-4-multimodal-instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/phi-4-reasoning/">Phi-4-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/stable-diffusion-3-5-large/">Stable Diffusion 3.5 Large</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/stable-image-core/">Stable Image Core</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/stable-image-ultra/">Stable Image Ultra</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/timegen-1/">TimeGEN-1</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-3.5 Turbo, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard chat completions, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/o1-preview/">o1-preview</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard chat completions</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/o3-deep-research/">o3-deep-research</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global coverage, Standard (all), Standard embeddings, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/tsuzumi-7b/">tsuzumi-7b</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/codestral-2501/">Codestral-2501</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/cohere-command-r-08-2024/">Cohere Command R 08-2024</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/cohere-command-r+-08-2024/">Cohere Command R+ 08-2024</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/cohere-embed-v3---english/">Cohere Embed v3 - English</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/cohere-embed-v3---multilingual/">Cohere Embed v3 - Multilingual</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/cohere-rerank-v3-5/">Cohere Rerank v3.5</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Other</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/llama-3-1-405b-instruct/">Llama 3.1 405B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/llama-3-1-8b-instruct/">Llama 3.1 8B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama 3.3 70B Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/llama-3-2-11b-vision-instruct/">Llama-3.2-11B-Vision-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/llama-3-2-1b/">Llama-3.2-1B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/llama-3-2-1b-instruct/">Llama-3.2-1B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/llama-3-2-3b/">Llama-3.2-3B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/llama-3-2-3b-instruct/">Llama-3.2-3B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/llama-3-2-90b-vision-instruct/">Llama-3.2-90B-Vision-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/llama-guard-3-11b-vision/">Llama-Guard-3-11B-Vision</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/llama-guard-3-1b/">Llama-Guard-3-1B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/ministral-3b/">Ministral-3B</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/mistral-medium-3-(25-05)/">Mistral Medium 3 (25.05)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/mistral-small-25-03/">Mistral Small 25.03</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/phi-4/">Phi-4</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/phi-4-mini-instruct/">Phi-4-mini-instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/phi-4-mini-reasoning/">Phi-4-mini-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/phi-4-multimodal-instruct/">Phi-4-multimodal-instruct</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/phi-4-reasoning/">Phi-4-reasoning</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/stable-diffusion-3-5-large/">Stable Diffusion 3.5 Large</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/stable-image-core/">Stable Image Core</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/stable-image-ultra/">Stable Image Ultra</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/timegen-1/">TimeGEN-1</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-3.5 Turbo</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global coverage, Provisioned (PTU managed), Standard GPT-4</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard GPT-4, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard global deployments, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>Global</td>
      <td>Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard global deployments, Standard image generation</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Global, Other</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global, Other</td>
      <td>Data Zone Standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned global, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global coverage, Provisioned (PTU managed), Provisioned global, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global coverage, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage, Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global coverage, Standard (all), Standard global deployments</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/tsuzumi-7b/">tsuzumi-7b</a></td>
      <td>Global, Other</td>
      <td>Global coverage, Region Availability Maas</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/tts/">tts</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all)</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/tts-hd/">tts-hd</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard (all)</td>
    </tr>
  </tbody>
</table>
</div>

---

_Last updated: 2026-01-23 17:04 UTC_
