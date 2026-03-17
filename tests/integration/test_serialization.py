"""Integration tests for serialization and loading."""

from silo import Silo
from storage.serializer import SiloSerializer
from storage.exporter import SiloExporter
from storage.loader import SiloLoader


class TestSerializationWorkflow:
    def test_serialize_to_dict(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100, "test")
        serializer = SiloSerializer(silo)
        data = serializer.to_dict()
        assert len(data["bins"]) == 2
        assert len(data["pours"]) == 1

    def test_serialize_to_json(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 50)
        serializer = SiloSerializer(silo)
        json_str = serializer.to_json()
        assert "A" in json_str

    def test_snapshot(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        serializer = SiloSerializer(silo)
        snap = serializer.snapshot()
        assert snap["A"] == 100
        assert snap["B"] == -100

    def test_roundtrip(self):
        silo = Silo()
        silo.create_bin("X")
        silo.create_bin("Y")
        silo.transfer("X", "Y", 200, "init")
        serializer = SiloSerializer(silo)
        data = serializer.to_dict()
        restored = SiloLoader.from_dict(data)
        assert restored.get_bin("X").level == 200
        assert restored.get_bin("Y").level == -200

    def test_roundtrip_json(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 75)
        serializer = SiloSerializer(silo)
        json_str = serializer.to_json()
        restored = SiloLoader.from_json(json_str)
        assert restored.get_bin("A").level == 75

    def test_export_csv(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        exporter = SiloExporter(silo)
        csv = exporter.to_csv()
        assert "id,dest,source,amount,note" in csv

    def test_export_text(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        exporter = SiloExporter(silo)
        text = exporter.to_text()
        assert "Pour Log" in text

    def test_bin_summary(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        exporter = SiloExporter(silo)
        summary = exporter.bin_summary()
        assert "Bin Summary" in summary
