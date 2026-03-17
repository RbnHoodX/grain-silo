"""Tests for aggregation utilities."""

from silo import Silo
from utils.aggregation import sum_amounts, group_by_note, average_amount


class TestSumAmounts:
    def test_empty(self):
        assert sum_amounts([]) == 0

    def test_single_pour(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        pours = silo.log_entries()
        assert sum_amounts(pours) == 100

    def test_multiple_pours(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        silo.transfer("B", "A", 50)
        silo.transfer("A", "B", 25)
        pours = silo.log_entries()
        assert sum_amounts(pours) == 175


class TestGroupByNote:
    def test_empty(self):
        assert group_by_note([]) == {}

    def test_single_group(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100, "fill")
        silo.transfer("B", "A", 50, "fill")
        groups = group_by_note(silo.log_entries())
        assert "fill" in groups
        assert len(groups["fill"]) == 2

    def test_multiple_groups(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100, "fill")
        silo.transfer("B", "A", 50, "drain")
        groups = group_by_note(silo.log_entries())
        assert len(groups) == 2
        assert len(groups["fill"]) == 1
        assert len(groups["drain"]) == 1


class TestAverageAmount:
    def test_empty(self):
        assert average_amount([]) == 0

    def test_single(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        assert average_amount(silo.log_entries()) == 100

    def test_multiple(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        silo.transfer("B", "A", 200)
        assert average_amount(silo.log_entries()) == 150
