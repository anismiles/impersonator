#!/bin/bash
# Download subtitles for a YouTube video.
# Usage: ./download_subtitles.sh <YouTube_URL> [output folder]
# Manual subtitles come first. If there are none, it falls back to auto-generated subtitles.
# Priority: English manual > any manual > English auto-generated

set -e

URL="$1"
OUTPUT_DIR="${2:-.}"

if [ -z "$URL" ]; then
    echo "Usage: ./download_subtitles.sh <YouTube_URL> [output folder]"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

# Marker file: only subtitle files newer than this count as downloaded by this run
MARKER="$OUTPUT_DIR/.ytdlp_marker"
touch "$MARKER"
trap 'rm -f "$MARKER"' EXIT

find_new_subs() {
    find "$OUTPUT_DIR" \( -name "*.srt" -o -name "*.vtt" \) -newer "$MARKER" 2>/dev/null | head -1
}

echo ">>> Checking available subtitles..."
yt-dlp --list-subs --no-download "$URL" 2>/dev/null | tail -20 || true

echo ""
echo ">>> Trying English manual subtitles..."

# Attempt 1: English manual subtitles
if yt-dlp --write-subs --sub-langs "en,en-US,en-GB" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL" 2>/dev/null; then
    FOUND=$(find_new_subs)
    if [ -n "$FOUND" ]; then
        echo "Downloaded: $FOUND"
        exit 0
    fi
fi

# Attempt 2: manual subtitles in any language
echo ">>> No English manual subtitles. Trying manual subtitles in any language..."
if yt-dlp --write-subs --sub-langs "all,-live_chat" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL" 2>/dev/null; then
    FOUND=$(find_new_subs)
    if [ -n "$FOUND" ]; then
        echo "Downloaded: $FOUND"
        exit 0
    fi
fi

# Attempt 3: English auto-generated subtitles
echo ">>> No manual subtitles. Trying English auto-generated subtitles..."
if yt-dlp --write-auto-subs --sub-langs "en,en-US,en-GB" --sub-format srt --skip-download -o "$OUTPUT_DIR/%(title)s" "$URL" 2>/dev/null; then
    FOUND=$(find_new_subs)
    if [ -n "$FOUND" ]; then
        echo "Downloaded auto-generated subtitles: $FOUND"
        exit 0
    fi
fi

echo "ERROR: no usable subtitles found"
exit 1
