"""Validation utilities for grain silo operations."""

from config import BIN_KINDS, MAX_BIN_NAME_LENGTH


def validate_bin_name(name):
    """Validate a bin name. Returns True if valid."""
    if not isinstance(name, str):
        return False
    if not name or len(name) > MAX_BIN_NAME_LENGTH:
        return False
    if not name[0].isupper():
        return False
    return True


def validate_amount(amount):
    """Validate a pour amount. Returns True if valid."""
    if not isinstance(amount, (int, float)):
        return False
    return amount > 0


def validate_bin_kind(kind):
    """Validate a bin kind. Returns True if valid."""
    return kind in BIN_KINDS
