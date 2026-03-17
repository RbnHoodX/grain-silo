"""Tests for formatting utilities."""

from utils.formatting import format_amount, format_header, truncate


class TestFormatAmount:
    def test_int_amount(self):
        assert format_amount(100) == "100 bu"

    def test_float_amount(self):
        assert format_amount(3.14) == "3.14 bu"

    def test_custom_unit(self):
        assert format_amount(50, "kg") == "50 kg"


class TestFormatHeader:
    def test_default_width(self):
        header = format_header("Test")
        lines = header.split("\n")
        assert len(lines) == 3
        assert lines[0] == "=" * 50

    def test_custom_width(self):
        header = format_header("X", width=20)
        lines = header.split("\n")
        assert len(lines[0]) == 20


class TestTruncate:
    def test_short_text(self):
        assert truncate("hello") == "hello"

    def test_exact_length(self):
        text = "a" * 40
        assert truncate(text) == text

    def test_long_text(self):
        text = "a" * 50
        result = truncate(text)
        assert len(result) == 40
        assert result.endswith("...")

    def test_custom_max(self):
        result = truncate("abcdefgh", max_length=5)
        assert len(result) == 5
        assert result.endswith("...")
