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

# Image, audio, video and other non-text models. Meter names for these are too
# irregular to parse, so each tracked model lists the Global meter(s) for every
# price kind. Alternatives are tried in order (newest version first).
# Token kinds are stored per 1M tokens; per_* kinds per single unit
# (image, megapixel, second, hour, page, query); per_1m_chars per 1M characters.
TOKEN_KINDS = {
    "text_in", "text_out", "cached_text", "audio_in", "audio_out", "cached_audio",
    "image_in", "image_out", "cached_image",
}


def _realtime(prefix: str) -> Dict[str, Tuple[str, ...]]:
    return {
        "audio_in": (rf"{prefix} Audio inp Gl 1M Tokens",),
        "audio_out": (rf"{prefix} Audio opt Gl 1M Tokens",),
        "cached_audio": (rf"{prefix} Audio cd inp Gl 1M Tokens",),
        "text_in": (rf"{prefix} Text inp Gl 1M Tokens",),
        "text_out": (rf"{prefix} Text opt Gl 1M Tokens",),
        "cached_text": (rf"{prefix} Text cd inp Gl 1M Tokens",),
        "image_in": (rf"{prefix} Image inp Gl 1M Tokens",),
    }


def _image_family(prefix: str) -> Dict[str, Tuple[str, ...]]:
    return {
        "text_in": (rf"{prefix} txt inp Gl 1M Tokens",),
        "image_in": (rf"{prefix} img inp Gl 1M Tokens",),
        "cached_text": (rf"{prefix} txt cd inp Gl 1M Tokens",),
        "cached_image": (rf"{prefix} img cd inp Gl 1M Tokens",),
        "image_out": (rf"{prefix} img opt Gl 1M Tokens",),
    }


def _mai_image(prefix: str, suffix: str) -> Dict[str, Tuple[str, ...]]:
    return {
        "text_in": (rf"{prefix} Text Input {suffix}",),
        "image_in": (rf"{prefix} Image Input {suffix}",),
        "image_out": (rf"{prefix} Image Output {suffix}",),
    }


MEDIA_METERS: Dict[str, Dict[str, Tuple[str, ...]]] = {
    "gpt-4o-transcribe": {
        "audio_in": (r"gpt-4o-transcribe-aud-inp-glbl Tokens",),
        "text_in": (r"gpt-4o-transcribe-txt-inp-glbl Tokens",),
        "text_out": (r"gpt-4o-transcribe-txt-out-glbl Tokens",),
    },
    "gpt-4o-mini-transcribe": {
        "audio_in": (r"gpt4o mn trscb aud in gl 1215 1M Tokens", r"gpt-4o-mini-transcribe-aud-inp-glbl Tokens"),
        "text_in": (r"gpt4o mn trscb txt in gl 1215 1M Tokens", r"gpt-4o-mini-transcribe-txt-inp-glbl Tokens"),
        "text_out": (r"gpt4o mn trscb txt out gl 1215 1M Tokens", r"gpt-4o-mini-transcribe-txt-out-glbl Tokens"),
    },
    "gpt-4o-transcribe-diarize": {
        "audio_in": (r"gpt 4o tcrb d aud inp glbl Tokens",),
        "text_in": (r"gpt 4o tcrb d txt inp glbl Tokens",),
        "text_out": (r"gpt 4o tcrb d txt out glbl Tokens",),
    },
    "gpt-4o-mini-tts": {
        "text_in": (r"gpt4o mn tts txt in gl 1215 1M Tokens", r"gpt-4o-mini-tts-txt-inp-glbl Tokens"),
        "audio_out": (r"gpt4o mn tts aud out gl 1215 1M Tokens", r"gpt-4o-mini-tts-aud-out-glbl Tokens"),
    },
    "gpt-audio": {
        "audio_in": (r"gpt aud 0828 Inp glbl Tokens",),
        "audio_out": (r"gpt aud 0828 Outp glbl Tokens",),
        "text_in": (r"gpt aud 0828 txt Inp glbl Tokens",),
        "text_out": (r"gpt aud 0828 txt Outp glbl Tokens",),
    },
    "gpt-audio-mini": {
        "audio_in": (r"gpt aud mn in gl 1215 1M Tokens", r"gpt aud mini Inp glbl Tokens"),
        "audio_out": (r"gpt aud mn out gl 1215 1M Tokens", r"gpt aud mini Outp glbl Tokens"),
        "text_in": (r"gpt aud mn txt in gl 1215 1M Tokens", r"gpt aud mini txt Inp glbl Tokens"),
        "text_out": (r"gpt aud mn txt out gl 1215 1M Tokens", r"gpt aud mini txt Outp glbl Tokens"),
    },
    "gpt-audio-1.5": {
        "audio_in": (r"gpt aud 1\.5 inp Gl 1M Tokens",),
        "audio_out": (r"gpt aud 1\.5 opt Gl 1M Tokens",),
        "text_in": (r"gpt aud 1\.5 txt inp Gl 1M Tokens",),
        "text_out": (r"gpt aud 1\.5 txt opt Gl 1M Tokens",),
    },
    "gpt-realtime": {
        "audio_in": (r"gpt rt aud 0828 Inp glbl Tokens",),
        "audio_out": (r"gpt rt aud 0828 Outp glbl Tokens",),
        "cached_audio": (r"gpt rt aud 0828 cchd Inp glbl Tokens",),
        "text_in": (r"gpt rt txt 0828 Inp glbl Tokens",),
        "text_out": (r"gpt rt txt 0828 Outp glbl Tokens",),
        "cached_text": (r"gpt rt txt 0828 cchd Inp glbl Tokens",),
        "image_in": (r"gpt rt img 0828 Inp glbl Tokens",),
    },
    "gpt-realtime-mini": {
        "audio_in": (r"gpt rt aud mn in gl 1215 1M Tokens", r"gpt rt aud mini Inp glbl Tokens"),
        "audio_out": (r"gpt rt aud mn out gl 1215 1M Tokens", r"gpt rt aud mini Outp glbl Tokens"),
        "cached_audio": (r"gpt rt aud mn cd in gl 1215 1M Tokens", r"gpt rt aud mini cchd Inp glbl Tokens"),
        "text_in": (r"gpt rt txt mn in gl 1215 1M Tokens", r"gpt rt txt mini Inp glbl Tokens"),
        "text_out": (r"gpt rt txt mn Out gl 1215 1M Tokens", r"gpt rt txt mini Outp glbl Tokens"),
        "cached_text": (r"gpt rt txt mn cd in gl 1215 1M Tokens", r"gpt rt txt mini cchd Inp glbl Tokens"),
        "image_in": (r"gpt rt img mn in gl 1215 1M Tokens", r"gpt rt img mini Inp glbl Tokens"),
    },
    "gpt-realtime-1.5": {
        "audio_in": (r"gpt rt 1\.5 aud inp Gl 1M Tokens",),
        "audio_out": (r"gpt rt 1\.5 aud opt Gl 1M Tokens",),
        "cached_audio": (r"gpt rt 1\.5 aud cd inp Gl 1M Tokens",),
        "text_in": (r"gpt rt 1\.5 txt inp Gl 1M Tokens",),
        "text_out": (r"gpt rt 1\.5 txt opt Gl 1M Tokens",),
        "cached_text": (r"gpt rt 1\.5 txt cd inp Gl 1M Tokens",),
        "image_in": (r"gpt rt 1\.5 img inp Gl 1M Tokens",),
    },
    "gpt-realtime-2": _realtime(r"gpt-realtime-2"),
    "gpt-realtime-2.1": _realtime(r"gpt-realtime-2\.1"),
    "gpt-realtime-2.1-mini": _realtime(r"gpt-realtime-2\.1-mini"),
    "gpt-realtime-whisper": {"per_hour": (r"gpt-realtime-whisper Opt Gl Unit",)},
    "gpt-realtime-translate": {"per_hour": (r"gpt-realtime-translate Opt Gl Unit",)},
    "whisper": {"per_hour": (r"Speech-to-Text-Batch-Whisper-glbl Unit",)},
    "tts": {"per_1m_chars": (r"Speech-Text to Speech-global Characters",)},
    "tts-hd": {"per_1m_chars": (r"Speech-Text to Speech HD-global Characters",)},
    "gpt-image-1": {
        "text_in": (r"gpt-image-1-inp-txt-glbl Tokens",),
        "image_in": (r"gpt-image-1-inp-img-glbl Tokens",),
        "cached_text": (r"gpt-image-1-inp-cached-txt-glbl Tokens",),
        "cached_image": (r"gpt-image-1-inp-cached-img-glbl Tokens",),
        "image_out": (r"gpt-image-1-output-img-glbl Tokens",),
    },
    "gpt-image-1-mini": {
        "text_in": (r"gpt img 1 mini inp txt glbl Tokens",),
        "image_in": (r"gpt img 1 mini inp img glbl Tokens",),
        "cached_text": (r"gpt img 1 mini inp cchd txt glbl Tokens",),
        "cached_image": (r"gpt img 1 mini inp cchd img glbl Tokens",),
        "image_out": (r"gpt img 1 mini out img glbl Tokens",),
    },
    "gpt-image-1.5": {
        "text_in": (r"gpt img 1\.5 in txt gl 1M Tokens",),
        "image_in": (r"gpt img 1\.5 in img gl 1M Tokens",),
        "cached_text": (r"gpt img 1\.5 in cd txt gl 1M Tokens",),
        "cached_image": (r"gpt img 1\.5 in cd img gl 1M Tokens",),
        "image_out": (r"gpt img 1\.5 out img gl 1M Tokens",),
        "text_out": (r"gpt img 1\.5 out txt gl 1M Tokens",),
    },
    "gpt-image-2": _image_family(r"Image 2"),
    "gpt-image-2.5-flare": _image_family(r"Image-2\.5-flare"),
    "gpt-image-2.5-sunburst": _image_family(r"Image-2\.5-sunburst"),
    "MAI-Image-2.5": _mai_image(r"Image 2\.5", r"glbl Tokens"),
    "MAI-Image-2.5-Flash": _mai_image(r"Image 2\.5 Flash", r"glbl Tokens"),
    "MAI-Image-2.5-Pro": _mai_image(r"Image 2\.5 Pro", r"glbl 1M Tokens"),
    "MAI-Image-2.6": _mai_image(r"Image 2\.6", r"Glbl 1M Tokens"),
    "MAI-Image-2.6-Flash": {
        "text_in": (r"Img 2\.6 Flash Text In Glbl 1M Tokens",),
        "image_in": (r"Image 2\.6 Flash Image Input Glbl 1M Tokens",),
        "image_out": (r"Image 2\.6 Flash Image Output Glbl 1M Tokens",),
    },
    "sora-2": {"per_second": (r"Sora 2 glbl Second",)},
    "FLUX-1.1-pro": {"per_image": (r"Flux 1\.1 Pro glbl Images",)},
    "FLUX.1-Kontext-pro": {"per_image": (r"Kontext Pro glbl Images",)},
    "FLUX.2-pro": {
        "per_megapixel_first": (r"Flux 2 Pro Initial MP Megapixel",),
        "per_megapixel": (r"Flux 2 Pro MP Megapixel",),
    },
    "FLUX.2-flex": {"per_megapixel": (r"Flex Megapixel",)},
    "mistral-document-ai-2505": {"per_page": (r"Doc AI glbl 2505 Pages",)},
    "Cohere-rerank-v4.0-fast": {"per_query": (r"Rerank v4 Fast Glbl Search",)},
    "Cohere-rerank-v4.0-pro": {"per_query": (r"Rerank v4 Pro Glbl Search",)},
}
# Classic TTS and Whisper meters are not sold in REGION; use this region instead.
MEDIA_FALLBACK_REGION = "northcentralus"

# Partner models sold through Azure Marketplace are billed by the publisher and
# are absent from the Retail Prices API. The public Marketplace catalog lists
# their pay-as-you-go meters.
MARKETPLACE_API = "https://catalogapi.azure.com/offers"
MARKETPLACE_API_VERSION = "2018-08-01-beta"
MARKETPLACE_PUBLISHERS = ["anthropic", "cohere", "metagenai", "stabilityai", "nixtla"]
MARKETPLACE_METERS = {
    "paygo-inference-input-tokens": "in",
    "paygo-inf-input-tokens": "in",
    "embedding-tokens": "in",
    "paygo-inference-output-tokens": "out",
    "paygo-inf-output-tokens": "out",
    "paygo-inference-cache-hit-tokens": "cached",
    "paygo-inf-cache-hit-tokens": "cached",
    "paygo-inference-output-image": "per_image",
    "queries": "per_query",
}
MARKETPLACE_UNITS = {
    "per 1000 tokens": 1000.0,   # -> per 1M tokens
    "per 1m tokens": 1.0,
    "per 1000 images": 0.001,     # -> per image
    "per 1000 queries": 0.001,    # -> per query
}


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


def media_unit_price(item: dict, kind: str) -> Optional[float]:
    unit = item.get("unitOfMeasure", "")
    price = float(item.get("retailPrice", 0))
    if kind in TOKEN_KINDS:
        return per_million(item)
    if kind == "per_1m_chars":
        return round(price, 6) if unit == "1M" else None
    scale = {"1K": 1000, "100": 100, "1": 1, "1 Hour": 1, "1 Second": 1}.get(unit)
    return round(price / scale, 8) if scale else None


def build_media_prices(items: Iterable[dict], fallback: Iterable[dict], tracked: List[str]) -> Dict:
    names = set(tracked)
    by_meter: Dict[str, dict] = {}
    for pool in (fallback, items):  # primary region wins on duplicates
        for item in pool:
            if item.get("type") == "Consumption":
                by_meter[item.get("meterName", "").lower()] = item
    media: Dict[str, Dict[str, float]] = {}
    for model, kinds in MEDIA_METERS.items():
        if model not in names:
            continue
        prices: Dict[str, float] = {}
        for kind, patterns in kinds.items():
            for pattern in patterns:
                rx = re.compile(pattern, re.I)
                item = next((v for k, v in by_meter.items() if rx.fullmatch(k)), None)
                if item:
                    price = media_unit_price(item, kind)
                    if price is not None:
                        prices[kind] = price
                        break
        if prices:
            media[model] = prices
    return media


def marketplace_get(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": "foundry-model-availability-notifications"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except Exception:  # noqa: BLE001 - retry transient network errors
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)
    return {}


def loose(text: str) -> str:
    text = text.lower().replace("+", "plus")
    text = re.sub(r"^(meta|stability ai)\b", "", text)
    return re.sub(r"[^a-z0-9]", "", text)


def fetch_marketplace(tracked: List[str]) -> Tuple[Dict, Dict]:
    """Return ({model: {kind: per-1M price}}, {model: {per_image|per_query: price}})."""
    keys = {loose(name): name for name in tracked}
    tokens: Dict[str, Dict[str, float]] = {}
    units: Dict[str, Dict[str, float]] = {}
    query = f"api-version={MARKETPLACE_API_VERSION}&market=US"
    for publisher in MARKETPLACE_PUBLISHERS:
        publisher_filter = urllib.parse.quote(f"publisherId eq '{publisher}'")
        listing = marketplace_get(f"{MARKETPLACE_API}?{query}&$filter={publisher_filter}")
        for offer in listing.get("items", []):
            model = keys.get(loose(offer.get("displayName", "")))
            if not model:
                continue
            detail = marketplace_get(f"{MARKETPLACE_API}/{offer['id']}?{query}")
            for plan in detail.get("plans", []):
                for avail in plan.get("availabilities", []):
                    if avail.get("pricingAudience") != "DirectCommercial":
                        continue
                    meter = avail.get("meter") or {}
                    kind = MARKETPLACE_METERS.get(meter.get("meterId", ""))
                    scale = MARKETPLACE_UNITS.get((avail.get("consumptionUnitType") or "").lower())
                    price = (meter.get("price") or {}).get("listPrice")
                    if not kind or not scale or not price:
                        continue
                    target = tokens if kind in ("in", "out", "cached") else units
                    value = round(float(price) * scale, 8)
                    # Several plans can carry the same meter; keep the higher (list) price.
                    slot = target.setdefault(model, {})
                    slot[kind] = max(slot.get(kind, 0.0), value)
    return tokens, units


def main() -> int:
    tracked = sorted(json.loads(SNAPSHOT.read_text(encoding="utf-8")))
    base = f"serviceName eq 'Foundry Models' and armRegionName eq '{REGION}'"
    consumption = fetch(f"{base} and type eq 'Consumption'")
    reservations = fetch(f"productName eq '{RESERVATION_PRODUCT}' and armRegionName eq '{REGION}'")
    if not consumption:
        print("No meters returned; keeping the existing pricing.json", file=sys.stderr)
        return 1
    try:
        fallback = fetch(
            f"serviceName eq 'Foundry Models' and armRegionName eq '{MEDIA_FALLBACK_REGION}' "
            "and type eq 'Consumption' and productName eq 'Azure OpenAI'"
        )
    except Exception as exc:  # noqa: BLE001
        print(f"Fallback region fetch failed: {exc}", file=sys.stderr)
        fallback = []

    try:
        previous = json.loads(OUTPUT.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        previous = {}

    models, unmatched = build_token_prices(consumption, tracked)
    media = build_media_prices(consumption, fallback, tracked)
    sources: Dict[str, str] = {}
    try:
        market_tokens, market_units = fetch_marketplace(tracked)
    except Exception as exc:  # noqa: BLE001 - keep last known Marketplace prices
        print(f"Marketplace fetch failed, reusing previous prices: {exc}", file=sys.stderr)
        old_sources = previous.get("sources", {})
        market_tokens = {k: v.get("global", {}) for k, v in previous.get("models", {}).items()
                         if old_sources.get(k) == "marketplace"}
        market_units = {k: v for k, v in previous.get("media", {}).items() if old_sources.get(k) == "marketplace"}
    for model, prices in market_tokens.items():
        if model not in models and prices.get("in") is not None:
            models[model] = {"global": dict(sorted(prices.items()))}
            sources[model] = "marketplace"
    for model, prices in market_units.items():
        if model not in media and model not in models:
            media[model] = dict(sorted(prices.items()))

    data = {
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "https://prices.azure.com/api/retail/prices",
        "marketplace_source": MARKETPLACE_API,
        "region": REGION,
        "media_fallback_region": MEDIA_FALLBACK_REGION,
        "currency": "USD",
        "unit": "per 1M tokens",
        "models": {k: models[k] for k in sorted(models)},
        "media": {k: media[k] for k in sorted(media)},
        "sources": {k: sources[k] for k in sorted(sources)},
        "ptu": build_ptu_prices(consumption, reservations),
        "unmatched_meters": unmatched,
    }
    # Keep the file (and its date) untouched when no price moved, so the daily job doesn't commit noise.
    compared = ("region", "models", "media", "sources", "ptu", "unmatched_meters")
    unchanged = all(previous.get(key) == data[key] for key in compared)
    if not unchanged:
        OUTPUT.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    state = "unchanged" if unchanged else "updated"
    priced = len(set(models) | set(media))
    print(
        f"Priced {priced} of {len(tracked)} tracked models "
        f"({len(models)} token, {len(media)} media, {len(sources)} via Marketplace) "
        f"from {len(consumption)} meters ({state})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
