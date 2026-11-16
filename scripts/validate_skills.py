#!/usr/bin/env python3
"""Validate all skills/*/SKILL.md manifests in the repository."""

from pathlib import Path
import sys


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("Missing opening '---' YAML frontmatter delimiter")
    end_idx = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break
    if end_idx is None:
        raise ValueError("Missing closing '---' YAML frontmatter delimiter")

    meta: dict[str, str] = {}
    for line in lines[1:end_idx]:
        if ":" in line and not line.startswith(" "):
            key, val = line.split(":", 1)
            meta[key.strip()] = val.strip().strip("'\"")
    return meta


def main() -> int:
    skills_dir = Path(__file__).resolve().parent.parent / "skills"
    skill_files = sorted(skills_dir.glob("*/SKILL.md"))
    if not skill_files:
        print("ERROR: No skills/*/SKILL.md files found", file=sys.stderr)
        return 1

    errors = 0
    for skill_file in skill_files:
        folder_name = skill_file.parent.name
        try:
            meta = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
            name = meta.get("name", "")
            desc = meta.get("description", "")
            if not name:
                raise ValueError("Missing 'name' in frontmatter")
            if name != folder_name:
                raise ValueError(f"Frontmatter name '{name}' != folder '{folder_name}'")
            if len(desc) < 20:
                raise ValueError("'description' is missing or too short")
            print(f"OK: {folder_name}")
        except Exception as exc:
            print(f"FAIL: {skill_file}: {exc}", file=sys.stderr)
            errors += 1

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
