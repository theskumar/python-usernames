from usernames import is_safe_username


def test_usernames():
    unsafe_words = [
        '!',
        '#',
        '',
        '()',
        '-hello',
        '.hello',
        'fuck',
        'hel--lo',
        'hel-.lo',
        'hel..lo',
        'hel__lo',
        'hello-',
        'hello.',
        'sex',
    ]

    safe_words = [
        '10101',
        '1he-llo',
        '_hello',
        'he-llo',
        'he.llo_',
        'hello',
        'hello_',
    ]

    for w in unsafe_words:
        assert not is_safe_username(w)

    for w in safe_words:
        assert is_safe_username(w)
