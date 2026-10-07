#!/usr/bin/env python3
"""Generate MkDocs pages from AI Foundry model availability snapshot data."""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timedelta, timezone
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


# Slugs of generated model detail pages; populated in main() so links to models
# without a detail page render as plain text instead of 404s.
MODEL_PAGE_SLUGS: Set[str] = set()


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
    """Return a model detail link, or plain text when no detail page exists."""
    slug = slugify(model)
    if MODEL_PAGE_SLUGS and slug not in MODEL_PAGE_SLUGS:
        return html_escape(model)
    class_attr = f' class="{class_name}"' if class_name else ""
    return f'<a{class_attr} href="{prefix}{slug}/">{html_escape(model)}</a>'


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


def generate_lifecycle_section(
    retirement_entries: List[Dict],
    model_regions_lookup: Dict[str, Set[str]],
    today: datetime = None,
) -> str:
    """Render per-version lifecycle tracks (released -> deprecated -> retired) for a model page."""
    today = today or datetime.utcnow()
    if not retirement_entries:
        return """## :material-clock-alert: Lifecycle

<div class="lc-empty">No deprecation or retirement date has been announced for this model in Microsoft's retirement table. See the <a href="../../lifecycle/">lifecycle guide</a> for how dates are set.</div>
"""

    def version_key(entry: Dict) -> str:
        return str(entry.get("version") or "")

    tracks = []
    notes: List[str] = []
    for entry in sorted(retirement_entries, key=version_key, reverse=True):
        stage = entry_stage(entry, today)
        label, tone, _ = LIFECYCLE_STAGES[stage]
        released, _ = parse_lifecycle_date(entry.get("version"))
        deprecated, dep_est = parse_lifecycle_date(entry.get("deprecation_date"))
        retires, ret_est = parse_lifecycle_date(entry.get("retirement_date"))

        start = released or (deprecated - timedelta(days=365) if deprecated else None) or (retires - timedelta(days=548) if retires else None) or today - timedelta(days=180)
        end = retires or (deprecated + timedelta(days=180) if deprecated else None) or today + timedelta(days=180)
        span_end = max(end, today)
        span = max((span_end - start).days, 1)

        def pct(value: datetime) -> float:
            return min(max((value - start).days / span * 100, 0), 100)

        first_phase = "preview" if (entry.get("status") or "").lower() == "preview" else "ga"
        segments = []
        ga_end = deprecated or end
        segments.append(f'<span class="lc-seg lc-seg--{first_phase}" style="left:0;width:{pct(ga_end):.2f}%"></span>')
        if deprecated and deprecated < end:
            segments.append(f'<span class="lc-seg lc-seg--deprecated{" lc-seg--estimate" if dep_est else ""}" style="left:{pct(deprecated):.2f}%;width:{pct(end) - pct(deprecated):.2f}%"></span>')
        if retires and today > retires:
            segments.append(f'<span class="lc-seg lc-seg--retired" style="left:{pct(retires):.2f}%;width:{100 - pct(retires):.2f}%"></span>')
        if not retires:
            segments.append('<span class="lc-seg lc-seg--open" style="left:calc(100% - 2rem);width:2rem"></span>')
        today_pct = pct(today)
        today_class = " lc-today--end" if today_pct > 88 else " lc-today--start" if today_pct < 12 else ""
        segments.append(f'<span class="lc-today{today_class}" style="left:{today_pct:.2f}%"><em>Today</em></span>')

        date_bits = []
        if released:
            date_bits.append(f"<span><b>Released</b> {format_short_date(released)}</span>")
        if deprecated:
            date_bits.append(f"<span><b>{'Deprecates' if deprecated > today else 'Deprecated'}</b> {'≥ ' if dep_est else ''}{format_short_date(deprecated)}</span>")
        if retires:
            verb = "Retired" if retires < today and not ret_est else "Retires"
            date_bits.append(f"<span><b>{verb}</b> {'≥ ' if ret_est else ''}{format_short_date(retires)}</span>")
        else:
            date_bits.append("<span><b>Retires</b> not announced</span>")

        countdown = ""
        if retires:
            days = (retires - today).days
            countdown = f'<span class="lc-version__countdown lc-version__countdown--{tone}">{"No earlier than " if ret_est else ""}{format_countdown(days)}</span>' if days >= 0 or not ret_est else '<span class="lc-version__countdown lc-version__countdown--warning">Date passed · may retire any time</span>'

        replacement_html = ""
        replacement = entry.get("replacement")
        if replacement:
            replacement_slug = slugify(replacement)
            if replacement_slug in model_regions_lookup:
                replacement_html = f'<div class="lc-version__replacement">Replacement <a href="../{replacement_slug}/">{html_escape(replacement)}</a> <span>{len(model_regions_lookup[replacement_slug])} regions</span></div>'
            else:
                replacement_html = f'<div class="lc-version__replacement">Replacement <code>{html_escape(replacement)}</code> <span>not yet tracked</span></div>'

        note = entry.get("retirement_note")
        if note and note not in notes:
            notes.append(note)

        tracks.append(f"""<div class="lc-version lc-version--{tone}">
    <div class="lc-version__head">
        <code>{html_escape(version_key(entry) or '-')}</code>
        <span class="lc-badge lc-badge--{tone}"{tip_attrs(LIFECYCLE_EXPLAINERS[stage]['title'], LIFECYCLE_EXPLAINERS[stage]['body'] + ' ' + LIFECYCLE_EXPLAINERS[stage]['action'])}>{html_escape(label)}</span>
        {countdown}
    </div>
    <div class="lc-bar" aria-hidden="true">{''.join(segments)}</div>
    <div class="lc-version__dates">{''.join(date_bits)}</div>
    {replacement_html}
</div>""")

    notes_html = "".join(
        f'\n!!! note "Retirement date update"\n    {note}\n'
        for note in notes
    )
    return f"""## :material-clock-alert: Lifecycle

<div class="lc-versions">
{chr(10).join(tracks)}
</div>
{notes_html}
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

- [Foundry Models Lifecycle & Support Policy](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirements)
- [Model Deprecation and Retirement](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirements)
- [Migration Best Practices](https://learn.microsoft.com/azure/foundry-classic/openai/how-to/migration)

---

_Data sourced from [Microsoft Azure AI Documentation](https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/articles/foundry/openai/includes/retirement/models.md)_

_Last updated: {datetime.utcnow():%Y-%m-%d %H:%M UTC}_
"""


MODEL_FAMILY_RULES: List[Tuple[Tuple[str, ...], str]] = [
    (("claude",), "Anthropic"),
    (("cohere", "embed-v"), "Cohere"),
    (("deepseek",), "DeepSeek"),
    (("flux",), "Black Forest Labs"),
    (("grok",), "xAI"),
    (("llama",), "Meta"),
    (("phi-", "mai-"), "Microsoft"),
    (("mistral", "ministral", "codestral"), "Mistral AI"),
    (("stable",), "Stability AI"),
    (("kimi",), "Moonshot AI"),
    (("gpt", "o1", "o3", "o4", "codex", "dall-e", "sora", "whisper", "tts",
      "text-embedding", "computer-use", "model-router"), "OpenAI"),
]

LIFECYCLE_STAGES: Dict[str, Tuple[str, str, int]] = {
    # key: (label, css tone, urgency rank - lower is more urgent)
    "soon": ("Retiring within 30 days", "danger", 0),
    "retiring": ("Retiring within 90 days", "warning", 1),
    "pending": ("Retirement imminent", "warning", 2),
    "deprecated": ("Deprecated", "caution", 3),
    "preview": ("Preview", "info", 4),
    "ga": ("Generally available", "success", 5),
    "retired": ("Retired", "muted", 6),
    "untracked": ("No retirement date", "neutral", 7),
}


def model_family(name: str) -> str:
    """Return the provider family for a model name."""
    lowered = name.lower()
    for prefixes, family in MODEL_FAMILY_RULES:
        if lowered.startswith(prefixes):
            return family
    return "Partner"


def parse_lifecycle_date(value: str) -> Tuple[datetime, bool]:
    """Parse a lifecycle date. Returns (date or None, is_not_earlier_than)."""
    if not value:
        return None, False
    text = str(value).strip()
    estimate = False
    if text.lower().startswith("no earlier than"):
        text = text[len("no earlier than"):].strip()
        estimate = True
    try:
        return datetime.strptime(text, "%Y-%m-%d"), estimate
    except ValueError:
        return None, estimate


def format_short_date(value: datetime) -> str:
    return f"{value:%b} {value.day}, {value:%Y}"


def format_countdown(days: int) -> str:
    if days < 0:
        return f"{pluralize(-days, 'day')} ago"
    if days == 0:
        return "today"
    if days < 60:
        return f"in {pluralize(days, 'day')}"
    return f"in {round(days / 30.4)} months"


def entry_stage(entry: Dict, today: datetime) -> str:
    """Classify a single retirement-data entry into a lifecycle stage key."""
    retire_dt, retire_est = parse_lifecycle_date(entry.get("retirement_date"))
    deprecate_dt, deprecate_est = parse_lifecycle_date(entry.get("deprecation_date"))
    if retire_dt:
        days = (retire_dt - today).days
        if days < 0:
            return "pending" if retire_est else "retired"
        if days <= 30:
            return "soon"
        if days <= 90:
            return "retiring"
    if deprecate_dt and not deprecate_est and deprecate_dt <= today:
        return "deprecated"
    if (entry.get("status") or "").lower() == "preview":
        return "preview"
    return "ga"


def summarize_model_lifecycle(entries: List[Dict], today: datetime) -> Dict:
    """Return the headline lifecycle state for a model across all its versions."""
    if not entries:
        label, tone, _ = LIFECYCLE_STAGES["untracked"]
        return {"key": "untracked", "label": label, "tone": tone}

    staged = [(entry_stage(entry, today), entry) for entry in entries]
    active = [(stage, entry) for stage, entry in staged if stage != "retired"]
    pool = active or staged
    stage, entry = min(pool, key=lambda item: LIFECYCLE_STAGES[item[0]][2])
    label, tone, _ = LIFECYCLE_STAGES[stage]
    summary = {"key": stage, "label": label, "tone": tone, "version": entry.get("version", "")}

    upcoming = []
    for _, item in active:
        retire_dt, estimate = parse_lifecycle_date(item.get("retirement_date"))
        if retire_dt and retire_dt >= today:
            upcoming.append((retire_dt, estimate, item))
    if upcoming:
        retire_dt, estimate, item = min(upcoming, key=lambda value: value[0])
        summary.update({
            "next_date": f"{retire_dt:%Y-%m-%d}",
            "next_label": ("No earlier than " if estimate else "") + format_short_date(retire_dt),
            "days": (retire_dt - today).days,
            "estimate": estimate,
            "replacement": item.get("replacement") or "",
        })
    else:
        replacements = [item.get("replacement") for _, item in staged if item.get("replacement")]
        if replacements:
            summary["replacement"] = replacements[0]
    return summary


def lifecycle_badge(summary: Dict) -> str:
    title, body = lifecycle_tip_text(summary)
    return f'<span class="lc-badge lc-badge--{summary["tone"]}"{tip_attrs(title, body)}>{html_escape(lifecycle_badge_text(summary))}</span>'


def build_model_lifecycles(model_regions: Dict[str, Set[str]], retirement_index: Dict[str, List[Dict]], today: datetime) -> Dict[str, Dict]:
    return {
        model: summarize_model_lifecycle(retirement_index.get(slugify(model), []), today)
        for model in model_regions
    }


def build_model_finder_data(
    model_regions: Dict[str, Set[str]],
    model_sku_regions: Dict[str, Dict[str, Set[str]]],
    lifecycles: Dict[str, Dict],
) -> List[Dict]:
    """Compact per-model records for the client-side model finder."""
    records = []
    for model in sorted(model_regions, key=str.lower):
        categories = sorted({get_sku_category(sku) for sku in model_sku_regions[model]} - {"Other"})
        lifecycle = lifecycles.get(model, {})
        record = {
            "n": model,
            "s": slugify(model),
            "f": model_family(model),
            "r": len(model_regions[model]),
            "c": categories,
            "lk": lifecycle.get("key", "untracked"),
            "ll": lifecycle.get("label", ""),
            "lt": lifecycle.get("tone", "neutral"),
        }
        if lifecycle.get("next_label"):
            record["nd"] = lifecycle["next_label"]
            record["dd"] = lifecycle["days"]
        if lifecycle.get("replacement"):
            record["rp"] = lifecycle["replacement"]
            record["rs"] = slugify(lifecycle["replacement"]) if slugify(lifecycle["replacement"]) in MODEL_PAGE_SLUGS else ""
        records.append(record)
    return records


# ---------------------------------------------------------------------------
# Availability explorer, plain-language glossaries and dashboard charts
# ---------------------------------------------------------------------------

# Deployment types shown in the explorer. Each raw snapshot SKU key maps to one bit.
DEPLOYMENT_TYPES: List[Dict] = [
    {"k": "gs", "bit": 1, "group": "paygo", "label": "Global Standard", "short": "Global",
     "tip": "Pay per token. Requests can be processed in any Azure region worldwide. Highest default quota — the best place to start."},
    {"k": "dz", "bit": 2, "group": "paygo", "label": "Data Zone Standard", "short": "Data Zone",
     "tip": "Pay per token. Processing stays inside the Microsoft-defined data zone (US or EU)."},
    {"k": "rs", "bit": 4, "group": "paygo", "label": "Regional Standard", "short": "Regional",
     "tip": "Pay per token. Processing stays in the region you deploy to."},
    {"k": "gp", "bit": 8, "group": "ptu", "label": "Global Provisioned (PTU)", "short": "Global PTU",
     "tip": "Reserved throughput (PTUs) billed hourly or via reservation. Processing can happen in any Azure region."},
    {"k": "dp", "bit": 16, "group": "ptu", "label": "Data Zone Provisioned (PTU)", "short": "Data Zone PTU",
     "tip": "Reserved throughput (PTUs) with processing kept inside the data zone (US or EU)."},
    {"k": "rp", "bit": 32, "group": "ptu", "label": "Regional Provisioned (PTU)", "short": "Regional PTU",
     "tip": "Reserved throughput (PTUs) with processing kept in the deployment region."},
    {"k": "bt", "bit": 64, "group": "batch", "label": "Batch", "short": "Batch",
     "tip": "Asynchronous jobs with a 24-hour target turnaround at a lower price than Standard."},
    {"k": "mp", "bit": 128, "group": "partner", "label": "Partner / Marketplace", "short": "Partner",
     "tip": "Partner model deployed as a serverless API, typically billed through Azure Marketplace."},
    {"k": "av", "bit": 256, "group": "other", "label": "Listed (type not published)", "short": "Listed",
     "tip": "Microsoft lists the model in this region but the deployment type is not broken out."},
]
DEPLOYMENT_TYPE_BY_KEY = {item["k"]: item for item in DEPLOYMENT_TYPES}

SKU_KEY_TO_TYPE: Dict[str, str] = {
    "standard-global": "gs",
    "standard-global-by-capability": "gs",
    "standard-global-priority-processing": "gs",
    "datazone-standard": "dz",
    "datazone-standard-gov": "dz",
    "datazone-standard-priority-processing": "dz",
    "deployments-standard": "rs",
    "standard-models": "rs",
    "standard-models-gov": "rs",
    "provisioned-global": "gp",
    "datazone-provisioned-managed": "dp",
    "datazone-provisioned-managed-gov": "dp",
    "provisioned-models": "rp",
    "provisioned-models-gov": "rp",
    "deployments-provisioned": "rp",
    "global-batch": "bt",
    "global-batch-datazone": "bt",
    "deployments-batch": "bt",
    "marketplace-deployments-standard": "mp",
    "region-availability-maas": "mp",
}

REGION_GEOS: List[str] = ["Americas", "Europe", "Asia Pacific", "Middle East & Africa", "US Government"]


def sku_type_key(sku_key: str, label: str = "") -> str:
    """Map a raw snapshot SKU key to an explorer deployment type key."""
    if sku_key in SKU_KEY_TO_TYPE:
        return SKU_KEY_TO_TYPE[sku_key]
    text = f"{sku_key} {label}".lower()
    if "batch" in text:
        return "bt"
    if "provisioned" in text or "ptu" in text:
        if "global" in text:
            return "gp"
        return "dp" if "datazone" in text or "data zone" in text else "rp"
    if "marketplace" in text or "maas" in text:
        return "mp"
    if "datazone" in text or "data zone" in text:
        return "dz"
    if "global" in text:
        return "gs"
    if "standard" in text:
        return "rs"
    return "av"


def region_geo(region: str) -> str:
    lowered = region.lower()
    if lowered.startswith("usgov") or "gov" in lowered:
        return "US Government"
    if "us" in lowered.split() or any(token in lowered for token in ("canada", "brazil", "mexico", "chile")):
        return "Americas"
    if any(token in lowered for token in ("uae", "qatar", "saudi", "israel", "africa")):
        return "Middle East & Africa"
    if any(token in lowered for token in ("asia", "japan", "korea", "australia", "india", "indonesia", "malaysia", "new zealand", "taiwan")):
        return "Asia Pacific"
    return "Europe"


def build_availability_bits(data: Dict[str, dict]) -> Dict[str, Dict[str, int]]:
    """Return model -> region -> bitmask of explorer deployment types."""
    bits: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for model, payload in data.items():
        for sku_key, sku in payload.get("skus", {}).items():
            type_bit = DEPLOYMENT_TYPE_BY_KEY[sku_type_key(sku_key, sku.get("label", ""))]["bit"]
            for region in sku.get("regions", []):
                bits[model][region] |= type_bit
        for region in payload.get("all", []):
            if not bits[model][region]:
                bits[model][region] = DEPLOYMENT_TYPE_BY_KEY["av"]["bit"]
    return bits


# Plain-language explanations for every lifecycle badge.
LIFECYCLE_EXPLAINERS: Dict[str, Dict[str, str]] = {
    "soon": {
        "title": "Retiring within 30 days",
        "body": "This version is switched off on its retirement date; after that every request returns 410 Gone. Standard deployments may be auto-upgraded to the replacement — provisioned (PTU) deployments are not.",
        "action": "Move traffic to the replacement now.",
    },
    "retiring": {
        "title": "Retiring within 90 days",
        "body": "A firm retirement date is less than three months away. Existing deployments keep working until then. PTU deployments must be migrated by hand.",
        "action": "Test the replacement and plan the cut-over.",
    },
    "pending": {
        "title": "Retirement imminent",
        "body": "Microsoft said this version retires no earlier than a date that has now passed, so it can be switched off at any time once notice is given.",
        "action": "Treat it as retiring now — migrate.",
    },
    "deprecated": {
        "title": "Deprecated",
        "body": "No longer available to new customers. Subscriptions that already deployed this version can keep creating and managing deployments until it retires.",
        "action": "Don't start new work on it; schedule a migration before retirement.",
    },
    "preview": {
        "title": "Preview",
        "body": "Experimental: weights, runtime and API might change and it is not guaranteed to reach GA. When it retires it is force-upgraded or removed with at least 30 days notice.",
        "action": "Great for evaluation — avoid for critical production.",
    },
    "ga": {
        "title": "Generally available",
        "body": "Production-ready: weights and APIs are fixed and new deployments are allowed. Most GA models get about 18 months before retirement (12 for some partner models).",
        "action": "Safe to build on — note the retirement date in your roadmap.",
    },
    "retired": {
        "title": "Retired",
        "body": "Removed from service. All inference requests return 410 Gone.",
        "action": "Use the replacement model.",
    },
    "untracked": {
        "title": "No retirement date published",
        "body": "Microsoft's retirement tables don't list a date for this model yet (common for new and partner models).",
        "action": "Check the model card in Foundry before committing long-term.",
    },
}


def lifecycle_tip_text(summary: Dict) -> Tuple[str, str]:
    """Return (title, body) for a lifecycle badge tooltip."""
    key = summary.get("key", "untracked")
    info = LIFECYCLE_EXPLAINERS.get(key, LIFECYCLE_EXPLAINERS["untracked"])
    parts = [info["body"]]
    if summary.get("next_label"):
        version = summary.get("version")
        parts.append(f"Next retirement: {summary['next_label']}" + (f" (version {version})" if version else "") + ".")
    if summary.get("replacement"):
        parts.append(f"Replacement: {summary['replacement']}.")
    parts.append(info["action"])
    return info["title"], " ".join(parts)


def lifecycle_badge_text(summary: Dict) -> str:
    key = summary.get("key")
    days = summary.get("days")
    if key in ("soon", "retiring") and days is not None:
        return f"Retires in {pluralize(days, 'day')}"
    if key == "ga" and summary.get("next_date"):
        retire_dt = datetime.strptime(summary["next_date"], "%Y-%m-%d")
        return f"GA · until {'≥ ' if summary.get('estimate') else ''}{retire_dt:%b %Y}"
    return summary.get("label", "")


def tip_attrs(title: str, body: str) -> str:
    return f' tabindex="0" data-tip-title="{html_escape(title)}" data-tip="{html_escape(body)}"'


def build_explorer_data(
    model_regions: Dict[str, Set[str]],
    model_sku_regions: Dict[str, Dict[str, Set[str]]],
    lifecycles: Dict[str, Dict],
    availability_bits: Dict[str, Dict[str, int]],
    all_regions: Set[str],
    today: datetime,
) -> Dict:
    """Single JSON payload behind the model finder and the availability explorer."""
    regions = sorted(all_regions, key=lambda region: (REGION_GEOS.index(region_geo(region)), region.lower()))
    models = build_model_finder_data(model_regions, model_sku_regions, lifecycles)
    for record in models:
        model_bits = availability_bits.get(record["n"], {})
        record["a"] = [model_bits.get(region, 0) for region in regions]
        if record.get("lk") in LIFECYCLE_EXPLAINERS:
            title, body = lifecycle_tip_text(lifecycles.get(record["n"], {"key": record["lk"]}))
            record["lb"] = lifecycle_badge_text(lifecycles.get(record["n"], {"key": record["lk"], "label": record["ll"]}))
            record["tip"] = body
    return {
        "generated": f"{today:%Y-%m-%d}",
        "regions": [{"n": region, "g": region_geo(region)} for region in regions],
        "geos": REGION_GEOS,
        "types": [{key: item[key] for key in ("k", "bit", "group", "label", "short", "tip")} for item in DEPLOYMENT_TYPES],
        "stages": {
            key: {"label": LIFECYCLE_STAGES[key][0], "tone": LIFECYCLE_STAGES[key][1], **LIFECYCLE_EXPLAINERS[key]}
            for key in LIFECYCLE_STAGES
        },
        "models": models,
    }


# ----------------------------- charts ------------------------------------

CHART_STAGE_GROUPS: List[Tuple[str, str, Tuple[str, ...], str]] = [
    # (filter key, label, stage keys, tone)
    ("risk", "Retiring ≤ 90 days", ("soon", "retiring", "pending"), "danger"),
    ("deprecated", "Deprecated", ("deprecated",), "caution"),
    ("preview", "Preview", ("preview",), "info"),
    ("ga", "Generally available", ("ga",), "success"),
    ("untracked", "No date published", ("untracked",), "neutral"),
    ("retired", "Retired", ("retired",), "muted"),
]


GEO_TONES = {
    "Americas": "americas",
    "Europe": "europe",
    "Asia Pacific": "apac",
    "Middle East & Africa": "mea",
    "US Government": "gov",
}

# Land mask for the dotted world map: Natural Earth 1:110m land (public domain),
# rasterized to a 2.5° grid starting at 80°N / 180°W. Rows are ';'-separated,
# each a list of "startColumn+runLength" land runs.
WORLD_GRID_COLS, WORLD_GRID_STEP, WORLD_GRID_TOP = 144, 2.5, 80.0
WORLD_LAND_RLE = "33+11,45+20,78+5,109+3;24+2,37+4,44+20,78+1,113+1;27+2,32+8,49+15,94+2,107+10,127+3,131+1;22+2,25+3,29+1,31+2,34+1,36+4,50+13,93+1,100+1,104+20,128+2;7+8,25+7,34+1,38+2,41+4,50+13,80+4,99+2,102+34,140+1;0+2,6+22,29+10,41+1,43+3,51+8,78+10,91+10,102+42;2+1,5+32,38+1,41+4,51+5,63+3,76+4,82+4,88+56;6+29,38+1,44+1,52+3,74+5,80+57,138+6;5+8,15+19,41+3,74+5,81+1,84+50,137+2;9+2,19+16,41+6,70+1,77+2,82+46,135+2;6+1,20+19,41+8,70+1,75+1,80+46,134+3;21+18,41+9,68+1,70+3,74+55,134+1;21+24,49+1,72+56,129+1;22+24,50+1,71+57;22+23,46+1,71+6,78+6,85+1,87+40;22+22,68+5,75+3,79+4,89+35,128+1;22+20,68+4,75+1,78+1,80+2,83+37,121+2,128+1;23+18,68+4,77+1,83+38,123+1,127+1;24+18,69+7,85+35,125+3;25+15,68+10,80+1,86+34,124+1;27+9,38+1,68+23,92+29;26+1,28+5,39+1,67+18,86+6,93+27;27+1,29+4,66+20,87+6,94+1,99+22;30+3,38+2,65+22,88+8,100+8,109+9;30+3,36+1,41+1,65+22,88+7,101+5,109+5;31+6,66+21,89+5,101+4,110+5,120+1;35+4,65+23,89+3,102+2,111+5,120+1;37+2,65+24,102+2,111+1,113+3,120+1;38+1,42+1,44+3,66+26,102+2,111+1,114+1,119+1;41+8,67+25,104+1,122+1;41+10,68+2,71+1,74+17,110+1,112+1,118+2;41+11,76+14,111+1,113+1,117+2;40+12,76+13,112+2,116+3;40+15,76+12,112+2,116+3,120+1,125+3;39+18,77+11,127+3;40+18,77+11,115+2,127+4;41+17,77+11,121+1,131+1;41+16,77+11,124+3;42+14,77+11,91+1,122+4,129+1;43+13,77+10,90+2,121+9;44+12,77+9,90+1,120+11;44+11,78+8,89+2,117+15;44+9,78+8,90+1,117+16;44+9,78+7,118+15;43+9,79+5,118+15;43+8,79+4,118+4,126+7;43+6,127+5;43+6,128+4;43+4,142+1;42+5,130+1,140+1;42+4,139+1;42+4;42+3;42+2;44+2"

# Approximate datacenter locations (lat, lon) for Azure regions.
REGION_COORDS: Dict[str, Tuple[float, float]] = {
    "Brazil South": (-23.55, -46.63), "Brazil Southeast": (-22.9, -43.2),
    "Canada Central": (43.65, -79.38), "Canada East": (46.81, -71.21),
    "Central US": (41.59, -93.6), "East US": (37.37, -79.82), "East US 2": (36.67, -78.39),
    "North Central US": (41.88, -87.63), "South Central US": (29.42, -98.49),
    "West Central US": (41.14, -104.82), "West US": (37.78, -122.42),
    "West US 2": (47.23, -119.85), "West US 3": (33.45, -112.07),
    "Mexico Central": (20.59, -100.39), "Chile Central": (-33.45, -70.67),
    "France Central": (46.37, 2.37), "France South": (43.83, 2.21),
    "Germany West Central": (50.11, 8.68), "Germany North": (53.07, 8.81),
    "Italy North": (45.46, 9.19), "North Europe": (53.35, -6.26), "West Europe": (52.37, 4.9),
    "Norway East": (59.91, 10.75), "Norway West": (58.97, 5.73), "Poland Central": (52.23, 21.01),
    "Spain Central": (40.42, -3.7), "Sweden Central": (60.67, 17.14), "Sweden South": (55.6, 13.0),
    "Switzerland North": (47.45, 8.56), "Switzerland West": (46.2, 6.14),
    "UK South": (51.51, -0.13), "UK West": (51.48, -3.18), "Austria East": (48.21, 16.37),
    "Belgium Central": (50.85, 4.35), "Denmark East": (55.68, 12.57),
    "Australia East": (-33.86, 151.21), "Australia Southeast": (-37.81, 144.96),
    "Australia Central": (-35.28, 149.13), "Japan East": (35.68, 139.77), "Japan West": (34.69, 135.5),
    "Korea Central": (37.57, 126.98), "Korea South": (35.18, 129.08),
    "South India": (12.98, 80.16), "Central India": (18.52, 73.86), "West India": (19.08, 72.88),
    "Southeast Asia": (1.28, 103.83), "East Asia": (22.27, 114.19),
    "Indonesia Central": (-6.2, 106.85), "Malaysia West": (3.14, 101.69),
    "New Zealand North": (-36.85, 174.76), "Taiwan North": (25.03, 121.57),
    "South Africa North": (-25.73, 28.22), "South Africa West": (-34.08, 18.42),
    "UAE North": (25.27, 55.3), "UAE Central": (24.47, 54.37), "Qatar Central": (25.29, 51.53),
    "Israel Central": (31.77, 35.21), "Saudi Arabia East": (26.4, 50.1),
    "usgovarizona": (33.45, -112.07), "usgovvirginia": (37.37, -79.82), "usgovtexas": (29.42, -98.49),
}


def _fmt_num(value: int) -> str:
    return f"{value:,}"


def render_lifecycle_waffle(lifecycles: Dict[str, Dict], href_prefix: str, model_prefix: str = "models/") -> str:
    """One square per model, ordered most-urgent first."""
    order = {stage: index for index, (_, _, stages, _) in enumerate(CHART_STAGE_GROUPS) for stage in stages}
    tone_of = {stage: tone for _, _, stages, tone in CHART_STAGE_GROUPS for stage in stages}
    ranked = sorted(
        lifecycles.items(),
        key=lambda item: (order.get(item[1]["key"], 99), item[1].get("days", 10**6), item[0].lower()),
    )
    cells = []
    for model, summary in ranked:
        tone = tone_of.get(summary["key"], "neutral")
        detail = summary.get("label", "")
        if summary.get("next_label"):
            detail += f" · retires {summary['next_label']}"
            if summary.get("days") is not None:
                detail += f" ({pluralize(summary['days'], 'day')})"
        if summary.get("replacement"):
            detail += f" · move to {summary['replacement']}"
        cells.append(
            f'<a class="waffle__cell waffle__cell--{tone}" href="{model_prefix}{slugify(model)}/"'
            f'{tip_attrs(model, detail)} aria-label="{html_escape(model)}: {html_escape(summary.get("label", ""))}"></a>'
        )
    legend = []
    total = len(lifecycles) or 1
    for key, label, stages, tone in CHART_STAGE_GROUPS:
        count = sum(1 for summary in lifecycles.values() if summary["key"] in stages)
        if count:
            legend.append(
                f'<li><a href="{href_prefix}#lc={key}"><span class="chart-swatch chart-swatch--{tone}"></span>'
                f'{label}<b>{count}</b><small>{count / total * 100:.0f}%</small></a></li>'
            )
    return f"""<div class="waffle" role="img" aria-label="{len(lifecycles)} models by lifecycle stage">{''.join(cells)}</div>
    <ul class="chart-legend waffle-legend">{''.join(legend)}</ul>"""


def render_retirement_runway(retirement_data: Dict, today: datetime, available_slugs: Set[str], days: int = 364) -> Tuple[str, str]:
    """Beeswarm timeline of version retirements over the next year. Returns (html, subtitle)."""
    bins: Dict[int, List[Tuple]] = defaultdict(list)
    later = 0
    items = []
    for category, entries in retirement_data.get("models", {}).items():
        if category == "fine_tuned":
            continue
        for entry in entries:
            retire_dt, estimate = parse_lifecycle_date(entry.get("retirement_date"))
            if not retire_dt or retire_dt < today:
                continue
            offset = (retire_dt - today).days
            if offset > days:
                later += 1
                continue
            items.append((offset, retire_dt, estimate, entry))
    items.sort(key=lambda item: (item[0], item[3].get("model", "")))
    for item in items:
        bins[item[0] // 7].append(item)

    dots = []
    for week, members in bins.items():
        x = (week * 7 + 3.5) / days * 100
        for stack, (offset, retire_dt, estimate, entry) in enumerate(members):
            model = entry.get("model", "")
            version = entry.get("version", "")
            tone = "danger" if offset <= 30 else "warning" if offset <= 90 else "info"
            slug = slugify(model)
            href = f"models/{slug}/" if slug in available_slugs else "retirements/"
            body = f"{'No earlier than ' if estimate else 'Retires '}{format_short_date(retire_dt)} · in {pluralize(offset, 'day')}"
            if entry.get("replacement"):
                body += f" · replacement: {entry['replacement']}"
            dots.append(
                f'<a class="rw-dot rw-dot--{tone}{" rw-dot--est" if estimate else ""}" href="{href}" '
                f'style="--x:{x:.2f}%;--y:{stack}"{tip_attrs(f"{model} {version}".strip(), body)}></a>'
            )
    rows = max((len(members) for members in bins.values()), default=1)

    ticks = []
    cursor = datetime(today.year, today.month, 1)
    while True:
        month = cursor.month + 1
        cursor = datetime(cursor.year + (month > 12), (month - 1) % 12 + 1, 1)
        offset = (cursor - today).days
        if offset > days:
            break
        label = f"{cursor:%b}" + (f" ’{cursor:%y}" if cursor.month == 1 else "")
        ticks.append(f'<span class="rw-tick" style="--x:{offset / days * 100:.2f}%">{label}</span>')

    band30, band90 = 30 / days * 100, 90 / days * 100
    soon = sum(1 for item in items if item[0] <= 30)
    nxt = items[0] if items else None
    subtitle = f"{pluralize(len(items), 'version')} retire in the next 12 months"
    if nxt:
        subtitle += f" · next in {pluralize(nxt[0], 'day')}"
    later_html = f'<span class="rw-later">+{later} later</span>' if later else ""
    html = f"""<div class="runway" style="--rows:{rows}">
        <div class="rw-plot">
            <span class="rw-band rw-band--danger" style="--x0:0%;--x1:{band30:.2f}%"><em>≤ 30 days · {soon}</em></span>
            <span class="rw-band rw-band--warning" style="--x0:{band30:.2f}%;--x1:{band90:.2f}%"><em>≤ 90 days</em></span>
            <span class="rw-today"><em>Today</em></span>
            {''.join(dots)}
        </div>
        <div class="rw-axis">{''.join(ticks)}{later_html}</div>
    </div>
    <p class="chart-note"><span class="rw-key rw-key--firm"></span>Firm date <span class="rw-key rw-key--est"></span>No-earlier-than date · one dot per model version, hover for details</p>"""
    return html, subtitle


def world_land_path() -> str:
    parts = []
    for row, runs in enumerate(WORLD_LAND_RLE.split(";")):
        for run in filter(None, runs.split(",")):
            start, length = run.split("+")
            parts.append(f"M{start} {row}h{length}v1h-{length}z")
    return "".join(parts)


def project_lat_lon(lat: float, lon: float) -> Tuple[float, float]:
    return (lon + 180) / WORLD_GRID_STEP, (WORLD_GRID_TOP - lat) / WORLD_GRID_STEP + 0.5


def render_world_map(model_regions: Dict[str, Set[str]], all_regions: Set[str], href_prefix: str, top: int = 10) -> str:
    counts: Dict[str, int] = defaultdict(int)
    for regions in model_regions.values():
        for region in regions:
            counts[region] += 1
    peak = max(counts.values(), default=1) or 1
    total = len(model_regions)
    rows = int(WORLD_LAND_RLE.count(";")) + 1
    bubbles = []
    for region in sorted(all_regions, key=lambda r: -counts[r]):
        coords = REGION_COORDS.get(region)
        if not coords:
            continue
        x, y = project_lat_lon(*coords)
        radius = 0.55 + 1.85 * (counts[region] / peak) ** 0.5
        tone = GEO_TONES.get(region_geo(region), "europe")
        bubbles.append(
            f'<a href="{href_prefix}#rg={quote(region)}" data-region="{html_escape(region)}"'
            f'{tip_attrs(region, f"{counts[region]} of {total} models available here · {region_geo(region)}. Click to see which.")}>'
            f'<circle class="wmap__bubble wmap__bubble--{tone}" cx="{x:.2f}" cy="{y:.2f}" r="{radius:.2f}"/></a>'
        )
    ranked = sorted(all_regions, key=lambda r: (-counts[r], r))
    list_items = "".join(
        f'<li><a href="{href_prefix}#rg={quote(region)}" data-region="{html_escape(region)}">'
        f'<span class="wmap-rank__dot wmap-rank__dot--{GEO_TONES.get(region_geo(region), "europe")}"></span>'
        f'<span class="wmap-rank__name">{html_escape(region)}</span>'
        f'<span class="wmap-rank__bar"><span style="width:{counts[region] / peak * 100:.1f}%"></span></span>'
        f'<b>{counts[region]}</b></a></li>'
        for region in ranked[:top]
    )
    geo_counts = defaultdict(int)
    for region in all_regions:
        geo_counts[region_geo(region)] += 1
    geo_legend = "".join(
        f'<li><span class="wmap-rank__dot wmap-rank__dot--{GEO_TONES[geo]}"></span>{geo} <b>{geo_counts[geo]}</b></li>'
        for geo in REGION_GEOS if geo_counts.get(geo)
    )
    return f"""<div class="wmap-wrap" data-wmap>
        <figure class="wmap-figure">
            <svg class="wmap" viewBox="0 -0.5 {WORLD_GRID_COLS} {rows + 0.5}" role="img" aria-label="Azure regions sized by number of available models">
                <defs><pattern id="wmap-dot" width="1" height="1" patternUnits="userSpaceOnUse"><circle cx="0.5" cy="0.5" r="0.3"/></pattern></defs>
                <path class="wmap__land" d="{world_land_path()}" fill="url(#wmap-dot)"/>
                <g class="wmap__bubbles">{''.join(bubbles)}</g>
            </svg>
            <ul class="wmap-legend">{geo_legend}<li class="wmap-legend__size"><i></i><i></i><i></i>more models</li></ul>
        </figure>
        <div class="wmap-rank">
            <h4>Top regions</h4>
            <ol>{list_items}</ol>
            <a class="wmap-rank__more" href="by-region/">All {len(all_regions)} regions {icon("arrow")}</a>
        </div>
    </div>"""


def render_provider_matrix(model_regions: Dict[str, Set[str]], availability_bits: Dict[str, Dict[str, int]], href_prefix: str, top: int = 8) -> str:
    """Provider × deployment type: how many of each provider's models offer each type."""
    types = [item for item in DEPLOYMENT_TYPES if item["k"] != "av"]
    providers: Dict[str, List[str]] = defaultdict(list)
    for model in model_regions:
        providers[model_family(model)].append(model)
    ranked = sorted(providers.items(), key=lambda item: (-len(item[1]), item[0]))
    rows_data = [(name, models) for name, models in ranked[:top]]
    rest = [model for _, models in ranked[top:] for model in models]
    if rest:
        rows_data.append(("Other", rest))

    def offers(model: str, bit: int) -> bool:
        return any(bits & bit for bits in availability_bits.get(model, {}).values())

    groups = []
    for item in types:
        if groups and groups[-1][0] == item["group"]:
            groups[-1][1] += 1
        else:
            groups.append([item["group"], 1])
    group_labels = {"paygo": "Pay-as-you-go", "ptu": "Provisioned", "batch": "Batch", "partner": "Partner"}
    head_groups = "".join(f'<th colspan="{span}" class="pmx__group pmx__group--{group}">{group_labels.get(group, group)}</th>' for group, span in groups)
    head_types = "".join(f'<th{tip_attrs(item["label"], item["tip"])}>{item["short"]}</th>' for item in types)

    def row(name: str, models: List[str], is_total: bool = False) -> str:
        cells = []
        for item in types:
            count = sum(1 for model in models if offers(model, item["bit"]))
            share = count / len(models) if models else 0
            hash_parts = [f"t={item['k']}"] + ([] if is_total or name == "Other" else [f"p={quote(name)}"])
            tip_body = f"{count} of {len(models)} {name if not is_total else ''} models ({share * 100:.0f}%) can deploy as {item['label']} in at least one region."
            cells.append(
                f'<td class="pmx__cell pmx__cell--{item["group"]}" style="--s:{share:.2f}">'
                + (f'<a href="{href_prefix}#{"&".join(hash_parts)}"{tip_attrs(f"{name} · {item["short"]}", " ".join(tip_body.split()))}>{count}</a>' if count else '<span class="pmx__zero">·</span>')
                + "</td>"
            )
        label = html_escape(name)
        name_html = label if is_total or name == "Other" else f'<a href="{href_prefix}#p={quote(name)}">{label}</a>'
        return f'<tr class="{"pmx__total" if is_total else ""}"><th scope="row">{name_html}</th><td class="pmx__n">{len(models)}</td>{"".join(cells)}</tr>'

    body = row("All models", list(model_regions), True) + "".join(row(name, models) for name, models in rows_data)
    return f"""<div class="pmx-scroll"><table class="pmx">
        <thead><tr><th rowspan="2" class="pmx__corner">Provider</th><th rowspan="2" class="pmx__n">Models</th>{head_groups}</tr><tr>{head_types}</tr></thead>
        <tbody>{body}</tbody>
    </table></div>
    <p class="chart-note">Cell = models from that provider offering the deployment type somewhere · darker = larger share of the provider's lineup</p>"""


def render_momentum_chart(history: List[Dict], all_regions: Set[str], known_models: Set[str], today: datetime, months: int = 12) -> Tuple[str, str]:
    rows = flatten_history_changes(history, all_regions, known_models)
    keys = []
    year, month = today.year, today.month
    for _ in range(months):
        keys.append((year, month))
        month -= 1
        if month == 0:
            year, month = year - 1, 12
    keys.reverse()
    added = {key: 0 for key in keys}
    removed = {key: 0 for key in keys}
    for row in rows:
        key = (row["timestamp"].year, row["timestamp"].month)
        if key in added:
            (added if row["change"] == "added" else removed)[key] += 1
    peak = max(list(added.values()) + list(removed.values()) + [1])
    cols = []
    for key in keys:
        label = datetime(key[0], key[1], 1)
        a, r = added[key], removed[key]
        net = a - r
        tip = f"+{_fmt_num(a)} added · −{_fmt_num(r)} removed · net {'+' if net >= 0 else '−'}{_fmt_num(abs(net))}"
        cols.append(
            f'<li class="mo-col"{tip_attrs(f"{label:%B %Y}", tip + " regional SKU offers.")}>'
            f'<span class="mo-up"><span style="--h:{a / peak * 100:.1f}%"></span></span>'
            f'<span class="mo-down"><span style="--h:{r / peak * 100:.1f}%"></span></span>'
            f'<small>{label:%b}</small></li>'
        )
    total_added, total_removed = sum(added.values()), sum(removed.values())
    subtitle = f"+{_fmt_num(total_added)} / −{_fmt_num(total_removed)} regional SKU offers over 12 months"
    html = f"""<ol class="momentum" aria-label="Availability changes per month">{''.join(cols)}</ol>
    <p class="chart-note"><span class="chart-swatch chart-swatch--success"></span>Added <span class="chart-swatch chart-swatch--danger"></span>Removed</p>"""
    return html, subtitle


ICONS = {
    "cube": "M21 16.5c0 .38-.21.71-.53.88l-7.9 4.44a1 1 0 0 1-1.14 0l-7.9-4.44A1 1 0 0 1 3 16.5v-9c0-.38.21-.71.53-.88l7.9-4.44a1 1 0 0 1 1.14 0l7.9 4.44c.32.17.53.5.53.88zM12 4.15 6.04 7.5 12 10.85l5.96-3.35zM5 15.91l6 3.38v-6.71L5 9.21zm14 0v-6.7l-6 3.37v6.71z",
    "globe": "M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20m6.93 6h-2.95a15.7 15.7 0 0 0-1.38-3.56A8 8 0 0 1 18.93 8M12 4.04c.83 1.2 1.48 2.53 1.91 3.96h-3.82c.43-1.43 1.08-2.76 1.91-3.96M4.26 14a8 8 0 0 1 0-4h3.38a16 16 0 0 0 0 4zm.82 2h2.95c.32 1.25.78 2.45 1.38 3.56A8 8 0 0 1 5.08 16m2.95-8H5.08a8 8 0 0 1 4.33-3.56A15.7 15.7 0 0 0 8.03 8M12 19.96c-.83-1.2-1.48-2.53-1.91-3.96h3.82c-.43 1.43-1.08 2.76-1.91 3.96M14.34 14H9.66a14 14 0 0 1 0-4h4.68a14 14 0 0 1 0 4m.25 5.56c.6-1.11 1.06-2.31 1.38-3.56h2.95a8 8 0 0 1-4.33 3.56M16.36 14a16 16 0 0 0 0-4h3.38a8 8 0 0 1 0 4z",
    "clock": "M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20m0 18a8 8 0 1 1 0-16 8 8 0 0 1 0 16m.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z",
    "pulse": "M3 13h3.28l2.5-6.24 4.04 12.12L16.2 11H21V9h-6.2l-1.96 4.6L8.86 1.62 4.92 11H3z",
    "grid": "M3 3h8v8H3zm2 2v4h4V5zm8-2h8v8h-8zm2 2v4h4V5zM3 13h8v8H3zm2 2v4h4v-4zm8-2h8v8h-8zm2 2v4h4v-4z",
    "gauge": "M12 4a10 10 0 0 0-8.66 15h17.32A10 10 0 0 0 12 4m0 2a8 8 0 0 1 7.42 11H4.58A8 8 0 0 1 12 6m4.24 2.34-5.66 4.24a1.5 1.5 0 1 0 1.84 1.84z",
    "timeline": "M4 6h2v12H4zm4 3h12v2H8zm0 4h8v2H8zM8 5h10v2H8z",
    "table": "M3 4h18v16H3zm2 2v3h14V6zm0 5v3h6v-3zm8 0v3h6v-3zm-8 5v2h6v-2zm8 0v2h6v-2z",
    "arrow": "M5 11h11.17l-4.88-4.88L12.7 4.7 20 12l-7.3 7.3-1.41-1.42L16.17 13H5z",
}


def icon(name: str, cls: str = "fm-icon") -> str:
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true"><path d="{ICONS[name]}"/></svg>'


def chart_card(title: str, sub: str, body: str, span: str = "", link: Tuple[str, str] = None) -> str:
    link_html = f'<a class="bento__link" href="{link[0]}">{link[1]} {icon("arrow")}</a>' if link else ""
    return f"""<section class="bento__card chart-card{(' ' + span) if span else ''}">
        <header class="bento__head"><div><h3>{title}</h3><p>{sub}</p></div>{link_html}</header>
        {body}
    </section>"""


def build_dashboard_cards(
    model_regions: Dict[str, Set[str]],
    all_regions: Set[str],
    lifecycles: Dict[str, Dict],
    availability_bits: Dict[str, Dict[str, int]],
    retirement_data: Dict,
    history: List[Dict],
    today: datetime,
    href_prefix: str = "explorer/",
) -> Dict[str, str]:
    available_slugs = {slugify(model) for model in model_regions}
    runway_html, runway_sub = render_retirement_runway(retirement_data, today, available_slugs)
    momentum_html, momentum_sub = render_momentum_chart(history, all_regions, set(model_regions), today)
    at_risk = sum(1 for summary in lifecycles.values() if summary["key"] in ("soon", "retiring", "pending"))
    return {
        "runway": chart_card("Retirement runway", runway_sub, runway_html, "bento--8", ("retirements/", "Schedule")),
        "lifecycle": chart_card("Lifecycle at a glance", f"One square per model · {at_risk} at risk", render_lifecycle_waffle(lifecycles, href_prefix), "bento--4", (f"{href_prefix}#lc=risk", "At risk")),
        "map": chart_card("Where models run", f"{len(all_regions)} regions · bubble size = models available", render_world_map(model_regions, all_regions, href_prefix), "bento--12", (href_prefix, "Explorer")),
        "matrix": chart_card("Provider × deployment type", "How each provider's models can be deployed", render_provider_matrix(model_regions, availability_bits, href_prefix), "bento--8", ("ptu/", "PTU guide")),
        "momentum": chart_card("Availability momentum", momentum_sub, momentum_html, "bento--4", ("history/", "History")),
    }


def generate_explorer_page(all_regions: Set[str], model_count: int) -> str:
    type_chips = "".join(
        f'<button type="button" class="ax-chip ax-chip--{item["group"]}" data-type="{item["k"]}"{tip_attrs(item["label"], item["tip"])}>'
        f'<i class="ax-dot ax-dot--{item["group"]}"></i>{item["short"]}</button>'
        for item in DEPLOYMENT_TYPES if item["k"] != "av"
    )
    geo_options = "".join(f'<option value="{html_escape(geo)}">{html_escape(geo)}</option>' for geo in REGION_GEOS)
    stage_options = "".join(
        f'<option value="{key}">{label}</option>' for key, label, _, _ in CHART_STAGE_GROUPS
    )
    legend = "".join(
        f'<span{tip_attrs(title, body)}><i class="ax-dot ax-dot--{group}"></i>{title}</span>'
        for group, title, body in [
            ("paygo", "Pay-as-you-go", "Global, Data Zone or Regional Standard — billed per token."),
            ("ptu", "Provisioned (PTU)", "Reserved throughput. See the PTU guide for sizing and pricing."),
            ("batch", "Batch", "Asynchronous 24-hour jobs at a discount."),
            ("partner", "Partner", "Partner model via serverless API / Marketplace."),
            ("other", "Listed", "Available in the region; deployment type not published."),
        ]
    )
    return f"""---
hide:
  - navigation
  - toc
---

# Availability Explorer

<p class="page-lede">Every model, every region, every deployment type — in one view. Filters update the grid instantly; the URL updates too, so you can share exactly what you see.</p>

<div class="ax" data-explorer data-src="../assets/model-index.json" data-root="../">
    <div class="ax-toolbar">
        <div class="ax-search">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9.5 3a6.5 6.5 0 0 1 5.25 10.33l5.46 5.46-1.42 1.42-5.46-5.46A6.5 6.5 0 1 1 9.5 3m0 2a4.5 4.5 0 1 0 0 9 4.5 4.5 0 0 0 0-9"/></svg>
            <input type="search" data-ax="q" placeholder="Filter {model_count} models — e.g. gpt-5, claude, embedding" aria-label="Filter models" autocomplete="off" spellcheck="false">
        </div>
        <label class="ax-select"><span>Provider</span><select data-ax="p"><option value="">All providers</option></select></label>
        <label class="ax-select"><span>Lifecycle</span><select data-ax="lc"><option value="">Any stage</option>{stage_options}</select></label>
        <label class="ax-select"><span>Geography</span><select data-ax="g"><option value="">All geographies</option>{geo_options}</select></label>
        <label class="ax-select"><span>Sort</span><select data-ax="s">
            <option value="name">Name</option>
            <option value="coverage">Most regions</option>
            <option value="retire">Retiring soonest</option>
        </select></label>
    </div>
    <div class="ax-types" role="group" aria-label="Deployment type">
        <span class="ax-types__label">Deployment type</span>
        <button type="button" class="ax-chip is-active" data-type="">Any</button>
        {type_chips}
    </div>
    <div class="ax-status">
        <p class="ax-summary" data-ax-summary aria-live="polite">Loading…</p>
        <div class="ax-required" data-ax-required hidden></div>
        <div class="ax-actions">
            <label class="ax-toggle"><input type="checkbox" data-ax="he" checked> Hide empty regions</label>
            <button type="button" class="ax-btn" data-ax-action="reset">Reset</button>
            <button type="button" class="ax-btn" data-ax-action="csv">Download CSV</button>
        </div>
    </div>
    <div class="ax-legend">{legend}<em>Click a region header to require it.</em></div>
    <div class="ax-scroll" data-ax-scroll>
        <table class="ax-grid" data-ax-grid></table>
    </div>
</div>

<noscript>The explorer needs JavaScript. Browse the <a href="../models/">model table</a> instead.</noscript>
"""


# ----------------------------- PTU guide ---------------------------------

PTU_SOURCES = {
    "overview": "https://learn.microsoft.com/azure/foundry/openai/concepts/provisioned-throughput",
    "sizing": "https://learn.microsoft.com/azure/foundry/openai/how-to/provisioned-throughput-sizing",
    "billing": "https://learn.microsoft.com/azure/foundry/openai/concepts/provisioned-throughput-billing",
    "start": "https://learn.microsoft.com/azure/foundry/openai/how-to/provisioned-get-started",
    "spillover": "https://learn.microsoft.com/azure/foundry/openai/how-to/spillover-traffic-management",
    "calculator": "https://ai.azure.com/nextgen/goto/build/models/ptu-calculator",
    "quota_form": "https://aka.ms/oai/stuquotarequest",
    "benchmark": "https://github.com/Azure/azure-openai-benchmark",
}

# Source: provisioned-throughput-sizing "deployment parameters and throughput values by model" (retrieved 2026-10-07).
# (model, global/data zone min, global/data zone increment, regional min, regional increment, input TPM per PTU, output:input ratio)
PTU_SIZING: List[Tuple[str, int, int, int, int, int, int]] = [
    ("gpt-5.6-luna", 15, 5, 50, 50, 30000, 6),
    ("gpt-5.6-terra", 15, 5, 50, 50, 3000, 6),
    ("gpt-5.6-sol", 15, 5, 50, 50, 1200, 6),
    ("gpt-5.5", 15, 5, 50, 50, 1200, 6),
    ("gpt-5.4", 15, 5, 50, 50, 2400, 6),
    ("gpt-5.4-mini", 15, 5, 25, 25, 7900, 6),
    ("gpt-5.3-codex", 15, 5, 50, 50, 3400, 8),
    ("gpt-5.2", 15, 5, 50, 50, 3400, 8),
    ("gpt-5.2-codex", 15, 5, 50, 50, 3400, 8),
    ("gpt-5.1", 15, 5, 50, 50, 4750, 8),
    ("gpt-5.1-codex", 15, 5, 50, 50, 4750, 8),
    ("gpt-5", 15, 5, 50, 50, 4750, 8),
    ("gpt-5-mini", 15, 5, 50, 50, 4750, 8),
    ("gpt-4.1", 15, 5, 25, 25, 23750, 4),
    ("gpt-4.1-mini", 15, 5, 50, 50, 3000, 4),
    ("gpt-4.1-nano", 15, 5, 25, 25, 14900, 4),
    ("o3", 15, 5, 50, 50, 3000, 4),
    ("o4-mini", 15, 5, 25, 25, 5400, 4),
]


def generate_ptu_page(availability_bits: Dict[str, Dict[str, int]]) -> str:
    """Plain-language, step-by-step guide to provisioned throughput."""

    def models_with(type_key: str) -> int:
        bit = DEPLOYMENT_TYPE_BY_KEY[type_key]["bit"]
        return sum(1 for regions in availability_bits.values() if any(bits & bit for bits in regions.values()))

    def regions_with(type_key: str) -> int:
        bit = DEPLOYMENT_TYPE_BY_KEY[type_key]["bit"]
        return len({region for regions in availability_bits.values() for region, bits in regions.items() if bits & bit})

    type_cards = []
    for key, sku, routing, best, minimum in [
        ("gp", "GlobalProvisionedManaged", "Routed across Azure regions worldwide", "Highest availability and the most capacity", "15 PTU min · +5"),
        ("dp", "DataZoneProvisionedManaged", "Stays inside a data zone (US or EU)", "Zone-level data residency with better availability than regional", "15 PTU min · +5"),
        ("rp", "ProvisionedManaged", "Stays in the region you deploy to", "Strict single-region data residency", "25–50 PTU min · +25/50"),
    ]:
        item = DEPLOYMENT_TYPE_BY_KEY[key]
        type_cards.append(f"""<div class="ptu-type ptu-type--{key}">
        <h3>{item['label'].replace(' (PTU)', '')}</h3>
        <code>{sku}</code>
        <dl>
            <dt>Data processing</dt><dd>{routing}</dd>
            <dt>Best for</dt><dd>{best}</dd>
            <dt>Typical size</dt><dd>{minimum}</dd>
        </dl>
        <a class="ptu-type__link" href="../explorer/#t={key}">{models_with(key)} models · {regions_with(key)} regions →</a>
    </div>""")

    sizing_rows = "\n".join(
        f"| `{model}` | {gmin} (+{ginc}) | {rmin} (+{rinc}) | {tpm:,} | {ratio} |"
        for model, gmin, ginc, rmin, rinc, tpm, ratio in PTU_SIZING
    )
    calc_data = html_escape(json.dumps([
        {"m": model, "gmin": gmin, "ginc": ginc, "rmin": rmin, "rinc": rinc, "tpm": tpm, "ratio": ratio}
        for model, gmin, ginc, rmin, rinc, tpm, ratio in PTU_SIZING
    ], separators=(",", ":")))
    model_options = "".join(
        f'<option value="{model}"{" selected" if model == "gpt-4.1" else ""}>{model}</option>' for model, *_ in PTU_SIZING
    )

    return f"""---
hide:
  - toc
---

# Provisioned Throughput (PTU) Guide

<div class="ptu-hero">
    <p class="ptu-hero__lede"><strong>A PTU (provisioned throughput unit) is a slice of model capacity reserved only for you.</strong> You pay for it by the hour whether or not you send traffic. In return you get predictable latency, and when you hit 100% the service answers <code>429</code> immediately instead of slowing down.</p>
    <div class="ptu-hero__facts">
        <span{tip_attrs("Model-independent quota", "PTU quota is not tied to one model: the same quota can deploy any supported model.")}><b>Model-independent</b> quota</span>
        <span{tip_attrs("Region-specific", "Quota is granted per subscription, per region and per deployment type.")}><b>Per region</b> &amp; type</span>
        <span{tip_attrs("Throughput varies by model", "Each model gets a different number of tokens per minute from one PTU — see the sizing table.")}><b>Tokens/PTU</b> vary by model</span>
        <span{tip_attrs("Quota ≠ capacity", "Having PTU quota does not guarantee the capacity is free when you deploy.")}><b>Quota ≠</b> capacity</span>
    </div>
</div>

## 1 · Is PTU right for you?

<div class="ptu-fit">
    <div class="ptu-fit__col ptu-fit__col--yes">
        <h3>Choose PTU when…</h3>
        <ul>
            <li>Traffic is <strong>steady and predictable</strong></li>
            <li>You need <strong>consistent, low latency</strong> (real-time, interactive)</li>
            <li>Volume is <strong>production-scale</strong> and per-token bills are climbing</li>
        </ul>
    </div>
    <div class="ptu-fit__col ptu-fit__col--no">
        <h3>Stay on Standard when…</h3>
        <ul>
            <li>You're <strong>developing or testing</strong></li>
            <li>Usage is <strong>low</strong> or <strong>highly variable</strong></li>
            <li>You can't yet predict peak load well enough to size it</li>
        </ul>
    </div>
</div>

## 2 · Pick a provisioned deployment type

<div class="ptu-types">
{chr(10).join(type_cards)}
</div>

<p class="diagram-note">Reservations are bought per deployment type and are not interchangeable — decide this before you buy.</p>

## 3 · Size it

<ol class="ptu-steps">
    <li><strong>Measure your peak.</strong> Peak requests per minute, average prompt tokens, average response tokens and expected cache-hit rate.</li>
    <li><strong>Run the Foundry capacity calculator.</strong> In the Foundry portal open <em>Quota → Provisioned throughput</em>, or go straight to the <a href="{PTU_SOURCES['calculator']}">capacity calculator</a>. It rounds to the model's minimum and scale increment.</li>
    <li><strong>Benchmark it.</strong> Deploy the estimate and replay your traffic shape for 10+ minutes with the <a href="{PTU_SOURCES['benchmark']}">Azure OpenAI benchmark tool</a>, then with your real client.</li>
    <li><strong>Adjust.</strong> Watch utilization and 429 rates in Azure Monitor and resize.</li>
</ol>

<div class="ptu-calc" data-ptu-calc data-models="{calc_data}">
    <div class="ptu-calc__head">
        <h3>Quick estimate</h3>
        <p>Same formula as Microsoft's sizing guide. Always confirm in the <a href="{PTU_SOURCES['calculator']}">Foundry capacity calculator</a>.</p>
    </div>
    <div class="ptu-calc__form">
        <label>Model<select data-calc="model">{model_options}</select></label>
        <label>Deployment type<select data-calc="type"><option value="g">Global / Data Zone</option><option value="r">Regional</option></select></label>
        <label>Peak requests / min<input type="number" min="0" step="1" value="1000" data-calc="rpm"></label>
        <label>Prompt tokens / call<input type="number" min="0" step="1" value="200" data-calc="prompt"></label>
        <label>Response tokens / call<input type="number" min="0" step="1" value="20" data-calc="response"></label>
        <label>Cache-hit rate %<input type="number" min="0" max="100" step="1" value="0" data-calc="cache"></label>
    </div>
    <div class="ptu-calc__result" aria-live="polite">
        <div class="ptu-calc__big"><strong data-calc-out="ptu">–</strong><span>PTUs to deploy</span></div>
        <div class="ptu-calc__detail" data-calc-out="detail"></div>
    </div>
</div>

??? info "The formula and per-model numbers"
    - Input TPM = peak RPM × prompt tokens
    - Output TPM = peak RPM × response tokens
    - **Normalized TPM** = Input TPM × (1 − cache rate) + output-to-input ratio × Output TPM
    - **PTUs** = Normalized TPM ÷ input TPM per PTU, rounded up to the minimum / increment

    Worked example from Microsoft (gpt-5.2, Data Zone): 1,000 RPM × 200 prompt + 20 response tokens → 360,000 normalized TPM → 105.9 → **110 PTUs**. With a 50% cache rate → **80 PTUs**.

    | Model | Global / Data Zone min (step) | Regional min (step) | Input TPM per PTU | Output : input ratio |
    |---|---|---|---|---|
    {sizing_rows.replace(chr(10), chr(10) + '    ')}

    GPT-6 family and image models use normalized token accounting — use the capacity calculator for those. Source: [PTU sizing]({PTU_SOURCES['sizing']}).

## 4 · Get capacity, then reserve

<ol class="ptu-flow">
    <li class="ptu-flow__step"><span>1</span><strong>Check quota</strong><small>Foundry → Manage → Quota → Provisioned throughput unit. <a href="{PTU_SOURCES['quota_form']}">Request more</a> if needed.</small></li>
    <li class="ptu-flow__step"><span>2</span><strong>Deploy</strong><small>Creating the deployment is what actually claims capacity. The portal suggests other regions if yours is full.</small></li>
    <li class="ptu-flow__step"><span>3</span><strong>Reserve</strong><small>Only now buy a matching Azure Reservation (1 month or 1 year) to get the discounted rate.</small></li>
    <li class="ptu-flow__step"><span>4</span><strong>Go live</strong><small>Same API as Standard — call it with the deployment name.</small></li>
</ol>

!!! warning "Reservations don't guarantee capacity"
    Quota is just a limit, and a reservation is just a discount. Capacity is only held once a deployment exists. **Deploy first, then buy the reservation** — matching deployment type, region (Data Zone and Regional) and scope.

| | Hourly (no commitment) | Azure Reservation |
|---|---|---|
| Price | Full $/PTU/hour, prorated to the minute | Discounted $/PTU/hour |
| Term | None — stops only when you **delete** the deployment | 1 month or 1 year |
| Good for | Benchmarks, short events | Steady production |
| Watch out | Can't be paused; scaling down and back up risks losing capacity | Bought per deployment type; extra PTUs above the reservation bill hourly |

## 5 · Run it in production

<div class="ptu-ops">
    <div><h3>Monitor</h3><p>Azure Monitor metric <strong>Provisioned-managed utilization V2</strong> on the Foundry resource. Requests are rejected at 100%.</p></div>
    <div><h3>Handle 429s</h3><p>A 429 is a traffic signal, not an outage. Retry using the <code>retry-after-ms</code> header — SDK retries do this for you.</p></div>
    <div><h3>Spill over</h3><p>Send overflow to a Standard deployment in the same resource automatically with <a href="{PTU_SOURCES['spillover']}">spillover</a> (not yet for DeepSeek or Llama).</p></div>
    <div><h3>Plan retirements</h3><p>Provisioned deployments are <strong>never auto-upgraded</strong>. Watch the <a href="../retirements/">retirement dates</a> and migrate yourself.</p></div>
</div>

!!! tip "Cleaning up"
    Delete the deployment before deleting the resource — billing continues until the resource is purged. Cancel or exchange the reservation separately.

<p class="dash-footnote">Summarised from Microsoft Learn: <a href="{PTU_SOURCES['overview']}">What is provisioned throughput</a> · <a href="{PTU_SOURCES['sizing']}">PTU sizing</a> · <a href="{PTU_SOURCES['billing']}">Billing &amp; reservations</a> · <a href="{PTU_SOURCES['start']}">Operate in production</a>. Retrieved Oct 2026 — check the source pages for the latest numbers.</p>
"""


def model_finder_widget(data_src: str, root: str, placeholder: str = "Search models — e.g. gpt-5, o4-mini, claude, embedding", families: bool = True) -> str:
    return f"""<div class="model-finder" data-model-finder data-src="{data_src}" data-root="{root}">
    <div class="model-finder__field">
        <svg class="model-finder__icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M9.5 3a6.5 6.5 0 0 1 5.25 10.33l5.46 5.46-1.42 1.42-5.46-5.46A6.5 6.5 0 1 1 9.5 3m0 2a4.5 4.5 0 1 0 0 9 4.5 4.5 0 0 0 0-9"/></svg>
        <input type="search" class="model-finder__input" placeholder="{placeholder}" autocomplete="off" spellcheck="false" aria-label="Find a model" aria-controls="model-finder-results">
        <kbd class="model-finder__kbd">Ctrl K</kbd>
    </div>
    <div class="model-finder__chips" role="group" aria-label="Quick filters">
        <button type="button" class="finder-chip is-active" data-filter="all">All</button>
        <button type="button" class="finder-chip" data-filter="risk">Retiring soon</button>
        <button type="button" class="finder-chip" data-filter="preview">Preview</button>
        <button type="button" class="finder-chip" data-filter="Provisioned">Provisioned (PTU)</button>
        <button type="button" class="finder-chip" data-filter="Datazone">Data Zone</button>
        {'<span class="model-finder__families" data-family-chips></span>' if families else ''}
    </div>
    <div class="model-finder__results" id="model-finder-results" role="listbox" aria-live="polite" hidden></div>
</div>"""


def render_ga_timeline_diagram(compact: bool = False) -> str:
    """Proportional diagram of the GA model lifecycle with a zoom on the final 90 days."""
    ticks = "".join(f'<span style="--x:{month / 18 * 100:.2f}%">{month}</span>' for month in range(0, 19, 3))
    zoom = f"""
    <div class="lc-zoom" aria-label="Final 90 days before retirement">
        <div class="lc-zoom__title">Final 90 days</div>
        <div class="lc-track lc-track--zoom">
            <div class="lc-phase lc-phase--eval" style="--w:33.33%"><span>Evaluate replacement</span></div>
            <div class="lc-phase lc-phase--notice" style="--w:33.33%"><span>Notifications</span></div>
            <div class="lc-phase lc-phase--ptu" style="--w:33.34%"><span>PTU migration</span></div>
        </div>
        <ol class="lc-marks">
            <li class="lc-mark lc-mark--start" style="--x:0%"><b>−90 d</b><span>Replacement named</span></li>
            <li class="lc-mark" style="--x:33.33%"><b>−60 d</b><span>Active notice</span></li>
            <li class="lc-mark" style="--x:66.67%"><b>−30 d</b><span>PTU migration window</span></li>
            <li class="lc-mark lc-mark--end lc-mark--danger" style="--x:100%"><b>Retire</b><span>Requests fail</span></li>
        </ol>
    </div>"""
    return f"""<figure class="lc-diagram{' lc-diagram--compact' if compact else ''}">
    <figcaption><strong>GA model</strong> · about 18 months from launch to retirement</figcaption>
    <div class="lc-track">
        <div class="lc-phase lc-phase--ga" style="--w:66.67%"><span>Generally available · all customers</span></div>
        <div class="lc-phase lc-phase--deprecated" style="--w:33.33%"><span>Deprecated · existing customers</span></div>
        <div class="lc-zoom-bracket" style="--x:83.33%; --w:16.67%"></div>
    </div>
    <div class="lc-scale" aria-hidden="true">{ticks}<em>months</em></div>
    <ol class="lc-marks">
        <li class="lc-mark lc-mark--start" style="--x:0%"><b>Launch</b><span>Retirement date published</span></li>
        <li class="lc-mark" style="--x:66.67%"><b>12 mo · Deprecated</b><span>New customers blocked</span></li>
        <li class="lc-mark lc-mark--end lc-mark--danger" style="--x:100%"><b>18 mo · Retired</b><span>410 / errors</span></li>
    </ol>{zoom}
</figure>"""


def render_preview_timeline_diagram() -> str:
    return """<figure class="lc-diagram">
    <figcaption><strong>Preview model</strong> · not-sooner-than date, often ~90 days out</figcaption>
    <div class="lc-track">
        <div class="lc-phase lc-phase--preview" style="--w:66.67%"><span>Preview · evaluation only</span></div>
        <div class="lc-phase lc-phase--notice" style="--w:33.33%"><span>≥30 d notice</span></div>
    </div>
    <ol class="lc-marks">
        <li class="lc-mark lc-mark--start" style="--x:0%"><b>Launch</b><span>Not-sooner-than date set</span></li>
        <li class="lc-mark" style="--x:66.67%"><b>Notice</b><span>≥30 days warning</span></li>
        <li class="lc-mark lc-mark--end lc-mark--danger" style="--x:100%"><b>Upgrade or retire</b><span>Newer version or ends</span></li>
    </ol>
</figure>"""


def render_stage_flow(stage_counts: Dict[str, int] = None) -> str:
    stage_counts = stage_counts or {}
    stages = [
        ("preview", "Preview", "Evaluation only", "No SLA · can change or be force-upgraded"),
        ("ga", "Generally available", "All customers", "Production-ready · retirement date set at launch"),
        ("legacy", "Legacy", "All customers", "Newer model exists · start evaluating"),
        ("deprecated", "Deprecated", "Existing customers", "No new customers · migrate now"),
        ("retired", "Retired", "Nobody", "Removed · inference returns errors"),
    ]
    nodes = []
    for key, title, access, detail in stages:
        count = stage_counts.get(key)
        count_html = f'<span class="stage-node__count" title="Models tracked in this stage">{count}</span>' if count else ""
        nodes.append(f"""<li class="stage-node stage-node--{key}">
        <span class="stage-node__dot" aria-hidden="true"></span>
        <strong>{title}</strong>{count_html}
        <span class="stage-node__access">{access}</span>
        <small>{detail}</small>
    </li>""")
    return f"""<ol class="stage-flow" aria-label="Model lifecycle stages">
    {chr(10).join(nodes)}
</ol>"""


def lifecycle_stage_counts(lifecycles: Dict[str, Dict]) -> Dict[str, int]:
    counts: Dict[str, int] = defaultdict(int)
    for summary in lifecycles.values():
        key = summary["key"]
        if key in ("soon", "retiring", "pending", "deprecated"):
            counts["deprecated"] += 1
        elif key in ("preview", "ga", "retired"):
            counts[key] += 1
    return counts


def build_changes_panel(history: List[Dict], all_regions: Set[str], known_models: Set[str], max_rows: int = 8) -> Tuple[str, Dict]:
    """Compact feed of the latest grouped availability changes."""
    rows = flatten_history_changes(history, all_regions, known_models, limit=10)
    stats = {"added": 0, "removed": 0, "models": 0, "date": "", "label": ""}
    if not rows:
        return '<p class="dash-empty">No availability changes recorded yet.</p>', stats

    latest_timestamp = rows[0]["timestamp"]
    latest_rows = [row for row in rows if row["timestamp"] == latest_timestamp]
    stats.update({
        "added": sum(1 for row in latest_rows if row["change"] == "added"),
        "removed": sum(1 for row in latest_rows if row["change"] == "removed"),
        "models": len({row["model"] for row in latest_rows}),
        "date": f"{latest_timestamp:%Y-%m-%d}",
        "label": format_digest_date(latest_timestamp),
    })

    grouped: Dict[Tuple, Dict] = {}
    for row in rows:
        key = (row["timestamp"], row["change"], row["model"], row["sku"])
        group = grouped.setdefault(key, {**row, "regions": set()})
        group["regions"].add(row["region"])

    items = []
    groups = list(grouped.values())
    for group in groups[:max_rows]:
        added = group["change"] == "added"
        regions = sorted(region for region in group["regions"] if not region.startswith("("))
        if regions:
            scope = region_link(regions[0], class_name="feed-region")
            if len(regions) > 1:
                scope += f' <span class="feed-more">+{len(regions) - 1}</span>'
        else:
            scope = '<span class="feed-more">entire model</span>'
        sku = group["sku"]
        sku_html = sku_link(sku, class_name="feed-sku") if sku != "-" else ""
        items.append(f"""<li class="feed-item feed-item--{'added' if added else 'removed'}">
        <span class="feed-item__icon" aria-label="{'Added' if added else 'Removed'}">{'+' if added else '−'}</span>
        <div class="feed-item__body">
            <div class="feed-item__title">{model_link(group['model'])} {sku_html}</div>
            <div class="feed-item__meta"><time datetime="{group['timestamp']:%Y-%m-%d}">{group['timestamp']:%b} {group['timestamp'].day}</time> · {scope}</div>
        </div>
    </li>""")

    more = len(groups) - len(items)
    more_html = f'<a class="dash-panel__more" href="history/">{pluralize(more, "more change")} in history →</a>' if more > 0 else ""
    return f'<ul class="feed">{chr(10).join(items)}</ul>{more_html}', stats


def build_watchlist(retirement_data: Dict, available_slugs: Set[str], today: datetime, limit: int = 8) -> Tuple[str, Dict]:
    """Upcoming retirements, soonest first, with countdown and progress."""
    upcoming = []
    counts = {"soon": 0, "retiring": 0, "retired": 0}
    for category, entries in retirement_data.get("models", {}).items():
        if category == "fine_tuned":
            continue
        for entry in entries:
            retire_dt, estimate = parse_lifecycle_date(entry.get("retirement_date"))
            if not retire_dt:
                continue
            days = (retire_dt - today).days
            if days < 0:
                if not estimate:
                    counts["retired"] += 1
                continue
            if days <= 30:
                counts["soon"] += 1
            elif days <= 90:
                counts["retiring"] += 1
            upcoming.append((retire_dt, estimate, days, entry))

    upcoming.sort(key=lambda item: (item[0], item[3].get("model", "")))
    rows = []
    for retire_dt, estimate, days, entry in upcoming[:limit]:
        model = entry.get("model", "")
        slug = slugify(model)
        model_html = f'<a href="models/{slug}/">{html_escape(model)}</a>' if slug in available_slugs else html_escape(model)
        tone = "danger" if days <= 30 else "warning" if days <= 90 else "neutral"
        start_dt, _ = parse_lifecycle_date(entry.get("deprecation_date"))
        if not start_dt or start_dt >= retire_dt:
            start_dt = retire_dt - timedelta(days=180)
        span = max((retire_dt - start_dt).days, 1)
        progress = min(max((today - start_dt).days / span * 100, 0), 100)
        replacement = entry.get("replacement")
        replacement_html = ""
        if replacement:
            replacement_slug = slugify(replacement)
            target = f'<a href="models/{replacement_slug}/">{html_escape(replacement)}</a>' if replacement_slug in available_slugs else html_escape(replacement)
            replacement_html = f'<span class="watch-item__replacement">→ {target}</span>'
        rows.append(f"""<li class="watch-item watch-item--{tone}">
        <div class="watch-item__main">
            <div class="watch-item__title">{model_html} <code>{html_escape(str(entry.get('version', '')))}</code></div>
            <div class="watch-item__meta">{'≥ ' if estimate else ''}{format_short_date(retire_dt)} {replacement_html}</div>
            <div class="watch-item__meter" aria-hidden="true"><span style="width:{progress:.0f}%"></span></div>
        </div>
        <span class="watch-item__countdown">{'≥ ' if estimate else ''}{days}<small>days</small></span>
    </li>""")

    if not rows:
        return '<p class="dash-empty">No upcoming retirements announced.</p>', counts
    more = len(upcoming) - len(rows)
    more_html = f'<a class="dash-panel__more" href="retirements/">{pluralize(more, "more scheduled retirement")} →</a>' if more > 0 else ""
    return f'<ul class="watchlist">{chr(10).join(rows)}</ul>{more_html}', counts


def generate_index_page(
    model_regions: Dict[str, Set[str]],
    model_sku_regions: Dict[str, Dict[str, Set[str]]],
    all_labels: Set[str],
    all_regions: Set[str],
    retirement_data: Dict = None,
    history: List[Dict] = None,
    lifecycles: Dict[str, Dict] = None,
    availability_bits: Dict[str, Dict[str, int]] = None,
) -> str:
    """Generate the dashboard home page."""
    today = datetime.utcnow()
    retirement_data = retirement_data or {"models": {}}
    lifecycles = lifecycles or {}
    available_slugs = {slugify(model) for model in model_regions}

    watchlist_html, watch_counts = build_watchlist(retirement_data, available_slugs, today)
    changes_html, change_stats = build_changes_panel(history or [], all_regions, set(model_regions))
    families = {model_family(model) for model in model_regions}
    due_90 = watch_counts["soon"] + watch_counts["retiring"]
    retire_tone = "danger" if watch_counts["soon"] else "warning" if due_90 else "success"

    changes_href = history_link(date=change_stats["date"]) if change_stats["date"] else "history/"
    retirement_source_date = retirement_data.get("last_updated", "")
    source_note = f" · retirement data as of {retirement_source_date}" if retirement_source_date else ""
    cards = build_dashboard_cards(model_regions, all_regions, lifecycles, availability_bits or {}, retirement_data, history or [], today)
    ga_count = sum(1 for summary in lifecycles.values() if summary["key"] == "ga")

    return f"""---
hide:
  - navigation
  - toc
---

<section class="dash-hero">
    <div class="dash-hero__head">
        <div>
            <p class="dash-eyebrow"><span class="dash-freshness__dot"></span>Live · updated {today:%b} {today.day}, {today:%Y}</p>
            <h1 class="dash-title">Foundry Model Availability</h1>
            <p class="dash-lede">Where every model runs, how you can deploy it, and when it retires.</p>
        </div>
        <a class="dash-hero__cta" href="explorer/">{icon("grid")}<span>Open explorer</span></a>
    </div>
    {model_finder_widget("assets/model-index.json", "", families=False)}
</section>

<div class="kpi-grid">
    <a class="kpi kpi--accent" href="models/">
        <span class="kpi__icon">{icon("cube")}</span>
        <span class="kpi__label">Models tracked</span>
        <strong class="kpi__value">{len(model_regions)}</strong>
        <span class="kpi__hint">{len(families)} providers · {ga_count} GA</span>
    </a>
    <a class="kpi kpi--info" href="by-region/">
        <span class="kpi__icon">{icon("globe")}</span>
        <span class="kpi__label">Azure regions</span>
        <strong class="kpi__value">{len(all_regions)}</strong>
        <span class="kpi__hint">with at least one model</span>
    </a>
    <a class="kpi kpi--{retire_tone} kpi--alert" href="retirements/">
        <span class="kpi__icon">{icon("clock")}</span>
        <span class="kpi__label">Retiring ≤ 90 days</span>
        <strong class="kpi__value">{due_90}</strong>
        <span class="kpi__hint"><b>{watch_counts['soon']}</b> within 30 days</span>
    </a>
    <a class="kpi kpi--success" href="{changes_href}">
        <span class="kpi__icon">{icon("pulse")}</span>
        <span class="kpi__label">Latest change run</span>
        <strong class="kpi__value"><span class="kpi__plus">+{change_stats['added']}</span> <span class="kpi__minus">−{change_stats['removed']}</span></strong>
        <span class="kpi__hint">{change_stats['label'] or 'no runs yet'} · {pluralize(change_stats['models'], 'model')}</span>
    </a>
</div>

<div class="bento">
    {cards['runway']}
    {cards['lifecycle']}
    <section class="bento__card bento--6" aria-labelledby="watchlist-title">
        <header class="bento__head"><div><h3 id="watchlist-title">Retirement watchlist</h3><p>Soonest first · {watch_counts['retired']} versions already retired</p></div><a class="bento__link" href="retirements/">All {icon("arrow")}</a></header>
        {watchlist_html}
    </section>
    <section class="bento__card bento--6" aria-labelledby="changes-title">
        <header class="bento__head"><div><h3 id="changes-title">Latest availability changes</h3><p>Regional SKU additions and removals</p></div><a class="bento__link" href="history/">History {icon("arrow")}</a></header>
        {changes_html}
    </section>
    {cards['map']}
    {cards['matrix']}
    {cards['momentum']}
    <nav class="bento__card bento--12 bento-links bento-links--row" aria-label="Guides">
        <a href="explorer/">{icon("grid", "fm-icon bento-links__icon")}<span><strong>Availability explorer</strong><small>Every model × region in one grid</small></span></a>
        <a href="ptu/">{icon("gauge", "fm-icon bento-links__icon")}<span><strong>PTU guide</strong><small>Size and buy provisioned throughput</small></span></a>
        <a href="lifecycle/">{icon("timeline", "fm-icon bento-links__icon")}<span><strong>Lifecycle guide</strong><small>What each badge means</small></span></a>
        <a href="models/">{icon("table", "fm-icon bento-links__icon")}<span><strong>Model catalog</strong><small>Sortable table of all models</small></span></a>
    </nav>
</div>

<p class="dash-footnote">Snapshot generated {today:%Y-%m-%d %H:%M} UTC{source_note}. Validate active deployments with the Models API and Azure Service Health.</p>
"""


def generate_lifecycle_page(lifecycles: Dict[str, Dict]) -> str:
    """Standalone guide explaining how Foundry model lifecycles work."""
    counts = lifecycle_stage_counts(lifecycles)
    return f"""# Model Lifecycle

<p class="page-lede">Every Foundry model version moves through the same stages. Knowing where a model sits tells you whether to build on it, plan a migration, or move now.</p>

## Stages

{render_stage_flow(counts)}

<p class="diagram-note">Counts group tracked models by their most urgent active version; Deprecated also includes versions with a retirement due. Legacy has no published date, so it is not counted.</p>

## Retirement timelines

{render_ga_timeline_diagram()}

{render_preview_timeline_diagram()}

## When to act

<div class="act-grid">
    <div class="act-card act-card--watch"><span>1</span><strong>Start watching</strong><p>The model shows as Deprecated, Legacy, or has a scheduled retirement on its model page.</p></div>
    <div class="act-card act-card--test"><span>2</span><strong>Start testing</strong><p>A replacement is named — usually 90–120 days before retirement. Evaluate it in Global Standard.</p></div>
    <div class="act-card act-card--notify"><span>3</span><strong>Expect notices</strong><p>GA retirements get at least 60 days active notice; preview models at least 30 days.</p></div>
    <div class="act-card act-card--manual"><span>4</span><strong>Migrate PTU yourself</strong><p>Provisioned deployments never auto-upgrade. Plan capacity in the replacement before the 30-day window.</p></div>
</div>

## Upgrade behavior by deployment type

| Deployment type | At retirement | What you should do |
|---|---|---|
| <span class="sku-badge sku-global">Global</span> Global Standard / Batch | Auto-upgraded to the replacement when an upgrade policy allows it | Pin a version and test the replacement before the date |
| <span class="sku-badge sku-datazone">Datazone</span> Data Zone Standard | Auto-upgraded within the data zone | Confirm the replacement is available in your data zone |
| <span class="sku-badge sku-standard">Standard</span> Regional Standard | Auto-upgraded when available in the region | Check regional availability of the replacement |
| <span class="sku-badge sku-provisioned">Provisioned</span> Provisioned (PTU) | **Not upgraded** — requests fail after retirement | Create a new PTU deployment on the replacement and move traffic |

## What each stage lets you do

| Stage | Meaning | New deployments | Existing deployments |
|---|---|---|---|
| <span class="lc-badge lc-badge--info">Preview</span> | Experimental — weights, runtime and API might change; not guaranteed to reach GA | Yes | Yes |
| <span class="lc-badge lc-badge--success">Generally available</span> | Production-ready — weights and APIs are fixed | Yes | Yes |
| Legacy | Newer, more capable models exist (optional stage) | Yes, until deprecated | Yes |
| <span class="lc-badge lc-badge--caution">Deprecated</span> | No longer available to new customers | Only subscriptions that already used this version | Yes |
| <span class="lc-badge lc-badge--muted">Retired</span> | Removed from service — every request returns `410 Gone` | No | No |

!!! info "Key timings"
    - GA models get **about 18 months** from launch to retirement and become Deprecated at **12 months**. GA models from Anthropic, DeepSeek, Fireworks and Mistral AI follow a **12-month** lifecycle.
    - A replacement is named **90–120 days** before retirement — in Global Standard about 90 days out, and in provisioned regions about 30 days out.
    - Preview models launch with a *not-sooner-than* date (typically ~90 days) and are force-upgraded or removed with **at least 30 days** notice.
    - Standard deployment types can be auto-upgraded. **Provisioned (PTU) deployments are never auto-upgraded** — you must migrate them yourself.

## How this site labels models

Hover or tap any lifecycle badge on this site for a plain-language explanation of what it means for you.

| Badge | What it means | What to do |
|---|---|---|
| <span class="lc-badge lc-badge--danger">Retires in 12 days</span> | Firm retirement date within 30 days | Move traffic to the replacement now |
| <span class="lc-badge lc-badge--warning">Retires in 60 days</span> | Firm retirement date within 90 days | Test the replacement and plan the cut-over |
| <span class="lc-badge lc-badge--warning">Retirement imminent</span> | A *no-earlier-than* date has passed — it can retire any time after notice | Treat as retiring now |
| <span class="lc-badge lc-badge--caution">Deprecated</span> | Closed to new customers | Don't start new work on it |
| <span class="lc-badge lc-badge--success">GA · until Jun 2027</span> | Generally available, with its next retirement month | Safe to build on |
| <span class="lc-badge lc-badge--neutral">No retirement date</span> | Not in Microsoft's retirement tables yet (common for new and partner models) | Check the model card in Foundry |

## Reading the Models API

| API `lifecycleStatus` | Means | Badge on this site |
|---|---|---|
| `Preview` | Preview, not for production | <span class="lc-badge lc-badge--info">Preview</span> |
| `GenerallyAvailable` | GA and open to new customers | <span class="lc-badge lc-badge--success">Generally available</span> |
| `Deprecating` | Deprecated — existing customers only | <span class="lc-badge lc-badge--caution">Deprecated</span> |
| `Deprecated` | Retired — no longer served | <span class="lc-badge lc-badge--muted">Retired</span> |

Adapted from [Foundry Models lifecycle and support policy](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirements). See [Retirements](../retirements/) for every model-specific date.
"""


def generate_model_index_page(
    model_regions: Dict[str, Set[str]],
    model_sku_regions: Dict[str, Dict[str, Set[str]]],
    all_regions: Set[str],
    lifecycles: Dict[str, Dict] = None,
) -> str:
    """Generate the models index page with filterable table."""
    lifecycles = lifecycles or {}
    untracked = {"key": "untracked", "label": LIFECYCLE_STAGES["untracked"][0], "tone": LIFECYCLE_STAGES["untracked"][1]}
    
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
      <td data-search="{html_escape(lifecycles.get(model, untracked)['label'])}">{lifecycle_badge(lifecycles.get(model, untracked))}</td>
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
    
    lifecycle_options = "\n".join(
        f'      <option value="{html_escape(label)}">{html_escape(label)}</option>'
        for label in dict.fromkeys(LIFECYCLE_STAGES[key][0] for key in LIFECYCLE_STAGES)
        if any(item["label"] == label for item in lifecycles.values())
    )

    return f"""---
hide:
  - toc
---

# All Models

<p class="page-lede">Jump straight to a model, or use the table below to compare deployment coverage across the full catalog.</p>

{model_finder_widget("../assets/model-index.json", "../")}

<div class="filter-controls">
  <div class="filter-group">
    <label for="lifecycle-filter">Lifecycle</label>
    <select id="lifecycle-filter" onchange="filterModelsTable()">
      <option value="">All Stages</option>
{lifecycle_options}
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
    lifecycle: Dict = None,
    today: datetime = None,
) -> str:
    """Generate detailed page for a single model."""
    today = today or datetime.utcnow()
    lifecycle = lifecycle or summarize_model_lifecycle(retirement_info or [], today)

    count = len(regions)
    total_region_count = max(len(all_regions), 1)
    coverage_pct = round(count / total_region_count * 100)
    bucket_label, bucket_class, bucket_description = pick_bucket(count)

    # Group SKUs by category
    sku_by_category: Dict[str, List[Tuple[str, Set[str]]]] = defaultdict(list)
    for sku, sku_regs in sorted(sku_regions.items()):
        cat = get_sku_category(sku)
        sku_by_category[cat].append((sku, sku_regs))

    retirement_section = generate_lifecycle_section(retirement_info or [], model_regions_lookup or {}, today)

    categories = sorted(sku_by_category.keys())
    category_summary = ", ".join(categories) if categories else "No SKU categories"
    category_chips = " ".join(sku_category_badge(cat) for cat in categories) or '<span class="sku-badge sku-other">No SKU data</span>'

    if sku_regions:
        top_sku, top_sku_regions = max(sku_regions.items(), key=lambda item: (len(item[1]), item[0]))
        top_sku_pct = round(len(top_sku_regions) / total_region_count * 100)
        top_sku_href = query_url("../../by-sku/", {"sku": top_sku})
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
            region_link(region, prefix="../../by-region/", class_name="region-badge model-region-chip")
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
    <div class="model-metric model-metric--{lifecycle["tone"]}">
        <span>Next retirement</span>
        <strong>{html_escape(format_countdown(lifecycle["days"]) if "days" in lifecycle else "None set")}</strong>
    </div>
</div>"""

    model_profile = f"""<div class="model-profile" aria-label="Model availability profile">
    <div class="model-profile__main">
        <div class="model-profile__badges">
            <span class="badge {bucket_class}">{bucket_label}</span>
            {lifecycle_badge(lifecycle)}
            <span class="model-profile__family">{html_escape(model_family(model))}</span>
            <span class="model-profile__coverage-note">{bucket_description} tracked</span>
        </div>
        <p class="model-profile__lead">Available in <strong>{count}</strong> of <strong>{len(all_regions)}</strong> tracked regions with <strong>{len(sku_regions)}</strong> deployment SKU types.</p>
        <div class="model-profile__chips" aria-label="Deployment categories">{category_chips}</div>
        <div class="model-profile__actions">
            <a class="md-button md-button--primary" href="#deployment-options">Deployment options</a>
            <a class="md-button" href="#lifecycle">Lifecycle</a>
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
            sku_href = query_url("../../by-sku/", {"sku": sku})
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
        html_rows.append(f"<tr data-region=\"{html_escape(region)}\"><td><strong>{html_escape(region)}</strong></td>{''.join(cells)}</tr>")

    matrix_html = f"""<div class="matrix-tools">
    <input type="search" class="matrix-filter" data-matrix-filter placeholder="Filter {count} regions…" aria-label="Filter regions">
    <span class="matrix-count" data-matrix-count>{count} regions</span>
</div>
<div class="table-responsive">
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
    MODEL_PAGE_SLUGS.update(slugify(model) for model in model_regions)
    history = load_history(HISTORY_DIR)
    
    # Load retirement data
    retirement_data = load_retirement_data(RETIREMENT_PATH)
    retirement_index = build_retirement_index(retirement_data)
    
    # Build normalized model_regions lookup for retirement sections
    model_regions_normalized = {
        slugify(model): regions for model, regions in model_regions.items()
    }
    
    today = datetime.utcnow()
    lifecycles = build_model_lifecycles(model_regions, retirement_index, today)
    availability_bits = build_availability_bits(data)

    # Generate main pages
    pages = {
        "index.md": generate_index_page(model_regions, model_sku_regions, all_labels, all_regions, retirement_data, history, lifecycles, availability_bits),
        "explorer.md": generate_explorer_page(all_regions, len(model_regions)),
        "ptu.md": generate_ptu_page(availability_bits),
        "lifecycle.md": generate_lifecycle_page(lifecycles),
        "models/index.md": generate_model_index_page(model_regions, model_sku_regions, all_regions, lifecycles),
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

    assets_dir = DOCS_DIR / "assets"
    assets_dir.mkdir(exist_ok=True)
    finder_path = assets_dir / "model-index.json"
    finder_path.write_text(
        json.dumps(build_explorer_data(model_regions, model_sku_regions, lifecycles, availability_bits, all_regions, today), separators=(",", ":"), ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Generated: {finder_path}")
    
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
            lifecycle=lifecycles.get(model),
            today=today,
        )
        path = DOCS_DIR / "models" / f"{slugify(model)}.md"
        path.write_text(content, encoding="utf-8")
        print(f"Generated: {path}")
    
    print(f"\nDone! Generated {len(pages) + len(model_regions)} pages.")


if __name__ == "__main__":
    main()
