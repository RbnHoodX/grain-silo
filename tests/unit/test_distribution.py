"""Tests for distribution analysis."""

from silo import Silo
from analysis.distribution import DistributionReport


class TestDistributionReport:
    def test_by_bin_kind_empty(self):
        silo = Silo()
        report = DistributionReport(silo)
        assert report.by_bin_kind() == {}

    def test_by_bin_kind(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B", "overflow")
        silo.create_bin("C")
        silo.transfer("A", "B", 100)
        report = DistributionReport(silo)
        kinds = report.by_bin_kind()
        assert "standard" in kinds
        assert "overflow" in kinds

    def test_top_loaded(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.create_bin("C")
        silo.transfer("A", "B", 200)
        silo.transfer("C", "B", 50)
        report = DistributionReport(silo)
        top = report.top_loaded(2)
        assert len(top) == 2
        assert top[0].name == "A"

    def test_empty_bins(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        report = DistributionReport(silo)
        assert len(report.empty_bins()) == 2

    def test_summary_empty(self):
        silo = Silo()
        report = DistributionReport(silo)
        s = report.summary()
        assert s["count"] == 0

    def test_summary_with_data(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        report = DistributionReport(silo)
        s = report.summary()
        assert s["count"] == 2
