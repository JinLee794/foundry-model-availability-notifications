# Change History

Recent changes to AI Foundry model regional availability.

<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-value">17</div>
    <div class="stat-label">Change Events</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" style="color: #22c55e;">736</div>
    <div class="stat-label">Additions</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" style="color: #ef4444;">331</div>
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
      <option value="2026-01-08">2026-01-08</option>
      <option value="2026-01-07">2026-01-07</option>
      <option value="2025-12-17">2025-12-17</option>
      <option value="2025-12-12">2025-12-12</option>
      <option value="2025-12-09">2025-12-09</option>
      <option value="2025-12-06">2025-12-06</option>
      <option value="2025-12-04">2025-12-04</option>
      <option value="2025-12-02">2025-12-02</option>
      <option value="2025-11-20">2025-11-20</option>
      <option value="2025-11-07">2025-11-07</option>
      <option value="2025-11-04">2025-11-04</option>
      <option value="2025-10-31">2025-10-31</option>
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
      <option value="codex-mini">codex-mini</option>
      <option value="computer-use-preview">computer-use-preview</option>
      <option value="gpt-35-turbo">gpt-35-turbo</option>
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
      <option value="gpt-audio">gpt-audio</option>
      <option value="gpt-audio-mini">gpt-audio-mini</option>
      <option value="gpt-image-1">gpt-image-1</option>
      <option value="gpt-image-1-mini">gpt-image-1-mini</option>
      <option value="gpt-image-1.5">gpt-image-1.5</option>
      <option value="gpt-realtime">gpt-realtime</option>
      <option value="gpt-realtime-mini">gpt-realtime-mini</option>
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
      <option value="Datazone provisioned managed">Datazone provisioned managed</option>
      <option value="Datazone standard">Datazone standard</option>
      <option value="Global batch">Global batch</option>
      <option value="Global batch datazone">Global batch datazone</option>
      <option value="Provisioned (PTU managed)">Provisioned (PTU managed)</option>
      <option value="Provisioned global">Provisioned global</option>
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
    <tr>
      <td data-order="20251107021555">2025-11-07</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>East US 2</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251107021555">2025-11-07</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>Sweden Central</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251107021555">2025-11-07</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>Norway East</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251107021555">2025-11-07</td>
      <td><span class="badge-removed">Removed</span></td>
      <td><a href="../models/gpt-realtime/">gpt-realtime</a></td>
      <td>West US</td>
      <td>Standard global deployments</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1/">gpt-4.1</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-mini/">gpt-4.1-mini</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-1-nano/">gpt-4.1-nano</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o/">gpt-4o</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4o-mini/">gpt-4o-mini</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Australia East</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Brazil South</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Canada East</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>East US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>East US 2</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>France Central</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Germany West Central</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Japan East</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Korea Central</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>North Central US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Norway East</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Poland Central</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>South Africa North</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>South Central US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>South India</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Sweden Central</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>Switzerland North</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>UK South</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>West Europe</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>West US</td>
      <td>Global batch</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>East US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>East US 2</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>North Central US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>South Central US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>West US</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-5/">gpt-5</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3/">o3</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o3-mini/">o3-mini</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251104064836">2025-11-04</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/o4-mini/">o4-mini</a></td>
      <td>West US 3</td>
      <td>Global batch datazone</td>
    </tr>
    <tr>
      <td data-order="20251031181625">2025-10-31</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>France Central</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251031181625">2025-10-31</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Germany West Central</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251031181625">2025-10-31</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4-32k/">gpt-4-32k</a></td>
      <td>Korea Central</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251031175611">2025-10-31</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Norway East</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251031175611">2025-10-31</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Poland Central</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251031175611">2025-10-31</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>South Africa North</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251031175303">2025-10-31</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>South Central US</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251031175303">2025-10-31</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>South India</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251031174959">2025-10-31</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>UK South</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251031174959">2025-10-31</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>West US</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251031164951">2025-10-31</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>Poland Central</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251031164951">2025-10-31</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>South Africa North</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
    <tr>
      <td data-order="20251031164951">2025-10-31</td>
      <td><span class="badge-added">Added</span></td>
      <td><a href="../models/gpt-4/">gpt-4</a></td>
      <td>South Central US</td>
      <td>Provisioned (PTU managed)</td>
    </tr>
  </tbody>
</table>
</div>

---

_Last updated: 2026-01-13 21:07 UTC_
