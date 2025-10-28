# -*- coding: utf-8 -*-

from python_usernames import validate_username, ValidationReason, ValidationResult


def test_valid_usernames():
    """Test that valid usernames return VALID reason."""
    valid_usernames = [
        "hello",
        "hello_world",
        "hello-world",
        "hello.world",
        "user123",
        "123user",
        "_hello",
        "he_llo",
        "he-llo",
        "he.llo",
        "a",
        "10101",
    ]

    for username in valid_usernames:
        result = validate_username(username)
        assert result.is_valid, (
            f"Expected '{username}' to be valid, got: {result.message}"
        )
        assert result.reason == ValidationReason.VALID
        assert result.suggested_fix is None


def test_too_long():
    """Test max_length validation."""
    result = validate_username("a" * 11, max_length=10)
    assert not result.is_valid
    assert result.reason == ValidationReason.TOO_LONG
    assert "10 characters or less" in result.message
    assert "11 characters" in result.message
    assert result.suggested_fix == "a" * 10


def test_empty_username():
    """Test empty username validation."""
    result = validate_username("")
    assert not result.is_valid
    assert result.reason == ValidationReason.EMPTY
    assert "empty" in result.message.lower()
    assert result.suggested_fix is None


def test_only_underscore():
    """Test username that is only an underscore."""
    result = validate_username("_")
    assert not result.is_valid
    assert result.reason == ValidationReason.ONLY_UNDERSCORE
    assert "only an underscore" in result.message.lower()
    assert result.suggested_fix is None


def test_starts_with_special():
    """Test usernames that start with dash or dot."""
    result = validate_username("-hello")
    assert not result.is_valid
    assert result.reason == ValidationReason.STARTS_WITH_SPECIAL
    assert "cannot start" in result.message.lower()
    assert result.suggested_fix == "hello"

    result = validate_username(".world")
    assert not result.is_valid
    assert result.reason == ValidationReason.STARTS_WITH_SPECIAL
    assert result.suggested_fix == "world"

    result = validate_username("--test")
    assert not result.is_valid
    assert result.reason == ValidationReason.STARTS_WITH_SPECIAL
    assert result.suggested_fix == "test"


def test_ends_with_special():
    """Test usernames that end with dash or dot."""
    result = validate_username("hello-")
    assert not result.is_valid
    assert result.reason == ValidationReason.ENDS_WITH_SPECIAL
    assert "cannot end" in result.message.lower()
    assert result.suggested_fix == "hello"

    result = validate_username("world.")
    assert not result.is_valid
    assert result.reason == ValidationReason.ENDS_WITH_SPECIAL
    assert result.suggested_fix == "world"


def test_consecutive_special():
    """Test usernames with consecutive special characters."""
    test_cases = [
        ("hello__world", "__"),
        ("hello..world", ".."),
        ("hello--world", "--"),
        ("hello_.world", "_."),
        ("hello._world", "._"),
        ("hello-.world", "-."),
        ("hello.-world", ".-"),
    ]

    for username, pattern in test_cases:
        result = validate_username(username)
        assert not result.is_valid, f"Expected '{username}' to be invalid"
        assert result.reason == ValidationReason.CONSECUTIVE_SPECIAL
        assert pattern in result.message
        assert "consecutive special characters" in result.message.lower()


def test_invalid_characters():
    """Test usernames with invalid characters."""
    result = validate_username("hello!")
    assert not result.is_valid
    assert result.reason == ValidationReason.INVALID_CHARACTERS
    assert "invalid characters" in result.message.lower()
    assert "!" in result.message
    assert result.suggested_fix == "hello"

    result = validate_username("user@name")
    assert not result.is_valid
    assert result.reason == ValidationReason.INVALID_CHARACTERS
    assert "@" in result.message
    assert result.suggested_fix == "username"

    result = validate_username("hello world")
    assert not result.is_valid
    assert result.reason == ValidationReason.INVALID_CHARACTERS
    assert result.suggested_fix == "helloworld"

    # Test with emojis
    result = validate_username("hello😍")
    assert not result.is_valid
    assert result.reason == ValidationReason.INVALID_CHARACTERS
    assert result.suggested_fix == "hello"

    # Test with multiple invalid characters
    result = validate_username("user!@#$%name")
    assert not result.is_valid
    assert result.reason == ValidationReason.INVALID_CHARACTERS
    assert result.suggested_fix == "username"


def test_reserved_words():
    """Test usernames that are reserved words."""
    # These are from the reserved words list
    reserved_usernames = ["admin", "fuck", "sex", "root"]

    for username in reserved_usernames:
        result = validate_username(username)
        assert not result.is_valid, f"Expected '{username}' to be invalid (reserved)"
        assert result.reason == ValidationReason.RESERVED_WORD
        assert (
            "reserved" in result.message.lower()
            or "blocklist" in result.message.lower()
        )
        assert username.lower() in result.message.lower()


def test_whitelist():
    """Test that whitelisted words are valid even if reserved."""
    result = validate_username("fuck", whitelist=["fuck"])
    assert result.is_valid
    assert result.reason == ValidationReason.VALID

    # Test case insensitivity
    result = validate_username("fuck", whitelist=["FUCK"])
    assert result.is_valid

    # But invalid format should still fail even if whitelisted
    result = validate_username("fu..ck", whitelist=["fu..ck"])
    assert not result.is_valid
    assert result.reason == ValidationReason.CONSECUTIVE_SPECIAL


def test_blacklist():
    """Test that blacklisted words are invalid."""
    result = validate_username("myword", blacklist=["myword"])
    assert not result.is_valid
    assert result.reason == ValidationReason.RESERVED_WORD

    # Test case insensitivity
    result = validate_username("myword", blacklist=["MYWORD"])
    assert not result.is_valid
    assert result.reason == ValidationReason.RESERVED_WORD


def test_validation_order():
    """Test that validations happen in the correct order."""
    # Max length should be checked first
    result = validate_username("a" * 100, max_length=10)
    assert result.reason == ValidationReason.TOO_LONG

    # Empty checked before format issues
    result = validate_username("")
    assert result.reason == ValidationReason.EMPTY

    # Only underscore checked before other format issues
    result = validate_username("_")
    assert result.reason == ValidationReason.ONLY_UNDERSCORE

    # Start with special checked before consecutive
    result = validate_username("-__hello")
    assert result.reason == ValidationReason.STARTS_WITH_SPECIAL

    # End with special checked after start
    result = validate_username("hello__-")
    assert result.reason == ValidationReason.ENDS_WITH_SPECIAL

    # Consecutive checked before invalid chars
    result = validate_username("hello__world!")
    assert result.reason == ValidationReason.CONSECUTIVE_SPECIAL

    # Invalid chars checked before reserved words
    result = validate_username("admin!")
    assert result.reason == ValidationReason.INVALID_CHARACTERS


def test_custom_regex():
    """Test validation with custom regex."""
    # Custom regex that only allows lowercase letters
    import re

    custom_regex = re.compile(r"^[a-z]+$")

    result = validate_username("hello", regex=custom_regex)
    assert result.is_valid

    # This would normally be valid, but not with custom regex
    result = validate_username("Hello123", regex=custom_regex)
    assert not result.is_valid


def test_custom_regex_skips_builtin_checks():
    """Test that custom regex skips built-in format checks."""
    import re

    # Custom regex that allows things normally forbidden
    custom_regex = re.compile(r"^.+$")  # Allows anything non-empty

    # These would normally fail built-in checks but should pass with custom regex
    test_cases = [
        "--hello",  # starts with special
        "hello--",  # ends with special
        "hello__world",  # consecutive special
        "hello..world",  # consecutive special
        "_",  # only underscore
        "user@name",  # invalid character
        "hello world",  # space
    ]

    for username in test_cases:
        result = validate_username(username, regex=custom_regex)
        assert result.is_valid, f"Expected '{username}' to be valid with custom regex"
        assert result.reason == ValidationReason.VALID


def test_custom_regex_still_checks_max_length():
    """Test that custom regex still respects max_length."""
    import re

    custom_regex = re.compile(r"^.+$")

    result = validate_username("verylongusername", regex=custom_regex, max_length=10)
    assert not result.is_valid
    assert result.reason == ValidationReason.TOO_LONG


def test_custom_regex_still_checks_reserved_words():
    """Test that custom regex still checks reserved words."""
    import re

    custom_regex = re.compile(r"^[a-z]+$")

    # "admin" matches the regex but is reserved
    result = validate_username("admin", regex=custom_regex)
    assert not result.is_valid
    assert result.reason == ValidationReason.RESERVED_WORD


def test_custom_regex_with_whitelist():
    """Test that custom regex works with whitelist."""
    import re

    custom_regex = re.compile(r"^[a-z]+$")

    # "admin" is reserved but whitelisted
    result = validate_username("admin", regex=custom_regex, whitelist=["admin"])
    assert result.is_valid
    assert result.reason == ValidationReason.VALID


def test_result_dataclass():
    """Test that ValidationResult is a proper dataclass."""
    result = ValidationResult(
        is_valid=False,
        reason=ValidationReason.TOO_LONG,
        message="Test message",
        suggested_fix="fix",
    )

    assert result.is_valid is False
    assert result.reason == ValidationReason.TOO_LONG
    assert result.message == "Test message"
    assert result.suggested_fix == "fix"

    # Test without suggested_fix (should default to None)
    result = ValidationResult(
        is_valid=True, reason=ValidationReason.VALID, message="Valid"
    )
    assert result.suggested_fix is None


def test_validation_reason_enum():
    """Test ValidationReason enum values."""
    assert ValidationReason.VALID.value == "valid"
    assert ValidationReason.TOO_LONG.value == "too_long"
    assert ValidationReason.EMPTY.value == "empty"
    assert ValidationReason.INVALID_CHARACTERS.value == "invalid_characters"
    assert ValidationReason.RESERVED_WORD.value == "reserved_word"


def test_suggested_fixes():
    """Test that suggested fixes are appropriate."""
    # Too long
    result = validate_username("verylongusername", max_length=10)
    assert result.suggested_fix == "verylongus"

    # Starts with special
    result = validate_username("--user")
    assert result.suggested_fix == "user"

    # Ends with special
    result = validate_username("user..")
    assert result.suggested_fix == "user"

    # Invalid characters
    result = validate_username("user@#$name")
    assert result.suggested_fix == "username"

    # No fix for consecutive special
    result = validate_username("user__name")
    assert result.suggested_fix is None

    # No fix for reserved words
    result = validate_username("admin")
    assert result.suggested_fix is None

    # No fix for valid usernames
    result = validate_username("validuser")
    assert result.suggested_fix is None
