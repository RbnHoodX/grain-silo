"""Export utilities for silo data."""


class SiloExporter:
    """Exports silo data in various formats."""

    def __init__(self, silo):
        self._silo = silo

    def to_csv(self):
        """Export pour log as CSV."""
        lines = ["id,dest,source,amount,note"]
        for pour in self._silo.log_entries():
            lines.append(
                f"{pour.id},{pour.dest_bin.name},{pour.source_bin.name},"
                f"{pour.amount},{pour.note}"
            )
        return "\n".join(lines)

    def to_text(self):
        """Export pour log as formatted text."""
        lines = ["Pour Log"]
        lines.append("-" * 40)
        for pour in self._silo.log_entries():
            lines.append(
                f"#{pour.id}: {pour.source_bin.name} -> {pour.dest_bin.name} "
                f"amount={pour.amount} note={pour.note!r}"
            )
        return "\n".join(lines)

    def bin_summary(self):
        """Export bin summary as formatted text."""
        lines = ["Bin Summary"]
        lines.append("-" * 40)
        for b in self._silo.bins():
            lines.append(f"  {b.name}: level={b.level} kind={b.kind}")
        return "\n".join(lines)
