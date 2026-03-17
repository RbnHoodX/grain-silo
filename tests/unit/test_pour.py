"""Tests for Pour and PourLog classes."""

import pytest
from bin import Bin
from pour import Pour, PourLog


class TestPour:
    def test_pour_creation(self):
        a = Bin("A")
        b = Bin("B")
        pour = Pour(a, b, 100)
        assert pour.dest_bin is a
        assert pour.source_bin is b
        assert pour.amount == 100
        assert pour.note == ""

    def test_pour_with_note(self):
        a = Bin("A")
        b = Bin("B")
        pour = Pour(a, b, 50, "test note")
        assert pour.note == "test note"

    def test_pour_initial_id(self):
        a = Bin("A")
        b = Bin("B")
        pour = Pour(a, b, 100)
        assert pour.id == 0

    def test_pour_id_setter(self):
        a = Bin("A")
        b = Bin("B")
        pour = Pour(a, b, 100)
        pour.id = 5
        assert pour.id == 5


class TestPourLog:
    def test_log_empty(self):
        log = PourLog()
        assert log.pours() == []

    def test_log_record(self):
        log = PourLog()
        a = Bin("A")
        b = Bin("B")
        pour = Pour(a, b, 100)
        log.record(pour)
        assert len(log.pours()) == 1
        assert pour.id == 1

    def test_log_sequential_ids(self):
        log = PourLog()
        a = Bin("A")
        b = Bin("B")
        p1 = Pour(a, b, 100)
        p2 = Pour(b, a, 50)
        log.record(p1)
        log.record(p2)
        assert p1.id == 1
        assert p2.id == 2

    def test_log_updates_bins(self):
        log = PourLog()
        a = Bin("A")
        b = Bin("B")
        pour = Pour(a, b, 100)
        log.record(pour)
        assert len(a.pours()) == 1
        assert len(b.pours()) == 1
