# -*- coding: utf-8 -*-
import re

from .reserved_words import get_reserved_wordlist


def is_safe_username(username, whitelist=None, blacklist=None, regex="^[a-zA-Z0-9_.-]+$"):
    if not re.match(regex, username):
        return False
    wordlist = get_reserved_wordlist()
    whitelist = whitelist or set()
    blacklist = blacklist or set()
    wordlist = wordlist - whitelist
    wordlist = wordlist.union(blacklist)
    return False if username.lower() in wordlist else True
