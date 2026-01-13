#!/usr/bin/env python3
"""Generate MkDocs pages from AI Foundry model availability snapshot data."""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Set, Tuple

HERE = Path(__file__).resolve().parent
REGION_WATCH_DIR = HERE / ".region-watch"
SNAPSHOT_PATH = REGION_WATCH_DIR / "regions_snapshot.json"
HISTORY_DIR = REGION_WATCH_DIR / "history"
DOCS_DIR = HERE / "docs"

DEFAULT_LABEL = "Global coverage"

# Coverage buckets
BUCKETS: List[Tuple[int, str, str, str]] = [
    (25, "🟢 Broad", "badge-broad", "25+ regions"),
    (20, "🟡 Strong", "badge-strong", "20-24 regions"),
    (15, "🟠 Growing", "badge-growing", "15-19 regions"),
    (0, "🔴 Emerging", "badge-emerging", "Under 15 regions"),
]

# SKU category mapping with descriptions
SKU_CATEGORIES = {
    "Global": {
        "skus": ["Global coverage", "Global batch", "Global batch datazone", "Standard global deployments"],
        "description": "Worldwide availability with intelligent routing",
        "use_case": "Best for applications needing global reach with automatic failover",
    },
    "Datazone": {
        "skus": ["Datazone standard", "Datazone provisioned managed"],
        "description": "Data residency compliance deployments",
        "use_case": "Required for data sovereignty and compliance requirements (GDPR, etc.)",
    },
    "Standard": {
        "skus": ["Standard (all)", "Standard GPT-3.5 Turbo", "Standard GPT-4", "Standard audio", 
                 "Standard chat completions", "Standard completions", "Standard embeddings",
                 "Standard image generation"],
        "description": "Pay-as-you-go regional deployments",
        "use_case": "Best for variable workloads and cost-sensitive applications",
    },
    "Provisioned": {
        "skus": ["Provisioned (PTU managed)", "Provisioned global"],
        "description": "Reserved throughput capacity (PTU)",
        "use_case": "Best for predictable, high-volume production workloads",
    },
}


def get_sku_category(label: str) -> str:
    """Return the category for a SKU label."""
    for category, info in SKU_CATEGORIES.items():
        if label in info["skus"]:
            return category
    return "Other"


def load_snapshot(path: Path) -> Dict[str, dict]:
    """Load a JSON snapshot from disk."""
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def load_history(path: Path) -> List[Dict]:
    """Return a list of history entries with parsed changes."""
    entries = []
    if not path.exists():
        return entries

    for diff_path in sorted(path.glob("diff-*.json"), reverse=True):
        try:
            payload = json.loads(diff_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue

        timestamp_raw = payload.get("timestamp")
        changes = payload.get("changes", {})
        if not timestamp_raw or not changes:
            continue

        try:
            timestamp = datetime.fromisoformat(timestamp_raw)
        except ValueError:
            continue

        if timestamp.tzinfo is None:
            timestamp = timestamp.replace(tzinfo=timezone.utc)
        else:
            timestamp = timestamp.astimezone(timezone.utc)

        entries.append({
            "timestamp": timestamp,
            "changes": changes
        })

    return entries


def build_model_index(data: Dict[str, dict]) -> Tuple[
    Dict[str, Set[str]],
    Dict[str, Dict[str, Set[str]]],
    Dict[str, Dict[str, Set[str]]],
    Set[str],
    Set[str],
]:
    """Build model-centric data structures.
    
    Returns:
        model_regions: model -> set of all regions
        model_region_skus: model -> region -> set of SKU labels
        model_sku_regions: model -> SKU label -> set of regions
        all_labels: all SKU labels
        all_regions: all regions
    """
    model_regions: Dict[str, Set[str]] = defaultdict(set)
    model_region_skus: Dict[str, Dict[str, Set[str]]] = defaultdict(lambda: defaultdict(set))
    model_sku_regions: Dict[str, Dict[str, Set[str]]] = defaultdict(lambda: defaultdict(set))
    all_labels: Set[str] = set()
    all_regions: Set[str] = set()

    for model, payload in data.items():
        for region in payload.get("all", []):
            model_regions[model].add(region)
            model_region_skus[model][region].add(DEFAULT_LABEL)
            model_sku_regions[model][DEFAULT_LABEL].add(region)
            all_labels.add(DEFAULT_LABEL)
            all_regions.add(region)

        for sku_name, sku in payload.get("skus", {}).items():
            label = sku.get("label") or sku_name
            all_labels.add(label)
            for region in sku.get("regions", []):
                model_regions[model].add(region)
                model_region_skus[model][region].add(label)
                model_sku_regions[model][label].add(region)
                all_regions.add(region)

    return model_regions, model_region_skus, model_sku_regions, all_labels, all_regions


def pick_bucket(count: int) -> Tuple[str, str, str]:
    """Return (emoji_label, css_class, description) for coverage bucket."""
    for threshold, label, css_class, desc in BUCKETS:
        if count >= threshold:
            return label, css_class, desc
    return BUCKETS[-1][1], BUCKETS[-1][2], BUCKETS[-1][3]


def slugify(name: str) -> str:
    """Convert model name to URL-safe slug."""
    return name.lower().replace(" ", "-").replace(".", "-")


def generate_index_page(
    model_regions: Dict[str, Set[str]],
    model_sku_regions: Dict[str, Dict[str, Set[str]]],
    all_labels: Set[str],
    all_regions: Set[str],
) -> str:
    """Generate the index/home page with actionable insights."""
    total_models = len(model_regions)
    total_regions = len(all_regions)
    
    # Count models by coverage
    coverage_counts = {"Broad": 0, "Strong": 0, "Growing": 0, "Emerging": 0}
    for regions in model_regions.values():
        bucket, _, _ = pick_bucket(len(regions))
        if "Broad" in bucket:
            coverage_counts["Broad"] += 1
        elif "Strong" in bucket:
            coverage_counts["Strong"] += 1
        elif "Growing" in bucket:
            coverage_counts["Growing"] += 1
        else:
            coverage_counts["Emerging"] += 1

    # Find best models per category
    best_global = []
    best_provisioned = []
    for model, sku_regions in model_sku_regions.items():
        for sku, regions in sku_regions.items():
            if "Global" in sku or "global" in sku:
                best_global.append((model, len(regions)))
            if "Provisioned" in sku:
                best_provisioned.append((model, len(regions)))
    
    best_global = sorted(set(best_global), key=lambda x: -x[1])[:5]
    best_provisioned = sorted(set(best_provisioned), key=lambda x: -x[1])[:5]

    # Top regions by model coverage
    region_model_count = defaultdict(int)
    for model, regions in model_regions.items():
        for region in regions:
            region_model_count[region] += 1
    top_regions = sorted(region_model_count.items(), key=lambda x: -x[1])[:10]

    return f"""# AI Foundry Model Availability

Real-time tracking of Azure AI Foundry model availability across regions and deployment types.

<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-value">{total_models}</div>
    <div class="stat-label">Models Tracked</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{total_regions}</div>
    <div class="stat-label">Azure Regions</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{coverage_counts["Broad"]}</div>
    <div class="stat-label">Broadly Available</div>
  </div>
</div>

---

## 🎯 Quick Actions

### Need Global Availability?
These models have the widest global deployment options:

| Model | Global Regions | Details |
|-------|----------------|---------|
{chr(10).join([f"| **{m}** | {c} regions | [View details](models/{slugify(m)}.md) |" for m, c in best_global])}

### Need Reserved Capacity (PTU)?
These models support Provisioned Throughput Units:

| Model | PTU Regions | Details |
|-------|-------------|---------|
{chr(10).join([f"| **{m}** | {c} regions | [View details](models/{slugify(m)}.md) |" for m, c in best_provisioned]) if best_provisioned else "| No models currently | — | — |"}

---

## 📊 Coverage Overview

| Level | Description | Count | Example Models |
|-------|-------------|-------|----------------|
| 🟢 **Broad** | 25+ regions | {coverage_counts["Broad"]} | {", ".join([f"`{m}`" for m, r in sorted(model_regions.items(), key=lambda x: -len(x[1]))[:3] if len(r) >= 25])} |
| 🟡 **Strong** | 20-24 regions | {coverage_counts["Strong"]} | {", ".join([f"`{m}`" for m, r in sorted(model_regions.items(), key=lambda x: -len(x[1])) if 20 <= len(r) < 25][:3])} |
| 🟠 **Growing** | 15-19 regions | {coverage_counts["Growing"]} | {", ".join([f"`{m}`" for m, r in model_regions.items() if 15 <= len(r) < 20][:3])} |
| 🔴 **Emerging** | <15 regions | {coverage_counts["Emerging"]} | Limited regional availability |

---

## 🌍 Top Regions by Model Coverage

| Region | Models Available | 
|--------|------------------|
{chr(10).join([f"| **{region}** | {count} models |" for region, count in top_regions])}

---

## 📖 Browse By

| View | Description |
|------|-------------|
| [**All Models**](models/index.md) | Complete model catalog with SKU details |
| [**By Region**](by-region.md) | Find what's available in your region |
| [**By SKU Type**](by-sku.md) | Filter by deployment type |
| [**Change History**](history.md) | Recent availability changes |

---

_Last updated: {datetime.utcnow():%Y-%m-%d %H:%M UTC}_
"""


def generate_model_index_page(
    model_regions: Dict[str, Set[str]],
    model_sku_regions: Dict[str, Dict[str, Set[str]]],
    all_regions: Set[str],
) -> str:
    """Generate the models index page with filterable table."""
    
    def format_region_badge(region: str) -> str:
        """Create a clickable region badge."""
        return f'<span class="region-badge" onclick="filterByRegion(\'{region}\')">{region}</span>'
    
    def format_region_cell(regions_set: Set[str], category: str) -> str:
        """Format a region cell with clickable badges, expandable if > 3 regions."""
        if not regions_set:
            return '-'
        sorted_regions = sorted(regions_set)
        count = len(sorted_regions)
        badges = [format_region_badge(r) for r in sorted_regions]
        
        if count <= 3:
            return f'<span class="region-list">{" ".join(badges)}</span>'
        else:
            # Store just the region names as comma-separated, rebuild badges in JS
            preview_regions = ",".join(sorted_regions[:3])
            all_regions_str = ",".join(sorted_regions)
            preview_badges = " ".join(badges[:3])
            return f'<span class="region-list" data-preview-regions="{preview_regions}" data-all-regions="{all_regions_str}">{preview_badges} <button class="expand-btn" onclick="toggleRegionBadges(this)">+{count - 3} more</button></span>'
    
    # Build region options for filter
    sorted_regions = sorted(all_regions)
    region_options = "\n".join([f'      <option value="{r}">{r}</option>' for r in sorted_regions])
    
    # Build table rows with data attributes for filtering
    rows = []
    for model in sorted(model_regions.keys()):
        regions = model_regions[model]
        count = len(regions)
        bucket_label, bucket_class, _ = pick_bucket(count)

        # Count regions per SKU category
        cat_regions: Dict[str, Set[str]] = defaultdict(set)
        all_skus = []
        for sku, sku_regions in model_sku_regions[model].items():
            cat = get_sku_category(sku)
            cat_regions[cat].update(sku_regions)
            all_skus.append(sku)

        # Create SKU category badges
        sku_badges = []
        category_order = ['Global', 'Datazone', 'Standard', 'Provisioned']
        for cat in category_order:
            if cat in cat_regions:
                region_count = len(cat_regions[cat])
                sku_badges.append(f'<span class="sku-badge sku-{cat.lower()}" title="{region_count} regions">{cat}</span>')
        sku_badges_html = ' '.join(sku_badges) if sku_badges else '-'

        # Format region cells for each category
        global_cell = format_region_cell(cat_regions.get('Global', set()), 'Global')
        datazone_cell = format_region_cell(cat_regions.get('Datazone', set()), 'Datazone')
        standard_cell = format_region_cell(cat_regions.get('Standard', set()), 'Standard')
        provisioned_cell = format_region_cell(cat_regions.get('Provisioned', set()), 'Provisioned')

        # Categories string for filtering
        cats_str = ", ".join(sorted(cat_regions.keys()))
        regions_str = ", ".join(sorted(regions))  # Hidden column for filtering

        rows.append(f"""    <tr>
      <td><a href="{slugify(model)}.md"><strong>{model}</strong></a></td>
      <td><span class="badge {bucket_class}">{bucket_label}</span></td>
      <td>{sku_badges_html}</td>
      <td>{global_cell}</td>
      <td>{datazone_cell}</td>
      <td>{standard_cell}</td>
      <td>{provisioned_cell}</td>
      <td class="hidden-col">{cats_str}</td>
      <td class="hidden-col">{regions_str}</td>
    </tr>""")
    
    return f"""# All Models

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
{region_options}
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
      <th>SKU Types</th>
      <th>Global Regions</th>
      <th>Datazone Regions</th>
      <th>Standard Regions</th>
      <th>Provisioned Regions</th>
      <th class="hidden-col">Categories</th>
      <th class="hidden-col">Region List</th>
    </tr>
  </thead>
  <tbody>
{chr(10).join(rows)}
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

_Last updated: {datetime.utcnow():%Y-%m-%d %H:%M UTC}_
"""


def generate_model_detail_page(
    model: str,
    regions: Set[str],
    region_skus: Dict[str, Set[str]],
    sku_regions: Dict[str, Set[str]],
    all_regions: Set[str],
) -> str:
    """Generate detailed page for a single model."""
    
    count = len(regions)
    bucket_label, bucket_class, _ = pick_bucket(count)
    
    # Group SKUs by category
    sku_by_category: Dict[str, List[Tuple[str, Set[str]]]] = defaultdict(list)
    for sku, sku_regs in sorted(sku_regions.items()):
        cat = get_sku_category(sku)
        sku_by_category[cat].append((sku, sku_regs))
    
    # Build SKU breakdown sections
    sku_sections = []
    for cat in ["Global", "Datazone", "Standard", "Provisioned", "Other"]:
        if cat not in sku_by_category:
            continue
        
        cat_info = SKU_CATEGORIES.get(cat, {"description": "", "use_case": ""})
        
        section = f"""### {cat} Deployments

> **Use Case:** {cat_info.get('use_case', 'Various deployment options')}

| SKU Type | Regions | Coverage |
|----------|---------|----------|
"""
        for sku, sku_regs in sku_by_category[cat]:
            pct = round(len(sku_regs) / len(all_regions) * 100)
            section += f"| {sku} | {len(sku_regs)} | {pct}% |\n"
        
        # Add region list for this category
        section += "\n**Available Regions:**\n\n"
        all_cat_regions = set()
        for _, sku_regs in sku_by_category[cat]:
            all_cat_regions.update(sku_regs)
        section += ", ".join([f"`{r}`" for r in sorted(all_cat_regions)])
        section += "\n"
        
        sku_sections.append(section)
    
    # Build region matrix - which SKUs are available in each region
    # Use HTML table for proper rendering
    sku_labels = sorted(sku_regions.keys())
    
    # Build HTML table header
    header_cells = "".join([f"<th>{sku}</th>" for sku in sku_labels])
    
    # Build HTML table rows
    html_rows = []
    for region in sorted(regions):
        cells = []
        for sku in sku_labels:
            if region in sku_regions.get(sku, set()):
                cells.append("<td>✅</td>")
            else:
                cells.append("<td>—</td>")
        html_rows.append(f"<tr><td><strong>{region}</strong></td>{''.join(cells)}</tr>")
    
    matrix_html = f"""<div class="table-responsive">
<table class="matrix-table">
<thead>
<tr><th>Region</th>{header_cells}</tr>
</thead>
<tbody>
{chr(10).join(html_rows)}
</tbody>
</table>
</div>"""
    
    return f"""# {model}

<span class="badge {bucket_class}">{bucket_label}</span> Available in **{count}** of {len(all_regions)} regions

---

## 📊 Quick Stats

| Metric | Value |
|--------|-------|
| Total Regions | {count} |
| Coverage | {round(count / len(all_regions) * 100)}% |
| SKU Types | {len(sku_regions)} |
| Categories | {", ".join(sorted(sku_by_category.keys()))} |

---

## 🎯 Deployment Options

{chr(10).join(sku_sections)}

---

## 📋 Full Availability Matrix

This table shows exactly which SKU types are available in each region.

{matrix_html}

---

[← Back to All Models](index.md)

_Last updated: {datetime.utcnow():%Y-%m-%d %H:%M UTC}_
"""


def generate_by_region_page(
    model_regions: Dict[str, Set[str]],
    model_region_skus: Dict[str, Dict[str, Set[str]]],
    all_regions: Set[str],
) -> str:
    """Generate the by-region view page with proper SKU tables."""
    
    # Build region to models mapping
    region_models: Dict[str, Set[str]] = defaultdict(set)
    region_model_skus: Dict[str, Dict[str, Set[str]]] = defaultdict(lambda: defaultdict(set))
    
    for model, regions in model_regions.items():
        for region in regions:
            region_models[region].add(model)
            region_model_skus[region][model] = model_region_skus[model].get(region, set())
    
    # Sort regions alphabetically
    sorted_regions = sorted(region_models.keys())
    
    # Build region options for filter
    region_options = "\n".join([f'      <option value="{r}">{r}</option>' for r in sorted_regions])
    
    # Build a comprehensive table with one row per model-region-sku combination
    all_rows = []
    for region in sorted_regions:
        models = region_models[region]
        for model in sorted(models):
            skus = region_model_skus[region][model]
            cats = sorted(set(get_sku_category(s) for s in skus))
            sku_list = sorted(skus)
            
            all_rows.append(f"""    <tr>
      <td><strong>{region}</strong></td>
      <td><a href="models/{slugify(model)}.md">{model}</a></td>
      <td>{', '.join(cats)}</td>
      <td>{', '.join(sku_list)}</td>
    </tr>""")
    
    # Build summary stats
    total_entries = len(all_rows)
    total_regions = len(sorted_regions)
    total_models = len(model_regions)

    return f"""# Models by Region

Find which AI models are available in your Azure region, including their deployment SKU options.

---

## Quick Stats

<div class="stats-cards">
  <div class="stat-card">
    <div class="stat-value">{total_regions}</div>
    <div class="stat-label">Regions</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{total_models}</div>
    <div class="stat-label">Models</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{total_entries}</div>
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
{region_options}
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
{chr(10).join(all_rows)}
  </tbody>
</table>
</div>

---

_Last updated: {datetime.utcnow():%Y-%m-%d %H:%M UTC}_
"""


def generate_by_sku_page(
    model_regions: Dict[str, Set[str]],
    model_sku_regions: Dict[str, Dict[str, Set[str]]],
    all_labels: Set[str],
    all_regions: Set[str],
) -> str:
    """Generate the by-SKU view page with actionable guidance."""
    
    sections = []
    
    for cat_name, cat_info in SKU_CATEGORIES.items():
        cat_skus = cat_info["skus"]
        matching_labels = [l for l in all_labels if l in cat_skus]
        
        if not matching_labels:
            continue
        
        # Find models and their regions for each SKU in this category
        sku_data = []
        for sku_label in sorted(matching_labels):
            models_with_sku = []
            all_sku_regions = set()
            
            for model, sku_regions in model_sku_regions.items():
                if sku_label in sku_regions:
                    regions = sku_regions[sku_label]
                    models_with_sku.append((model, len(regions)))
                    all_sku_regions.update(regions)
            
            if models_with_sku:
                sku_data.append({
                    "label": sku_label,
                    "models": sorted(models_with_sku, key=lambda x: -x[1]),
                    "total_regions": len(all_sku_regions),
                })
        
        if not sku_data:
            continue
        
        # Build section
        section = f"""## {cat_name} Deployments

> **Description:** {cat_info['description']}
>
> **Best For:** {cat_info['use_case']}

"""
        for sku in sku_data:
            section += f"""### {sku['label']}

Available in **{sku['total_regions']}** regions across **{len(sku['models'])}** models.

| Model | Regions | Details |
|-------|---------|---------|
"""
            for model, region_count in sku['models'][:15]:
                section += f"| {model} | {region_count} | [View](models/{slugify(model)}.md) |\n"
            
            if len(sku['models']) > 15:
                section += f"\n*...and {len(sku['models']) - 15} more models*\n"
            
            section += "\n"
        
        sections.append(section)

    return f"""# Models by SKU Type

Choose the right deployment type for your workload.

---

## 🎯 SKU Selection Guide

| Need | Recommended SKU | Why |
|------|-----------------|-----|
| Global reach with failover | **Global** | Automatic routing, high availability |
| Data residency compliance | **Datazone** | Data stays in specified regions |
| Cost-effective, variable load | **Standard** | Pay-as-you-go pricing |
| Predictable high throughput | **Provisioned (PTU)** | Reserved capacity, guaranteed performance |

---

{chr(10).join(sections)}

---

_Last updated: {datetime.utcnow():%Y-%m-%d %H:%M UTC}_
"""


def generate_history_page(history: List[Dict]) -> str:
    """Generate the change history page with clean grouped format."""
    
    if not history:
        return """# Change History

No changes have been recorded yet.

---

_Last updated: """ + f"{datetime.utcnow():%Y-%m-%d %H:%M UTC}_"
    
    entries = []
    all_models = set()
    all_change_regions = set()
    all_skus = set()
    all_dates = set()
    all_rows = []  # Collect all changes for the unified table
    
    for entry in history[:20]:  # Last 20 change sets
        timestamp = entry["timestamp"]
        changes = entry["changes"]
        
        # Collect all changes into structured data with SKU info
        for model, change in sorted(changes.items()):
            all_models.add(model)
            # Get per-SKU changes for more detail
            skus_data = change.get("skus", {})
            
            for sku_key, sku_change in skus_data.items():
                sku_label = sku_change.get("label", sku_key)
                all_skus.add(sku_label)
                sku_added = sku_change.get("added", [])
                sku_removed = sku_change.get("removed", [])
                
                for region in sorted(sku_added):
                    all_change_regions.add(region)
                    all_dates.add(f"{timestamp:%Y-%m-%d}")
                    all_rows.append((timestamp, "added", model, region, sku_label))
                for region in sorted(sku_removed):
                    all_change_regions.add(region)
                    all_dates.add(f"{timestamp:%Y-%m-%d}")
                    all_rows.append((timestamp, "removed", model, region, sku_label))
            
            if change.get("model_removed"):
                all_rows.append((timestamp, "removed", model, "(entire model)", "-"))
    
    # Build filter options
    model_options = "\n".join([f'      <option value="{m}">{m}</option>' for m in sorted(all_models)])
    region_options = "\n".join([f'      <option value="{r}">{r}</option>' for r in sorted(all_change_regions)])
    sku_options = "\n".join([f'      <option value="{s}">{s}</option>' for s in sorted(all_skus)])
    date_options = "\n".join([f'      <option value="{d}">{d}</option>' for d in sorted(all_dates, reverse=True)])
    
    # Build table rows
    table_rows = []
    for timestamp, change_type, model, region, sku in all_rows:
        type_badge = '<span class="badge-added">Added</span>' if change_type == "added" else '<span class="badge-removed">Removed</span>'
        date_str = f"{timestamp:%Y-%m-%d}"
        table_rows.append(f'''    <tr>
      <td data-order="{timestamp:%Y%m%d%H%M%S}">{date_str}</td>
      <td>{type_badge}</td>
      <td><a href="models/{slugify(model)}.md">{model}</a></td>
      <td>{region}</td>
      <td>{sku}</td>
    </tr>''')

    # Calculate summary stats (per-SKU changes)
    total_additions = sum(1 for r in all_rows if r[1] == "added")
    total_removals = sum(1 for r in all_rows if r[1] == "removed")

    return f"""# Change History

Recent changes to AI Foundry model regional availability.

<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-value">{len(history)}</div>
    <div class="stat-label">Change Events</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" style="color: #22c55e;">{total_additions}</div>
    <div class="stat-label">Additions</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" style="color: #ef4444;">{total_removals}</div>
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
{date_options}
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
{model_options}
    </select>
  </div>
  <div class="filter-group">
    <label for="history-region-filter">Region</label>
    <select id="history-region-filter" onchange="filterHistoryTable()">
      <option value="">All Regions</option>
{region_options}
    </select>
  </div>
  <div class="filter-group">
    <label for="history-sku-filter">SKU Type</label>
    <select id="history-sku-filter" onchange="filterHistoryTable()">
      <option value="">All SKUs</option>
{sku_options}
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
{chr(10).join(table_rows)}
  </tbody>
</table>
</div>

---

_Last updated: {datetime.utcnow():%Y-%m-%d %H:%M UTC}_
"""


def main():
    """Generate all MkDocs pages."""
    # Ensure directories exist
    DOCS_DIR.mkdir(exist_ok=True)
    (DOCS_DIR / "stylesheets").mkdir(exist_ok=True)
    (DOCS_DIR / "javascripts").mkdir(exist_ok=True)
    (DOCS_DIR / "models").mkdir(exist_ok=True)
    
    # Load data
    data = load_snapshot(SNAPSHOT_PATH)
    model_regions, model_region_skus, model_sku_regions, all_labels, all_regions = build_model_index(data)
    history = load_history(HISTORY_DIR)
    
    # Generate main pages
    pages = {
        "index.md": generate_index_page(model_regions, model_sku_regions, all_labels, all_regions),
        "models/index.md": generate_model_index_page(model_regions, model_sku_regions, all_regions),
        "by-region.md": generate_by_region_page(model_regions, model_region_skus, all_regions),
        "by-sku.md": generate_by_sku_page(model_regions, model_sku_regions, all_labels, all_regions),
        "history.md": generate_history_page(history),
    }
    
    for filename, content in pages.items():
        path = DOCS_DIR / filename
        path.parent.mkdir(exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"Generated: {path}")
    
    # Generate individual model pages
    for model in model_regions.keys():
        content = generate_model_detail_page(
            model=model,
            regions=model_regions[model],
            region_skus=model_region_skus[model],
            sku_regions=model_sku_regions[model],
            all_regions=all_regions,
        )
        path = DOCS_DIR / "models" / f"{slugify(model)}.md"
        path.write_text(content, encoding="utf-8")
        print(f"Generated: {path}")
    
    print(f"\nDone! Generated {len(pages) + len(model_regions)} pages.")


if __name__ == "__main__":
    main()
