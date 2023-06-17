import re

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


def is_safe_username(
    username: str, whitelist=None, blacklist=None, regex=username_regex, max_length=None
) -> bool:
    # check for max length
    if max_length and len(username) > max_length:
        return False

    # check against provided regex
    if not re.match(regex, username):
        return False

    # ensure the word is not in the blacklist and is not a reserved word
    if whitelist is None:
        whitelist = []

    if blacklist is None:
        blacklist = []

    default_words = get_reserved_words()

    whitelist = set(
        [each_whitelisted_name.lower() for each_whitelisted_name in whitelist]
    )
    blacklist = set(
        [each_blacklisted_name.lower() for each_blacklisted_name in blacklist]
    )

    default_words = default_words - whitelist
    default_words = default_words.union(blacklist)

    return False if username.lower() in default_words else True
