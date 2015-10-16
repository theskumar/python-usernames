# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from .reserved_words import get_reserved_wordlist


username_regex = re.compile(r"""
    ^                       # beginning of string
    (?!_$)                  # no only _
    (?![-.])                # no - or . at the beginning
    (?!.*[_.-]{2})          # no __ or _. or ._ or .. or -- inside
    [a-zA-Z0-9_.-]+         # allowed characters, atleast one must be present
    (?<![.-])               # no - or . at the end
    $                       # end of string
    """, re.X)


def is_safe_username(username, whitelist=None, blacklist=None,
                     regex=username_regex):
    if not re.match(regex, username):
        return False
    wordlist = get_reserved_wordlist()
    whitelist = whitelist or set()
    blacklist = blacklist or set()
    wordlist = wordlist - whitelist
    wordlist = wordlist.union(blacklist)
    return False if username.lower() in wordlist else True
