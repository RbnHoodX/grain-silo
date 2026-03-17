"""Serialization utilities for silo state."""

import json


class SiloSerializer:
    """Serializes and deserializes silo state."""

    def __init__(self, silo):
        self._silo = silo

    def to_dict(self):
        """Serialize silo state to a dictionary."""
        bins_data = []
        for b in self._silo.bins():
            bins_data.append({
                "name": b.name,
                "kind": b.kind,
                "level": b.level,
            })

        pours_data = []
        for pour in self._silo.log_entries():
            pours_data.append({
                "id": pour.id,
                "dest": pour.dest_bin.name,
                "source": pour.source_bin.name,
                "amount": pour.amount,
                "note": pour.note,
            })

        return {
            "bins": bins_data,
            "pours": pours_data,
        }

    def to_json(self):
        """Serialize silo state to JSON string."""
        return json.dumps(self.to_dict(), indent=2)

    def snapshot(self):
        """Create a lightweight snapshot of current bin levels."""
        return {b.name: b.level for b in self._silo.bins()}
