#!/usr/bin/env python3
"""
Merge the research output of the 6 research agents into a summary table
for the Phase 1.5 research review checkpoint.

Scans the 01-06 markdown files in references/research/ and reports, for
each dimension, the number of sources, the primary/secondary source split,
and the key findings.

Usage:
    python3 merge_research.py <skill folder path>

Example:
    python3 merge_research.py .claude/skills/elon-musk-perspective

Output: prints a markdown-style summary table to stdout.
"""

import sys
import re
from pathlib import Path

AGENTS = {
    '01-writings': 'Writings',
    '02-conversations': 'Conversations',
    '03-expression-dna': 'Expression',
    '04-external-views': 'External',
    '05-decisions': 'Decisions',
    '06-timeline': 'Timeline',
}

URL_RE = re.compile(r'https?://[^\s\)\]>]+')
# Lines such as "Source: ..." or "- **Source**: ..."
SOURCE_LABEL_RE = re.compile(r'^\s*(?:[-*]\s*)?\**\s*Sources?\s*\**\s*:', re.IGNORECASE | re.MULTILINE)
PRIMARY_RE = re.compile(
    r'\b(?:primary|first-?hand|original text|in (?:his|her|their) own words|direct quote|verbatim)\b',
    re.IGNORECASE,
)
SECONDARY_RE = re.compile(
    r'\b(?:secondary|second-?hand|paraphrase[ds]?|summary|commentary|analysis)\b',
    re.IGNORECASE,
)
KEY_FINDINGS_RE = re.compile(
    r'^#{2,4}\s*Key findings\s*$(.*?)(?=^#{1,4}\s|\Z)',
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)
CONTRADICTION_RE = re.compile(
    r'\b(?:contradict\w*|conflict\w*|on the contrary|but in fact|disputed|controvers\w*|inconsistent)\b.{0,100}',
    re.IGNORECASE,
)


def count_sources(content: str) -> dict:
    """Count sources and the primary/secondary split."""
    # Unique URLs are the source count. If a file has no URLs,
    # fall back to the number of "Source:" labels.
    urls = URL_RE.findall(content)
    source_labels = len(SOURCE_LABEL_RE.findall(content))
    unique_urls = len(set(urls))

    return {
        'url_count': len(urls),
        'unique_urls': unique_urls,
        'source_count': unique_urls if unique_urls else source_labels,
        'primary_markers': len(PRIMARY_RE.findall(content)),
        'secondary_markers': len(SECONDARY_RE.findall(content)),
    }


def extract_key_findings(content: str, max_items: int = 3) -> list[str]:
    """Extract key findings.

    Order of preference: bullets under a "Key findings" heading, then
    level-2 headings, then bold items, then the first non-empty lines.
    """
    section = KEY_FINDINGS_RE.search(content)
    if section:
        bullets = re.findall(r'^\s*(?:[-*]|\d+\.)\s+(.+)$', section.group(1), re.MULTILINE)
        if bullets:
            return [re.sub(r'\*\*', '', b).strip() for b in bullets[:max_items]]

    headings = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
    if headings:
        return headings[:max_items]

    bolds = re.findall(r'\*\*(.+?)\*\*', content)
    if bolds:
        return bolds[:max_items]

    lines = [l.strip() for l in content.split('\n') if l.strip() and not l.startswith('#')]
    return [l[:50] + '...' if len(l) > 50 else l for l in lines[:max_items]]


def find_contradictions(files: dict[str, str]) -> list[str]:
    """Simple check for contradictions flagged in the research files."""
    contradictions = []
    for name, content in files.items():
        for m in CONTRADICTION_RE.findall(content):
            contradictions.append(f"{AGENTS.get(name, name)}: {m[:80]}")
    return contradictions[:5]  # At most 5 items


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 merge_research.py <skill folder path>")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    research_dir = skill_dir / 'references' / 'research'

    if not research_dir.exists():
        print(f"ERROR: folder not found: {research_dir}")
        sys.exit(1)

    files = {}
    rows = []
    total_sources = 0
    total_primary = 0
    total_secondary = 0
    missing = []

    for key, label in AGENTS.items():
        md_file = research_dir / f"{key}.md"
        if not md_file.exists():
            missing.append(label)
            rows.append(f"│ {label:<14} │ {'MISSING':<8} │ {'-':<26} │")
            continue

        content = md_file.read_text(encoding='utf-8')
        files[key] = content
        stats = count_sources(content)
        findings = extract_key_findings(content)

        total_sources += stats['source_count']
        total_primary += stats['primary_markers']
        total_secondary += stats['secondary_markers']

        findings_str = ', '.join(findings) if findings else '-'
        if len(findings_str) > 26:
            findings_str = findings_str[:23] + '...'

        rows.append(f"│ {label:<14} │ {stats['source_count']:<8} │ {findings_str:<26} │")

    contradictions = find_contradictions(files)

    print("┌────────────────┬──────────┬────────────────────────────┐")
    print("│ Agent          │ Sources  │ Key findings               │")
    print("├────────────────┼──────────┼────────────────────────────┤")
    for row in rows:
        print(row)
    print("├────────────────┼──────────┼────────────────────────────┤")

    marked = total_primary + total_secondary
    primary_ratio = f"{total_primary}/{marked}" if marked > 0 else "unmarked"
    print(f"│ {'Total sources':<14} │ {total_sources:<8} │ {'Primary: ' + primary_ratio:<26} │")

    if contradictions:
        print(f"│ {'Contradictions':<14} │ {len(contradictions):<8} │ {contradictions[0][:26]:<26} │")
    else:
        print(f"│ {'Contradictions':<14} │ {0:<8} │ {'-':<26} │")

    if missing:
        missing_str = ', '.join(missing)
        if len(missing_str) > 26:
            missing_str = missing_str[:23] + '...'
        print(f"│ {'Thin areas':<14} │ {len(missing):<8} │ {missing_str:<26} │")
    else:
        print(f"│ {'Thin areas':<14} │ {'none':<8} │ {'-':<26} │")

    print("└────────────────┴──────────┴────────────────────────────┘")

    if total_sources < 10:
        print("\nWARNING: fewer than 10 sources in total. Lower your expectations or do more research.")
    if missing:
        print(f"\nWARNING: missing dimensions: {', '.join(missing)}. Add research, or flag them in the honest boundaries.")


if __name__ == '__main__':
    main()
