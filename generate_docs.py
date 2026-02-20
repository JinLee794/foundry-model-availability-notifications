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
RETIREMENT_PATH = REGION_WATCH_DIR / "retirement_data.json"
HISTORY_DIR = REGION_WATCH_DIR / "history"
DOCS_DIR = HERE / "docs"

DEFAULT_LABEL = "Global coverage"

# Coverage buckets
BUCKETS: List[Tuple[int, str, str, str]] = [
    (25, "Broad", "badge-broad", "25+ regions"),
    (20, "Strong", "badge-strong", "20-24 regions"),
    (15, "Growing", "badge-growing", "15-19 regions"),
    (0, "Emerging", "badge-emerging", "Under 15 regions"),
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


def load_retirement_data(path: Path) -> Dict:
    """Load retirement data from JSON file."""
    if not path.exists():
        return {"models": {}}
    
    try:
        with path.open(encoding="utf-8") as fh:
            return json.load(fh)
    except json.JSONDecodeError:
        return {"models": {}}


def build_retirement_index(retirement_data: Dict) -> Dict[str, List[Dict]]:
    """Build a model-name to retirement info mapping.
    
    Returns:
        Dict mapping normalized model names to list of retirement entries
    """
    model_retirement: Dict[str, List[Dict]] = defaultdict(list)
    
    for category, entries in retirement_data.get("models", {}).items():
        # Skip fine_tuned - it has a different schema (training_retirement, deployment_retirement)
        if category == "fine_tuned":
            continue
        for entry in entries:
            model_name = entry.get("model", "")
            if model_name:
                # Normalize model name (e.g., gpt-4o -> gpt-4o)
                normalized = model_name.lower().replace(".", "-")
                model_retirement[normalized].append({
                    **entry,
                    "category": category
                })
    
    return dict(model_retirement)


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


def get_retirement_status(retirement_date: str, today: datetime = None) -> Tuple[str, str]:
    """Determine retirement status and return (status_text, css_class)."""
    if today is None:
        today = datetime.utcnow()
    
    if not retirement_date:
        return "Active", "badge-active"
    
    # Handle "No earlier than" dates
    if retirement_date.startswith("No earlier than"):
        return "Planned", "badge-planned"
    
    try:
        retire_dt = datetime.strptime(retirement_date, "%Y-%m-%d")
        days_until = (retire_dt - today).days
        
        if days_until < 0:
            return "Retired", "badge-retired"
        elif days_until <= 30:
            return "Retiring Soon", "badge-retiring-soon"
        elif days_until <= 90:
            return "Retiring", "badge-retiring"
        else:
            return "Scheduled", "badge-scheduled"
    except ValueError:
        return "Planned", "badge-planned"


def generate_retirement_section(
    model: str,
    retirement_entries: List[Dict],
    model_regions_lookup: Dict[str, Set[str]],
) -> str:
    """Generate the retirement notice section for a model page."""
    if not retirement_entries:
        return ""
    
    # Build retirement info table
    rows = []
    replacement_info = []
    
    for entry in retirement_entries:
        version = entry.get("version", "-")
        status = entry.get("status", "Unknown")
        deprecation = entry.get("deprecation_date") or "-"
        retirement = entry.get("retirement_date") or "-"
        replacement = entry.get("replacement")
        
        retire_status, retire_class = get_retirement_status(retirement)
        status_badge = f'<span class="badge {retire_class}">{retire_status}</span>'
        
        replacement_cell = "-"
        if replacement:
            replacement_slug = slugify(replacement)
            replacement_cell = f"[{replacement}](../{replacement_slug}/)"
            
            # Collect replacement info for availability section
            replacement_norm = replacement.lower().replace(".", "-")
            if replacement_norm in model_regions_lookup:
                replacement_info.append({
                    "model": replacement,
                    "slug": replacement_slug,
                    "regions": len(model_regions_lookup[replacement_norm])
                })
        
        rows.append(f"| {version} | {status} | {deprecation} | {retirement} | {status_badge} | {replacement_cell} |")
    
    # Build replacement availability section
    replacement_section = ""
    if replacement_info:
        unique_replacements = {r["model"]: r for r in replacement_info}.values()
        replacement_rows = []
        for r in unique_replacements:
            replacement_rows.append(f"| [{r['model']}](../{r['slug']}/) | {r['regions']} regions | [View Details](../{r['slug']}/) |")
        
        replacement_section = f"""

### Replacement Model Availability

| Model | Coverage | Details |
|-------|----------|---------|
{chr(10).join(replacement_rows)}
"""
    
    return f"""

!!! warning "Retirement Notice"
    This model has scheduled retirement dates. Plan your migration to the replacement model.

## :material-clock-alert: Retirement Schedule

| Version | Status | Deprecation Date | Retirement Date | Timeline | Replacement |
|---------|--------|------------------|-----------------|----------|-------------|
{chr(10).join(rows)}
{replacement_section}
"""


def generate_retirements_page(
    retirement_data: Dict,
    model_regions: Dict[str, Set[str]],
) -> str:
    """Generate the retirements overview page."""
    
    today = datetime.utcnow()
    
    # Categorize all retirements
    retiring_soon = []  # Within 30 days
    upcoming = []  # 31-90 days
    scheduled = []  # 91+ days
    retired = []  # Already retired
    
    all_entries = []
    for category, entries in retirement_data.get("models", {}).items():
        if category == "fine_tuned":
            continue  # Handle separately
        for entry in entries:
            entry_with_cat = {**entry, "category": category}
            all_entries.append(entry_with_cat)
            
            retirement_date = entry.get("retirement_date", "")
            status_text, _ = get_retirement_status(retirement_date, today)
            
            if status_text == "Retired":
                retired.append(entry_with_cat)
            elif status_text == "Retiring Soon":
                retiring_soon.append(entry_with_cat)
            elif status_text == "Retiring":
                upcoming.append(entry_with_cat)
            elif status_text in ["Scheduled", "Planned"]:
                scheduled.append(entry_with_cat)
    
    # Build summary stats
    total_models = len(set(e["model"] for e in all_entries))
    
    def build_table_rows(entries: List[Dict]) -> str:
        rows = []
        # Handle None values in sorting by using empty string as default
        for entry in sorted(entries, key=lambda x: (x.get("retirement_date") or "", x.get("model") or "")):
            model = entry.get("model", "")
            version = entry.get("version", "-")
            retirement = entry.get("retirement_date") or "-"
            replacement = entry.get("replacement")
            category = entry.get("category", "").replace("_", " ").title()
            
            model_slug = slugify(model)
            model_link = f"[{model}](./models/{model_slug}/)"
            
            replacement_cell = "-"
            if replacement:
                replacement_slug = slugify(replacement)
                # Check if replacement model exists in our data
                replacement_norm = replacement.lower().replace(".", "-")
                if replacement_norm in model_regions:
                    region_count = len(model_regions[replacement_norm])
                    replacement_cell = f"[{replacement}](./models/{replacement_slug}/) ({region_count} regions)"
                else:
                    replacement_cell = f"`{replacement}` (not yet available)"
            
            status_text, status_class = get_retirement_status(retirement, today)
            status_badge = f'<span class="badge {status_class}">{status_text}</span>'
            
            rows.append(f"| {model_link} | {version} | {category} | {retirement} | {status_badge} | {replacement_cell} |")
        return chr(10).join(rows)
    
    # Build fine-tuned models section
    fine_tuned_entries = retirement_data.get("models", {}).get("fine_tuned", [])
    fine_tuned_rows = []
    for entry in fine_tuned_entries:
        model = entry.get("model", "")
        version = entry.get("version", "-")
        training_ret = entry.get("training_retirement", "-")
        deploy_ret = entry.get("deployment_retirement", "-")
        note = entry.get("note", "")
        
        model_slug = slugify(model)
        note_str = f" ({note})" if note else ""
        
        fine_tuned_rows.append(f"| [{model}](./models/{model_slug}/) | {version} | {training_ret}{note_str} | {deploy_ret} |")
    
    fine_tuned_section = ""
    if fine_tuned_rows:
        fine_tuned_section = f"""

---

## :material-wrench-cog: Fine-Tuned Model Retirements

Fine-tuned models retire in two phases: training and deployment.

| Model | Version | Training Retirement | Deployment Retirement |
|-------|---------|---------------------|----------------------|
{chr(10).join(fine_tuned_rows)}

!!! info "Fine-Tuning Retirement Policy"
    - **Training retirement**: After this date, you cannot create new fine-tuned models.
    - **Deployment retirement**: After this date, inference and deployment return errors.
    - Models you've already trained remain available until deployment retirement.
"""

    return f"""# Model Retirements

Track upcoming Azure AI Foundry model retirements and plan your migrations.

<div class="stats-grid">
  <div class="stat-card" style="border-left-color: #ef4444;">
    <div class="stat-value" style="color: #ef4444;">{len(retiring_soon)}</div>
    <div class="stat-label">Retiring in 30 Days</div>
  </div>
  <div class="stat-card" style="border-left-color: #f59e0b;">
    <div class="stat-value" style="color: #f59e0b;">{len(upcoming)}</div>
    <div class="stat-label">Retiring in 90 Days</div>
  </div>
  <div class="stat-card" style="border-left-color: #3b82f6;">
    <div class="stat-value" style="color: #3b82f6;">{len(scheduled)}</div>
    <div class="stat-label">Scheduled</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{total_models}</div>
    <div class="stat-label">Total Models</div>
  </div>
</div>

---

{"## :material-alert-circle:{ .md-icon-retiring-soon } Retiring Soon (Within 30 Days)" if retiring_soon else ""}

{f'''These models require immediate migration attention.

| Model | Version | Category | Retirement Date | Status | Replacement |
|-------|---------|----------|-----------------|--------|-------------|
{build_table_rows(retiring_soon)}
''' if retiring_soon else ""}

{"## :material-calendar-alert:{ .md-icon-upcoming } Upcoming Retirements (31-90 Days)" if upcoming else ""}

{f'''Plan your migrations for these models.

| Model | Version | Category | Retirement Date | Status | Replacement |
|-------|---------|----------|-----------------|--------|-------------|
{build_table_rows(upcoming)}
''' if upcoming else ""}

## :material-calendar-clock: All Scheduled Retirements

Complete list of model retirements with replacement recommendations.

| Model | Version | Category | Retirement Date | Status | Replacement |
|-------|---------|----------|-----------------|--------|-------------|
{build_table_rows(all_entries)}
{fine_tuned_section}

---

## :material-book-open-variant: Understanding Retirement Timeline

| Status | Description | Action Required |
|--------|-------------|-----------------|
| <span class="badge badge-retiring-soon">Retiring Soon</span> | Within 30 days | **Immediate migration required** |
| <span class="badge badge-retiring">Retiring</span> | 31-90 days | Plan and test migration |
| <span class="badge badge-scheduled">Scheduled</span> | 91+ days | Monitor and prepare |
| <span class="badge badge-planned">Planned</span> | Date not finalized | Stay informed |
| <span class="badge badge-retired">Retired</span> | No longer available | Migration required |

---

## :material-bookshelf: Resources

- [Azure OpenAI Model Lifecycle](https://learn.microsoft.com/azure/ai-services/openai/concepts/model-lifecycle)
- [Model Deprecation and Retirement](https://learn.microsoft.com/azure/ai-services/openai/concepts/model-retirements)
- [Migration Best Practices](https://learn.microsoft.com/azure/ai-services/openai/how-to/migration)

---

_Data sourced from [Microsoft Azure AI Documentation](https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/articles/ai-foundry/openai/includes/retirement/models.md)_

_Last updated: {datetime.utcnow():%Y-%m-%d %H:%M UTC}_
"""


def generate_index_page(
    model_regions: Dict[str, Set[str]],
    model_sku_regions: Dict[str, Dict[str, Set[str]]],
    all_labels: Set[str],
    all_regions: Set[str],
    retirement_data: Dict = None,
    history: List[Dict] = None,
) -> str:
    """Generate the index/home page with actionable insights."""
    total_models = len(model_regions)
    total_regions = len(all_regions)

    today = datetime.utcnow()
    retirement_data = retirement_data or {"models": {}}

    # Categorize retirements
    retiring_soon: List[Dict] = []  # <=30 days
    upcoming: List[Dict] = []       # 31-90 days
    scheduled: List[Dict] = []      # 91+ days
    already_retired: List[Dict] = []

    for category, entries in retirement_data.get("models", {}).items():
        if category == "fine_tuned":
            continue
        for entry in entries:
            entry_with_cat = {**entry, "category": category}
            retirement_date = entry.get("retirement_date", "")
            status_text, status_class = get_retirement_status(retirement_date, today)
            entry_with_cat["_status_text"] = status_text
            entry_with_cat["_status_class"] = status_class

            if status_text == "Retired":
                already_retired.append(entry_with_cat)
            elif status_text == "Retiring Soon":
                retiring_soon.append(entry_with_cat)
            elif status_text == "Retiring":
                upcoming.append(entry_with_cat)
            elif status_text in ("Scheduled", "Planned"):
                scheduled.append(entry_with_cat)

    # Sort by retirement date
    def _sort_key(e: Dict) -> str:
        rd = e.get("retirement_date") or ""
        if rd.startswith("No earlier than"):
            return rd.replace("No earlier than ", "")
        return rd

    retiring_soon.sort(key=_sort_key)
    upcoming.sort(key=_sort_key)

    # Build retirement table rows helper
    def _retirement_rows(entries: List[Dict]) -> str:
        rows = []
        for e in entries:
            model = e.get("model", "")
            version = e.get("version", "-")
            cat_label = e.get("category", "").replace("_", " ").title()
            retirement = e.get("retirement_date") or "-"
            replacement = e.get("replacement")
            status_badge = f'<span class="badge {e["_status_class"]}">{e["_status_text"]}</span>'

            replacement_cell = "-"
            if replacement:
                replacement_cell = f"[{replacement}](models/{slugify(replacement)}/)"

            rows.append(
                f"    | [{model}](models/{slugify(model)}/) | {version} | {cat_label} | {retirement} | {status_badge} | {replacement_cell} |"
            )
        return chr(10).join(rows)

    # Build the urgent warnings section
    retirement_section_parts: List[str] = []

    if retiring_soon:
        retirement_section_parts.append(f"""!!! danger "Retiring Within 30 Days — {len(retiring_soon)} model version{'s' if len(retiring_soon) != 1 else ''}"
    These models require **immediate migration**. After the retirement date, API calls will return errors.

    | Model | Version | Category | Retirement Date | Status | Replacement |
    |-------|---------|----------|-----------------|--------|-------------|
{_retirement_rows(retiring_soon)}
""")

    if upcoming:
        retirement_section_parts.append(f"""!!! warning "Upcoming Retirements (31-90 Days) — {len(upcoming)} model version{'s' if len(upcoming) != 1 else ''}"
    Plan and test your migration to the replacement model.

    | Model | Version | Category | Retirement Date | Status | Replacement |
    |-------|---------|----------|-----------------|--------|-------------|
{_retirement_rows(upcoming)}
""")

    if already_retired:
        retirement_section_parts.append(f"""!!! failure "Already Retired — {len(already_retired)} model version{'s' if len(already_retired) != 1 else ''}"
    These models are no longer available. Migrate to the listed replacement.

    | Model | Version | Category | Retirement Date | Status | Replacement |
    |-------|---------|----------|-----------------|--------|-------------|
{_retirement_rows(already_retired)}
""")

    if not retiring_soon and not upcoming and not already_retired:
        retirement_section_parts.append('!!! success "No Urgent Retirements"\n    All models are currently within their supported lifecycle.\n')

    retirement_blocks = chr(10).join(retirement_section_parts)

    # Scheduled count for the stat card
    total_action_needed = len(retiring_soon) + len(upcoming) + len(already_retired)

    # Build the recent changes section from history data
    history = history or []
    recent_rows = []
    for entry in history[:10]:  # Last 10 change sets
        timestamp = entry["timestamp"]
        changes = entry["changes"]
        for model, change in sorted(changes.items()):
            skus_data = change.get("skus", {})
            for sku_key, sku_change in skus_data.items():
                sku_label = sku_change.get("label", sku_key)
                for region in sorted(sku_change.get("added", [])):
                    recent_rows.append(
                        f'    | {timestamp:%Y-%m-%d} | '
                        f'<span class="badge-added">Added</span> | '
                        f'[{model}](models/{slugify(model)}/) | '
                        f'{region} | {sku_label} |'
                    )
                for region in sorted(sku_change.get("removed", [])):
                    recent_rows.append(
                        f'    | {timestamp:%Y-%m-%d} | '
                        f'<span class="badge-removed">Removed</span> | '
                        f'[{model}](models/{slugify(model)}/) | '
                        f'{region} | {sku_label} |'
                    )
            if change.get("model_removed"):
                recent_rows.append(
                    f'    | {timestamp:%Y-%m-%d} | '
                    f'<span class="badge-removed">Removed</span> | '
                    f'{model} | (entire model) | - |'
                )

    if recent_rows:
        remaining = max(0, len(recent_rows) - 10)
        see_more = f"\n    *… and {remaining} more — see [full change history](history.md)*" if remaining else ""
        recent_changes_block = f"""???+ tip "Recent Availability Changes"
    | Date | Change | Model | Region | SKU Type |
    |------|--------|-------|--------|----------|
{chr(10).join(recent_rows[:10])}
{see_more}
"""
    else:
        recent_changes_block = """???+ tip "Recent Availability Changes"
    No recent changes detected. See [full change history](history.md) for historical data.
"""

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
    <div class="stat-value">{total_action_needed}</div>
    <div class="stat-label">Action Needed</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{len(scheduled)}</div>
    <div class="stat-label">Scheduled Retirements</div>
  </div>
</div>

---

{recent_changes_block}

---

## :material-alert-circle: Deprecation & Retirement Notices

{retirement_blocks}

??? info "Deprecation vs Retirement — What's the Difference?"
    **Deprecation** marks a model version as no longer recommended. It still works, but no new deployments can be created.
    After deprecation you should begin migrating to the replacement model.

    **Retirement** means the model version is fully removed. API calls will return errors after the retirement date.
    Always migrate **before** the retirement date.

    | Phase | New Deployments | Existing Deployments | API Calls |
    |-------|-----------------|----------------------|-----------|
    | **Active** | :material-check: Allowed | :material-check: Running | :material-check: Working |
    | **Deprecated** | :material-close: Blocked | :material-check: Running | :material-check: Working |
    | **Retired** | :material-close: Blocked | :material-close: Removed | :material-close: Errors |

    See [full retirement details](retirements.md) and [Microsoft's model lifecycle docs](https://learn.microsoft.com/azure/ai-services/openai/concepts/model-retirements).

---

## :material-book-open-variant: Browse By

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
      <td><a href="{slugify(model)}/"><strong>{model}</strong></a></td>
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
    retirement_info: List[Dict] = None,
    model_regions_lookup: Dict[str, Set[str]] = None,
) -> str:
    """Generate detailed page for a single model."""
    
    count = len(regions)
    bucket_label, bucket_class, _ = pick_bucket(count)
    
    # Group SKUs by category
    sku_by_category: Dict[str, List[Tuple[str, Set[str]]]] = defaultdict(list)
    for sku, sku_regs in sorted(sku_regions.items()):
        cat = get_sku_category(sku)
        sku_by_category[cat].append((sku, sku_regs))
    
    # Build retirement section if applicable
    retirement_section = ""
    if retirement_info:
        retirement_section = generate_retirement_section(model, retirement_info, model_regions_lookup or {})
    
    # Build SKU breakdown sections
    sku_sections = []
    for cat in ["Global", "Datazone", "Standard", "Provisioned", "Other"]:
        if cat not in sku_by_category:
            continue
        
        cat_info = SKU_CATEGORIES.get(cat, {"description": "", "use_case": ""})
        
        section = f"""### {cat} Deployments

!!! tip "Use Case"
    {cat_info.get('use_case', 'Various deployment options')}

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
                cells.append('<td class="matrix-yes">&#10003;</td>')
            else:
                cells.append('<td class="matrix-no">&mdash;</td>')
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
{retirement_section}
---

## :material-chart-box-outline: Quick Stats

| Metric | Value |
|--------|-------|
| Total Regions | {count} |
| Coverage | {round(count / len(all_regions) * 100)}% |
| SKU Types | {len(sku_regions)} |
| Categories | {", ".join(sorted(sku_by_category.keys()))} |

---

## :material-target: Deployment Options

{chr(10).join(sku_sections)}

---

## :material-clipboard-list: Full Availability Matrix

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
      <td><a href="../models/{slugify(model)}/">{model}</a></td>
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
    """Generate the by-SKU view page as an interactive filterable table."""

    total_regions = len(all_regions)

    # Collect all unique SKU labels and build category mapping
    sku_to_category: Dict[str, str] = {}
    for label in sorted(all_labels):
        sku_to_category[label] = get_sku_category(label)

    # Build flat rows: one per model × SKU combination
    all_rows = []
    sku_model_counts: Dict[str, int] = defaultdict(int)
    sku_region_sets: Dict[str, Set[str]] = defaultdict(set)
    category_model_sets: Dict[str, Set[str]] = defaultdict(set)

    for model in sorted(model_sku_regions.keys()):
        for sku_label, regions in model_sku_regions[model].items():
            cat = sku_to_category.get(sku_label, "Other")
            region_count = len(regions)
            pct = round(region_count / total_regions * 100) if total_regions else 0
            bucket_label, bucket_class, _ = pick_bucket(region_count)

            sku_model_counts[sku_label] += 1
            sku_region_sets[sku_label].update(regions)
            category_model_sets[cat].add(model)

            regions_str = ", ".join(sorted(regions))

            all_rows.append(f"""    <tr>
      <td><a href="../models/{slugify(model)}/"><strong>{model}</strong></a></td>
      <td><span class="sku-badge sku-{cat.lower()}">{cat}</span></td>
      <td>{sku_label}</td>
      <td>{region_count}</td>
      <td><span class="badge {bucket_class}">{bucket_label}</span></td>
      <td>{pct}%</td>
      <td class="hidden-col">{regions_str}</td>
    </tr>""")

    # Stats
    total_skus = len([s for s in sku_model_counts if sku_model_counts[s] > 0])
    total_models = len(model_sku_regions)
    total_deployments = len(all_rows)

    # Build filter options
    sorted_sku_labels = sorted(sku_model_counts.keys())
    sku_options = "\n".join(
        [f'      <option value="{s}">{s}</option>' for s in sorted_sku_labels]
    )

    # Build SKU summary rows for the overview table
    sku_summary_rows = []
    for cat_name in ["Global", "Datazone", "Standard", "Provisioned", "Other"]:
        cat_skus = [(s, sku_model_counts[s], len(sku_region_sets[s]))
                     for s in sorted_sku_labels
                     if sku_to_category.get(s) == cat_name and sku_model_counts[s] > 0]
        for sku_label, model_count, region_count in cat_skus:
            pct = round(region_count / total_regions * 100) if total_regions else 0
            sku_summary_rows.append(
                f'| <span class="sku-badge sku-{cat_name.lower()}">{cat_name}</span> '
                f'| {sku_label} | {model_count} | {region_count} | {pct}% |'
            )

    return f"""# Models by SKU Type

Explore every deployment SKU and discover which models and regions support it.

<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-value">{total_skus}</div>
    <div class="stat-label">SKU Types</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{total_models}</div>
    <div class="stat-label">Models</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{total_deployments}</div>
    <div class="stat-label">Model × SKU Combinations</div>
  </div>
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
{chr(10).join(sku_summary_rows)}

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
{sku_options}
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
{chr(10).join(all_rows)}
  </tbody>
</table>
</div>

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
      <td><a href="../models/{slugify(model)}/">{model}</a></td>
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
    
    # Load retirement data
    retirement_data = load_retirement_data(RETIREMENT_PATH)
    retirement_index = build_retirement_index(retirement_data)
    
    # Build normalized model_regions lookup for retirement sections
    model_regions_normalized = {
        slugify(model): regions for model, regions in model_regions.items()
    }
    
    # Generate main pages
    pages = {
        "index.md": generate_index_page(model_regions, model_sku_regions, all_labels, all_regions, retirement_data, history),
        "models/index.md": generate_model_index_page(model_regions, model_sku_regions, all_regions),
        "by-region.md": generate_by_region_page(model_regions, model_region_skus, all_regions),
        "by-sku.md": generate_by_sku_page(model_regions, model_sku_regions, all_labels, all_regions),
        "history.md": generate_history_page(history),
        "retirements.md": generate_retirements_page(retirement_data, model_regions_normalized),
    }
    
    for filename, content in pages.items():
        path = DOCS_DIR / filename
        path.parent.mkdir(exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"Generated: {path}")
    
    # Generate individual model pages
    for model in model_regions.keys():
        # Look up retirement info for this model
        model_normalized = slugify(model)
        retirement_info = retirement_index.get(model_normalized, [])
        
        content = generate_model_detail_page(
            model=model,
            regions=model_regions[model],
            region_skus=model_region_skus[model],
            sku_regions=model_sku_regions[model],
            all_regions=all_regions,
            retirement_info=retirement_info,
            model_regions_lookup=model_regions_normalized,
        )
        path = DOCS_DIR / "models" / f"{slugify(model)}.md"
        path.write_text(content, encoding="utf-8")
        print(f"Generated: {path}")
    
    print(f"\nDone! Generated {len(pages) + len(model_regions)} pages.")


if __name__ == "__main__":
    main()
