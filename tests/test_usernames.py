# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from usernames import is_safe_username


def test_usernames():
    unsafe_words = [
        '!',
        '#',
        '',
        '()',
        '-',
        '-hello',
        '.',
        '.hello',
        '_',
        'a@!/',
        'fuck',
        'hel--lo',
        'hel-.lo',
        'hel..lo',
        'hel__lo',
        'hello-',
        'hello.',
        'sex',
        "\\",
        "\\\\",
        "--1",
        "!@#$%^&*()`~",
        "`⁄€‹›ﬁﬂ‡°·‚—±",
        "⅛⅜⅝⅞",
    ]

    safe_words = [
        'a'
        '10101',
        '1he-llo',
        '_hello',
        'he-llo',
        'he.llo_',
        'hello',
        'hello_',
        "999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
    ]

    for w in unsafe_words:
        assert not is_safe_username(w)

    for w in safe_words:
        assert is_safe_username(w)
