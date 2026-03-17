"""Integration tests for manifest building and formatting."""

import json
from silo import Silo
from manifests.builder import ManifestBuilder
from manifests.formatter import ManifestFormatter
from manifests.validator import ManifestValidator


class TestManifestWorkflow:
    def test_build_manifest(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100, "initial")
        builder = ManifestBuilder(silo)
        manifest = builder.build()
        assert manifest["entry_count"] == 1
        assert manifest["bin_count"] == 2

    def test_manifest_to_json(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 50)
        builder = ManifestBuilder(silo)
        json_str = builder.to_json()
        data = json.loads(json_str)
        assert data["entry_count"] == 1

    def test_build_for_bin(self):
        silo = Silo()
        silo.create_bin("X")
        silo.create_bin("Y")
        silo.transfer("X", "Y", 75, "test")
        builder = ManifestBuilder(silo)
        manifest = builder.build_for_bin("X")
        assert manifest["bin_name"] == "X"
        assert manifest["level"] == 75

    def test_format_text(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        builder = ManifestBuilder(silo)
        manifest = builder.build()
        formatter = ManifestFormatter(manifest)
        text = formatter.to_text()
        assert "1 entries" in text

    def test_format_csv(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        builder = ManifestBuilder(silo)
        manifest = builder.build()
        formatter = ManifestFormatter(manifest)
        csv = formatter.to_csv()
        assert "id,source,dest,amount,note" in csv

    def test_validate_manifest(self):
        silo = Silo()
        silo.create_bin("A")
        silo.create_bin("B")
        silo.transfer("A", "B", 100)
        builder = ManifestBuilder(silo)
        manifest = builder.build()
        validator = ManifestValidator(manifest)
        assert validator.is_valid() is True

    def test_validate_bad_manifest(self):
        validator = ManifestValidator({})
        assert validator.is_valid() is False
