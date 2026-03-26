# Models by Region

Find which AI models are available in your Azure region, including their deployment SKU options.

---

## Quick Stats

<div class="stats-cards">
  <div class="stat-card">
    <div class="stat-value">32</div>
    <div class="stat-label">Regions</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">86</div>
    <div class="stat-label">Models</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">1624</div>
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
      <option value="Japan West">Japan West</option>
      <option value="Korea Central">Korea Central</option>
      <option value="North Central US">North Central US</option>
      <option value="Norway East">Norway East</option>
      <option value="Poland Central">Poland Central</option>
      <option value="Qatar Central">Qatar Central</option>
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
      <option value="West Central US">West Central US</option>
      <option value="West Europe">West Europe</option>
      <option value="West US">West US</option>
      <option value="West US 2">West US 2</option>
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
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/dall-e-3/">dall-e-3</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Australia East</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Brazil South</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-4o-mini-transcribe/">gpt-4o-mini-transcribe</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-4o-transcribe/">gpt-4o-transcribe</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-4o-transcribe-diarize/">gpt-4o-transcribe-diarize</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
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
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-realtime-1-5/">gpt-realtime-1.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/gpt-realtime-mini/">gpt-realtime-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada Central</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
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
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Canada East</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/codex-mini/">codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-4o-mini-transcribe/">gpt-4o-mini-transcribe</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-4o-transcribe/">gpt-4o-transcribe</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-4o-transcribe-diarize/">gpt-4o-transcribe-diarize</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-audio/">gpt-audio</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-audio-1-5/">gpt-audio-1.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-audio-mini/">gpt-audio-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-realtime-1-5/">gpt-realtime-1.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/gpt-realtime-mini/">gpt-realtime-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/o3-pro/">o3-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Central US</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/dall-e-3/">dall-e-3</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-4o-mini-audio-preview/">gpt-4o-mini-audio-preview</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>East US</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/codex-mini/">codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-audio-preview/">gpt-4o-audio-preview</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-mini-audio-preview/">gpt-4o-mini-audio-preview</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-mini-realtime-preview/">gpt-4o-mini-realtime-preview</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-mini-transcribe/">gpt-4o-mini-transcribe</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-mini-tts/">gpt-4o-mini-tts</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-realtime-preview/">gpt-4o-realtime-preview</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-transcribe/">gpt-4o-transcribe</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-4o-transcribe-diarize/">gpt-4o-transcribe-diarize</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-1-codex-max/">gpt-5.1-codex-max</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-2-chat/">gpt-5.2-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-3-chat/">gpt-5.3-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-4/">gpt-5.4</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-5-4-pro/">gpt-5.4-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-audio/">gpt-audio</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-audio-1-5/">gpt-audio-1.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-audio-mini/">gpt-audio-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-realtime-1-5/">gpt-realtime-1.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/gpt-realtime-mini/">gpt-realtime-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/o3-pro/">o3-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/sora/">sora</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/sora-2/">sora-2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>East US 2</strong></td>
      <td><a href="../models/whisper/">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-4o-mini-transcribe/">gpt-4o-mini-transcribe</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-4o-transcribe/">gpt-4o-transcribe</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-4o-transcribe-diarize/">gpt-4o-transcribe-diarize</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-realtime-1-5/">gpt-realtime-1.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/gpt-realtime-mini/">gpt-realtime-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>France Central</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Germany West Central</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Italy North</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Japan East</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Japan West</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Korea Central</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/tts/">tts</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/tts-hd/">tts-hd</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>North Central US</strong></td>
      <td><a href="../models/whisper/">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/o3-deep-research/">o3-deep-research</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Norway East</strong></td>
      <td><a href="../models/whisper/">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5-4/">gpt-5.4</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-5-4-pro/">gpt-5.4-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Poland Central</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Qatar Central</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Qatar Central</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Qatar Central</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Qatar Central</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Qatar Central</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Qatar Central</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Qatar Central</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Qatar Central</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Qatar Central</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Qatar Central</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Qatar Central</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Qatar Central</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Qatar Central</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Qatar Central</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Qatar Central</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Qatar Central</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Africa North</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-4/">gpt-5.4</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/gpt-5-4-pro/">gpt-5.4-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South Central US</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>South India</strong></td>
      <td><a href="../models/whisper/">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
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
      <td>Global Standard, Global coverage, Provisioned global</td>
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
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Southeast Asia</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Spain Central</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/codex-mini/">codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/dall-e-3/">dall-e-3</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4o-audio-preview/">gpt-4o-audio-preview</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4o-mini-realtime-preview/">gpt-4o-mini-realtime-preview</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4o-mini-transcribe/">gpt-4o-mini-transcribe</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4o-realtime-preview/">gpt-4o-realtime-preview</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4o-transcribe/">gpt-4o-transcribe</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-4o-transcribe-diarize/">gpt-4o-transcribe-diarize</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-1-codex-max/">gpt-5.1-codex-max</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-2-chat/">gpt-5.2-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-3-chat/">gpt-5.3-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-4/">gpt-5.4</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-5-4-pro/">gpt-5.4-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-audio/">gpt-audio</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-audio-1-5/">gpt-audio-1.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-audio-mini/">gpt-audio-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-realtime-1-5/">gpt-realtime-1.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/gpt-realtime-mini/">gpt-realtime-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/o3-pro/">o3-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/sora/">sora</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/sora-2/">sora-2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/tts/">tts</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/tts-hd/">tts-hd</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Sweden Central</strong></td>
      <td><a href="../models/whisper/">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Switzerland North</strong></td>
      <td><a href="../models/whisper/">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
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
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>Switzerland West</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
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
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>UAE North</strong></td>
      <td><a href="../models/whisper/">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Global, Provisioned, Standard</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Global, Provisioned</td>
      <td>Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>UK South</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Global, Standard</td>
      <td>Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Central US</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>West Europe</strong></td>
      <td><a href="../models/whisper/">whisper</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/o3-deep-research/">o3-deep-research</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>West US</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 2</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-fast/">Cohere-rerank-v4.0-fast</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/cohere-rerank-v4-0-pro/">Cohere-rerank-v4.0-pro</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/deepseek-v3-2/">DeepSeek-V3.2</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/deepseek-v3-2-speciale/">DeepSeek-V3.2-Speciale</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/flux-2-pro/">FLUX.2-pro</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/kimi-k2-thinking/">Kimi-K2-Thinking</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/kimi-k2-5/">Kimi-K2.5</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Global, Provisioned</td>
      <td>Global Provisioned Managed, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/meta-llama-3-70b-instruct/">Meta-Llama-3-70B-Instruct</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/mistral-large-3/">Mistral-Large-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/cohere-command-a/">cohere-command-a</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/embed-v-4-0/">embed-v-4-0</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Global Standard, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-5-3-codex/">gpt-5.3-codex</a></td>
      <td>Global, Provisioned</td>
      <td>Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/grok-4-1-fast-non-reasoning/">grok-4.1-fast-non-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/grok-4-1-fast-reasoning/">grok-4.1-fast-reasoning</a></td>
      <td>Global</td>
      <td>Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/mistral-document-ai-2512/">mistral-document-ai-2512</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global coverage, Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Datazone, Global, Provisioned</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned global</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Datazone, Global, Provisioned, Standard</td>
      <td>Datazone provisioned managed, Datazone standard, Global Standard, Global batch, Global batch datazone, Global coverage, Provisioned (PTU managed), Provisioned global, Standard</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Datazone, Global</td>
      <td>Datazone standard, Global Standard, Global coverage</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Datazone, Global, Standard</td>
      <td>Datazone standard, Global Standard, Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/tts/">tts</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
    <tr>
      <td><strong>West US 3</strong></td>
      <td><a href="../models/tts-hd/">tts-hd</a></td>
      <td>Global, Standard</td>
      <td>Global coverage, Standard</td>
    </tr>
  </tbody>
</table>
</div>

---

_Last updated: 2026-03-26 14:34 UTC_
