#!/usr/bin/env python3
"""Report how many live models have region availability data.

Live models are the non-retired entries in Microsoft's retirement schedule
(.region-watch/retirement_data.json), the broadest published list of Foundry models. A live model is
covered when it appears in .region-watch/regions_snapshot.json. Some models (for example those only
listed in capability tables) have no published region table, so full coverage isn't expected.

Writes a Markdown summary to $GITHUB_STEP_SUMMARY when set. Exits 1 if coverage falls below
--min-coverage.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent


def norm(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", name.lower())


def live_models(retirement: dict, today: str) -> dict:
    models = {}
    for category, entries in (retirement.get("models") or {}).items():
        if category == "fine_tuned":
            continue
        for entry in entries:
            if entry.get("lifecycle") == "Retired":
                continue
            date = re.sub(r"(?i)^no earlier than\s*", "", str(entry.get("retirement_date") or "")).strip()
            if re.match(r"^\d{4}-\d{2}-\d{2}$", date) and date < today:
                continue
            models.setdefault(norm(entry["model"]), entry["model"])
    return models


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--min-coverage", type=float, default=0.0, help="fail below this ratio (0-1)")
    args = parser.parse_args()

    snapshot = json.loads((HERE / "regions_snapshot.json").read_text(encoding="utf-8"))
    retirement = json.loads((HERE / "retirement_data.json").read_text(encoding="utf-8"))
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    live = live_models(retirement, today)
    tracked = {norm(name) for name in snapshot}
    missing = sorted((name for key, name in live.items() if key not in tracked), key=str.lower)
    covered = len(live) - len(missing)
    ratio = covered / len(live) if live else 1.0

    lines = [
        "## Model coverage",
        "",
        f"- Models with region data: **{len(snapshot)}**",
        f"- Live models in the retirement schedule with region data: **{covered} / {len(live)} ({ratio:.0%})**",
    ]
    if missing:
        lines += ["", "Live models without a published region table:", ""]
        lines += [f"- `{name}`" for name in missing]
    report = "\n".join(lines) + "\n"
    print(report)

    summary = os.getenv("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as handle:
            handle.write(report)
    if missing and os.getenv("GITHUB_ACTIONS"):
        print(f"::warning title=Model coverage::{len(missing)} live models have no region data: {', '.join(missing)}")

    if ratio < args.min_coverage:
        print(f"Coverage {ratio:.0%} is below the required {args.min_coverage:.0%}.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
