"""Tests for limit checking."""

from silo import Silo
from analysis.limits import LimitChecker


class TestLimitChecker:
    def test_no_low_level_bins(self):
        silo = Silo()
        silo.create_bin("A")
        checker = LimitChecker(silo)
        assert checker.low_level_bins() == []

    def test_low_level_bin(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 50)
        checker = LimitChecker(silo)
        low = checker.low_level_bins()
        assert len(low) == 1
        assert low[0].name == "A"

    def test_no_high_level_bins(self):
        silo = Silo()
        silo.create_bin("A")
        checker = LimitChecker(silo)
        assert checker.high_level_bins() == []

    def test_critical_bins(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 30)
        checker = LimitChecker(silo)
        critical = checker.critical_bins()
        assert len(critical) == 1
        assert critical[0].name == "A"

    def test_check_all(self):
        silo = Silo()
        silo.create_bin("A")
        checker = LimitChecker(silo)
        result = checker.check_all()
        assert "low" in result
        assert "high" in result
        assert "critical" in result
