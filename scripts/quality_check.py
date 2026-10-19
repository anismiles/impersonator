#!/usr/bin/env python3
"""
Check a generated person skill against the Phase 4 pass criteria.

The checks count real content (models with evidence and limits, filled
fields, list items, research files with URLs) instead of matching keywords,
so a skill cannot pass by renaming headings.

Usage:
    python3 quality_check.py <path to SKILL.md>

Example:
    python3 quality_check.py .claude/skills/paul-graham-perspective/SKILL.md
"""

import re
import sys
from pathlib import Path

# Template placeholders look like [Name] or [Source 1, with URL]. Markdown links
# ([text](url)) are not placeholders, so a "(" right after "]" is excluded.
PLACEHOLDER = re.compile(r"\[(?:[A-Z][^\]\n]{0,60}|\.\.\.|N|YYYY-MM-DD|year|Date)\](?!\()")
URL = re.compile(r"https?://\S+")


def section(content: str, title: str, level: int = 2) -> str:
    """Return the body of the first heading whose text starts with title."""
    hashes = "#" * level
    m = re.search(rf"^{hashes}\s+{re.escape(title)}[^\n]*\n(.*?)(?=^#{{1,{level}}}\s|\Z)",
                  content, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    return m.group(1) if m else ""


def bullets(text: str, min_words: int = 1) -> list[str]:
    items = re.findall(r"^\s*(?:[-*]|\d+\.)\s+(.*)$", text, re.MULTILINE)
    return [i for i in items if len(i.split()) >= min_words]


def field(block: str, name: str) -> str:
    m = re.search(rf"\*\*{re.escape(name)}\*\*\s*:?\s*(.*?)(?=\n\*\*|\Z)", block, re.DOTALL | re.IGNORECASE)
    return m.group(1).strip() if m else ""


def check_models(content: str) -> tuple[bool, str]:
    """3-7 models, each with evidence from 2+ contexts and a real limit."""
    body = section(content, "Core Mental Models")
    blocks = re.split(r"^###\s+", body, flags=re.MULTILINE)[1:]
    if not blocks:
        return False, "no models under '## Core Mental Models'"
    weak = []
    for b in blocks:
        name = b.splitlines()[0].strip()
        evidence = field(b, "Evidence")
        limits = field(b, "Limits")
        pieces = len(bullets(evidence)) or len(re.findall(r"[.;]\s|\n", evidence)) + 1
        if pieces < 2 or len(evidence.split()) < 15:
            weak.append(f"{name}: evidence thin")
        if len(limits.split()) < 6:
            weak.append(f"{name}: limits missing or vague")
    count = len(blocks)
    ok = 3 <= count <= 7 and not weak
    detail = f"{count} models"
    if not 3 <= count <= 7:
        detail += " (need 3-7)"
    if weak:
        detail += "; " + "; ".join(weak)
    return ok, detail


def check_heuristics(content: str) -> tuple[bool, str]:
    body = section(content, "Decision Heuristics")
    rules = re.findall(r"^\d+\.\s+\*\*", body, re.MULTILINE)
    ok = 5 <= len(rules) <= 10
    return ok, f"{len(rules)} heuristics" + ("" if ok else " (need 5-10)")


def check_expression_dna(content: str) -> tuple[bool, str]:
    """At least 4 of the 6 style fields filled with real content."""
    body = section(content, "Expression DNA")
    names = ["Sentence style", "Vocabulary", "Rhythm", "Humor", "Certainty", "Citation habits"]
    filled = 0
    for n in names:
        m = re.search(rf"^\s*-\s*{n}\s*:\s*(.+)$", body, re.MULTILINE | re.IGNORECASE)
        if m and len(m.group(1).split()) >= 4 and not PLACEHOLDER.search(m.group(1)):
            filled += 1
    ok = filled >= 4
    return ok, f"{filled}/6 style fields filled" + ("" if ok else " (need 4)")


def check_boundaries(content: str) -> tuple[bool, str]:
    """3+ specific limits beyond the generic ones, plus a research date."""
    body = section(content, "Honest Boundaries")
    generic = re.compile(r"cannot replace|not the real person|research date", re.IGNORECASE)
    specific = [b for b in bullets(body, min_words=6) if not generic.search(b)]
    has_date = bool(re.search(r"research date:\s*\d{4}-\d{2}-\d{2}", body, re.IGNORECASE))
    ok = len(specific) >= 3 and has_date
    detail = f"{len(specific)} specific limits"
    if len(specific) < 3:
        detail += " (need 3)"
    if not has_date:
        detail += "; research date missing"
    return ok, detail


def check_tensions(content: str) -> tuple[bool, str]:
    body = section(content, "Internal tensions", level=3)
    items = bullets(body, min_words=6)
    ok = len(items) >= 2
    return ok, f"{len(items)} tensions" + ("" if ok else " (need 2)")


def check_sources(content: str) -> tuple[bool, str]:
    """Primary sources are more than half of all listed sources."""
    primary = bullets(section(content, "Primary sources", level=3))
    secondary = bullets(section(content, "Secondary sources", level=3))
    total = len(primary) + len(secondary)
    if total == 0:
        return False, "no sources listed"
    ratio = len(primary) / total
    ok = ratio > 0.5
    return ok, f"primary {len(primary)}/{total} ({ratio:.0%})" + ("" if ok else " (need >50%)")


def check_research_files(skill_path: Path) -> tuple[bool, str]:
    """Research notes exist next to the skill and cite URLs."""
    folder = skill_path.parent / "references" / "research"
    files = sorted(folder.glob("*.md")) if folder.is_dir() else []
    urls = sum(len(URL.findall(f.read_text(encoding="utf-8"))) for f in files)
    ok = len(files) >= 3 and urls >= 10
    return ok, f"{len(files)} research files, {urls} URLs" + ("" if ok else " (need 3 files, 10 URLs)")


def check_placeholders(content: str) -> tuple[bool, str]:
    left = sorted(set(PLACEHOLDER.findall(content)))
    ok = not left
    return ok, "none left" if ok else "left: " + ", ".join(left[:5])


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 quality_check.py <path to SKILL.md>")
        sys.exit(1)
    skill_path = Path(sys.argv[1])
    if not skill_path.exists():
        print(f"File not found: {skill_path}")
        sys.exit(1)
    content = skill_path.read_text(encoding="utf-8")

    checks = [
        ("Mental models", lambda: check_models(content)),
        ("Heuristics", lambda: check_heuristics(content)),
        ("Expression DNA", lambda: check_expression_dna(content)),
        ("Honest boundaries", lambda: check_boundaries(content)),
        ("Internal tensions", lambda: check_tensions(content)),
        ("Primary sources", lambda: check_sources(content)),
        ("Research files", lambda: check_research_files(skill_path)),
        ("Placeholders", lambda: check_placeholders(content)),
    ]

    print(f"Quality check: {skill_path}")
    print("=" * 60)
    passed = 0
    for name, fn in checks:
        ok, detail = fn()
        passed += ok
        print(f"  {name:<18} {'PASS' if ok else 'FAIL'}  {detail}")
    print("=" * 60)
    print(f"Result: {passed}/{len(checks)} passed")
    if passed == len(checks):
        print("All checks passed. Ready for the Phase 4 behavior tests.")
    else:
        print("Fix the failed items in Phase 2 or 3. Do not rename headings to pass.")
    sys.exit(0 if passed == len(checks) else 1)


if __name__ == "__main__":
    main()
