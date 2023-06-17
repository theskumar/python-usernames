"""
List of reserved usernames (pre-defined list of special banned and reserved
keywords in names, such as "root", "www", "admin"). Useful when creating
public systems, where users can choose a login name or a sub-domain name.

__References:__
1. http://www.bannedwordlist.com/
2. http://blog.postbit.com/reserved-username-list.html
3. https://ldpreload.com/blog/names-to-reserve
"""

import importlib.resources as pkg_resources


def get_reserved_words():
    with (pkg_resources.files("python_usernames") / "words.txt").open() as _f:
        return set(_f.read().splitlines())

__all__ = ["get_reserved_words"]
