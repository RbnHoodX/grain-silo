"""Tests for search utilities."""

from silo import Silo
from utils.search import (
    find_pours_by_note,
    find_bins_by_kind,
    find_empty_bins,
    find_largest_pour,
    count_pours_per_bin,
)


class TestFindPoursByNote:
    def test_no_matches(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 10, "x")
        assert find_pours_by_note(silo, "y") == []

    def test_matching_note(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 10, "fill")
        result = find_pours_by_note(silo, "fill")
        assert len(result) == 1


class TestFindBinsByKind:
    def test_find_standard(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B", "overflow")
        result = find_bins_by_kind(silo, "standard")
        assert len(result) == 1

    def test_find_overflow(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B", "overflow")
        result = find_bins_by_kind(silo, "overflow")
        assert len(result) == 1


class TestFindEmptyBins:
    def test_all_empty(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        assert len(find_empty_bins(silo)) == 2

    def test_some_filled(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        empty = find_empty_bins(silo)
        assert len(empty) == 0


class TestFindLargestPour:
    def test_no_pours(self):
        silo = Silo()
        assert find_largest_pour(silo) is None

    def test_multiple_pours(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 50)
        silo.transfer("B", "A", 200)
        largest = find_largest_pour(silo)
        assert largest.amount == 200


class TestCountPoursPerBin:
    def test_counts(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        counts = count_pours_per_bin(silo)
        assert counts["A"] == 1
        assert counts["B"] == 1
