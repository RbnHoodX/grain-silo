"""Tests for the Bin class."""

import pytest
from bin import Bin


class TestBinCreation:
    def test_create_bin_with_name(self):
        b = Bin("WHEAT-1")
        assert b.name == "WHEAT-1"

    def test_create_bin_default_kind(self):
        b = Bin("WHEAT-1")
        assert b.kind == "standard"

    def test_create_bin_custom_kind(self):
        b = Bin("INTAKE", kind="overflow")
        assert b.kind == "overflow"

    def test_bin_initial_level_zero(self):
        b = Bin("CORN-1")
        assert b.level == 0

    def test_bin_initial_pours_empty(self):
        b = Bin("CORN-1")
        assert b.pours() == []


class TestBinRepr:
    def test_repr_standard(self):
        b = Bin("WHEAT-1")
        assert repr(b) == "Bin(name='WHEAT-1', kind='standard')"

    def test_repr_overflow(self):
        b = Bin("INTAKE", "overflow")
        assert repr(b) == "Bin(name='INTAKE', kind='overflow')"
