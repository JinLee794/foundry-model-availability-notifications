#!/usr/bin/env python3
"""Generate MkDocs pages from AI Foundry model availability snapshot data."""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timezone
from html import escape as html_escape
from pathlib import Path
from typing import Dict, List, Set, Tuple
from urllib.parse import quote

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

# Normalize legacy/non-canonical SKU labels to valid Azure AI Foundry deployment type names.
# Source: https://learn.microsoft.com/azure/foundry/foundry-models/concepts/deployment-types
SKU_LABEL_NORMALIZATION: Dict[str, str] = {
    # Legacy model-family-specific Standard labels → canonical "Standard"
    "Standard (all)": "Standard",
    "Standard GPT-3.5 Turbo": "Standard",
    "Standard GPT-4": "Standard",
    "Standard audio": "Standard",
    "Standard chat completions": "Standard",
    "Standard completions": "Standard",
    "Standard embeddings": "Standard",
    "Standard image generation": "Standard",
    # "Standard global deployments" is the Global Standard deployment type
    "Standard global deployments": "Global Standard",
    # Normalize alternate casing for Data Zone Standard
    "Data Zone Standard": "Datazone standard",
}

# SKU category mapping with descriptions
SKU_CATEGORIES = {
    "Global": {
        "skus": ["Global coverage", "Global batch", "Global batch datazone", "Global Standard"],
        "description": "Worldwide availability with intelligent routing",
        "use_case": "Best for applications needing global reach with automatic failover",
        "compliance": "⚠ Data may be processed in any Azure region — not suitable for HIPAA, FedRAMP, or strict data-residency requirements",
    },
    "Datazone": {
        "skus": ["Datazone standard", "Datazone provisioned managed"],
        "description": "Data residency compliance deployments",
        "use_case": "Required for data sovereignty and compliance requirements (GDPR, etc.)",
        "compliance": "✓ Data stays within the specified geographic zone — supports GDPR and regional data-residency policies",
    },
    "Standard": {
        "skus": ["Standard"],
        "description": "Pay-as-you-go regional deployments",
        "use_case": "Best for variable workloads and cost-sensitive applications",
        "compliance": "✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft",
    },
    "Provisioned": {
        "skus": ["Provisioned (PTU managed)", "Provisioned global", "Global Provisioned Managed"],
        "description": "Reserved throughput capacity (PTU)",
        "use_case": "Best for predictable, high-volume production workloads",
        "compliance": "✓ Single-region deployment — HIPAA-eligible in supported regions with a BAA from Microsoft",
    },
}

# Provisioned sub-SKU groupings for granular column display
PROVISIONED_PTU_SKUS: Set[str] = {"Provisioned (PTU managed)"}
PROVISIONED_GLOBAL_SKUS: Set[str] = {"Provisioned global", "Global Provisioned Managed"}

KNOWN_AZURE_REGION_NAMES: Set[str] = {
    "East US", "East US 2", "West US", "West US 2", "West US 3",
    "Central US", "North Central US", "South Central US", "West Central US",
    "Brazil South", "Brazil Southeast", "Canada Central", "Canada East",
    "North Europe", "West Europe", "UK South", "UK West", "France Central",
    "France South", "Germany North", "Germany West Central", "Switzerland North",
    "Switzerland West", "Norway East", "Norway West", "Sweden Central",
    "Sweden South", "Spain Central", "Italy North", "Poland Central",
    "Netherlands West", "Finland Central", "UAE North", "UAE Central",
    "Qatar Central", "Saudi Arabia Central", "South Africa North",
    "South Africa West", "East Asia", "Southeast Asia", "Japan East",
    "Japan West", "Korea Central", "Korea South", "Australia East",
    "Australia Southeast", "Australia Central", "Australia Central 2",
    "India Central", "India South", "West India", "Central India", "South India",
    "Jio India West", "Jio India Central",
}


def get_sku_category(label: str) -> str:
    """Return the category for a SKU label."""
    for category, info in SKU_CATEGORIES.items():
        if label in info["skus"]:
            return category
    return "Other"


def sku_category_badge(cat: str, extra_title: str = "") -> str:
    """Return an HTML badge for a SKU category with a tooltip from SKU_CATEGORIES."""
    info = SKU_CATEGORIES.get(cat, {})
    desc = info.get("description", "")
    use_case = info.get("use_case", "")
    compliance = info.get("compliance", "")
    parts = [p for p in [desc, use_case, compliance] if p]
    tooltip = " | ".join(parts) if parts else extra_title
    tooltip_attr = f' data-tooltip="{tooltip}"' if tooltip else (f' title="{extra_title}"' if extra_title else "")
    return f'<span class="sku-badge sku-{cat.lower()}"{tooltip_attr}>{cat}</span>'


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
            label = SKU_LABEL_NORMALIZATION.get(label, label)
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


def normalize_lookup_key(value: str) -> str:
    """Normalize names for model/region lookup comparisons."""
    return "".join(ch for ch in str(value).lower() if ch.isalnum())


def normalize_sku_label(label: str) -> str:
    """Normalize SKU labels for display and filtering."""
    return SKU_LABEL_NORMALIZATION.get(label, label)


def query_url(base: str, params: Dict[str, str]) -> str:
    """Build a relative URL with encoded query-string filters."""
    query_parts = []
    for key, value in params.items():
        if value in (None, "", "-"):
            continue
        query_parts.append(f"{quote(str(key), safe='')}={quote(str(value), safe='')}")
    if not query_parts:
        return base
    return f"{base}?{'&'.join(query_parts)}"


def model_link(model: str, prefix: str = "models/", class_name: str = "") -> str:
    """Return a model detail link."""
    class_attr = f' class="{class_name}"' if class_name else ""
    return f'<a{class_attr} href="{prefix}{slugify(model)}/">{html_escape(model)}</a>'


def region_link(region: str, prefix: str = "by-region/", class_name: str = "region-badge") -> str:
    """Return a link to the region explorer with the region filter applied."""
    if region.startswith("("):
        return html_escape(region)
    class_attr = f' class="{class_name}"' if class_name else ""
    href = query_url(prefix, {"region": region})
    return f'<a{class_attr} href="{href}">{html_escape(region)}</a>'


def sku_link(sku_label: str, prefix: str = "by-sku/", class_name: str = "change-link-pill") -> str:
    """Return a link to the SKU explorer with the SKU filter applied."""
    if sku_label in ("", "-"):
        return "-"
    class_attr = f' class="{class_name}"' if class_name else ""
    href = query_url(prefix, {"sku": sku_label})
    return f'<a{class_attr} href="{href}">{html_escape(sku_label)}</a>'


def history_link(prefix: str = "history/", **params: str) -> str:
    """Return a link to the change history with filters applied."""
    return query_url(prefix, params)


def flatten_history_changes(
    history: List[Dict],
    known_regions: Set[str] = None,
    known_models: Set[str] = None,
    limit: int = None,
) -> List[Dict]:
    """Flatten history payloads into model/region/SKU change rows.

    Older history snapshots were region-centric, while current snapshots are
    model-centric. This normalizes both shapes so rendered history stays useful.
    """
    rows: List[Dict] = []
    entries = history[:limit] if limit else history
    region_candidates = set(known_regions or set()) | KNOWN_AZURE_REGION_NAMES
    region_lookup = {
        normalize_lookup_key(region): region
        for region in region_candidates
        if region in KNOWN_AZURE_REGION_NAMES
    }
    region_keys = set(region_lookup.keys())
    model_lookup = {
        normalize_lookup_key(model): model
        for model in (known_models or set())
        if normalize_lookup_key(model) not in region_keys
    }

    for entry in entries:
        timestamp = entry.get("timestamp")
        changes = entry.get("changes", {})
        if not timestamp or not isinstance(changes, dict):
            continue
        has_model_subjects = bool(model_lookup) and any(
            normalize_lookup_key(subject) in model_lookup
            for subject in changes
        )

        for subject, change in sorted(changes.items(), key=lambda item: item[0].lower()):
            if not isinstance(change, dict):
                continue
            subject_region = region_lookup.get(normalize_lookup_key(subject))
            if subject_region and has_model_subjects:
                continue
            skus_data = change.get("skus", {})

            for sku_key, sku_change in skus_data.items():
                if not isinstance(sku_change, dict):
                    continue
                sku_label = normalize_sku_label(sku_change.get("label", sku_key))

                for change_type in ("added", "removed"):
                    for value in sorted(sku_change.get(change_type, [])):
                        if subject_region:
                            model = value
                            region = subject_region
                        else:
                            model = subject
                            region = value
                        rows.append({
                            "timestamp": timestamp,
                            "change": change_type,
                            "model": model,
                            "region": region,
                            "sku": sku_label,
                        })

            if change.get("model_removed") and not subject_region:
                rows.append({
                    "timestamp": timestamp,
                    "change": "removed",
                    "model": subject,
                    "region": "(entire model)",
                    "sku": "-",
                })

    return sorted(
        rows,
        key=lambda row: (
            -row["timestamp"].timestamp(),
            0 if row["change"] == "removed" else 1,
            row["model"].lower(),
            row["sku"].lower(),
            row["region"].lower(),
        ),
    )


def pluralize(count: int, singular: str, plural: str = None) -> str:
    """Return a count-aware label."""
    label = singular if count == 1 else (plural or f"{singular}s")
    return f"{count} {label}"


def format_digest_date(timestamp: datetime) -> str:
    """Format a compact date without platform-specific strftime flags."""
    return f"{timestamp:%b} {timestamp.day}, {timestamp:%Y}"


def format_region_links(regions: Set[str], max_visible: int = 3) -> str:
    """Format region links for a compact digest row."""
    sorted_regions = sorted(regions)
    visible = sorted_regions[:max_visible]
    parts = [region_link(region) for region in visible]
    remaining = len(sorted_regions) - len(visible)
    if remaining:
        parts.append(f'<span class="change-more-count">+{remaining} more</span>')
    return " ".join(parts)


def build_recent_changes_block(history: List[Dict], all_regions: Set[str], known_models: Set[str]) -> str:
    """Build the grouped recent availability digest for the home page."""
    rows = flatten_history_changes(history, all_regions, known_models, limit=10)
    if not rows:
        return f"""<div class="changes-digest" aria-label="Recent availability changes">
    <div class="changes-digest__header">
        <div>
            <span class="changes-digest__eyebrow">Recent availability changes</span>
            <h2 class="changes-digest__title">Latest Availability Digest</h2>
            <p>No recent changes detected.</p>
        </div>
        <a class="md-button" href="history/">View full history</a>
    </div>
</div>"""

    latest_timestamp = rows[0]["timestamp"]
    latest_date = f"{latest_timestamp:%Y-%m-%d}"
    latest_rows = [row for row in rows if row["timestamp"] == latest_timestamp]
    latest_additions = sum(1 for row in latest_rows if row["change"] == "added")
    latest_removals = sum(1 for row in latest_rows if row["change"] == "removed")
    latest_models = len({row["model"] for row in latest_rows})
    latest_regions = len({row["region"] for row in latest_rows if not row["region"].startswith("(")})

    grouped: Dict[Tuple[datetime, str, str, str], Dict] = {}
    for row in rows:
        key = (row["timestamp"], row["change"], row["model"], row["sku"])
        if key not in grouped:
            grouped[key] = {
                "timestamp": row["timestamp"],
                "change": row["change"],
                "model": row["model"],
                "sku": row["sku"],
                "regions": set(),
            }
        grouped[key]["regions"].add(row["region"])

    digest_rows = []
    groups = list(grouped.values())
    for group in groups[:16]:
        change_type = group["change"]
        badge = '<span class="badge-added">Added</span>' if change_type == "added" else '<span class="badge-removed">Removed</span>'
        row_class = "change-row--added" if change_type == "added" else "change-row--removed"
        regions = group["regions"]
        region_count = len([region for region in regions if not region.startswith("(")])
        region_phrase = pluralize(region_count, "region") if region_count else "Catalog"
        sku = group["sku"]
        sku_html = sku_link(sku, class_name="change-link-pill change-link-pill--sku") if sku != "-" else "Model availability"
        digest_rows.append(f"""        <div class="change-row {row_class}" role="row">
            <div class="change-row__date" role="cell"><time datetime="{group['timestamp']:%Y-%m-%d}">{group['timestamp']:%b} {group['timestamp'].day}</time></div>
            <div class="change-row__change" role="cell">{badge}</div>
            <div class="change-row__model" role="cell">{model_link(group['model'])}</div>
            <div class="change-row__sku" role="cell">{sku_html}</div>
            <div class="change-row__scope" role="cell">{region_phrase}</div>
            <div class="change-row__regions" role="cell">{format_region_links(regions)}</div>
        </div>""")

    remaining_groups = len(groups) - len(digest_rows)
    more_note = ""
    if remaining_groups > 0:
        more_note = f"""
    <p class="changes-digest__more">{pluralize(remaining_groups, "more grouped change")} available in <a href="history/">full change history</a>.</p>"""

    return f"""<div class="changes-digest" aria-label="Recent availability changes">
    <div class="changes-digest__header">
        <div>
            <span class="changes-digest__eyebrow">Recent availability changes</span>
            <h2 class="changes-digest__title">Latest Availability Digest</h2>
            <p>Latest run: {format_digest_date(latest_timestamp)}. Changes are grouped by model, deployment SKU, and affected regions.</p>
        </div>
        <a class="md-button" href="history/">View full history</a>
    </div>
    <div class="changes-summary" aria-label="Latest change summary">
        <a class="changes-summary__item changes-summary__item--added" href="{history_link(date=latest_date, type='Added')}">
            <strong>{latest_additions}</strong>
            <span>Additions</span>
        </a>
        <a class="changes-summary__item changes-summary__item--removed" href="{history_link(date=latest_date, type='Removed')}">
            <strong>{latest_removals}</strong>
            <span>Removals</span>
        </a>
        <a class="changes-summary__item" href="{history_link(date=latest_date)}">
            <strong>{latest_models}</strong>
            <span>Models affected</span>
        </a>
        <a class="changes-summary__item" href="{history_link(date=latest_date)}">
            <strong>{latest_regions}</strong>
            <span>Regions affected</span>
        </a>
    </div>
    <div class="changes-table" role="table" aria-label="Grouped availability updates">
        <div class="change-row change-row--head" role="row">
            <div role="columnheader">Date</div>
            <div role="columnheader">Change</div>
            <div role="columnheader">Model</div>
            <div role="columnheader">SKU type</div>
            <div role="columnheader">Scope</div>
            <div role="columnheader">Regions</div>
        </div>
{chr(10).join(digest_rows)}
    </div>{more_note}
</div>"""


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
            if replacement_slug in model_regions_lookup:
                replacement_cell = f"[{replacement}](../{replacement_slug}/)"
                replacement_info.append({
                    "model": replacement,
                    "slug": replacement_slug,
                    "regions": len(model_regions_lookup[replacement_slug])
                })
            else:
                replacement_cell = f"`{replacement}` (not yet available)"
        
        rows.append(f"| {version} | {status} | {deprecation} | {retirement} | {status_badge} | {replacement_cell} |")
    
    # Collect any retirement notes to display
    retirement_notes = []
    seen_notes: set = set()
    for entry in retirement_entries:
        note = entry.get("retirement_note")
        if note and note not in seen_notes:
            seen_notes.add(note)
            retirement_notes.append(note)

    # Build retirement notes admonition blocks
    notes_section = ""
    if retirement_notes:
        note_blocks = []
        for note in retirement_notes:
            note_blocks.append(
                f'!!! note "Retirement Date Update"\n'
                f'    {note}\n'
                f'\n'
                f'    For more details, see the [Azure AI Foundry model retirements documentation]'
                f'(https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements'
                f'?view=foundry-classic&tabs=text).\n'
            )
        notes_section = "\n" + "\n".join(note_blocks)

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
{notes_section}{replacement_section}
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

    # Collect unique retirement notes, grouped by note text -> list of (model, version) pairs
    notes_to_models: Dict[str, List[str]] = {}
    seen_model_note_pairs: set = set()
    for entry in all_entries:
        note = entry.get("retirement_note")
        if note:
            model = entry.get("model", "")
            pair = (model, note)
            if pair not in seen_model_note_pairs:
                seen_model_note_pairs.add(pair)
                if note not in notes_to_models:
                    notes_to_models[note] = []
                if model not in notes_to_models[note]:
                    notes_to_models[note].append(model)

    def build_retirement_notes_section() -> str:
        if not notes_to_models:
            return ""
        blocks = []
        for note, models in notes_to_models.items():
            model_list = " and ".join(f"**{m}**" for m in sorted(set(models)))
            blocks.append(
                f'!!! note "{model_list} Retirement Update"\n'
                f'    {note}\n'
                f'\n'
                f'    For more details, see the [Azure AI Foundry model retirements documentation]'
                f'(https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements'
                f'?view=foundry-classic&tabs=text).\n'
            )
        return "\n".join(blocks)

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
            model_link = f"[{model}](models/{model_slug}.md)" if model_slug in model_regions else f"`{model}`"
            
            replacement_cell = "-"
            if replacement:
                replacement_slug = slugify(replacement)
                # Check if replacement model exists in our data
                if replacement_slug in model_regions:
                    region_count = len(model_regions[replacement_slug])
                    replacement_cell = f"[{replacement}](models/{replacement_slug}.md) ({region_count} regions)"
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
        model_cell = f"[{model}](models/{model_slug}.md)" if model_slug in model_regions else f"`{model}`"
        
        fine_tuned_rows.append(f"| {model_cell} | {version} | {training_ret}{note_str} | {deploy_ret} |")
    
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
{build_retirement_notes_section()}

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

- [Azure OpenAI Model Lifecycle](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirements)
- [Model Deprecation and Retirement](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirements)
- [Migration Best Practices](https://learn.microsoft.com/azure/foundry-classic/openai/how-to/migration)

---

_Data sourced from [Microsoft Azure AI Documentation](https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/articles/foundry/openai/includes/retirement/models.md)_

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
    available_model_slugs = {slugify(model) for model in model_regions}

    def _retirement_rows(entries: List[Dict]) -> str:
        rows = []
        for e in entries:
            model = e.get("model", "")
            version = e.get("version", "-")
            cat_label = e.get("category", "").replace("_", " ").title()
            retirement = e.get("retirement_date") or "-"
            replacement = e.get("replacement")
            status_badge = f'<span class="badge {e["_status_class"]}">{e["_status_text"]}</span>'
            model_slug = slugify(model)
            model_cell = f"[{model}](models/{model_slug}.md)" if model_slug in available_model_slugs else f"`{model}`"

            replacement_cell = "-"
            if replacement:
                replacement_slug = slugify(replacement)
                if replacement_slug in available_model_slugs:
                    replacement_cell = f"[{replacement}](models/{replacement_slug}.md)"
                else:
                    replacement_cell = f"`{replacement}` (not yet available)"

            rows.append(
                f"    | {model_cell} | {version} | {cat_label} | {retirement} | {status_badge} | {replacement_cell} |"
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

    history = history or []
    recent_changes_block = build_recent_changes_block(history, all_regions, set(model_regions.keys()))

    lifecycle_guide = """<div class="lifecycle-guide" aria-label="Model lifecycle guidance">
    <div class="lifecycle-guide__header">
        <span class="lifecycle-guide__eyebrow">Lifecycle signals</span>
        <p>Microsoft Foundry models move through predictable stages so teams can test replacements before old versions stop serving traffic. Use this dashboard for dates and model-level risk, then validate active deployments with the Models API and Azure Service Health.</p>
    </div>

    <div class="lifecycle-rail" aria-label="Lifecycle stages">
        <div class="lifecycle-stage lifecycle-stage--preview">
            <span class="lifecycle-stage__number">1</span>
            <strong>Preview</strong>
            <span>Experimental. Suitable for evaluation, not production.</span>
        </div>
        <div class="lifecycle-stage lifecycle-stage--ga">
            <span class="lifecycle-stage__number">2</span>
            <strong>Generally available</strong>
            <span>Production-ready. Retirement date is set at launch.</span>
        </div>
        <div class="lifecycle-stage lifecycle-stage--legacy">
            <span class="lifecycle-stage__number">3</span>
            <strong>Legacy</strong>
            <span>Newer models exist. Begin replacement evaluation.</span>
        </div>
        <div class="lifecycle-stage lifecycle-stage--deprecated">
            <span class="lifecycle-stage__number">4</span>
            <strong>Deprecated</strong>
            <span>Existing customers can continue. New customers are blocked.</span>
        </div>
        <div class="lifecycle-stage lifecycle-stage--retired">
            <span class="lifecycle-stage__number">5</span>
            <strong>Retired</strong>
            <span>Removed from service. Inference returns 410 Gone.</span>
        </div>
    </div>

    <div class="lifecycle-timelines">
        <section class="lifecycle-timeline lifecycle-timeline--ga" aria-labelledby="ga-lifecycle-title">
            <div class="lifecycle-timeline__title" id="ga-lifecycle-title">GA model retirement path</div>
            <ol class="lifecycle-steps">
                <li>
                    <span class="lifecycle-step__marker">Launch</span>
                    <strong>GA starts</strong>
                    <span>Retirement date is set about 18 months out and exposed by the Models API.</span>
                </li>
                <li>
                    <span class="lifecycle-step__marker">12 mo</span>
                    <strong>Deprecated</strong>
                    <span>Existing subscriptions can continue; new customers cannot access that version.</span>
                </li>
                <li>
                    <span class="lifecycle-step__marker">90 d</span>
                    <strong>Replacement named</strong>
                    <span>Replacement is typically available in Global Standard for evaluation.</span>
                </li>
                <li>
                    <span class="lifecycle-step__marker">30 d</span>
                    <strong>Provisioned window</strong>
                    <span>Provisioned regions get a short manual migration window.</span>
                </li>
                <li>
                    <span class="lifecycle-step__marker">Retire</span>
                    <strong>Traffic stops</strong>
                    <span>Requests to the retired version fail. Retirement dates are not extended.</span>
                </li>
            </ol>
        </section>

        <section class="lifecycle-timeline lifecycle-timeline--preview" aria-labelledby="preview-lifecycle-title">
            <div class="lifecycle-timeline__title" id="preview-lifecycle-title">Preview model retirement path</div>
            <ol class="lifecycle-steps lifecycle-steps--compact">
                <li>
                    <span class="lifecycle-step__marker">Preview</span>
                    <strong>Not for production</strong>
                    <span>Launches with a not-sooner-than retirement date, often around 90 days out.</span>
                </li>
                <li>
                    <span class="lifecycle-step__marker">30 d</span>
                    <strong>Notice period</strong>
                    <span>Customers receive at least 30 days notice before upgrade or retirement.</span>
                </li>
                <li>
                    <span class="lifecycle-step__marker">Upgrade</span>
                    <strong>Force-upgrade or end</strong>
                    <span>Preview deployments move to a newer preview or GA model, or retire if no replacement exists.</span>
                </li>
            </ol>
        </section>
    </div>

    <div class="attention-grid" aria-label="When to pay attention">
        <div class="attention-item attention-item--watch">
            <strong>Start watching</strong>
            <span>A model enters Legacy or Deprecated, or appears as Scheduled in this dashboard.</span>
        </div>
        <div class="attention-item attention-item--test">
            <strong>Start testing</strong>
            <span>The replacement is declared, usually 90-120 days before retirement.</span>
        </div>
        <div class="attention-item attention-item--notify">
            <strong>Expect notifications</strong>
            <span>GA retirements get at least 60 days active notice; preview models get at least 30 days.</span>
        </div>
        <div class="attention-item attention-item--manual">
            <strong>Check deployment type</strong>
            <span>Global Standard, Data Zone Standard, and Standard can auto-upgrade. Provisioned deployments must be migrated manually.</span>
        </div>
        <div class="attention-item attention-item--api">
            <strong>Read API status carefully</strong>
            <span>In the Models API, <code>Deprecating</code> means deprecated; <code>Deprecated</code> means retired.</span>
        </div>
    </div>

    <p class="lifecycle-guide__source">Adapted from <a href="https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements">Microsoft Foundry Models lifecycle and support policy</a>. See <a href="retirements/">full retirement details</a> for model-specific dates.</p>
</div>
"""

    return f"""# AI Foundry Model Availability

<div class="dashboard-hero">
    <div class="dashboard-hero__copy">
        <p class="dashboard-hero__eyebrow">Azure AI Foundry operations</p>
        <p class="dashboard-hero__lede">Track model availability, regional coverage, deployment SKUs, and retirement risk from one searchable dashboard.</p>
    </div>
    <div class="dashboard-hero__actions">
        <a class="md-button md-button--primary" href="models/">Browse models</a>
        <a class="md-button" href="retirements/">Review retirements</a>
    </div>
</div>

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

{lifecycle_guide}

---

## :material-book-open-variant: Browse By

<div class="browse-grid">
    <a class="browse-card" href="models/">
        <span class="browse-card__label">Catalog</span>
        <strong>All Models</strong>
        <span>Complete model catalog with SKU and region coverage details.</span>
    </a>
    <a class="browse-card" href="by-region/">
        <span class="browse-card__label">Regions</span>
        <strong>By Region</strong>
        <span>Find what is available in each Azure region.</span>
    </a>
    <a class="browse-card" href="by-sku/">
        <span class="browse-card__label">Deployment</span>
        <strong>By SKU Type</strong>
        <span>Compare Global, Datazone, Standard, and Provisioned options.</span>
    </a>
    <a class="browse-card" href="history/">
        <span class="browse-card__label">Changes</span>
        <strong>Change History</strong>
        <span>Review recent availability additions and removals.</span>
    </a>
</div>

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
        for sku, sku_regions_set in model_sku_regions[model].items():
            cat = get_sku_category(sku)
            cat_regions[cat].update(sku_regions_set)
            all_skus.append(sku)

        # Compute granular provisioned sub-type regions
        prov_ptu_regions: Set[str] = set()
        prov_global_regions: Set[str] = set()
        for sku, sku_regions_set in model_sku_regions[model].items():
            if sku in PROVISIONED_PTU_SKUS:
                prov_ptu_regions.update(sku_regions_set)
            elif sku in PROVISIONED_GLOBAL_SKUS:
                prov_global_regions.update(sku_regions_set)

        # Create SKU category badges — tooltip for Global/Datazone/Standard; granular sub-type for Provisioned
        sku_badges = []
        for cat in ['Global', 'Datazone', 'Standard']:
            if cat in cat_regions:
                region_count = len(cat_regions[cat])
                sku_badges.append(sku_category_badge(cat, f"{region_count} regions"))
        if prov_ptu_regions:
            sku_badges.append(f'<span class="sku-badge sku-provisioned" title="{len(prov_ptu_regions)} regions">Prov.PTU</span>')
        if prov_global_regions:
            sku_badges.append(f'<span class="sku-badge sku-provisioned-global" title="{len(prov_global_regions)} regions">Prov.Global</span>')
        sku_badges_html = ' '.join(sku_badges) if sku_badges else '-'

        # Format region cells for each category/sub-category
        global_cell = format_region_cell(cat_regions.get('Global', set()), 'Global')
        datazone_cell = format_region_cell(cat_regions.get('Datazone', set()), 'Datazone')
        standard_cell = format_region_cell(cat_regions.get('Standard', set()), 'Standard')
        prov_ptu_cell = format_region_cell(prov_ptu_regions, 'Prov. PTU')
        prov_global_cell = format_region_cell(prov_global_regions, 'Prov. Global')

        # Categories string for filtering (hidden column)
        cats_str = ", ".join(sorted(cat_regions.keys()))
        regions_str = ", ".join(sorted(regions))  # Hidden column for filtering

        rows.append(f"""    <tr>
      <td><a href="{slugify(model)}/"><strong>{model}</strong></a></td>
      <td><span class="badge {bucket_class}">{bucket_label}</span></td>
      <td>{sku_badges_html}</td>
      <td>{global_cell}</td>
      <td>{datazone_cell}</td>
      <td>{standard_cell}</td>
      <td>{prov_ptu_cell}</td>
      <td>{prov_global_cell}</td>
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
      <th>Prov. PTU Regions</th>
      <th>Prov. Global Regions</th>
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
| **Prov. PTU** | Regional reserved throughput capacity (PTU) | High-volume workloads in a specific region |
| **Prov. Global** | Global reserved throughput capacity (PTU) | High-volume workloads with global routing |

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
    total_region_count = max(len(all_regions), 1)
    coverage_pct = round(count / total_region_count * 100)
    bucket_label, bucket_class, bucket_description = pick_bucket(count)

    # Group SKUs by category
    sku_by_category: Dict[str, List[Tuple[str, Set[str]]]] = defaultdict(list)
    for sku, sku_regs in sorted(sku_regions.items()):
        cat = get_sku_category(sku)
        sku_by_category[cat].append((sku, sku_regs))

    # Build retirement section if applicable
    retirement_section = ""
    if retirement_info:
        retirement_section = generate_retirement_section(model, retirement_info, model_regions_lookup or {})

    categories = sorted(sku_by_category.keys())
    category_summary = ", ".join(categories) if categories else "No SKU categories"
    category_chips = " ".join(sku_category_badge(cat) for cat in categories) or '<span class="sku-badge sku-other">No SKU data</span>'

    if sku_regions:
        top_sku, top_sku_regions = max(sku_regions.items(), key=lambda item: (len(item[1]), item[0]))
        top_sku_pct = round(len(top_sku_regions) / total_region_count * 100)
        top_sku_href = query_url("../by-sku/", {"sku": top_sku})
        top_sku_html = f'<a href="{top_sku_href}">{html_escape(top_sku)}</a>'
        top_sku_category = get_sku_category(top_sku)
    else:
        top_sku = "No SKU data"
        top_sku_regions = set()
        top_sku_pct = 0
        top_sku_html = html_escape(top_sku)
        top_sku_category = "Other"

    def render_region_chips(values: Set[str], max_visible: int = 18) -> str:
        sorted_values = sorted(values)
        if not sorted_values:
            return '<span class="model-region-empty">No regions listed</span>'
        chips = [
            region_link(region, prefix="../by-region/", class_name="region-badge model-region-chip")
            for region in sorted_values[:max_visible]
        ]
        remaining = len(sorted_values) - len(chips)
        if remaining:
            chips.append(f'<span class="model-region-more">+{remaining} more in matrix</span>')
        return " ".join(chips)

    metric_cards = f"""<div class="model-profile__metrics" aria-label="Model availability metrics">
    <div class="model-metric">
        <span>Total regions</span>
        <strong>{count}</strong>
    </div>
    <div class="model-metric">
        <span>Coverage</span>
        <strong>{coverage_pct}%</strong>
    </div>
    <div class="model-metric">
        <span>SKU types</span>
        <strong>{len(sku_regions)}</strong>
    </div>
    <div class="model-metric">
        <span>Categories</span>
        <strong>{len(categories)}</strong>
    </div>
</div>"""

    model_profile = f"""<div class="model-profile" aria-label="Model availability profile">
    <div class="model-profile__main">
        <div class="model-profile__badges">
            <span class="badge {bucket_class}">{bucket_label}</span>
            <span class="model-profile__coverage-note">{bucket_description} tracked</span>
        </div>
        <p class="model-profile__lead">Available in <strong>{count}</strong> of <strong>{len(all_regions)}</strong> tracked regions with <strong>{len(sku_regions)}</strong> deployment SKU types.</p>
        <div class="model-profile__chips" aria-label="Deployment categories">{category_chips}</div>
        <div class="model-profile__actions">
            <a class="md-button md-button--primary" href="#deployment-options">Deployment options</a>
            <a class="md-button" href="#full-availability-matrix">Availability matrix</a>
        </div>
    </div>
    {metric_cards}
    <div class="model-profile__insight">
        <span>Widest SKU footprint</span>
        <strong>{top_sku_html}</strong>
        <small>{len(top_sku_regions)} regions · {top_sku_pct}% coverage · {html_escape(top_sku_category)}</small>
    </div>
</div>"""

    deployment_lanes = []
    for cat in ["Global", "Datazone", "Standard", "Provisioned", "Other"]:
        if cat not in sku_by_category:
            continue

        cat_info = SKU_CATEGORIES.get(cat, {})
        description = cat_info.get("description") or "Deployment labels outside the canonical SKU groups"
        use_case = cat_info.get("use_case") or "Review individual SKU labels for deployment behavior."
        compliance = cat_info.get("compliance", "")
        compliance_html = f'<p class="deployment-lane__compliance">{html_escape(compliance)}</p>' if compliance else ""

        sku_rows = []
        all_cat_regions = set()
        for sku, sku_regs in sku_by_category[cat]:
            all_cat_regions.update(sku_regs)
            sku_pct = round(len(sku_regs) / total_region_count * 100)
            meter_pct = max(2, min(sku_pct, 100)) if sku_regs else 0
            sku_href = query_url("../by-sku/", {"sku": sku})
            sku_rows.append(f"""        <div class="deployment-sku-row">
            <div class="deployment-sku-row__copy">
                <a class="deployment-sku-row__name" href="{sku_href}">{html_escape(sku)}</a>
                <span>{len(sku_regs)} regions · {sku_pct}% coverage</span>
            </div>
            <div class="availability-meter" aria-hidden="true"><span style="width: {meter_pct}%;"></span></div>
        </div>""")

        cat_slug = cat.lower().replace(" ", "-")
        deployment_lanes.append(f"""<section class="deployment-lane deployment-lane--{cat_slug}" aria-labelledby="{cat_slug}-deployments">
    <div class="deployment-lane__header">
        <div>
            <div class="deployment-lane__badge">{sku_category_badge(cat)}</div>
            <h3 id="{cat_slug}-deployments">{html_escape(cat)} deployments</h3>
            <p>{html_escape(description)}</p>
        </div>
        <p class="deployment-lane__use-case">{html_escape(use_case)}</p>
    </div>
    <div class="deployment-lane__body">
        <div class="deployment-sku-list">
{chr(10).join(sku_rows)}
        </div>
        <div class="deployment-lane__regions" aria-label="{html_escape(cat)} deployment regions">
            {render_region_chips(all_cat_regions)}
        </div>
        {compliance_html}
    </div>
</section>""")

    deployment_options_html = "\n".join(deployment_lanes) if deployment_lanes else "<p>No deployment SKU information is available for this model.</p>"

    # Build region matrix - which SKUs are available in each region
    # Use HTML table for proper rendering
    sku_labels = sorted(sku_regions.keys())

    # Build HTML table header
    header_cells = "".join([f"<th>{html_escape(sku)}</th>" for sku in sku_labels])

    # Build HTML table rows
    html_rows = []
    for region in sorted(regions):
        cells = []
        for sku in sku_labels:
            if region in sku_regions.get(sku, set()):
                cells.append('<td class="matrix-yes">&#10003;</td>')
            else:
                cells.append('<td class="matrix-no">&mdash;</td>')
        html_rows.append(f"<tr><td><strong>{html_escape(region)}</strong></td>{''.join(cells)}</tr>")

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

{model_profile}
{retirement_section}

## :material-target: Deployment Options

<div class="deployment-lanes">
{deployment_options_html}
</div>

## :material-clipboard-list: Full Availability Matrix

<div class="matrix-intro">
    <strong>Exact region-by-SKU map</strong>
    <span>Use this matrix when you need to verify a specific deployment type in a specific region. Summary chips above intentionally show a compact region preview.</span>
</div>

{matrix_html}

[← Back to All Models](index.md)

_Last updated: {datetime.utcnow():%Y-%m-%d %H:%M UTC}_
"""


def generate_by_region_page(
    model_regions: Dict[str, Set[str]],
    model_region_skus: Dict[str, Dict[str, Set[str]]],
    all_regions: Set[str],
) -> str:
    """Generate the by-region view page with proper SKU tables."""
    
    region_models: Dict[str, Set[str]] = defaultdict(set)
    region_model_skus: Dict[str, Dict[str, Set[str]]] = defaultdict(lambda: defaultdict(set))
    
    for model, regions in model_regions.items():
        for region in regions:
            region_models[region].add(model)
            region_model_skus[region][model] = model_region_skus[model].get(region, set())
    
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

    def _sku_region_badge(region: str) -> str:
        return f'<span class="region-badge" onclick="filterBySkuRegion(\'{region}\')">{region}</span>'

    def _sku_region_cell(regions_set: Set[str]) -> str:
        if not regions_set:
            return '-'
        sorted_regs = sorted(regions_set)
        count = len(sorted_regs)
        badges = [_sku_region_badge(r) for r in sorted_regs]
        if count <= 3:
            return f'<span class="region-list">{" ".join(badges)}</span>'
        preview_regions = ",".join(sorted_regs[:3])
        all_regs_str = ",".join(sorted_regs)
        preview_badges = " ".join(badges[:3])
        return (
            f'<span class="region-list" data-preview-regions="{preview_regions}"'
            f' data-all-regions="{all_regs_str}">'
            f'{preview_badges} <button class="expand-btn" onclick="toggleSkuRegionBadges(this)">'
            f'+{count - 3} more</button></span>'
        )

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
            regions_cell = _sku_region_cell(regions)

            all_rows.append(f"""    <tr>
      <td><a href="../models/{slugify(model)}/"><strong>{model}</strong></a></td>
      <td>{sku_category_badge(cat)}</td>
      <td>{sku_label}</td>
      <td>{regions_cell}</td>
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
    region_options = "\n".join(
        [f'      <option value="{r}">{r}</option>' for r in sorted(all_regions)]
    )

    # Build per-category region sets for the explainer cards
    category_region_sets: Dict[str, Set[str]] = defaultdict(set)
    for label, label_regions in sku_region_sets.items():
        cat = sku_to_category.get(label, "Other")
        category_region_sets[cat].update(label_regions)

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

    # Build per-category SKU type lists for explainer cards
    def _sku_list(cat_name: str) -> str:
        skus = [s for s in sorted_sku_labels if sku_to_category.get(s) == cat_name and sku_model_counts[s] > 0]
        return " · ".join(f"`{s}`" for s in skus) if skus else "-"

    # Per-category stats for explainer cards
    def _cat_stats(cat_name: str) -> tuple:
        models = len(category_model_sets.get(cat_name, set()))
        regions = len(category_region_sets.get(cat_name, set()))
        pct = round(regions / total_regions * 100) if total_regions else 0
        return models, regions, pct

    g_models, g_regions, g_pct = _cat_stats("Global")
    d_models, d_regions, d_pct = _cat_stats("Datazone")
    s_models, s_regions, s_pct = _cat_stats("Standard")
    p_models, p_regions, p_pct = _cat_stats("Provisioned")

    global_skus = _sku_list("Global")
    datazone_skus = _sku_list("Datazone")
    standard_skus = _sku_list("Standard")
    provisioned_skus = _sku_list("Provisioned")

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

## :material-layers-outline: SKU Deployment Types Explained

??? example ":material-earth: Global — Worldwide availability with intelligent routing"

    Routes requests intelligently across Azure regions for maximum availability and throughput.
    Data may be processed in any region within the Azure geography.

    | | |
    |---|---|
    | :material-cube-outline: Models | **{g_models}** |
    | :material-map-marker-outline: Regions | **{g_regions}** ({g_pct}% coverage) |

    **SKU types:** {global_skus}

    **:material-check-circle-outline: Best for:** Applications needing worldwide reach, automatic
    failover, and maximum uptime across Azure's global network.

    **:material-alert-outline: Compliance:** Data may cross region boundaries — not suitable for
    HIPAA, FedRAMP, or strict data-residency requirements.

??? example ":material-shield-lock-outline: Datazone — Data residency compliance deployments"

    Keeps data within a specified geographic zone to satisfy compliance and residency policies.
    Choose the zone; Azure handles routing within that boundary.

    | | |
    |---|---|
    | :material-cube-outline: Models | **{d_models}** |
    | :material-map-marker-outline: Regions | **{d_regions}** ({d_pct}% coverage) |

    **SKU types:** {datazone_skus}

    **:material-check-circle-outline: Best for:** GDPR compliance, data sovereignty requirements,
    regulated industries (finance, healthcare, government).

    **:material-shield-check-outline: Compliance:** Data stays within the specified geographic zone —
    supports GDPR and regional data-residency policies.

??? example ":material-cash-multiple: Standard — Pay-as-you-go regional deployments"

    Pay-as-you-go deployments in a single Azure region with flexible, on-demand scaling.
    No capacity reservation required — you pay only for what you use.

    | | |
    |---|---|
    | :material-cube-outline: Models | **{s_models}** |
    | :material-map-marker-outline: Regions | **{s_regions}** ({s_pct}% coverage) |

    **SKU types:** {standard_skus}

    **:material-check-circle-outline: Best for:** Variable workloads, development and testing,
    cost-sensitive applications, or when you don't need guaranteed throughput.

    **:material-shield-check-outline: Compliance:** Single-region deployment — HIPAA-eligible in
    supported regions with a BAA from Microsoft.

??? example ":material-speedometer: Provisioned (PTU) — Reserved throughput capacity"

    Reserved throughput units (PTUs) guarantee consistent, high-performance inference at scale.
    Capacity is pre-allocated, so latency and throughput are predictable regardless of platform load.

    | | |
    |---|---|
    | :material-cube-outline: Models | **{p_models}** |
    | :material-map-marker-outline: Regions | **{p_regions}** ({p_pct}% coverage) |

    **SKU types:** {provisioned_skus}

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
{chr(10).join(['    ' + r for r in sku_summary_rows])}

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
    <label for="sku-region-filter">Region</label>
    <select id="sku-region-filter" onchange="filterSkuTable()">
      <option value="">All Regions</option>
{region_options}
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


def generate_history_page(history: List[Dict], all_regions: Set[str], known_models: Set[str]) -> str:
    """Generate the change history page with clean grouped format."""
    
    if not history:
        return """# Change History

No changes have been recorded yet.

---

_Last updated: """ + f"{datetime.utcnow():%Y-%m-%d %H:%M UTC}_"
    
    all_rows = flatten_history_changes(history, all_regions, known_models, limit=20)
    all_models = {row["model"] for row in all_rows}
    all_change_regions = {row["region"] for row in all_rows if not row["region"].startswith("(")}
    all_skus = {row["sku"] for row in all_rows if row["sku"] != "-"}
    all_dates = {f"{row['timestamp']:%Y-%m-%d}" for row in all_rows}
    
    # Build filter options
    model_options = "\n".join([f'      <option value="{html_escape(m)}">{html_escape(m)}</option>' for m in sorted(all_models)])
    region_options = "\n".join([f'      <option value="{html_escape(r)}">{html_escape(r)}</option>' for r in sorted(all_change_regions)])
    sku_options = "\n".join([f'      <option value="{html_escape(s)}">{html_escape(s)}</option>' for s in sorted(all_skus)])
    date_options = "\n".join([f'      <option value="{d}">{d}</option>' for d in sorted(all_dates, reverse=True)])
    
    # Build table rows
    table_rows = []
    for row in all_rows:
        timestamp = row["timestamp"]
        change_type = row["change"]
        model = row["model"]
        region = row["region"]
        sku = row["sku"]
        type_badge = '<span class="badge-added">Added</span>' if change_type == "added" else '<span class="badge-removed">Removed</span>'
        date_str = f"{timestamp:%Y-%m-%d}"
        table_rows.append(f'''    <tr>
            <td data-order="{timestamp:%Y%m%d%H%M%S}">{date_str}</td>
            <td>{type_badge}</td>
            <td>{model_link(model, prefix="../models/")}</td>
            <td>{region_link(region, prefix="../by-region/")}</td>
            <td>{sku_link(sku, prefix="../by-sku/", class_name="change-link-pill change-link-pill--sku")}</td>
    </tr>''')

    # Calculate summary stats (per-SKU changes)
    total_additions = sum(1 for row in all_rows if row["change"] == "added")
    total_removals = sum(1 for row in all_rows if row["change"] == "removed")

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
        "history.md": generate_history_page(history, all_regions, set(model_regions.keys())),
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
