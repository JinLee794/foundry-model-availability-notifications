#!/usr/bin/env python3
"""Refresh .region-watch/retirement_data.json from Microsoft's Foundry model retirement schedule.

The schedule is a Markdown include in MicrosoftDocs/azure-ai-docs with one table per provider
(Model | Version | Lifecycle | Retirement date | Replacement) plus a fine-tuned table. The upstream
table has no deprecation dates, so dates and notes we already hold are carried forward when the
same model version is still listed with the same retirement date.

Writes only when the parsed data changes. Exits 0 without writing if the source can't be fetched
or parses to an implausibly small table, so a docs reshuffle never wipes the site's lifecycle data.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

SOURCE_PATH = "articles/foundry/openai/includes/concepts-model-retirement-schedule-content.md"
RAW_URL = f"https://raw.githubusercontent.com/MicrosoftDocs/azure-ai-docs/main/{SOURCE_PATH}"
SOURCE_URL = f"https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/{SOURCE_PATH}"
PAGE_URL = "https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule"
OUTPUT = Path(__file__).resolve().parent / "retirement_data.json"
MIN_ENTRIES = 40

DASHES = {"", "-", "—", "–", "n/a"}
LIFECYCLES = {"ga": "GA", "generally available": "GA", "preview": "Preview", "legacy": "Legacy",
              "deprecated": "Deprecated", "retired": "Retired"}

CATEGORY_RULES: List[Tuple[str, str]] = [
    ("embedding", r"embed"),
    ("document_and_search", r"rerank|parse|document|ocr"),
    ("audio", r"transcribe|tts|whisper|audio|realtime|speech"),
    ("image_and_video", r"image|sora|flux|stable-|video"),
]


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "foundry-model-availability-notifications"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8")


def clean(cell: str) -> str:
    cell = re.sub(r"<sup>.*?</sup>", "", cell)
    cell = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", cell)
    return re.sub(r"\s+", " ", cell.replace("**", "").replace("`", "")).strip()


def has_footnote(cell: str) -> bool:
    return "<sup>" in cell


def blank(value: str) -> bool:
    return value.strip().lower() in DASHES


def category_for(model: str) -> str:
    name = model.lower()
    for category, pattern in CATEGORY_RULES:
        if re.search(pattern, name):
            return category
    return "text_generation"


def split_cells(line: str) -> List[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [cell.strip() for cell in line.split("|")]


def iter_tables(markdown: str):
    """Yield (headings, header_cells, rows) for every pipe table, with the active H2/H3/H4 headings."""
    headings: Dict[int, str] = {}
    lines = markdown.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        heading = re.match(r"^(#{2,4})\s+(.*)$", line)
        if heading:
            level = len(heading.group(1))
            headings[level] = clean(heading.group(2))
            for deeper in [k for k in headings if k > level]:
                del headings[deeper]
            i += 1
            continue
        if line.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{3,}", lines[i + 1]):
            header = [clean(c).lower() for c in split_cells(line)]
            rows = []
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(split_cells(lines[i]))
                i += 1
            yield dict(headings), header, rows
            continue
        i += 1


def parse_model_cell(cell: str) -> Tuple[str, str]:
    """'claude-mythos-preview (gated research preview)' -> ('claude-mythos-preview', 'gated research preview')."""
    text = clean(cell)
    match = re.match(r"^(.*?)\s*\(([^)]*)\)\s*$", text)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return text, ""


def parse_replacements(cell: str) -> List[Tuple[str, str]]:
    """Return [(model, version)]; 'sora-2 (2025-12-08)' names a specific version of a model."""
    text = clean(cell)
    if blank(text):
        return []
    out: List[Tuple[str, str]] = []
    for part in text.split(","):
        part = part.strip()
        version = ""
        match = re.match(r"^(.*?)\s*\((\d{4}-\d{2}-\d{2})\)$", part)
        if match:
            part, version = match.group(1).strip(), match.group(2)
        if part and not blank(part) and part not in [name for name, _ in out]:
            out.append((part, version))
    return out


def parse(markdown: str) -> Tuple[Dict[str, List[Dict]], str]:
    models: Dict[str, List[Dict]] = {}
    updated = ""
    date_match = re.search(r"^ms\.date:\s*(\d{1,2})/(\d{1,2})/(\d{4})", markdown, re.M)
    if date_match:
        month, day, year = date_match.groups()
        updated = f"{year}-{int(month):02d}-{int(day):02d}"

    for headings, header, rows in iter_tables(markdown):
        col = {name: idx for idx, name in enumerate(header)}
        provider = headings.get(3, "")
        sold_by = "partner" if "partner" in headings.get(2, "").lower() else "azure"
        if "training retirement date" in col:
            for row in rows:
                if len(row) < len(header):
                    continue
                model, _ = parse_model_cell(row[col["model"]])
                training_cell = row[col["training retirement date"]]
                entry = {
                    "model": model,
                    "version": clean(row[col["version"]]),
                    "training_retirement": clean(training_cell),
                    "deployment_retirement": clean(row[col["deployment retirement date"]]),
                }
                if has_footnote(training_cell):
                    entry["note"] = "For existing customers only"
                models.setdefault("fine_tuned", []).append(entry)
            continue
        if not {"model", "lifecycle", "retirement date"} <= set(col):
            continue
        for row in rows:
            if len(row) < len(header):
                continue
            model, qualifier = parse_model_cell(row[col["model"]])
            if blank(model):
                continue
            lifecycle_raw = clean(row[col["lifecycle"]])
            lifecycle = LIFECYCLES.get(lifecycle_raw.lower(), lifecycle_raw)
            retirement = clean(row[col["retirement date"]])
            version = clean(row[col["version"]]) if "version" in col else ""
            replacements = parse_replacements(row[col["replacement"]]) if "replacement" in col else []
            entry = {
                "model": model,
                "version": "" if blank(version) else version,
                "provider": provider,
                "sold_by": sold_by,
                "status": "Preview" if lifecycle == "Preview" else "Generally Available",
                "lifecycle": lifecycle,
                "deprecation_date": None,
                "retirement_date": None if blank(retirement) else retirement,
                "replacement": replacements[0][0] if replacements else None,
            }
            if replacements and replacements[0][1]:
                entry["replacement_version"] = replacements[0][1]
            if len(replacements) > 1:
                entry["replacement_alts"] = [name for name, _ in replacements[1:]]
            if qualifier:
                entry["qualifier"] = qualifier
            models.setdefault(category_for(model), []).append(entry)
    return models, updated


def deprecation_still_valid(entry: Dict, value: str, today: str) -> bool:
    """A remembered deprecation date only stands if upstream agrees the version is deprecated,
    or if the date is still ahead (a scheduled deprecation for a GA/Preview/Legacy version)."""
    if entry.get("lifecycle") in ("Deprecated", "Retired"):
        return True
    date = re.sub(r"(?i)^no earlier than\s*", "", str(value)).strip()
    return date > today


def carry_forward(models: Dict[str, List[Dict]], previous: Dict) -> None:
    """Keep deprecation dates and retirement notes we already know for unchanged model versions."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    known: Dict[Tuple[str, str], Dict] = {}
    for category, entries in (previous.get("models") or {}).items():
        if category == "fine_tuned":
            continue
        for entry in entries:
            key = (str(entry.get("model", "")).lower(), str(entry.get("version") or ""))
            known[key] = entry
    for category, entries in models.items():
        if category == "fine_tuned":
            continue
        for entry in entries:
            old = known.get((entry["model"].lower(), entry["version"]))
            if not old:
                continue
            old_dep = old.get("deprecation_date")
            if old_dep and not entry.get("deprecation_date") and deprecation_still_valid(entry, old_dep, today):
                entry["deprecation_date"] = old_dep
            if old.get("retirement_note") and old.get("retirement_date") == entry.get("retirement_date"):
                entry["retirement_note"] = old["retirement_note"]


def main() -> int:
    try:
        markdown = fetch(RAW_URL)
    except Exception as exc:  # network or HTTP error: keep the existing file
        print(f"Could not fetch retirement schedule: {exc}", file=sys.stderr)
        return 0

    models, updated = parse(markdown)
    count = sum(len(v) for k, v in models.items() if k != "fine_tuned")
    if count < MIN_ENTRIES:
        print(f"Parsed only {count} retirement entries; leaving {OUTPUT.name} unchanged.", file=sys.stderr)
        return 0

    previous: Dict = {}
    if OUTPUT.exists():
        try:
            previous = json.loads(OUTPUT.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            previous = {}
    carry_forward(models, previous)

    data = {
        "source": SOURCE_URL,
        "page": PAGE_URL,
        "last_updated": updated or previous.get("last_updated", ""),
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "models": models,
    }
    unchanged = all(previous.get(key) == data[key] for key in ("source", "last_updated", "models"))
    if not unchanged:
        OUTPUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    providers = sorted({e.get("provider", "") for k, v in models.items() if k != "fine_tuned" for e in v})
    with_replacement = sum(1 for k, v in models.items() if k != "fine_tuned" for e in v if e.get("replacement"))
    print(f"Retirement schedule {'unchanged' if unchanged else 'updated'}: {count} model versions across "
          f"{len(providers)} providers, {with_replacement} with a named replacement, "
          f"{len(models.get('fine_tuned', []))} fine-tuned rows (source updated {data['last_updated']}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
