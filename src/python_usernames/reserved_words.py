"""
List of reserved usernames (pre-defined list of special banned and reserved
keywords in names, such as "root", "www", "admin"). Useful when creating
public systems, where users can choose a login name or a sub-domain name.

__References:__
1. http://www.bannedwordlist.com/
2. http://blog.postbit.com/reserved-username-list.html
3. https://ldpreload.com/blog/names-to-reserve
"""

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources


def get_reserved_words():
    content = ""
    # https://stackoverflow.com/questions/6028000/
    try:
        with (pkg_resources.files("python_usernames") / "words.txt").open() as _f:
            content = _f.read()
    except AttributeError:
        # Python < PY3.9, fall back to method deprecated in PY3.11.
        content = pkg_resources.read_text("python_usernames", "words.txt")

    return set(content.splitlines())


__all__ = ["get_reserved_words"]
