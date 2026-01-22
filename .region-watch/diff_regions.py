#!/usr/bin/env python3
import json, os, re, sys, requests
from collections import defaultdict
from datetime import datetime, timezone
from typing import Optional

# Model matrix directories to check for availability data
MODEL_MATRIX_DIRS = [
    "articles/ai-foundry/openai/includes/model-matrix",  # OpenAI models (gpt, dall-e, whisper, etc.)
    # Additional directories for non-OpenAI models (phi, mistral, qwen, gpt-oss, etc.)
    # These may be added as Azure documents them in similar matrix format:
    # "articles/ai-foundry/foundry-models/includes/model-matrix",
    # "articles/ai-foundry/models/includes/model-matrix",
]

def get_model_matrix_directories() -> list:
    """Get list of model matrix directories to check, including any from environment."""
    dirs = list(MODEL_MATRIX_DIRS)
    # Allow adding additional directories via environment variable
    extra_dirs = os.getenv("MODEL_MATRIX_EXTRA_DIRS", "")
    if extra_dirs:
        for directory in extra_dirs.split(","):
            directory = directory.strip()
            if directory and directory not in dirs:
                dirs.append(directory)
    return dirs

def get_model_matrix_api_url(directory: str) -> str:
    return f"https://api.github.com/repos/MicrosoftDocs/azure-ai-docs/contents/{directory}?ref=main"

# Azure region codes -> display names
REGION_MAP = {
    "eastus": "East US", "eastus2": "East US 2", "westus": "West US", "westus2": "West US 2", "westus3": "West US 3",
    "centralus": "Central US", "northcentralus": "North Central US", "southcentralus": "South Central US",
    "westcentralus": "West Central US", "brazilsouth": "Brazil South", "brazilsoutheast": "Brazil Southeast",
    "canadacentral": "Canada Central", "canadaeast": "Canada East",
    "northeurope": "North Europe", "westeurope": "West Europe", "uksouth": "UK South", "ukwest": "UK West",
    "francecentral": "France Central", "francesouth": "France South",
    "germanynorth": "Germany North", "germanywestcentral": "Germany West Central",
    "switzerlandnorth": "Switzerland North", "switzerlandwest": "Switzerland West",
    "norwayeast": "Norway East", "norwaywest": "Norway West", "swedencentral": "Sweden Central", "swedensouth": "Sweden South",
    "spaincentral": "Spain Central", "italynorth": "Italy North", "polandcentral": "Poland Central",
    "netherlandswest": "Netherlands West", "finlandcentral": "Finland Central",
    "uaenorth": "UAE North", "uaecentral": "UAE Central", "qatarcentral": "Qatar Central",
    "saudiarabiacentral": "Saudi Arabia Central",
    "southafricanorth": "South Africa North", "southafricawest": "South Africa West",
    "eastasia": "East Asia", "southeastasia": "Southeast Asia",
    "japaneast": "Japan East", "japanwest": "Japan West", "koreacentral": "Korea Central", "koreasouth": "Korea South",
    "australiaeast": "Australia East", "australiasoutheast": "Australia Southeast",
    "australiacentral": "Australia Central", "australiacentral2": "Australia Central 2",
    "indiacentral": "India Central", "indiasouth": "India South", "westindia": "West India",
    "centralindia": "Central India", "southindia": "South India",
    "jioindiawest": "Jio India West", "jioindiacentral": "Jio India Central"
}

def normalize_model_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", name.lower())

def normalize_region_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())

REGION_LOOKUP = {normalize_region_key(k): v for k, v in REGION_MAP.items()}

SKU_LABEL_OVERRIDES = {
    "standard-models": "Standard (all)",
    "standard-global": "Standard global deployments",
    "standard-gpt-4": "Standard GPT-4",
    "standard-gpt-35-turbo": "Standard GPT-3.5 Turbo",
    "standard-chat-completions": "Standard chat completions",
    "standard-completions": "Standard completions",
    "standard-embeddings": "Standard embeddings",
    "standard-audio": "Standard audio",
    "standard-image-generation": "Standard image generation",
    "provisioned-models": "Provisioned (PTU managed)",
    "provisioned-global": "Provisioned global",
    "datazone-standard": "Datazone standard",
    "datazone-provisioned-managed": "Datazone provisioned managed",
    "global-batch": "Global batch",
    "global-batch-datazone": "Global batch datazone",
    "quota": "Quota",
}

def github_headers(accept: str) -> dict:
    headers = {"Accept": accept}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def parse_env_list(name: str, normalizer=None) -> set:
    raw = os.getenv(name, "")
    items = set()
    for token in raw.split(","):
        token = token.strip()
        if not token:
            continue
        if normalizer:
            token = normalizer(token)
        items.add(token)
    return items

def sku_slug(filename: str) -> str:
    return os.path.splitext(filename)[0].lower()

def sku_label(slug: str) -> str:
    if slug in SKU_LABEL_OVERRIDES:
        return SKU_LABEL_OVERRIDES[slug]
    words = re.split(r"[-_]+", slug)
    return " ".join(word.capitalize() for word in words if word)

def list_markdown_files() -> list:
    """List markdown files from all configured model matrix directories."""
    include_files = parse_env_list("MODEL_MATRIX_INCLUDE_FILES", lambda v: v.lower())
    exclude_files = parse_env_list("MODEL_MATRIX_EXCLUDE_FILES", lambda v: v.lower())
    
    all_files = []
    for directory in get_model_matrix_directories():
        try:
            api_url = get_model_matrix_api_url(directory)
            listing = requests.get(api_url, headers=github_headers("application/vnd.github+json"), timeout=30)
            listing.raise_for_status()
            
            for item in listing.json():
                if item.get("type") != "file":
                    continue
                name = item.get("name", "")
                if not name.endswith(".md"):
                    continue
                lowered = name.lower()
                if include_files and lowered not in include_files:
                    continue
                if lowered in exclude_files:
                    continue
                slug = sku_slug(name)
                all_files.append({
                    "name": name,
                    "slug": slug,
                    "label": sku_label(slug),
                    "url": item.get("download_url"),
                    "source_dir": directory,
                })
        except requests.exceptions.HTTPError as e:
            # If a directory doesn't exist or is inaccessible, log and continue
            print(f"Warning: Could not access directory {directory}: {e}", file=sys.stderr)
            continue
        except Exception as e:
            print(f"Warning: Error processing directory {directory}: {e}", file=sys.stderr)
            continue
    
    return all_files

def fetch_markdown(url: str) -> str:
    resp = requests.get(url, headers=github_headers("application/vnd.github.v3.raw"), timeout=30)
    resp.raise_for_status()
    return resp.text

def split_cells(row: str) -> list:
    row = row.strip()
    if not row.startswith("|"):
        return []
    return [c.strip() for c in row.strip().strip("|").split("|")]

def parse_model_names(cell: str) -> list:
    cell = re.sub(r"\*\*|\*", "", cell).strip()
    if not cell:
        return []
    models = []
    seen = set()
    for segment in re.split(r"<br\s*/?>|\n|;", cell):
        segment = segment.strip()
        if not segment:
            continue
        base = segment.split(",")[0].split("/")[0].strip(" -")
        base = re.sub(r"\s+", " ", base)
        if not base or base.lower() in {"region", "model"}:
            continue
        key = normalize_model_name(base)
        if not key or key in seen:
            continue
        seen.add(key)
        models.append(base)
    return models

def is_available_cell(cell: str) -> bool:
    if not cell:
        return False
    if "✅" in cell or "✔" in cell:
        return True
    return cell.strip().lower() in {"yes", "y", "true"}

def format_region_name(cell: str) -> Optional[str]:
    cell = re.sub(r"<br\s*/?>", " ", cell)
    cell = " ".join(cell.split())
    if not cell:
        return None
    key = normalize_region_key(cell)
    return REGION_LOOKUP.get(key, cell)

def parse_table(table: str) -> dict:
    rows = [line for line in table.strip().splitlines() if line.strip()]
    if len(rows) < 3:
        return {}

    header_cells = split_cells(rows[0])
    if not header_cells:
        return {}

    header_models = [parse_model_names(cell) for cell in header_cells]
    model_regions = defaultdict(set)

    for row in rows[2:]:  # skip separator row
        cells = split_cells(row)
        if not cells:
            continue
        region = format_region_name(cells[0])
        if not region:
            continue
        for idx, models in enumerate(header_models):
            if idx >= len(cells) or not models:
                continue
            if is_available_cell(cells[idx]):
                for model in models:
                    model_regions[model].add(region)

    return model_regions

def extract_models_from_markdown(markdown: str) -> dict:
    combined = defaultdict(set)
    for table in re.findall(r"(?:^\|.*\n)+", markdown, re.MULTILINE):
        data = parse_table(table)
        for model, regions in data.items():
            combined[model].update(regions)
    return combined

def build_current_snapshot(files: list) -> dict:
    combined = defaultdict(lambda: defaultdict(set))
    for entry in files:
        if not entry.get("url"):
            continue
        markdown = fetch_markdown(entry["url"])
        data = extract_models_from_markdown(markdown)
        sku = entry.get("slug")
        for model, regions in data.items():
            combined[model][sku].update(regions)

    result = {}
    for model in sorted(combined.keys(), key=str.lower):
        sku_map = combined[model]
        all_regions = set()
        formatted_skus = {}
        for sku_key in sorted(sku_map.keys()):
            regions = sorted(sku_map[sku_key])
            all_regions.update(regions)
            formatted_skus[sku_key] = {
                "label": sku_label(sku_key),
                "regions": regions,
            }
        result[model] = {
            "all": sorted(all_regions),
            "skus": formatted_skus,
        }
    return result

def _history_filename(now: datetime) -> str:
    base = now.strftime("%Y%m%dT%H%M%S")
    millis = int(now.microsecond / 1000)
    return f"diff-{base}{millis:03d}Z.json"

def write_diff_history(changes: dict, timestamp: str, now: datetime) -> None:
    if not changes:
        return
    history_dir = ".region-watch/history"
    os.makedirs(history_dir, exist_ok=True)
    payload = {
        "timestamp": timestamp,
        "changes": changes,
    }
    filename = os.path.join(history_dir, _history_filename(now))
    with open(filename, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)

def filter_models(data: dict) -> dict:
    include_models = parse_env_list("MODEL_MATRIX_INCLUDE_MODELS", normalize_model_name)
    exclude_models = parse_env_list("MODEL_MATRIX_EXCLUDE_MODELS", normalize_model_name)

    filtered = {}
    for model, info in data.items():
        key = normalize_model_name(model)
        if include_models and key not in include_models:
            continue
        if key in exclude_models:
            continue
        filtered[model] = info
    return filtered

def load_snapshot(path: str) -> dict:
    return json.load(open(path, "r", encoding="utf-8")) if os.path.exists(path) else {}

def _normalize_model_entry(entry) -> dict:
    if isinstance(entry, dict):
        all_regions = entry.get("all", [])
        skus = entry.get("skus", {})
        normalized_skus = {}
        for sku_key, sku_value in skus.items():
            if isinstance(sku_value, dict):
                normalized_skus[sku_key] = {
                    "label": sku_value.get("label", sku_label(sku_key)),
                    "regions": sku_value.get("regions", []),
                }
            elif isinstance(sku_value, list):
                normalized_skus[sku_key] = {
                    "label": sku_label(sku_key),
                    "regions": sku_value,
                }
        return {
            "all": all_regions,
            "skus": normalized_skus,
        }
    if isinstance(entry, list):
        return {"all": entry, "skus": {}}
    return {"all": [], "skus": {}}

def diff(old: dict, new: dict) -> dict:
    changes = {}
    for model, info in new.items():
        new_info = _normalize_model_entry(info)
        old_info = _normalize_model_entry(old.get(model, {}))

        overall_added = sorted(set(new_info["all"]) - set(old_info["all"]))
        overall_removed = sorted(set(old_info["all"]) - set(new_info["all"]))

        sku_changes = {}
        for sku_key, sku_detail in new_info["skus"].items():
            old_sku_detail = old_info["skus"].get(sku_key, {"label": sku_detail["label"], "regions": []})
            added = sorted(set(sku_detail["regions"]) - set(old_sku_detail.get("regions", [])))
            removed = sorted(set(old_sku_detail.get("regions", [])) - set(sku_detail["regions"]))
            if added or removed or sku_key not in old_info["skus"]:
                sku_changes[sku_key] = {
                    "label": sku_detail["label"],
                    "added": added,
                    "removed": removed,
                }

        for sku_key, old_sku_detail in old_info["skus"].items():
            if sku_key not in new_info["skus"]:
                sku_changes[sku_key] = {
                    "label": old_sku_detail.get("label", sku_label(sku_key)),
                    "added": [],
                    "removed": sorted(old_sku_detail.get("regions", [])),
                    "sku_removed": True,
                }

        if overall_added or overall_removed or sku_changes:
            changes[model] = {
                "all": {"added": overall_added, "removed": overall_removed},
                "skus": sku_changes,
            }

    # Detect models removed entirely
    for model, old_info in old.items():
        if model not in new:
            normalized_old = _normalize_model_entry(old_info)
            changes[model] = {
                "all": {"added": [], "removed": normalized_old["all"]},
                "skus": {
                    sku: {
                        "label": detail.get("label", sku_label(sku)),
                        "added": [],
                        "removed": detail.get("regions", []),
                        "sku_removed": True,
                    }
                    for sku, detail in normalized_old["skus"].items()
                },
                "model_removed": True,
            }

    return changes

def main() -> int:
    files = list_markdown_files()
    current = filter_models(build_current_snapshot(files))
    snap_path = ".region-watch/regions_snapshot.json"
    baseline = load_snapshot(snap_path)

    if not baseline:
        baseline = current

    changes = diff(baseline, current)
    now = datetime.now(timezone.utc)
    timestamp_iso = now.isoformat()
    file_names = [entry["name"] for entry in files]
    output = {
        "timestamp": timestamp_iso,
        "changes": changes,
        "current": current,
        "files": file_names,
    }
    print(json.dumps(output, indent=2))

    write_diff_history(changes, timestamp_iso, now)

    if os.getenv("TEAMS_WEBHOOK") and any(
        change["all"]["added"]
        or change["all"]["removed"]
        or any(sku_change.get("added") or sku_change.get("removed") or sku_change.get("sku_removed") for sku_change in change["skus"].values())
        or change.get("model_removed")
        for change in changes.values()
    ):
        lines = ["Model region changes detected:"]
        for model, change in changes.items():
            if change["all"]["added"]:
                lines.append(f"• {model}: added -> {', '.join(change['all']['added'])}")
            if change["all"]["removed"]:
                lines.append(f"• {model}: removed -> {', '.join(change['all']['removed'])}")
            for sku_key, sku_change in change["skus"].items():
                if sku_change.get("added"):
                    lines.append(
                        f"  - {sku_change['label']} ({sku_key}): added -> {', '.join(sku_change['added'])}"
                    )
                if sku_change.get("removed"):
                    lines.append(
                        f"  - {sku_change['label']} ({sku_key}): removed -> {', '.join(sku_change['removed'])}"
                    )
                if sku_change.get("sku_removed"):
                    lines.append(f"  - {sku_change['label']} ({sku_key}): sku removed")
            if change.get("model_removed"):
                lines.append("  - model removed")
        try:
            requests.post(os.getenv("TEAMS_WEBHOOK"), json={"text": "\n".join(lines)}, timeout=10)
        except Exception:
            pass

    os.makedirs(".region-watch", exist_ok=True)
    with open(snap_path, "w", encoding="utf-8") as handle:
        json.dump(current, handle, indent=2, sort_keys=True)

    return 0

if __name__ == "__main__":
    sys.exit(main())