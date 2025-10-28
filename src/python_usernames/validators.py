import re
from dataclasses import dataclass
from enum import Enum

from .reserved_words import get_reserved_words


class ValidationReason(Enum):
    """Enum representing different validation failure reasons."""

    VALID = "valid"
    TOO_LONG = "too_long"
    EMPTY = "empty"
    ONLY_UNDERSCORE = "only_underscore"
    STARTS_WITH_SPECIAL = "starts_with_special"
    ENDS_WITH_SPECIAL = "ends_with_special"
    CONSECUTIVE_SPECIAL = "consecutive_special"
    INVALID_CHARACTERS = "invalid_characters"
    RESERVED_WORD = "reserved_word"


@dataclass
class ValidationResult:
    """Result of username validation with detailed information."""

    is_valid: bool
    reason: ValidationReason
    message: str
    suggested_fix: str | None = None


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


def validate_username(
    username: str, whitelist=None, blacklist=None, regex=username_regex, max_length=None
) -> ValidationResult:
    """
    Validate a username and return detailed validation result.

    Args:
        username: The username to validate
        whitelist: List of words that should be considered safe (case insensitive)
        blacklist: List of words that should be considered unsafe (case insensitive)
        regex: Regular expression pattern for validation. If a custom regex is provided,
               only that regex will be used (skipping detailed format checks)
        max_length: Maximum allowed length for username

    Returns:
        ValidationResult with is_valid, reason, message, and optional suggested_fix

    Note:
        When a custom regex is provided, only max_length, regex, and reserved word
        checks are performed. Built-in format checks are skipped.
    """
    # Determine if custom regex is provided
    is_custom_regex = regex is not username_regex

    # check for max length
    if max_length and len(username) > max_length:
        return ValidationResult(
            is_valid=False,
            reason=ValidationReason.TOO_LONG,
            message=f"Username must be {max_length} characters or less (currently {len(username)} characters)",
            suggested_fix=username[:max_length] if username[:max_length] else None,
        )

    # If custom regex provided, skip detailed checks and only use regex + reserved words
    if is_custom_regex:
        # Check against custom regex
        if not re.match(regex, username):
            return ValidationResult(
                is_valid=False,
                reason=ValidationReason.INVALID_CHARACTERS,
                message="Username does not match the required format",
                suggested_fix=None,
            )
    else:
        # Use detailed built-in validation checks
        # check for empty username
        if not username:
            return ValidationResult(
                is_valid=False,
                reason=ValidationReason.EMPTY,
                message="Username cannot be empty",
                suggested_fix=None,
            )

        # check for only underscore
        if username == "_":
            return ValidationResult(
                is_valid=False,
                reason=ValidationReason.ONLY_UNDERSCORE,
                message="Username cannot be only an underscore",
                suggested_fix=None,
            )

        # check if starts with special character
        if username[0] in "-.":
            return ValidationResult(
                is_valid=False,
                reason=ValidationReason.STARTS_WITH_SPECIAL,
                message="Username cannot start with a dash (-) or dot (.)",
                suggested_fix=username.lstrip("-."),
            )

        # check if ends with special character
        if username[-1] in "-.":
            return ValidationResult(
                is_valid=False,
                reason=ValidationReason.ENDS_WITH_SPECIAL,
                message="Username cannot end with a dash (-) or dot (.)",
                suggested_fix=username.rstrip("-."),
            )

        # check for consecutive special characters
        consecutive_patterns = ["__", "..", "--", "_.", "._", "-.", ".-"]
        found_pattern = next((p for p in consecutive_patterns if p in username), None)
        if found_pattern:
            return ValidationResult(
                is_valid=False,
                reason=ValidationReason.CONSECUTIVE_SPECIAL,
                message=f"Username cannot contain consecutive special characters like '{found_pattern}'",
                suggested_fix=None,
            )

        # check for invalid characters
        valid_chars = set(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-"
        )
        invalid_chars = [c for c in username if c not in valid_chars]
        if invalid_chars:
            unique_invalid = list(
                dict.fromkeys(invalid_chars)
            )  # preserve order, remove duplicates
            invalid_display = ", ".join(
                f"'{c}'" for c in unique_invalid[:5]
            )  # show first 5
            if len(unique_invalid) > 5:
                invalid_display += ", ..."
            return ValidationResult(
                is_valid=False,
                reason=ValidationReason.INVALID_CHARACTERS,
                message=f"Username contains invalid characters: {invalid_display}. Only alphanumeric characters, underscore (_), dash (-), and dot (.) are allowed",
                suggested_fix="".join(c for c in username if c in valid_chars) or None,
            )

        # final regex check (should pass if all above checks passed)
        if not re.match(regex, username):
            return ValidationResult(
                is_valid=False,
                reason=ValidationReason.INVALID_CHARACTERS,
                message="Username format is invalid",
                suggested_fix=None,
            )

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

    if username.lower() in default_words:
        return ValidationResult(
            is_valid=False,
            reason=ValidationReason.RESERVED_WORD,
            message=f"Username '{username}' is not allowed (reserved word or in blocklist)",
            suggested_fix=None,
        )

    return ValidationResult(
        is_valid=True,
        reason=ValidationReason.VALID,
        message="Username is valid",
        suggested_fix=None,
    )


def is_safe_username(
    username: str, whitelist=None, blacklist=None, regex=username_regex, max_length=None
) -> bool:
    """
    Check if a username is safe/valid (backward compatible function).

    Args:
        username: The username to validate
        whitelist: List of words that should be considered safe (case insensitive)
        blacklist: List of words that should be considered unsafe (case insensitive)
        regex: Regular expression pattern for validation
        max_length: Maximum allowed length for username

    Returns:
        bool: True if username is valid, False otherwise

    Note:
        For detailed validation information, use validate_username() instead.
    """
    result = validate_username(username, whitelist, blacklist, regex, max_length)
    return result.is_valid
