# python-usernames

[![Test](https://github.com/theskumar/python-usernames/actions/workflows/test.yml/badge.svg)](https://github.com/theskumar/python-usernames/actions/workflows/test.yml)
[![PyPI version](https://badge.fury.io/py/python-usernames.svg)](https://pypi.org/project/python-usernames/)
[![Python Versions](https://img.shields.io/pypi/pyversions/python-usernames.svg)](https://pypi.org/project/python-usernames/)

Python library to validate usernames suitable for use in public facing
applications where use can choose login names and sub-domains.

## Features

-   Provides a default regex validator
-   Validates against list of [banned
    words](https://github.com/theskumar/python-usernames/blob/master/usernames/reserved_words.py)
    that should not be used as username.
-   Python 3.8+

## Installation

    pip install python-usernames

## Usages

```python
from python_usernames import is_safe_username

>>> is_safe_username("jerk")
False  # contains one of the banned words

>>> is_safe_username("handsome!")
False  # contains non-url friendly `!`
```

**is\_safe\_username** takes the following optional arguments:

-   `whitelist`: a case insensitive list of words that should be
    considered as always safe. Default: `[]`
-   `blacklist`: a case insensitive list of words that should be
    considered as unsafe. Default: `[]`
-   `max_length`: specify the maximun character a username can have.
    Default: `None`

- `regex`: regular expression string that must pass before the banned
:   words is checked.

The default regular expression is as follows:

    ^                       # beginning of string
    (?!_$)                  # no only _
    (?![-.])                # no - or . at the beginning
    (?!.*[_.-]{2})          # no __ or _. or ._ or .. or -- inside
    [a-zA-Z0-9_.-]+         # allowed characters, atleast one must be present
    (?<![.-])               # no - or . at the end
    $                       # end of string

## Credits

- [The-Big-Username-Blocklist](https://github.com/marteinn/The-Big-Username-Blocklist)
- [Profanity-filter](https://github.com/rominf/profanity-filter/blob/master/profanity_filter/data/en_profane_words.txt)

## Further Reading

-   [Let’s talk about
    usernames](https://www.b-list.org/weblog/2018/feb/11/usernames/)

## Gotchas

Words like `bigcock12` will validated just fine, only equality against
the [banned word
lists](https://github.com/theskumar/python-usernames/blob/master/usernames/reserved_words.py)
is checked. We don't try to be smart to avoid [Scunthorpe
problem](https://en.wikipedia.org/wiki/Scunthorpe_problem). If you can
come up with a algorithm/solution, please create an issue/pr :).

## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management and packaging.

### Setup

1. Install uv:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Clone the repository and sync dependencies:
   ```bash
   git clone https://github.com/theskumar/python-usernames.git
   cd python-usernames
   uv sync --all-groups
   ```

### Running Tests

```bash
uv run pytest
```

### Linting

```bash
uv run ruff check .
uv run black --check .
```

### Building

```bash
uv build
```

## License

MIT
