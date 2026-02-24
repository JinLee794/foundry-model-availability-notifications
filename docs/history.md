# Change History

Recent changes to AI Foundry model regional availability.

<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-value">27</div>
    <div class="stat-label">Change Events</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" style="color: #22c55e;">1597</div>
    <div class="stat-label">Additions</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" style="color: #ef4444;">394</div>
    <div class="stat-label">Removals</div>
  </div>
</div>

---

## All Changes

Filter and search through all recent availability changes.

<div class="filter-controls">
  <div class="filter-group">
    <label for="history-date-filter">Date</label>
    <select id="history-date-filter" onchange="filterHistoryTable()">
      <option value="">All Dates</option>
      <option value="2026-02-18">2026-02-18</option>
      <option value="2026-02-12">2026-02-12</option>
      <option value="2026-02-06">2026-02-06</option>
      <option value="2026-01-31">2026-01-31</option>
      <option value="2026-01-28">2026-01-28</option>
      <option value="2026-01-22">2026-01-22</option>
      <option value="2026-01-15">2026-01-15</option>
      <option value="2026-01-08">2026-01-08</option>
      <option value="2026-01-07">2026-01-07</option>
      <option value="2025-12-17">2025-12-17</option>
      <option value="2025-12-12">2025-12-12</option>
      <option value="2025-12-09">2025-12-09</option>
      <option value="2025-12-06">2025-12-06</option>
      <option value="2025-12-04">2025-12-04</option>
      <option value="2025-12-02">2025-12-02</option>
      <option value="2025-11-20">2025-11-20</option>
    </select>
  </div>
  <div class="filter-group">
    <label for="history-type-filter">Change Type</label>
    <select id="history-type-filter" onchange="filterHistoryTable()">
      <option value="">All Changes</option>
      <option value="Added">Added</option>
      <option value="Removed">Removed</option>
    </select>
  </div>
  <div class="filter-group">
    <label for="history-model-filter">Model</label>
    <select id="history-model-filter" onchange="filterHistoryTable()">
      <option value="">All Models</option>
      <option value="Claude Haiku 4.5 (preview)">Claude Haiku 4.5 (preview)</option>
      <option value="Claude Opus 4.1 (preview)">Claude Opus 4.1 (preview)</option>
      <option value="Claude Opus 4.5 (preview)">Claude Opus 4.5 (preview)</option>
      <option value="Claude Opus 4.6 (preview)">Claude Opus 4.6 (preview)</option>
      <option value="Claude Sonnet 4.5 (preview)">Claude Sonnet 4.5 (preview)</option>
      <option value="Claude Sonnet 4.6 (preview)">Claude Sonnet 4.6 (preview)</option>
      <option value="Codestral-2501">Codestral-2501</option>
      <option value="Cohere Command R 08-2024">Cohere Command R 08-2024</option>
      <option value="Cohere Command R+ 08-2024">Cohere Command R+ 08-2024</option>
      <option value="Cohere Embed v3 - English">Cohere Embed v3 - English</option>
      <option value="Cohere Embed v3 - Multilingual">Cohere Embed v3 - Multilingual</option>
      <option value="Cohere Rerank v3.5">Cohere Rerank v3.5</option>
      <option value="DeepSeek-R1">DeepSeek-R1</option>
      <option value="DeepSeek-R1-0528">DeepSeek-R1-0528</option>
      <option value="DeepSeek-V3-0324">DeepSeek-V3-0324</option>
      <option value="DeepSeek-V3.1">DeepSeek-V3.1</option>
      <option value="FLUX-1.1-pro">FLUX-1.1-pro</option>
      <option value="FLUX.1-Kontext-pro">FLUX.1-Kontext-pro</option>
      <option value="Gretel-Navigator">Gretel-Navigator</option>
      <option value="JAIS 30B Chat">JAIS 30B Chat</option>
      <option value="Llama 3.1 405B Instruct">Llama 3.1 405B Instruct</option>
      <option value="Llama 3.1 8B Instruct">Llama 3.1 8B Instruct</option>
      <option value="Llama 3.3 70B Instruct">Llama 3.3 70B Instruct</option>
      <option value="Llama-3.2-11B-Vision-Instruct">Llama-3.2-11B-Vision-Instruct</option>
      <option value="Llama-3.2-1B">Llama-3.2-1B</option>
      <option value="Llama-3.2-1B-Instruct">Llama-3.2-1B-Instruct</option>
      <option value="Llama-3.2-3B">Llama-3.2-3B</option>
      <option value="Llama-3.2-3B-Instruct">Llama-3.2-3B-Instruct</option>
      <option value="Llama-3.2-90B-Vision-Instruct">Llama-3.2-90B-Vision-Instruct</option>
      <option value="Llama-3.3-70B-Instruct">Llama-3.3-70B-Instruct</option>
      <option value="Llama-4-Maverick-17B-128E-Instruct-FP8">Llama-4-Maverick-17B-128E-Instruct-FP8</option>
      <option value="Llama-Guard-3-11B-Vision">Llama-Guard-3-11B-Vision</option>
      <option value="Llama-Guard-3-1B">Llama-Guard-3-1B</option>
      <option value="MAI-DS-R1">MAI-DS-R1</option>
      <option value="Ministral-3B">Ministral-3B</option>
      <option value="Mistral Medium 3 (25.05)">Mistral Medium 3 (25.05)</option>
      <option value="Mistral Nemo">Mistral Nemo</option>
      <option value="Mistral OCR 25.03">Mistral OCR 25.03</option>
      <option value="Mistral Small 25.03">Mistral Small 25.03</option>
      <option value="Mistral-Large (2411)">Mistral-Large (2411)</option>
      <option value="Phi-4">Phi-4</option>
      <option value="Phi-4-mini-instruct">Phi-4-mini-instruct</option>
      <option value="Phi-4-mini-reasoning">Phi-4-mini-reasoning</option>
      <option value="Phi-4-multimodal-instruct">Phi-4-multimodal-instruct</option>
      <option value="Phi-4-reasoning">Phi-4-reasoning</option>
      <option value="Stable Diffusion 3.5 Large">Stable Diffusion 3.5 Large</option>
      <option value="Stable Image Core">Stable Image Core</option>
      <option value="Stable Image Ultra">Stable Image Ultra</option>
      <option value="TimeGEN-1">TimeGEN-1</option>
      <option value="codex-mini">codex-mini</option>
      <option value="computer-use-preview">computer-use-preview</option>
      <option value="gpt-35-turbo">gpt-35-turbo</option>
      <option value="gpt-35-turbo-instruct">gpt-35-turbo-instruct</option>
      <option value="gpt-4">gpt-4</option>
      <option value="gpt-4-32k">gpt-4-32k</option>
      <option value="gpt-4.1">gpt-4.1</option>
      <option value="gpt-4.1-mini">gpt-4.1-mini</option>
      <option value="gpt-4.1-nano">gpt-4.1-nano</option>
      <option value="gpt-4o">gpt-4o</option>
      <option value="gpt-4o-audio-preview">gpt-4o-audio-preview</option>
      <option value="gpt-4o-mini">gpt-4o-mini</option>
      <option value="gpt-4o-mini-audio-preview">gpt-4o-mini-audio-preview</option>
      <option value="gpt-4o-mini-realtime-preview">gpt-4o-mini-realtime-preview</option>
      <option value="gpt-4o-mini-tts">gpt-4o-mini-tts</option>
      <option value="gpt-4o-transcribe">gpt-4o-transcribe</option>
      <option value="gpt-4o-transcribe-diarize">gpt-4o-transcribe-diarize</option>
      <option value="gpt-5">gpt-5</option>
      <option value="gpt-5-chat">gpt-5-chat</option>
      <option value="gpt-5-codex">gpt-5-codex</option>
      <option value="gpt-5-mini">gpt-5-mini</option>
      <option value="gpt-5-nano">gpt-5-nano</option>
      <option value="gpt-5-pro">gpt-5-pro</option>
      <option value="gpt-5.1">gpt-5.1</option>
      <option value="gpt-5.1-chat">gpt-5.1-chat</option>
      <option value="gpt-5.1-codex">gpt-5.1-codex</option>
      <option value="gpt-5.1-codex-max">gpt-5.1-codex-max</option>
      <option value="gpt-5.1-codex-mini">gpt-5.1-codex-mini</option>
      <option value="gpt-5.2">gpt-5.2</option>
      <option value="gpt-5.2-chat">gpt-5.2-chat</option>
      <option value="gpt-5.2-codex">gpt-5.2-codex</option>
      <option value="gpt-audio">gpt-audio</option>
      <option value="gpt-audio-mini">gpt-audio-mini</option>
      <option value="gpt-image-1">gpt-image-1</option>
      <option value="gpt-image-1-mini">gpt-image-1-mini</option>
      <option value="gpt-image-1.5">gpt-image-1.5</option>
      <option value="gpt-realtime">gpt-realtime</option>
      <option value="gpt-realtime-mini">gpt-realtime-mini</option>
      <option value="grok-3">grok-3</option>
      <option value="grok-3-mini">grok-3-mini</option>
      <option value="grok-4">grok-4</option>
      <option value="grok-4-fast-non-reasoning">grok-4-fast-non-reasoning</option>
      <option value="grok-4-fast-reasoning">grok-4-fast-reasoning</option>
      <option value="grok-code-fast-1">grok-code-fast-1</option>
      <option value="mistral-document-ai-2505">mistral-document-ai-2505</option>
      <option value="model-router">model-router</option>
      <option value="o1">o1</option>
      <option value="o1-mini">o1-mini</option>
      <option value="o3">o3</option>
      <option value="o3-deep-research">o3-deep-research</option>
      <option value="o3-mini">o3-mini</option>
      <option value="o3-pro">o3-pro</option>
      <option value="o4-mini">o4-mini</option>
      <option value="sora-2">sora-2</option>
      <option value="text-embedding-3-large">text-embedding-3-large</option>
      <option value="text-embedding-3-small">text-embedding-3-small</option>
      <option value="text-embedding-ada-002">text-embedding-ada-002</option>
      <option value="tsuzumi-7b">tsuzumi-7b</option>
    </select>
  </div>
  <div class="filter-group">
    <label for="history-region-filter">Region</label>
    <select id="history-region-filter" onchange="filterHistoryTable()">
      <option value="">All Regions</option>
      <option value="Australia East">Australia East</option>
      <option value="Brazil South">Brazil South</option>
      <option value="Canada Central">Canada Central</option>
      <option value="Canada East">Canada East</option>
      <option value="Central India">Central India</option>
      <option value="Central US">Central US</option>
      <option value="East Asia">East Asia</option>
      <option value="East US">East US</option>
      <option value="East US 2">East US 2</option>
      <option value="France Central">France Central</option>
      <option value="Germany West Central">Germany West Central</option>
      <option value="Italy North">Italy North</option>
      <option value="Japan East">Japan East</option>
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
      <option value="West Europe">West Europe</option>
      <option value="West US">West US</option>
      <option value="West US 3">West US 3</option>
    </select>
  </div>
  <div class="filter-group">
    <label for="history-sku-filter">SKU Type</label>
    <select id="history-sku-filter" onchange="filterHistoryTable()">
      <option value="">All SKUs</option>
      <option value="Data Zone Standard">Data Zone Standard</option>
      <option value="Datazone provisioned managed">Datazone provisioned managed</option>
      <option value="Datazone standard">Datazone standard</option>
      <option value="Global Provisioned Managed">Global Provisioned Managed</option>
      <option value="Global Standard">Global Standard</option>
      <option value="Global batch">Global batch</option>
      <option value="Global batch datazone">Global batch datazone</option>
      <option value="Provisioned (PTU managed)">Provisioned (PTU managed)</option>
      <option value="Provisioned global">Provisioned global</option>
      <option value="Region Availability Maas">Region Availability Maas</option>
      <option value="Standard (all)">Standard (all)</option>
      <option value="Standard global deployments">Standard global deployments</option>
      <option value="Standard image generation">Standard image generation</option>
    </select>
  </div>
  <div class="filter-group">
    <label>&nbsp;</label>
    <button onclick="resetHistoryFilters()" class="md-button">Reset</button>
  </div>
</div>

<div class="table-responsive">
<table id="history-table" class="display">
  <thead>
    <tr>
      <th>Date</th>
      <th>Change</th>
      <th>Model</th>
      <th>Region</th>
      <th>SKU Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td data-order="20260218075112">2026-02-18</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/claude-sonnet-4-6-(preview)/">Claude Sonnet 4.6 (preview)</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260218075112">2026-02-18</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/claude-sonnet-4-6-(preview)/">Claude Sonnet 4.6 (preview)</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>France Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Germany West Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Italy North</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Poland Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Spain Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Sweden Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>West Europe</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>France Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Germany West Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Italy North</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Poland Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Spain Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Sweden Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>West Europe</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>France Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Germany West Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Italy North</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Poland Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Spain Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Sweden Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260212075326">2026-02-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>West Europe</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260206074806">2026-02-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/claude-opus-4-6-(preview)/">Claude Opus 4.6 (preview)</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260206074806">2026-02-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/claude-opus-4-6-(preview)/">Claude Opus 4.6 (preview)</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gretel-navigator/">Gretel-Navigator</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gretel-navigator/">Gretel-Navigator</a></td>
      <td>(entire model)</td>
      <td>-</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>(entire model)</td>
      <td>-</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>(entire model)</td>
      <td>-</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>(entire model)</td>
      <td>-</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260131073001">2026-01-31</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>(entire model)</td>
      <td>-</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>West US 3</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>West US 3</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>West US 3</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>West US 3</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>West US 3</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>West US 3</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Australia East</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Brazil South</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Canada East</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Central US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>East US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>East US 2</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>France Central</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Germany West Central</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Japan East</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Korea Central</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>North Central US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Norway East</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Poland Central</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>South Africa North</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>South Central US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>South India</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Sweden Central</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Switzerland North</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>UK South</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>West Europe</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>West US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>West US 3</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Central US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>East US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>East US 2</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>North Central US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>South Central US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>West US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>West US 3</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>West US 3</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>West US 3</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20260128072753">2026-01-28</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/codestral-2501/">Codestral-2501</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/codestral-2501/">Codestral-2501</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/codestral-2501/">Codestral-2501</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/codestral-2501/">Codestral-2501</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/codestral-2501/">Codestral-2501</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/codestral-2501/">Codestral-2501</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/codestral-2501/">Codestral-2501</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-command-r-08-2024/">Cohere Command R 08-2024</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-command-r-08-2024/">Cohere Command R 08-2024</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-command-r-08-2024/">Cohere Command R 08-2024</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-command-r-08-2024/">Cohere Command R 08-2024</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-command-r-08-2024/">Cohere Command R 08-2024</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-command-r-08-2024/">Cohere Command R 08-2024</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-command-r-08-2024/">Cohere Command R 08-2024</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-command-r+-08-2024/">Cohere Command R+ 08-2024</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-command-r+-08-2024/">Cohere Command R+ 08-2024</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-command-r+-08-2024/">Cohere Command R+ 08-2024</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-command-r+-08-2024/">Cohere Command R+ 08-2024</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-command-r+-08-2024/">Cohere Command R+ 08-2024</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-command-r+-08-2024/">Cohere Command R+ 08-2024</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-command-r+-08-2024/">Cohere Command R+ 08-2024</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-embed-v3---english/">Cohere Embed v3 - English</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-embed-v3---english/">Cohere Embed v3 - English</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-embed-v3---english/">Cohere Embed v3 - English</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-embed-v3---english/">Cohere Embed v3 - English</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-embed-v3---english/">Cohere Embed v3 - English</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-embed-v3---english/">Cohere Embed v3 - English</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-embed-v3---english/">Cohere Embed v3 - English</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-embed-v3---multilingual/">Cohere Embed v3 - Multilingual</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-embed-v3---multilingual/">Cohere Embed v3 - Multilingual</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-embed-v3---multilingual/">Cohere Embed v3 - Multilingual</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-embed-v3---multilingual/">Cohere Embed v3 - Multilingual</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-embed-v3---multilingual/">Cohere Embed v3 - Multilingual</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-embed-v3---multilingual/">Cohere Embed v3 - Multilingual</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-embed-v3---multilingual/">Cohere Embed v3 - Multilingual</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-rerank-v3-5/">Cohere Rerank v3.5</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-rerank-v3-5/">Cohere Rerank v3.5</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-rerank-v3-5/">Cohere Rerank v3.5</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-rerank-v3-5/">Cohere Rerank v3.5</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-rerank-v3-5/">Cohere Rerank v3.5</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-rerank-v3-5/">Cohere Rerank v3.5</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/cohere-rerank-v3-5/">Cohere Rerank v3.5</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gretel-navigator/">Gretel-Navigator</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/jais-30b-chat/">JAIS 30B Chat</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-1-405b-instruct/">Llama 3.1 405B Instruct</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-1-405b-instruct/">Llama 3.1 405B Instruct</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-1-405b-instruct/">Llama 3.1 405B Instruct</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-1-405b-instruct/">Llama 3.1 405B Instruct</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-1-405b-instruct/">Llama 3.1 405B Instruct</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-1-405b-instruct/">Llama 3.1 405B Instruct</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-1-8b-instruct/">Llama 3.1 8B Instruct</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-1-8b-instruct/">Llama 3.1 8B Instruct</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-1-8b-instruct/">Llama 3.1 8B Instruct</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-1-8b-instruct/">Llama 3.1 8B Instruct</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-1-8b-instruct/">Llama 3.1 8B Instruct</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-1-8b-instruct/">Llama 3.1 8B Instruct</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-1-8b-instruct/">Llama 3.1 8B Instruct</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama 3.3 70B Instruct</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama 3.3 70B Instruct</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama 3.3 70B Instruct</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama 3.3 70B Instruct</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama 3.3 70B Instruct</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama 3.3 70B Instruct</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama 3.3 70B Instruct</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-11b-vision-instruct/">Llama-3.2-11B-Vision-Instruct</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-11b-vision-instruct/">Llama-3.2-11B-Vision-Instruct</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-11b-vision-instruct/">Llama-3.2-11B-Vision-Instruct</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-11b-vision-instruct/">Llama-3.2-11B-Vision-Instruct</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-11b-vision-instruct/">Llama-3.2-11B-Vision-Instruct</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-11b-vision-instruct/">Llama-3.2-11B-Vision-Instruct</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-11b-vision-instruct/">Llama-3.2-11B-Vision-Instruct</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-1b/">Llama-3.2-1B</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-1b/">Llama-3.2-1B</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-1b/">Llama-3.2-1B</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-1b/">Llama-3.2-1B</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-1b/">Llama-3.2-1B</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-1b/">Llama-3.2-1B</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-1b/">Llama-3.2-1B</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-1b-instruct/">Llama-3.2-1B-Instruct</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-1b-instruct/">Llama-3.2-1B-Instruct</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-1b-instruct/">Llama-3.2-1B-Instruct</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-1b-instruct/">Llama-3.2-1B-Instruct</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-1b-instruct/">Llama-3.2-1B-Instruct</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-1b-instruct/">Llama-3.2-1B-Instruct</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-1b-instruct/">Llama-3.2-1B-Instruct</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-3b/">Llama-3.2-3B</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-3b/">Llama-3.2-3B</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-3b/">Llama-3.2-3B</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-3b/">Llama-3.2-3B</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-3b/">Llama-3.2-3B</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-3b/">Llama-3.2-3B</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-3b/">Llama-3.2-3B</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-3b-instruct/">Llama-3.2-3B-Instruct</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-3b-instruct/">Llama-3.2-3B-Instruct</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-3b-instruct/">Llama-3.2-3B-Instruct</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-3b-instruct/">Llama-3.2-3B-Instruct</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-3b-instruct/">Llama-3.2-3B-Instruct</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-3b-instruct/">Llama-3.2-3B-Instruct</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-3b-instruct/">Llama-3.2-3B-Instruct</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-90b-vision-instruct/">Llama-3.2-90B-Vision-Instruct</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-90b-vision-instruct/">Llama-3.2-90B-Vision-Instruct</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-90b-vision-instruct/">Llama-3.2-90B-Vision-Instruct</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-90b-vision-instruct/">Llama-3.2-90B-Vision-Instruct</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-90b-vision-instruct/">Llama-3.2-90B-Vision-Instruct</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-90b-vision-instruct/">Llama-3.2-90B-Vision-Instruct</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-2-90b-vision-instruct/">Llama-3.2-90B-Vision-Instruct</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-guard-3-11b-vision/">Llama-Guard-3-11B-Vision</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-guard-3-11b-vision/">Llama-Guard-3-11B-Vision</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-guard-3-11b-vision/">Llama-Guard-3-11B-Vision</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-guard-3-11b-vision/">Llama-Guard-3-11B-Vision</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-guard-3-11b-vision/">Llama-Guard-3-11B-Vision</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-guard-3-11b-vision/">Llama-Guard-3-11B-Vision</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-guard-3-11b-vision/">Llama-Guard-3-11B-Vision</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-guard-3-1b/">Llama-Guard-3-1B</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-guard-3-1b/">Llama-Guard-3-1B</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-guard-3-1b/">Llama-Guard-3-1B</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-guard-3-1b/">Llama-Guard-3-1B</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-guard-3-1b/">Llama-Guard-3-1B</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-guard-3-1b/">Llama-Guard-3-1B</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-guard-3-1b/">Llama-Guard-3-1B</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/ministral-3b/">Ministral-3B</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/ministral-3b/">Ministral-3B</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/ministral-3b/">Ministral-3B</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/ministral-3b/">Ministral-3B</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/ministral-3b/">Ministral-3B</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/ministral-3b/">Ministral-3B</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/ministral-3b/">Ministral-3B</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-medium-3-(25-05)/">Mistral Medium 3 (25.05)</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-medium-3-(25-05)/">Mistral Medium 3 (25.05)</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-medium-3-(25-05)/">Mistral Medium 3 (25.05)</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-medium-3-(25-05)/">Mistral Medium 3 (25.05)</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-medium-3-(25-05)/">Mistral Medium 3 (25.05)</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-medium-3-(25-05)/">Mistral Medium 3 (25.05)</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-medium-3-(25-05)/">Mistral Medium 3 (25.05)</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-nemo/">Mistral Nemo</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-ocr-25-03/">Mistral OCR 25.03</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-small-25-03/">Mistral Small 25.03</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-small-25-03/">Mistral Small 25.03</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-small-25-03/">Mistral Small 25.03</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-small-25-03/">Mistral Small 25.03</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-small-25-03/">Mistral Small 25.03</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-small-25-03/">Mistral Small 25.03</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-small-25-03/">Mistral Small 25.03</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-large-(2411)/">Mistral-Large (2411)</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4/">Phi-4</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4/">Phi-4</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4/">Phi-4</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4/">Phi-4</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4/">Phi-4</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4/">Phi-4</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4/">Phi-4</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-mini-instruct/">Phi-4-mini-instruct</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-mini-instruct/">Phi-4-mini-instruct</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-mini-instruct/">Phi-4-mini-instruct</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-mini-instruct/">Phi-4-mini-instruct</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-mini-instruct/">Phi-4-mini-instruct</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-mini-instruct/">Phi-4-mini-instruct</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-mini-instruct/">Phi-4-mini-instruct</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-mini-reasoning/">Phi-4-mini-reasoning</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-mini-reasoning/">Phi-4-mini-reasoning</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-mini-reasoning/">Phi-4-mini-reasoning</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-mini-reasoning/">Phi-4-mini-reasoning</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-mini-reasoning/">Phi-4-mini-reasoning</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-mini-reasoning/">Phi-4-mini-reasoning</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-multimodal-instruct/">Phi-4-multimodal-instruct</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-multimodal-instruct/">Phi-4-multimodal-instruct</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-multimodal-instruct/">Phi-4-multimodal-instruct</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-multimodal-instruct/">Phi-4-multimodal-instruct</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-multimodal-instruct/">Phi-4-multimodal-instruct</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-multimodal-instruct/">Phi-4-multimodal-instruct</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-multimodal-instruct/">Phi-4-multimodal-instruct</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-reasoning/">Phi-4-reasoning</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-reasoning/">Phi-4-reasoning</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-reasoning/">Phi-4-reasoning</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-reasoning/">Phi-4-reasoning</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-reasoning/">Phi-4-reasoning</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/phi-4-reasoning/">Phi-4-reasoning</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-diffusion-3-5-large/">Stable Diffusion 3.5 Large</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-diffusion-3-5-large/">Stable Diffusion 3.5 Large</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-diffusion-3-5-large/">Stable Diffusion 3.5 Large</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-diffusion-3-5-large/">Stable Diffusion 3.5 Large</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-diffusion-3-5-large/">Stable Diffusion 3.5 Large</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-diffusion-3-5-large/">Stable Diffusion 3.5 Large</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-image-core/">Stable Image Core</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-image-core/">Stable Image Core</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-image-core/">Stable Image Core</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-image-core/">Stable Image Core</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-image-core/">Stable Image Core</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-image-core/">Stable Image Core</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-image-ultra/">Stable Image Ultra</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-image-ultra/">Stable Image Ultra</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-image-ultra/">Stable Image Ultra</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-image-ultra/">Stable Image Ultra</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-image-ultra/">Stable Image Ultra</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/stable-image-ultra/">Stable Image Ultra</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/timegen-1/">TimeGEN-1</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/timegen-1/">TimeGEN-1</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/timegen-1/">TimeGEN-1</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/timegen-1/">TimeGEN-1</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/timegen-1/">TimeGEN-1</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/timegen-1/">TimeGEN-1</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/timegen-1/">TimeGEN-1</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/tsuzumi-7b/">tsuzumi-7b</a></td>
      <td>East US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/tsuzumi-7b/">tsuzumi-7b</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/tsuzumi-7b/">tsuzumi-7b</a></td>
      <td>North Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/tsuzumi-7b/">tsuzumi-7b</a></td>
      <td>South Central US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/tsuzumi-7b/">tsuzumi-7b</a></td>
      <td>West US</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122215954">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/tsuzumi-7b/">tsuzumi-7b</a></td>
      <td>West US 3</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122214959">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/claude-haiku-4-5-(preview)/">Claude Haiku 4.5 (preview)</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122214959">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/claude-haiku-4-5-(preview)/">Claude Haiku 4.5 (preview)</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122214959">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/claude-opus-4-1-(preview)/">Claude Opus 4.1 (preview)</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122214959">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/claude-opus-4-1-(preview)/">Claude Opus 4.1 (preview)</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122214959">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/claude-opus-4-5-(preview)/">Claude Opus 4.5 (preview)</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122214959">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/claude-opus-4-5-(preview)/">Claude Opus 4.5 (preview)</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122214959">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/claude-sonnet-4-5-(preview)/">Claude Sonnet 4.5 (preview)</a></td>
      <td>East US 2</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122214959">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/claude-sonnet-4-5-(preview)/">Claude Sonnet 4.5 (preview)</a></td>
      <td>Sweden Central</td>
      <td>Region Availability Maas</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Australia East</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Brazil South</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Canada East</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>East US</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>East US 2</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>France Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Germany West Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Italy North</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Japan East</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Korea Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>North Central US</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Norway East</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Poland Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>South Africa North</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>South Central US</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>South India</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Spain Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Sweden Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Switzerland North</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Switzerland West</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>UAE North</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>UK South</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>West Europe</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>West US</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>West US 3</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Australia East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Brazil South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Canada East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>East US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>East US 2</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>France Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Germany West Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Italy North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Japan East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Korea Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>North Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Norway East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Poland Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>South Africa North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>South Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>South India</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Spain Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Sweden Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Switzerland North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>Switzerland West</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>UAE North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>UK South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>West Europe</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>West US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1/">DeepSeek-R1</a></td>
      <td>West US 3</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Australia East</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Brazil South</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Canada East</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>East US</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>East US 2</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>France Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Germany West Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Italy North</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Japan East</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Korea Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>North Central US</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Norway East</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Poland Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>South Africa North</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>South Central US</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>South India</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Spain Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Sweden Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Switzerland North</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Switzerland West</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>UAE North</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>UK South</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>West Europe</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>West US</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>West US 3</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Australia East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Brazil South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Canada East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>East US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>East US 2</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>France Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Germany West Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Italy North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Japan East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Korea Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>North Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Norway East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Poland Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>South Africa North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>South Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>South India</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Spain Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Sweden Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Switzerland North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>Switzerland West</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>UAE North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>UK South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>West Europe</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>West US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-r1-0528/">DeepSeek-R1-0528</a></td>
      <td>West US 3</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Australia East</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Brazil South</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Canada East</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>East US</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>East US 2</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>France Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Germany West Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Italy North</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Japan East</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Korea Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>North Central US</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Norway East</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Poland Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>South Africa North</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>South Central US</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>South India</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Spain Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Sweden Central</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Switzerland North</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Switzerland West</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>UAE North</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>UK South</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>West Europe</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>West US</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>West US 3</td>
      <td>Global Provisioned Managed</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Australia East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Brazil South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Canada East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>East US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>East US 2</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>France Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Germany West Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Italy North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Japan East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Korea Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>North Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Norway East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Poland Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>South Africa North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>South Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>South India</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Spain Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Sweden Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Switzerland North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>Switzerland West</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>UAE North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>UK South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>West Europe</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>West US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-0324/">DeepSeek-V3-0324</a></td>
      <td>West US 3</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Australia East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Brazil South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Canada East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>East US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>East US 2</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>France Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Germany West Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Italy North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Japan East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Korea Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>North Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Norway East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Poland Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>South Africa North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>South Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>South India</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Spain Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Sweden Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Switzerland North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>Switzerland West</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>UAE North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>UK South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>West Europe</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>West US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/deepseek-v3-1/">DeepSeek-V3.1</a></td>
      <td>West US 3</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Australia East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Brazil South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Canada East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>East US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>East US 2</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>France Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Germany West Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Italy North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Japan East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Korea Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>North Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Norway East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Poland Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>South Africa North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>South Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>South India</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Spain Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Sweden Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Switzerland North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>Switzerland West</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>UAE North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>UK South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>West Europe</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>West US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-1-pro/">FLUX-1.1-pro</a></td>
      <td>West US 3</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Australia East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Brazil South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Canada East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>East US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>East US 2</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>France Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Germany West Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Italy North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Japan East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Korea Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>North Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Norway East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Poland Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>South Africa North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>South Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>South India</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Spain Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Sweden Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Switzerland North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>Switzerland West</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>UAE North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>UK South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>West Europe</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>West US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/flux-1-kontext-pro/">FLUX.1-Kontext-pro</a></td>
      <td>West US 3</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Australia East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Brazil South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Canada East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>East US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>East US 2</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>France Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Germany West Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Italy North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Japan East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Korea Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>North Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Norway East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Poland Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>South Africa North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>South Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>South India</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Spain Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Sweden Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Switzerland North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>Switzerland West</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>UAE North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>UK South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>West Europe</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>West US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-3-3-70b-instruct/">Llama-3.3-70B-Instruct</a></td>
      <td>West US 3</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Australia East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Brazil South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Canada East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>East US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>East US 2</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>France Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Germany West Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Italy North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Japan East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Korea Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>North Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Norway East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Poland Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>South Africa North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>South Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>South India</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Spain Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Sweden Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Switzerland North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>Switzerland West</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>UAE North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>UK South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>West Europe</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>West US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/llama-4-maverick-17b-128e-instruct-fp8/">Llama-4-Maverick-17B-128E-Instruct-FP8</a></td>
      <td>West US 3</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Australia East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Brazil South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Canada East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>East US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>East US 2</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>France Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Germany West Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Italy North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Japan East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Korea Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>North Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Norway East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Poland Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>South Africa North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>South Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>South India</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Spain Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Sweden Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Switzerland North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>Switzerland West</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>UAE North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>UK South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>West Europe</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>West US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mai-ds-r1/">MAI-DS-R1</a></td>
      <td>West US 3</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>East US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>East US 2</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>North Central US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>South Central US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>West US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>West US 3</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Australia East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Brazil South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Canada East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>East US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>East US 2</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>France Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Germany West Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Italy North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Japan East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Korea Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>North Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Norway East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Poland Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>South Africa North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>South Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>South India</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Spain Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Sweden Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Switzerland North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>Switzerland West</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>UAE North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>UK South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>West Europe</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>West US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3/">grok-3</a></td>
      <td>West US 3</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>East US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>East US 2</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>North Central US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>South Central US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>West US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>West US 3</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Australia East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Brazil South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Canada East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>East US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>East US 2</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>France Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Germany West Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Italy North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Japan East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Korea Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>North Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Norway East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Poland Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>South Africa North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>South Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>South India</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Spain Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Sweden Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Switzerland North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>Switzerland West</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>UAE North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>UK South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>West Europe</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>West US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-3-mini/">grok-3-mini</a></td>
      <td>West US 3</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Australia East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Brazil South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Canada East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>East US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>East US 2</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>France Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Germany West Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Italy North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Japan East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Korea Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>North Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Norway East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Poland Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>South Africa North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>South Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>South India</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Spain Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Sweden Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Switzerland North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>Switzerland West</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>UAE North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>UK South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>West Europe</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>West US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4/">grok-4</a></td>
      <td>West US 3</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>East US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>East US 2</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>North Central US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>South Central US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>West US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>West US 3</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Australia East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Brazil South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Canada East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>East US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>East US 2</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>France Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Germany West Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Italy North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Japan East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Korea Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>North Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Norway East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Poland Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>South Africa North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>South Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>South India</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Spain Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Sweden Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Switzerland North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>Switzerland West</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>UAE North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>UK South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>West Europe</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>West US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-non-reasoning/">grok-4-fast-non-reasoning</a></td>
      <td>West US 3</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>East US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>East US 2</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>North Central US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>South Central US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>West US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>West US 3</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Australia East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Brazil South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Canada East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>East US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>East US 2</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>France Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Germany West Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Italy North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Japan East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Korea Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>North Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Norway East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Poland Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>South Africa North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>South Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>South India</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Spain Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Sweden Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Switzerland North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>Switzerland West</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>UAE North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>UK South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>West Europe</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>West US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-4-fast-reasoning/">grok-4-fast-reasoning</a></td>
      <td>West US 3</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Australia East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Brazil South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Canada East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>East US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>East US 2</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>France Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Germany West Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Italy North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Japan East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Korea Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>North Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Norway East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Poland Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>South Africa North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>South Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>South India</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Spain Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Sweden Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Switzerland North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>Switzerland West</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>UAE North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>UK South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>West Europe</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>West US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/grok-code-fast-1/">grok-code-fast-1</a></td>
      <td>West US 3</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>East US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>East US 2</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>France Central</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Germany West Central</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Italy North</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>North Central US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Norway East</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Poland Central</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>South Central US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Spain Central</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Sweden Central</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Switzerland North</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Switzerland West</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>West Europe</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>West US</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>West US 3</td>
      <td>Data Zone Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Australia East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Brazil South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Canada East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>East US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>East US 2</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>France Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Germany West Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Italy North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Japan East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Korea Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>North Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Norway East</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Poland Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>South Africa North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>South Central US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>South India</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Spain Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Sweden Central</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Switzerland North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>Switzerland West</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>UAE North</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>UK South</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>West Europe</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>West US</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260122211948">2026-01-22</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/mistral-document-ai-2505/">mistral-document-ai-2505</a></td>
      <td>West US 3</td>
      <td>Global Standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Australia East</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Canada East</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>East US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>East US 2</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>France Central</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Japan East</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>North Central US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>South Central US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>South India</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Sweden Central</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Switzerland North</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>UK South</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>West Europe</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>West US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>West US 3</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo-instruct/">gpt-35-turbo-instruct</a></td>
      <td>East US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-35-turbo-instruct/">gpt-35-turbo-instruct</a></td>
      <td>Sweden Central</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>East US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>East US 2</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>North Central US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>South Central US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Sweden Central</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>West US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>West US 3</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>East US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>East US 2</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>North Central US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>South Central US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Sweden Central</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Switzerland North</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>West US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>West US 3</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Australia East</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Canada East</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>East US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>East US 2</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>France Central</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Japan East</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>North Central US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>South Central US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>South India</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Sweden Central</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Switzerland North</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>UK South</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>West Europe</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>West US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>West US 3</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>North Central US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Sweden Central</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Central US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>East US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>East US 2</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>North Central US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>South Central US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Sweden Central</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>West US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>West US 3</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>East US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>East US 2</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>North Central US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>South Central US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Sweden Central</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>West US</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>West US 3</td>
      <td>Standard (all)</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>East US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>East US 2</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>North Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>South Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>West US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>West US 3</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>East US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>East US 2</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>North Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>South Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>West US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>West US 3</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>East US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>East US 2</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>North Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>South Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>West US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115131040">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>West US 3</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260115065343">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260115065343">2026-01-15</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-2-codex/">gpt-5.2-codex</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-audio-preview/">gpt-4o-audio-preview</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-transcribe-diarize/">gpt-4o-transcribe-diarize</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>East US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>France Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Australia East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Canada East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Australia East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Canada East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Australia East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Canada East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-max/">gpt-5.1-codex-max</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-max/">gpt-5.1-codex-max</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Australia East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Canada East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>East US 2</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-audio/">gpt-audio</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-audio/">gpt-audio</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-audio/">gpt-audio</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>East US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-deep-research/">o3-deep-research</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-deep-research/">o3-deep-research</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260108065336">2026-01-08</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260107185245">2026-01-07</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o-mini-tts/">gpt-4o-mini-tts</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20260107022954">2026-01-07</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>East US 2</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20260107022954">2026-01-07</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>UK South</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251217065223">2025-12-17</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>UAE North</td>
      <td>Standard image generation</td>
    </tr>
    <tr>
      <td data-order="20251217065223">2025-12-17</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>East US 2</td>
      <td>Standard image generation</td>
    </tr>
    <tr>
      <td data-order="20251217065223">2025-12-17</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>Poland Central</td>
      <td>Standard image generation</td>
    </tr>
    <tr>
      <td data-order="20251217065223">2025-12-17</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>Sweden Central</td>
      <td>Standard image generation</td>
    </tr>
    <tr>
      <td data-order="20251217065223">2025-12-17</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>UAE North</td>
      <td>Standard image generation</td>
    </tr>
    <tr>
      <td data-order="20251217065223">2025-12-17</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1-5/">gpt-image-1.5</a></td>
      <td>West US 3</td>
      <td>Standard image generation</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o-audio-preview/">gpt-4o-audio-preview</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini-tts/">gpt-4o-mini-tts</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o-transcribe-diarize/">gpt-4o-transcribe-diarize</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-2/">gpt-5.2</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-2-chat/">gpt-5.2-chat</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-2-chat/">gpt-5.2-chat</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-audio/">gpt-audio</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-audio/">gpt-audio</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-audio/">gpt-audio</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/model-router/">model-router</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-deep-research/">o3-deep-research</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-deep-research/">o3-deep-research</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-deep-research/">o3-deep-research</a></td>
      <td>(entire model)</td>
      <td>-</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251212022526">2025-12-12</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251209022128">2025-12-09</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251209022128">2025-12-09</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251209022128">2025-12-09</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251209022128">2025-12-09</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251209022128">2025-12-09</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251209022128">2025-12-09</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251209022128">2025-12-09</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251209022128">2025-12-09</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251209022128">2025-12-09</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>West Europe</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251209022128">2025-12-09</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251209022128">2025-12-09</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>West Europe</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251209022128">2025-12-09</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251209022128">2025-12-09</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251209022128">2025-12-09</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251209022128">2025-12-09</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>East US</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>East US 2</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>France Central</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Germany West Central</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Italy North</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>North Central US</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Poland Central</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>South Central US</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Spain Central</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Sweden Central</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>West Europe</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>West US</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Australia East</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Brazil South</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Canada Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Canada East</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>East US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>East US 2</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>France Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Germany West Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Italy North</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Japan East</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Korea Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>North Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Norway East</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Poland Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>South Africa North</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>South Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>South India</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Southeast Asia</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Spain Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Sweden Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Switzerland North</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Switzerland West</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>UAE North</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>UK South</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>West Europe</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>West US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>West US 3</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>East US 2</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Australia East</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Canada East</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>East US 2</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Japan East</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Korea Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Switzerland North</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251206021517">2025-12-06</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>UK South</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/codex-mini/">codex-mini</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Australia East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Brazil South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Canada East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>East US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>France Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Germany West Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Italy North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/computer-use-preview/">computer-use-preview</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Australia East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Brazil South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Canada East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>East US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>France Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Germany West Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Italy North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>West US 3</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Canada Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>East US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>West US 3</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Australia East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Brazil South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Canada Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Canada East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>East US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>France Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Germany West Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Italy North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>West US 3</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Australia East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Brazil South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Canada Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Canada East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>France Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Germany West Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Italy North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>West US 3</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Canada Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>West US 3</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Canada Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Italy North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Switzerland West</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini-audio-preview/">gpt-4o-mini-audio-preview</a></td>
      <td>East US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o-mini-audio-preview/">gpt-4o-mini-audio-preview</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini-realtime-preview/">gpt-4o-mini-realtime-preview</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o-mini-realtime-preview/">gpt-4o-mini-realtime-preview</a></td>
      <td>East US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o-mini-tts/">gpt-4o-mini-tts</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-transcribe/">gpt-4o-transcribe</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-transcribe-diarize/">gpt-4o-transcribe-diarize</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-transcribe-diarize/">gpt-4o-transcribe-diarize</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>France Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Germany West Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Italy North</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>North Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Poland Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>South Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Spain Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>West Europe</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>West US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>West US 3</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Brazil South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>France Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Germany West Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Italy North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-chat/">gpt-5-chat</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-codex/">gpt-5-codex</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>France Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Germany West Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Italy North</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>North Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Poland Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>South Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Spain Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>West Europe</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>West US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>West US 3</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Brazil South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Canada East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>France Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Germany West Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Italy North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>East US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>France Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Germany West Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Italy North</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>North Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Poland Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>South Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Spain Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>West Europe</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>West US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>West US 3</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Australia East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Brazil South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Canada East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>East US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>France Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Germany West Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Italy North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-nano/">gpt-5-nano</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-pro/">gpt-5-pro</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>East US 2</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Sweden Central</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1/">gpt-5.1</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-chat/">gpt-5.1-chat</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex/">gpt-5.1-codex</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-1-codex-mini/">gpt-5.1-codex-mini</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-audio/">gpt-audio</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-audio-mini/">gpt-audio-mini</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-audio-mini/">gpt-audio-mini</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-audio-mini/">gpt-audio-mini</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1/">gpt-image-1</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>East US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-image-1-mini/">gpt-image-1-mini</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-realtime-mini/">gpt-realtime-mini</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-realtime-mini/">gpt-realtime-mini</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-realtime-mini/">gpt-realtime-mini</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>West US 3</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Australia East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Brazil South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Canada East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>France Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Germany West Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Italy North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Australia East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Brazil South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Canada East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>France Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Germany West Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1-mini/">o1-mini</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>West US 3</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-deep-research/">o3-deep-research</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-deep-research/">o3-deep-research</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>West US 3</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-pro/">o3-pro</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Central US</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>West US 3</td>
      <td>Datazone standard</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Southeast Asia</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/sora-2/">sora-2</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/sora-2/">sora-2</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-3-large/">text-embedding-3-large</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/text-embedding-3-small/">text-embedding-3-small</a></td>
      <td>West US 3</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Australia East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Brazil South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Canada East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>East US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>France Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Germany West Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Italy North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Japan East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Korea Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>North Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Poland Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>South Africa North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>South Central US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>South India</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Spain Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>Switzerland North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>UAE North</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>UK South</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>West Europe</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251204022139">2025-12-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/text-embedding-ada-002/">text-embedding-ada-002</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Central US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Central US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Central US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Central US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Central US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Central US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Central US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Central US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Central US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Central US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Central US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Central US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Central US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Central US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Central US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Central US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Central US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Central US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251202185131">2025-12-02</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Canada Central</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-35-turbo/">gpt-35-turbo</a></td>
      <td>Central US</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Canada Central</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Canada Central</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Central US</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Canada Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Central India</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>East Asia</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>North Europe</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Brazil South</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Central US</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>South India</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>Switzerland North</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Canada Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Central India</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>East Asia</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>North Europe</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>Brazil South</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>South India</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Canada Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>Central India</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>East Asia</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>North Europe</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Canada Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Central India</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>East Asia</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>North Europe</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Canada Central</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Central US</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>Switzerland West</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Canada Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Central India</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>East Asia</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>North Europe</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Canada Central</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>Switzerland West</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>France Central</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Germany West Central</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Italy North</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Poland Central</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Spain Central</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Sweden Central</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>West Europe</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Canada Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Central India</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>East Asia</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>North Europe</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Canada East</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Japan East</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>South India</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>East US</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>East US 2</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>France Central</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Germany West Central</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Italy North</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>North Central US</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Poland Central</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>South Central US</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Spain Central</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Sweden Central</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>West Europe</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>West US</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Australia East</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Brazil South</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Canada Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Canada East</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>East US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>East US 2</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>France Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Germany West Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Italy North</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Japan East</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Korea Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>North Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Norway East</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Poland Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>South Africa North</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>South Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>South India</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Southeast Asia</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Spain Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Sweden Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Switzerland North</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>Switzerland West</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>UAE North</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>UK South</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>West Europe</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>West US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>West US 3</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5-mini/">gpt-5-mini</a></td>
      <td>East US 2</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Canada Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>Central India</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>East Asia</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o1/">o1</a></td>
      <td>North Europe</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Canada Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>Central India</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>East Asia</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>North Europe</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Canada Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>Central India</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>East Asia</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>North Europe</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>South Central US</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>South India</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>West US 3</td>
      <td>Datazone provisioned managed</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Canada Central</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Central US</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Central India</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>East Asia</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>North Europe</td>
      <td>Provisioned global</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Central US</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251120064715">2025-11-20</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>Japan East</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
  </tbody>
</table>
</div>

---

_Last updated: 2026-02-24 14:58 UTC_
