"""Manifest validation utilities."""


class ManifestValidator:
    """Validates grain manifest data."""

    def __init__(self, manifest):
        self._manifest = manifest

    def validate(self):
        """Run all validations and return a list of errors."""
        errors = []
        errors.extend(self._check_structure())
        errors.extend(self._check_entries())
        return errors

    def is_valid(self):
        """Return True if manifest passes all validations."""
        return len(self.validate()) == 0

    def _check_structure(self):
        """Check manifest has required top-level keys."""
        errors = []
        required = ["entry_count", "entries"]
        for key in required:
            if key not in self._manifest:
                errors.append(f"missing required key: {key}")
        return errors

    def _check_entries(self):
        """Check each entry has required fields."""
        errors = []
        entries = self._manifest.get("entries", [])
        required_fields = ["id", "dest", "source", "amount"]
        for i, entry in enumerate(entries):
            for field in required_fields:
                if field not in entry:
                    errors.append(f"entry {i}: missing field {field}")
            if "amount" in entry and entry["amount"] <= 0:
                errors.append(f"entry {i}: amount must be positive")
        return errors
