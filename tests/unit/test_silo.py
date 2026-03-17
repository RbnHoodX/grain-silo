"""Tests for the Silo class."""

import pytest
from silo import Silo


class TestSiloCreation:
    def test_silo_starts_empty(self):
        silo = Silo()
        assert silo.bins() == []

    def test_silo_log_starts_empty(self):
        silo = Silo()
        assert silo.log_entries() == []


class TestSiloCreateBin:
    def test_create_bin(self):
        silo = Silo()
        b = silo.create_bin("WHEAT-1")
        assert b.name == "WHEAT-1"

    def test_create_bin_default_kind(self):
        silo = Silo()
        b = silo.create_bin("CORN-1")
        assert b.kind == "standard"

    def test_create_bin_custom_kind(self):
        silo = Silo()
        b = silo.create_bin("INTAKE", kind="overflow")
        assert b.kind == "overflow"

    def test_create_duplicate_raises(self):
        silo = Silo()
        silo.create_bin("A")
        with pytest.raises(ValueError):
            silo.create_bin("A")

    def test_get_bin(self):
        silo = Silo()
        silo.create_bin("X")
        b = silo.get_bin("X")
        assert b.name == "X"

    def test_get_missing_bin_raises(self):
        silo = Silo()
        with pytest.raises(KeyError):
            silo.get_bin("MISSING")

    def test_bins_list(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        assert len(silo.bins()) == 2


class TestSiloTransfer:
    def test_transfer_basic(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        pour = silo.transfer("A", "B", 100)
        assert pour.amount == 100

    def test_transfer_updates_levels(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        assert silo.get_bin("A").level == 100
        assert silo.get_bin("B").level == -100

    def test_transfer_with_note(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        pour = silo.transfer("A", "B", 50, "test")
        assert pour.note == "test"

    def test_transfer_zero_raises(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        with pytest.raises(ValueError):
            silo.transfer("A", "B", 0)

    def test_transfer_negative_raises(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        with pytest.raises(ValueError):
            silo.transfer("A", "B", -10)

    def test_log_entries_after_transfer(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        assert len(silo.log_entries()) == 1


class TestVolumeSummary:
    def test_empty_summary(self):
        silo = Silo()
        assert silo.volume_summary() == (0, 0)

    def test_summary_after_transfers(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        silo.transfer("B", "A", 50)
        total_in, total_out = silo.volume_summary()
        assert total_in == 150
        assert total_out == 150
