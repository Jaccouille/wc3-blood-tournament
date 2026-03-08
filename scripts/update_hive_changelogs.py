#!/usr/bin/env python3
"""
Regenerates hiveChangelogs.md from .wurst changelog files.

Reads all v*.wurst files in wurst/changelogs/, parses version and entries,
then writes BBCode-formatted spoilers to hiveChangelogs.md (newest version first).
"""

import re
import os
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
CHANGELOGS_DIR = PROJECT_DIR / "wurst" / "changelogs"
OUTPUT_FILE = PROJECT_DIR / "hiveChangelogs.md"


def parse_wurst_file(path: Path):
    """
    Returns (sort_key, version_label, entries) or None if parsing fails.
    sort_key is (major, minor, patch_letter) for sorting.
    version_label is e.g. "0.3f".
    """
    text = path.read_text(encoding="utf-8")

    # Match: new ChangeLog(major, minor, 'patch')
    header_match = re.search(r"new ChangeLog\((\d+),\s*(\d+),\s*'([a-z])'\)", text)
    if not header_match:
        print(f"  WARNING: no ChangeLog constructor found in {path.name}, skipping.")
        return None

    major = int(header_match.group(1))
    minor = int(header_match.group(2))
    patch = header_match.group(3)

    version_label = f"{major}.{minor}{patch}"
    sort_key = (major, minor, patch)

    # Match all ..add("...") entries
    entries = re.findall(r'\.\.add\("([^"]+)"\)', text)

    return sort_key, version_label, entries


def build_hive_content(parsed: list[tuple]) -> str:
    lines = ["", "# Changelogs", "", "", "[SPOILER=\"Changelogs\"]", ""]

    for _, version_label, entries in parsed:
        lines.append(f'[SPOILER="{version_label}"]')
        for entry in entries:
            lines.append(f"-{entry}")
        lines.append("[/SPOILER]")
        lines.append("")

    lines.append("")
    lines.append("[/SPOILER]")
    lines.append("")

    return "\n".join(lines)


def main():
    wurst_files = sorted(CHANGELOGS_DIR.glob("v*.wurst"))
    if not wurst_files:
        print(f"No .wurst files found in {CHANGELOGS_DIR}")
        return

    print(f"Found {len(wurst_files)} changelog files.")

    parsed = []
    for f in wurst_files:
        result = parse_wurst_file(f)
        if result:
            parsed.append(result)
            print(f"  Parsed {f.name} -> {result[1]} ({len(result[2])} entries)")

    # Sort newest first: compare tuples (major, minor, patch_letter) descending
    parsed.sort(key=lambda x: (x[0][0], x[0][1], x[0][2]), reverse=True)

    content = build_hive_content(parsed)
    OUTPUT_FILE.write_text(content, encoding="utf-8")
    print(f"\nWrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
