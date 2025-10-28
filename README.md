# python-usernames

[![Build
Status](https://travis-ci.org/theskumar/python-usernames.svg?branch=v0.1.0)](https://travis-ci.org/theskumar/python-usernames)
[![Coverage
Status](https://coveralls.io/repos/theskumar/python-usernames/badge.svg?branch=master&service=github)](https://coveralls.io/github/theskumar/python-usernames?branch=master)
[![PyPI
version](https://badge.fury.io/py/python-usernames.svg)](http://badge.fury.io/py/python-usernames)

Python library to validate usernames suitable for use in public facing
applications where use can choose login names and sub-domains.

## Features

-   Provides a default regex validator
-   Validates against list of [banned
    words](https://github.com/theskumar/python-usernames/blob/master/usernames/reserved_words.py)
    that should not be used as username.
-   **Detailed validation results** with specific error messages and suggestions
-   Python 3.8+

## Installation

    pip install python-usernames

## Usage

### Simple Validation (Boolean Result)

```python
from python_usernames import is_safe_username

>>> is_safe_username("jerk")
False  # contains one of the banned words

>>> is_safe_username("handsome!")
False  # contains non-url friendly `!`
```

### Detailed Validation (With Error Messages)

```python
from python_usernames import validate_username

>>> result = validate_username("user@name")
>>> result.is_valid
False
>>> result.message
"Username contains invalid characters: '@'. Only alphanumeric characters, underscore (_), dash (-), and dot (.) are allowed"
>>> result.suggested_fix
'username'

>>> result = validate_username("john_doe")
>>> result.is_valid
True
```

### Options

Both **is\_safe\_username** and **validate\_username** take the following optional arguments:

-   `whitelist`: a case insensitive list of words that should be
    considered as always safe. Default: `[]`
-   `blacklist`: a case insensitive list of words that should be
    considered as unsafe. Default: `[]`
-   `max_length`: specify the maximun character a username can have.
    Default: `None`

-   `regex`: regular expression string that must pass before the banned
    words is checked. **Note**: When a custom regex is provided, only that
    regex, max_length, and reserved word checks are performed. Built-in format
    checks (like consecutive special characters) are skipped.

### Validation Reasons

The `validate_username()` function returns a `ValidationResult` with:

-   **is_valid**: `True` if valid, `False` otherwise
-   **reason**: Specific validation failure reason (enum)
-   **message**: Human-readable error message
-   **suggested_fix**: Automatic correction suggestion (when available)

Available reasons: `VALID`, `TOO_LONG`, `EMPTY`, `ONLY_UNDERSCORE`, `STARTS_WITH_SPECIAL`, 
`ENDS_WITH_SPECIAL`, `CONSECUTIVE_SPECIAL`, `INVALID_CHARACTERS`, `RESERVED_WORD`

### Default Regular Expression

    ^                       # beginning of string
    (?!_$)                  # no only _
    (?![-.])                # no - or . at the beginning
    (?!.*[_.-]{2})          # no __ or _. or ._ or .. or -- inside
    [a-zA-Z0-9_.-]+         # allowed characters, atleast one must be present
    (?<![.-])               # no - or . at the end
    $                       # end of string

### Real-World Example

```python
from python_usernames import validate_username

def register_user(username: str):
    result = validate_username(username, max_length=20)
    
    if not result.is_valid:
        print(f"Error: {result.message}")
        if result.suggested_fix:
            print(f"Try: '{result.suggested_fix}'")
        return False
    
    # Create user account
    return True
```

## Documentation

-   [Detailed Validation Guide](DETAILED_VALIDATION.md) - Comprehensive usage examples
-   [Migration Guide](MIGRATION_GUIDE.md) - How to upgrade from `is_safe_username()`
-   [Examples](examples/detailed_validation.py) - Real-world usage patterns

## Credits

- [The-Big-Username-Blocklist](https://github.com/marteinn/The-Big-Username-Blocklist)

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

## License

MIT
