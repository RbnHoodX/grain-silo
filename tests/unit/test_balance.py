"""Tests for balance analysis."""

from silo import Silo
from analysis.balance import BalanceAnalyzer


class TestBalanceAnalyzer:
    def test_total_level_empty(self):
        silo = Silo()
        analyzer = BalanceAnalyzer(silo)
        assert analyzer.total_level() == 0

    def test_total_level(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        analyzer = BalanceAnalyzer(silo)
        assert analyzer.total_level() == 0

    def test_average_level_empty(self):
        silo = Silo()
        analyzer = BalanceAnalyzer(silo)
        assert analyzer.average_level() == 0

    def test_average_level(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        analyzer = BalanceAnalyzer(silo)
        assert analyzer.average_level() == 0

    def test_is_balanced_empty(self):
        silo = Silo()
        analyzer = BalanceAnalyzer(silo)
        assert analyzer.is_balanced() is True

    def test_heaviest_bin(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        analyzer = BalanceAnalyzer(silo)
        assert analyzer.heaviest_bin().name == "A"

    def test_lightest_bin(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        analyzer = BalanceAnalyzer(silo)
        assert analyzer.lightest_bin().name == "B"

    def test_imbalance_report(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        analyzer = BalanceAnalyzer(silo)
        report = analyzer.imbalance_report()
        assert len(report) == 2
