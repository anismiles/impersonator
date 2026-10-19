#!/usr/bin/env python3
"""
Clean an SRT or VTT subtitle file into a plain-text transcript.
Removes timestamps, cue numbers, repeated lines and HTML tags, and
writes text you can read directly.

Usage:
    python3 srt_to_transcript.py input.srt [output.txt]
    python3 srt_to_transcript.py input.vtt [output.txt]

If you do not give an output file, the output goes to input_transcript.txt.
"""

import sys
import re
from pathlib import Path


def clean_srt(content: str) -> str:
    """Clean SRT subtitles."""
    lines = content.strip().split('\n')
    texts = []

    for line in lines:
        line = line.strip()
        # Skip cue number lines (digits only)
        if re.match(r'^\d+$', line):
            continue
        # Skip timestamp lines
        if re.match(r'\d{2}:\d{2}:\d{2}', line):
            continue
        # Skip empty lines
        if not line:
            continue
        # Remove HTML tags
        line = re.sub(r'<[^>]+>', '', line)
        # Remove VTT position settings
        line = re.sub(r'align:.*$|position:.*$', '', line).strip()
        if line:
            texts.append(line)

    # Remove consecutive duplicates (common in auto-generated subtitles)
    deduped = []
    for text in texts:
        if not deduped or text != deduped[-1]:
            deduped.append(text)

    # Build paragraphs: join short lines, and break at sentence-ending
    # punctuation or when the paragraph gets long
    result = []
    current = []

    for text in deduped:
        current.append(text)
        joined = ' '.join(current)
        if len(joined) > 200 or re.search(r'[.!?]["\')\]]?$', text):
            result.append(joined)
            current = []

    if current:
        result.append(' '.join(current))

    return '\n\n'.join(result)


def clean_vtt(content: str) -> str:
    """Clean VTT subtitles (strip the VTT header, then use the SRT logic)."""
    # Remove the WEBVTT header
    content = re.sub(r'^WEBVTT.*?\n\n', '', content, flags=re.DOTALL)
    # Remove NOTE blocks
    content = re.sub(r'NOTE.*?\n\n', '', content, flags=re.DOTALL)
    return clean_srt(content)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 srt_to_transcript.py <input.srt|input.vtt> [output.txt]")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"ERROR: file not found: {input_path}")
        sys.exit(1)

    # Default output file name
    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.parent / f"{input_path.stem}_transcript.txt"

    # Read the file and detect the format
    content = input_path.read_text(encoding='utf-8')

    if input_path.suffix.lower() == '.vtt' or content.startswith('WEBVTT'):
        transcript = clean_vtt(content)
    else:
        transcript = clean_srt(content)

    output_path.write_text(transcript, encoding='utf-8')

    # Stats
    word_count = len(transcript.split())
    paragraph_count = len([p for p in transcript.split('\n\n') if p.strip()])
    print(f"Done: {output_path}")
    print(f"   Words: {word_count}  Paragraphs: {paragraph_count}")


if __name__ == '__main__':
    main()
