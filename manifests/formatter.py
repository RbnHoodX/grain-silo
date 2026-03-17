"""Manifest formatting utilities."""


class ManifestFormatter:
    """Formats grain manifests for display."""

    def __init__(self, manifest):
        self._manifest = manifest

    def to_text(self):
        """Format manifest as plain text."""
        lines = [
            f"Grain Manifest ({self._manifest['entry_count']} entries)",
            "=" * 50,
        ]
        for entry in self._manifest.get("entries", []):
            lines.append(
                f"  #{entry['id']}: {entry['source']} -> {entry['dest']} "
                f"amount={entry['amount']}"
            )
        return "\n".join(lines)

    def to_csv(self):
        """Format manifest as CSV."""
        lines = ["id,source,dest,amount,note"]
        for entry in self._manifest.get("entries", []):
            lines.append(
                f"{entry['id']},{entry['source']},{entry['dest']},"
                f"{entry['amount']},{entry['note']}"
            )
        return "\n".join(lines)

    def summary(self):
        """Generate a brief summary string."""
        return (
            f"Manifest: {self._manifest.get('entry_count', 0)} entries, "
            f"{self._manifest.get('bin_count', '?')} bins"
        )
