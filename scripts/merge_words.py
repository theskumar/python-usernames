#!/usr/bin/env python3
"""
Utility script to merge new words into words.txt file.

Reads words from stdin (one word per line) and merges them with existing
words in the words.txt file, deduplicating any entries and maintaining
alphabetical order.

Usage:
    cat new_words.txt | python scripts/merge_words.py
    echo -e "newword1\nnewword2" | python scripts/merge_words.py
"""

import sys
from pathlib import Path


def main():
    # Determine the path to words.txt
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    words_file = project_root / "src" / "python_usernames" / "words.txt"

    if not words_file.exists():
        print(f"Error: words.txt not found at {words_file}", file=sys.stderr)
        sys.exit(1)

    # Read existing words from words.txt
    print(f"Reading existing words from {words_file}...", file=sys.stderr)
    with open(words_file, "r", encoding="utf-8") as f:
        existing_words = set(line.strip().lower() for line in f if line.strip())

    print(f"Found {len(existing_words)} existing words", file=sys.stderr)

    # Read new words from stdin
    print("Reading new words from stdin...", file=sys.stderr)
    new_words = set()
    for line in sys.stdin:
        word = line.strip().lower()
        if word:  # Skip empty lines
            new_words.add(word)

    print(f"Read {len(new_words)} new words from stdin", file=sys.stderr)

    # Merge and deduplicate
    all_words = existing_words | new_words

    # Count how many new words were actually added
    added_count = len(all_words) - len(existing_words)
    duplicate_count = len(new_words) - added_count

    print(f"Total unique words after merge: {len(all_words)}", file=sys.stderr)
    print(f"New words added: {added_count}", file=sys.stderr)
    print(f"Duplicates skipped: {duplicate_count}", file=sys.stderr)

    # Sort alphabetically
    sorted_words = sorted(all_words)

    # Write back to words.txt
    print(f"Writing merged words back to {words_file}...", file=sys.stderr)
    with open(words_file, "w", encoding="utf-8") as f:
        for word in sorted_words:
            f.write(f"{word}\n")

    print("✓ Successfully merged words!", file=sys.stderr)


if __name__ == "__main__":
    main()
