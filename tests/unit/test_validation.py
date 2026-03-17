"""Tests for validation utilities."""

import pytest
from utils.validation import validate_bin_name, validate_amount, validate_bin_kind


class TestValidateBinName:
    def test_valid_name(self):
        assert validate_bin_name("WHEAT-1") is True

    def test_empty_name(self):
        assert validate_bin_name("") is False

    def test_lowercase_start(self):
        assert validate_bin_name("wheat") is False

    def test_non_string(self):
        assert validate_bin_name(123) is False

    def test_too_long(self):
        assert validate_bin_name("A" * 51) is False

    def test_max_length(self):
        assert validate_bin_name("A" * 50) is True


class TestValidateAmount:
    def test_positive_int(self):
        assert validate_amount(100) is True

    def test_positive_float(self):
        assert validate_amount(3.5) is True

    def test_zero(self):
        assert validate_amount(0) is False

    def test_negative(self):
        assert validate_amount(-10) is False

    def test_non_numeric(self):
        assert validate_amount("abc") is False


class TestValidateBinKind:
    def test_standard(self):
        assert validate_bin_kind("standard") is True

    def test_overflow(self):
        assert validate_bin_kind("overflow") is True

    def test_invalid(self):
        assert validate_bin_kind("unknown") is False
