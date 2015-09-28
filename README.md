# python-usernames

[![Build Status](https://travis-ci.org/theskumar/python-usernames.svg?branch=v0.1.0)](https://travis-ci.org/theskumar/python-usernames) [![Coverage Status](https://coveralls.io/repos/theskumar/python-usernames/badge.svg?branch=master&service=github)](https://coveralls.io/github/theskumar/python-usernames?branch=master) [![PyPI version](https://badge.fury.io/py/python-usernames.svg)](http://badge.fury.io/py/python-usernames) [![PyPI](https://img.shields.io/pypi/dm/python-usernames.svg)](https://pypi.python.org/pypi/python-usernames)

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
