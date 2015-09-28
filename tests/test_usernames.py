from usernames import is_safe_username


def test_usernames():
    assert not is_safe_username("#")
    assert not is_safe_username("()")
    assert not is_safe_username("!")
    assert not is_safe_username("fuck")
