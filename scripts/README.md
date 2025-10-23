# Scripts

Utility scripts for maintaining the python-usernames project.

## merge_words.py

Merges new words into the `words.txt` file while deduplicating entries and maintaining alphabetical order.

### Usage

```bash
# From a file
cat new_words.txt | python scripts/merge_words.py

# Using echo
echo -e "newword1\nnewword2\nnewword3" | python scripts/merge_words.py

# From clipboard (macOS)
pbpaste | python scripts/merge_words.py

# Interactive input (Ctrl+D to finish)
python scripts/merge_words.py
```

### Features

- Reads words from stdin (one word per line)
- Automatically converts words to lowercase
- Deduplicates against existing words
- Maintains alphabetical ordering
- Provides progress feedback and statistics
- Skips empty lines

### Example

```bash
$ echo -e "admin\nnewword\nexample" | python scripts/merge_words.py
Reading existing words from .../src/python_usernames/words.txt...
Found 527 existing words
Reading new words from stdin...
Read 3 new words from stdin
Total unique words after merge: 528
New words added: 1
Duplicates skipped: 2
Writing merged words back to .../src/python_usernames/words.txt...
✓ Successfully merged words!
```
