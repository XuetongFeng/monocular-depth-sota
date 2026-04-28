#!/usr/bin/env python3
"""Validate the structured paper index."""

from __future__ import annotations

import json
from pathlib import Path


REQUIRED_KEYS = {
    "title",
    "system",
    "year",
    "venue",
    "category",
    "paper_url",
    "code_url",
    "note",
}


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    data_path = root / "data" / "papers.json"
    papers = json.loads(data_path.read_text(encoding="utf-8"))

    if not isinstance(papers, list) or not papers:
        raise SystemExit("papers.json must contain a non-empty list")

    seen_titles: set[str] = set()
    for index, paper in enumerate(papers, start=1):
        missing = REQUIRED_KEYS - paper.keys()
        if missing:
            raise SystemExit(f"paper #{index} missing keys: {sorted(missing)}")

        title = paper["title"].strip()
        if not title:
            raise SystemExit(f"paper #{index} has an empty title")
        if title in seen_titles:
            raise SystemExit(f"duplicate title: {title}")
        seen_titles.add(title)

        if not isinstance(paper["year"], int):
            raise SystemExit(f"{title}: year must be an integer")
        if paper["paper_url"] and not paper["paper_url"].startswith("https://"):
            raise SystemExit(f"{title}: paper_url should use https")
        if paper["code_url"] and not paper["code_url"].startswith("https://"):
            raise SystemExit(f"{title}: code_url should use https")

    print(f"Validated {len(papers)} papers.")


if __name__ == "__main__":
    main()

