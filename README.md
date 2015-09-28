# python-usernames
Python library to validate usernames suitable for use in public facing applications.

## Features

- Proviedes a default regex validator
- Validates against list of banned words that should not be used as username.
- Python 2.6, 2.7, 3.3, 3.4

## Installation

```
pip install python-usernames
```

## Usages

```python
from usernames import is_safe_username

>> is_safe_username("jerk")
False  # contains one of the banned words
>> is_safe_username("handsome!")
False  # contains non-url friendly `!`
```

__is_safe_username__ takes the following optional arguments:

- `regex`: regular expression string that must pass before the banned words is checked. Default is `^[a-zA-Z0-9_.-]+$`
- `whitelist`: a list of words that should be considered as always safe.
- `blacklist`: a list of words that should be considered as unsafe.

## License
MIT
