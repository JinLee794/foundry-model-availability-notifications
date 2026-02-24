#!/usr/bin/env python3
"""Render a markdown summary of AI Foundry model availability by region."""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Sequence, Set, Tuple

HERE = Path(__file__).resolve().parent
SNAPSHOT_PATH = HERE / "regions_snapshot.json"
HISTORY_DIR = HERE / "history"
OUTPUT_PATH = HERE.parent / "REGION_AVAILABILITY.md"
DEFAULT_LABEL = "Global coverage"

# Normalize legacy/non-canonical SKU labels to valid Azure AI Foundry deployment type names.
# Source: https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/deployment-types
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

# Buckets are evaluated in order; the first threshold that matches wins.
BUCKETS: Sequence[Tuple[int, str, str]] = (
    (25, "🟢 Broad", "25+ regions available"),
    (20, "🟡 Strong", "20-24 regions"),
    (15, "🟠 Growing", "15-19 regions"),
    (0, "🔴 Emerging", "Under 15 regions"),
)


def load_snapshot(path: Path) -> Dict[str, dict]:
    """Load a JSON snapshot from disk."""
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def load_history(path: Path) -> List[Tuple[datetime, str]]:
    """Return a list of (timestamp, summary) entries describing history changes."""
    entries: List[Tuple[datetime, str]] = []
    if not path.exists():
        return entries

    for diff_path in sorted(path.glob("diff-*.json")):
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

        summary_parts: List[str] = []
        for model in sorted(changes):
            change_payload = changes[model]
            model_parts: List[str] = []

            model_parts.extend(
                _summarise_change_block(DEFAULT_LABEL, change_payload.get("all") or {})
            )

            for sku_name in sorted(change_payload.get("skus", {})):
                sku_payload = change_payload["skus"][sku_name]
                label = sku_payload.get("label") or sku_name
                model_parts.extend(_summarise_change_block(label, sku_payload))

            if model_parts:
                summary_parts.append(f"{model}: {'; '.join(model_parts)}")

        if summary_parts:
            summary = " | ".join(summary_parts)
            entries.append((timestamp, summary))

    entries.sort(key=lambda item: item[0], reverse=True)
    return entries


def _summarise_change_block(label: str, block: dict) -> List[str]:
    """Return summary strings for a single change block."""
    if not block:
        return []

    summaries: List[str] = []
    added = sorted(set(block.get("added", [])))
    removed = sorted(set(block.get("removed", [])))

    if added:
        summaries.append(f"{label} added {format_list(added)}")
    if removed:
        summaries.append(f"{label} removed {format_list(removed)}")

    return summaries


def format_list(items: List[str]) -> str:
    """Return a human-friendly list string."""
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return ", ".join(items[:-1]) + f", and {items[-1]}"


def build_model_index(
    data: Dict[str, dict]
) -> Tuple[
    Dict[str, Set[str]],
    Dict[str, Dict[str, Set[str]]],
    Set[str],
    Set[str],
]:
    """Create model-centric structures including region and SKU metadata.

    Returns:
        model_regions: model -> set of region names
        model_region_skus: model -> region -> set of SKU labels
        all_labels: set of every SKU label encountered
        all_regions: set of every region encountered
    """
    model_regions: Dict[str, Set[str]] = defaultdict(set)
    model_region_skus: Dict[str, Dict[str, Set[str]]] = defaultdict(
        lambda: defaultdict(set)
    )
    all_labels: Set[str] = set()
    all_regions: Set[str] = set()

    for model, payload in data.items():
        for region in payload.get("all", []):
            model_regions[model].add(region)
            model_region_skus[model][region].add(DEFAULT_LABEL)
            all_labels.add(DEFAULT_LABEL)
            all_regions.add(region)

        for sku_name, sku in payload.get("skus", {}).items():
            label = sku.get("label") or sku_name
            label = SKU_LABEL_NORMALIZATION.get(label, label)
            all_labels.add(label)
            for region in sku.get("regions", []):
                model_regions[model].add(region)
                model_region_skus[model][region].add(label)
                all_regions.add(region)

    return model_regions, model_region_skus, all_labels, all_regions


def pick_bucket(count: int) -> Tuple[str, str]:
    """Return (label, description) for the coverage bucket."""
    for threshold, label, description in BUCKETS:
        if count >= threshold:
            return label, description
    # Fallback should never trigger because of the (0, ...) bucket.
    return BUCKETS[-1][1], BUCKETS[-1][2]
def render_markdown(
    index: Dict[str, Set[str]],
    model_region_skus: Dict[str, Dict[str, Set[str]]],
    all_labels: Set[str],
    all_regions: Set[str],
    history_entries: List[Tuple[datetime, str]],
) -> str:
    """Return the markdown document summarising model availability."""
    total_models = len(index)
    total_regions = len(all_regions)
    distinct_labels = len(all_labels)

    legend_lines = [f"- {label} — {description}" for _, label, description in BUCKETS]

    table_rows: List[str] = []
    detail_blocks: List[str] = []

    for model, regions in sorted(
        index.items(), key=lambda item: (-len(item[1]), item[0])
    ):
        sorted_regions = sorted(regions)
        count = len(sorted_regions)
        bucket_label, _ = pick_bucket(count)
        sample = ", ".join(f"`{name}`" for name in sorted_regions[:6])
        sku_labels = sorted(
            {
                label
                for labels in model_region_skus[model].values()
                for label in labels
            }
        )
        sku_preview = ", ".join(sku_labels[:3])
        if len(sku_labels) > 3:
            sku_preview += " +"
        sku_column = (
            f"{len(sku_labels)} ({sku_preview})" if sku_preview else str(len(sku_labels))
        )

        table_rows.append(
            f"| {model} | {bucket_label} | {count} | {sku_column} | {sample} |"
        )

        roster_lines = [
            f"- `{region}` — {', '.join(sorted(model_region_skus[model][region]))}"
            for region in sorted_regions
        ]
        detail_blocks.append(
            "\n".join(
                (
                    "<details>",
                    f"<summary>{model} — {count} regions across {len(sku_labels)} SKU labels</summary>",
                    "",
                    *roster_lines,
                    "",
                    "</details>",
                )
            )
        )

    table_header = (
        "| Model | Coverage | Regions | SKU labels | Regions (sample) |\n"
        "| --- | --- | --- | --- | --- |"
    )

    content: List[str] = [
        "# AI Foundry Model Availability by Region",
        "",
        f"_Last updated: {datetime.utcnow():%Y-%m-%d %H:%M UTC}_",
        "",
        f"- Models tracked: **{total_models}**",
        f"- Regions in snapshot: **{total_regions}**",
        f"- Distinct SKU labels: **{distinct_labels}**",
        "",
        "Coverage legend:",
        *legend_lines,
        "",
        "SKU labels observed:",
        *[f"- {label}" for label in sorted(all_labels)],
        "",
        "## Model reach overview",
        "",
        table_header,
        *table_rows,
        "",
        "## Regional rosters by model",
        "",
        *detail_blocks,
    ]

    if history_entries:
        content.extend(
            [
                "",
                "## Recent changes",
                "",
                *[
                    f"- **{timestamp:%Y-%m-%d %H:%M UTC}** — {summary}"
                    for timestamp, summary in history_entries
                ],
            ]
        )

    content.extend(
        [
            "",
            "_Generated by `.region-watch/render_markdown.py`_",
        ]
    )

    return "\n".join(content)


def main() -> None:
    data = load_snapshot(SNAPSHOT_PATH)
    index, model_region_skus, all_labels, all_regions = build_model_index(data)
    history_entries = load_history(HISTORY_DIR)
    markdown = render_markdown(
        index, model_region_skus, all_labels, all_regions, history_entries
    )
    OUTPUT_PATH.write_text(markdown, encoding="utf-8")


if __name__ == "__main__":
    main()
