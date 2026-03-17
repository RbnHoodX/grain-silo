"""Integration tests for silo workflows."""

from silo import Silo


class TestSiloWorkflow:
    def test_full_workflow(self):
        silo = Silo()
        a = silo.create_bin("WHEAT-1")
        b = silo.create_bin("WHEAT-2")
        c = silo.create_bin("OVERFLOW", kind="overflow")

        silo.transfer("WHEAT-1", "WHEAT-2", 500)
        silo.transfer("WHEAT-1", "OVERFLOW", 200)

        assert a.level == 700
        assert b.level == -500
        assert c.level == -200
        assert len(silo.log_entries()) == 2

    def test_back_and_forth(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")

        silo.transfer("A", "B", 100)
        silo.transfer("B", "A", 40)

        assert silo.get_bin("A").level == 60
        assert silo.get_bin("B").level == -60

    def test_multiple_bins(self):
        silo = Silo()
        for name in ["BIN-1", "BIN-2", "BIN-3", "BIN-4"]:
            silo.create_bin(name)

        silo.transfer("BIN-1", "BIN-2", 100)
        silo.transfer("BIN-3", "BIN-4", 200)
        silo.transfer("BIN-1", "BIN-3", 50)

        assert len(silo.log_entries()) == 3
        assert silo.get_bin("BIN-1").level == 150

    def test_volume_summary_tracks_all(self):
        silo = Silo()
        silo.create_bin("X")
        silo.create_bin("Y")
        silo.transfer("X", "Y", 100)
        silo.transfer("Y", "X", 30)
        total_in, total_out = silo.volume_summary()
        assert total_in == 130
        assert total_out == 130
