#!/usr/bin/env python3
"""Fetch Foundry model list prices from the public Azure Retail Prices API.

Writes .region-watch/pricing.json with pay-as-you-go token prices (USD per
1M tokens) for every tracked model that has a matching meter, plus the
provisioned throughput (PTU) hourly and reservation prices.

The Retail Prices API is public and needs no credentials:
https://learn.microsoft.com/rest/api/cost-management/retail-prices/azure-retail-prices

Meter names are not standardised, so each meter is tokenised into
<model stem> + <kind> + <deployment type>, and the stem is matched to a
tracked model key directly or through ALIASES.
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent
SNAPSHOT = ROOT / "regions_snapshot.json"
OUTPUT = ROOT / "pricing.json"

API = "https://prices.azure.com/api/retail/prices"
API_VERSION = "2023-01-01-preview"
REGION = "eastus2"
RESERVATION_PRODUCT = "Azure AI Foundry Provisioned Throughput Reservation"

# Products that are not first-party pay-as-you-go text models.
SKIP_PRODUCTS = {
    "Azure Fireworks Models",
    "Azure OpenAI Media",
    "Azure OpenAI PP FT GPT4s",
    "Azure BFL Flux Models",
    "Managed Compute",
}

# Prefix added to a stem when the meter name omits the model family.
PRODUCT_PREFIX = {
    "Azure Grok Models": "grok",
    "Azure Deepseek Models": "deepseek",
    "Azure Kimi": "kimi",
    "Azure OpenAI GPT5": "gpt",
    "Azure OpenAI GPT6": "gpt",
    "MAI Models": "mai",
}

# Normalised stem -> tracked model key(s).
ALIASES: Dict[str, List[str]] = {
    "computeruse": ["computer-use-preview"],
    "embeddingada": ["text-embedding-ada-002"],
    "grok4.1": ["grok-4-1-fast-reasoning", "grok-4-1-fast-non-reasoning"],
    "grok4.2": ["grok-4-20-reasoning", "grok-4-20-non-reasoning"],
    "deepseekv3.2sp": ["DeepSeek-V3.2-Speciale"],
    "deepseekmaidsr1": ["MAI-DS-R1"],
    "kimik2.5thinking": ["Kimi-K2.5"],
    "kimik2.6thinking": ["Kimi-K2.6"],
    "llama3.370b": ["Llama-3.3-70B-Instruct", "Llama 3.3 70B Instruct"],
    "llama4maverick17b": ["Llama-4-Maverick-17B-128E-Instruct-FP8"],
    "codestral": ["Codestral-2501"],
    "large3": ["Mistral-Large-3"],
    "mm3.5": ["mistral-medium-3-5"],
    "commanda": ["cohere-command-a"],
    "commandaplus": ["Cohere-command-a-plus-05-2026"],
    "phi4mini": ["Phi-4-mini-instruct"],
    "phi4minimm": ["Phi-4-multimodal-instruct"],
}

DEPLOY_TOKENS = {
    "global": {"glbl", "gl", "glb", "global"},
    "datazone": {"datazone", "dzone", "dz", "dzn"},
    "regional": {"regnl", "rgnl", "regional", "regn"},
}
INPUT_TOKENS = {"inp", "input", "in", "inpt"}
OUTPUT_TOKENS = {"outp", "output", "opt", "out", "outpt"}
CACHED_TOKENS = {"cached", "cchd", "ccchd", "cd", "cache", "ch"}
DROP_TOKENS = {"std", "shortco", "shco", "1m", "new"}
# A meter with any of these tokens is a variant we do not price
# (priority processing, flex, long context, fine-tuning, audio/image, ...).
SKIP_TOKENS = {
    "pp", "flex", "fl", "longco", "loco", "l", "wr", "ft", "finetuned", "training",
    "trng", "hosting", "hstng", "grader", "rft", "dev", "aud", "audio", "img", "image",
    "txt", "realtime", "rt", "tcrb", "tts", "transcribe",
}
DATE_RE = re.compile(r"^(\d{4}|\d{8})$")


def fetch(filter_expr: str) -> List[dict]:
    url = f"{API}?api-version={API_VERSION}&$filter={urllib.parse.quote(filter_expr)}"
    items: List[dict] = []
    while url:
        for attempt in range(4):
            try:
                with urllib.request.urlopen(url, timeout=60) as response:
                    page = json.load(response)
                break
            except Exception:  # noqa: BLE001 - retry transient network errors
                if attempt == 3:
                    raise
                time.sleep(2 ** attempt)
        items.extend(page.get("Items", []))
        url = page.get("NextPageLink")
    return items


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9.]", "", text.lower())


def version_rank(token: str) -> str:
    """Sort key for a date token: MMDD or MMDDYYYY -> YYYYMMDD."""
    if len(token) == 8:
        return token[4:] + token[:4]
    return "0000" + token


def tokenize(meter: str) -> List[str]:
    name = re.sub(r"\s+Tokens?$", "", meter, flags=re.I)
    name = re.sub(r"(?i)batch(?=inp|outp)", "batch ", name)
    name = re.sub(r"(?i)mini(?=\d{4})", "mini ", name)
    name = re.sub(r"(?i)data zone", "datazone", name)
    name = re.sub(r"(?i)aud(?=\d)", "aud ", name)
    return [t for t in re.split(r"[\s\-]+", name) if t]


def parse_meter(product: str, meter: str) -> Optional[Tuple[str, str, str, str]]:
    """Return (stem, version, deployment, kind) or None when not priceable."""
    tokens = tokenize(meter)
    lowered = [t.lower() for t in tokens]
    if any(t in SKIP_TOKENS for t in lowered):
        return None
    if "realtime" in meter.lower() or "rtime" in meter.lower():
        return None

    deployment = None
    stem: List[str] = []
    version = ""
    batch = cached = False
    direction = None
    for raw, low in zip(tokens, lowered):
        hit = next((d for d, words in DEPLOY_TOKENS.items() if low in words), None)
        if hit:
            deployment = hit
        elif low == "batch":
            batch = True
        elif low in CACHED_TOKENS:
            cached = True
        elif low in INPUT_TOKENS:
            direction = "in"
        elif low in OUTPUT_TOKENS:
            direction = "out"
        elif low in DROP_TOKENS:
            continue
        elif DATE_RE.match(low):
            version = low
        else:
            stem.append(raw)

    if not stem:
        return None
    if cached:
        if direction == "out":
            return None
        kind = "batch_cached" if batch else "cached"
    elif direction is None:
        # Embedding meters carry no direction: they only bill input tokens.
        if "embedding" not in meter.lower():
            return None
        kind = "batch_in" if batch else "in"
    else:
        kind = ("batch_" if batch else "") + direction
    if kind == "batch_cached":
        return None

    stem_text = " ".join(stem)
    prefix = PRODUCT_PREFIX.get(product)
    if prefix and not norm(stem_text).startswith(prefix):
        stem_text = f"{prefix} {stem_text}"
    # Phi meters have no deployment token; they are Global Standard.
    return stem_text, version, deployment or "global", kind


def resolve(stem: str, version: str, keys: Dict[str, str]) -> List[str]:
    full = norm(stem + (version or ""))
    base = norm(stem)
    for candidate in (full, base):
        if candidate in ALIASES:
            return ALIASES[candidate]
        if candidate in keys:
            return [keys[candidate]]
    return []


def per_million(item: dict) -> Optional[float]:
    unit = item.get("unitOfMeasure", "")
    price = float(item.get("retailPrice", 0))
    if unit == "1K":
        return round(price * 1000, 6)
    if unit == "1M":
        return round(price, 6)
    return None


def build_token_prices(items: Iterable[dict], tracked: List[str]) -> Tuple[Dict, List[str]]:
    keys = {norm(k): k for k in tracked}
    models: Dict[str, Dict[str, Dict[str, float]]] = {}
    ranks: Dict[Tuple[str, str, str], str] = {}
    unmatched: set = set()

    for item in items:
        product = item.get("productName", "")
        meter = item.get("meterName", "")
        if product in SKIP_PRODUCTS or item.get("type") != "Consumption":
            continue
        if not re.search(r"tokens?$", meter, re.I) and "embedding" not in meter.lower():
            continue
        price = per_million(item)
        if price is None:
            continue
        parsed = parse_meter(product, meter)
        if not parsed:
            continue
        stem, version, deployment, kind = parsed
        targets = resolve(stem, version, keys)
        if not targets:
            unmatched.add(f"{product}: {stem}")
            continue
        rank = version_rank(version) if version else "00000000"
        for key in targets:
            slot = (key, deployment, kind)
            if slot in ranks and ranks[slot] > rank:
                continue
            ranks[slot] = rank
            models.setdefault(key, {}).setdefault(deployment, {})[kind] = price

    return models, sorted(unmatched)


def build_ptu_prices(consumption: Iterable[dict], reservations: Iterable[dict]) -> Dict:
    hourly: Dict[str, float] = {}
    labels = {
        "Provisioned Managed Global": "global",
        "Provisioned Managed Data Zone": "datazone",
        "Provisioned Managed Regional": "regional",
    }
    for item in consumption:
        if item.get("productName") != "Azure OpenAI":
            continue
        deployment = labels.get(item.get("skuName", ""))
        if deployment and item.get("unitOfMeasure") == "1/Hour":
            hourly[deployment] = float(item["retailPrice"])

    reservation: Dict[str, Dict[str, float]] = {}
    for item in reservations:
        if item.get("type") != "Reservation":
            continue
        text = f"{item.get('skuName', '')} {item.get('meterName', '')}".lower()
        if "global" in text:
            deployment = "global"
        elif "data zone" in text or "datazone" in text:
            deployment = "datazone"
        elif "regional" in text:
            deployment = "regional"
        else:
            continue
        term = {"1 Month": "month", "1 Year": "year"}.get(item.get("reservationTerm", ""))
        if term:
            reservation.setdefault(term, {})[deployment] = float(item["retailPrice"])
    return {"hourly": hourly, "reservation": reservation}


def main() -> int:
    tracked = sorted(json.loads(SNAPSHOT.read_text(encoding="utf-8")))
    base = f"serviceName eq 'Foundry Models' and armRegionName eq '{REGION}'"
    consumption = fetch(f"{base} and type eq 'Consumption'")
    reservations = fetch(f"productName eq '{RESERVATION_PRODUCT}' and armRegionName eq '{REGION}'")
    if not consumption:
        print("No meters returned; keeping the existing pricing.json", file=sys.stderr)
        return 1

    models, unmatched = build_token_prices(consumption, tracked)
    data = {
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "https://prices.azure.com/api/retail/prices",
        "region": REGION,
        "currency": "USD",
        "unit": "per 1M tokens",
        "models": {k: models[k] for k in sorted(models)},
        "ptu": build_ptu_prices(consumption, reservations),
        "unmatched_meters": unmatched,
    }
    # Keep the file (and its date) untouched when no price moved, so the daily job doesn't commit noise.
    try:
        previous = json.loads(OUTPUT.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        previous = {}
    unchanged = all(previous.get(key) == data[key] for key in ("region", "models", "ptu", "unmatched_meters"))
    if not unchanged:
        OUTPUT.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    state = "unchanged" if unchanged else "updated"
    print(f"Priced {len(models)} of {len(tracked)} tracked models from {len(consumption)} meters ({state})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
