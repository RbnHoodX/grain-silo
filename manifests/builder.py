"""Manifest builder for grain shipments."""

import json


class ManifestBuilder:
    """Builds grain shipment manifests from pour logs."""

    def __init__(self, silo):
        self._silo = silo

    def build(self):
        """Build a manifest dict from the current pour log."""
        entries = []
        for pour in self._silo.log_entries():
            entries.append({
                "id": pour.id,
                "dest": pour.dest_bin.name,
                "source": pour.source_bin.name,
                "amount": pour.amount,
                "note": pour.note,
            })
        return {
            "bin_count": len(self._silo.bins()),
            "entry_count": len(entries),
            "entries": entries,
        }

    def build_for_bin(self, bin_name):
        """Build a manifest for a specific bin."""
        b = self._silo.get_bin(bin_name)
        entries = []
        for pour in b.pours():
            entries.append({
                "id": pour.id,
                "dest": pour.dest_bin.name,
                "source": pour.source_bin.name,
                "amount": pour.amount,
                "note": pour.note,
            })
        return {
            "bin_name": bin_name,
            "level": b.level,
            "entry_count": len(entries),
            "entries": entries,
        }

    def to_json(self):
        """Build and serialize manifest to JSON string."""
        return json.dumps(self.build(), indent=2)
