"""Loader utilities for silo data."""

import json
from silo import Silo


class SiloLoader:
    """Loads silo state from serialized data."""

    @staticmethod
    def from_dict(data):
        """Restore a silo from a dictionary."""
        silo = Silo()
        for bin_data in data.get("bins", []):
            silo.create_bin(bin_data["name"], bin_data.get("kind", "standard"))

        for pour_data in data.get("pours", []):
            silo.transfer(
                pour_data["dest"],
                pour_data["source"],
                pour_data["amount"],
                pour_data.get("note", ""),
            )
        return silo

    @staticmethod
    def from_json(json_str):
        """Restore a silo from a JSON string."""
        data = json.loads(json_str)
        return SiloLoader.from_dict(data)
