import re
from functools import lru_cache

from .reserved_words import get_reserved_words


username_regex = re.compile(
    r"""
    ^                       # beginning of string
    (?!_$)                  # no only _
    (?![-.])                # no - or . at the beginning
    (?!.*[_.-]{2})          # no __ or _. or ._ or .. or -- inside
    [a-zA-Z0-9_.-]+         # allowed characters, atleast one must be present
    (?<![.-])               # no - or . at the end
    $                       # end of string
    """,
    re.X,
)


@lru_cache(maxsize=1)
def _get_cached_reserved_words():
    """Cache reserved words to avoid repeated file I/O."""
    return get_reserved_words()


def is_safe_username(
    username: str, whitelist=None, blacklist=None, regex=username_regex, max_length=None
) -> bool:
    # check for max length (fastest check first)
    if max_length and len(username) > max_length:
        return False

    # check against provided regex
    if not regex.match(username):
        return False

    username_lower = username.lower()

    # Fast path: no custom lists
    if not whitelist and not blacklist:
        return username_lower not in _get_cached_reserved_words()

    # Start with reserved words
    forbidden = _get_cached_reserved_words().copy()

    # Apply whitelist (remove from forbidden)
    if whitelist:
        whitelist_set = {w.lower() for w in whitelist}
        forbidden -= whitelist_set

    # Apply blacklist (add to forbidden)
    if blacklist:
        blacklist_set = {w.lower() for w in blacklist}
        forbidden |= blacklist_set

    return username_lower not in forbidden
