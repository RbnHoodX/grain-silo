"""Balance analysis for grain distribution across bins."""


class BalanceAnalyzer:
    """Analyzes grain distribution balance across bins."""

    def __init__(self, silo):
        self._silo = silo

    def total_level(self):
        """Calculate total grain level across all bins."""
        return sum(b.level for b in self._silo.bins())

    def average_level(self):
        """Calculate average grain level per bin."""
        bins = self._silo.bins()
        if not bins:
            return 0
        return self.total_level() / len(bins)

    def is_balanced(self, tolerance=0.1):
        """Check if all bins are within tolerance of average level."""
        avg = self.average_level()
        if avg == 0:
            return True
        for b in self._silo.bins():
            if abs(b.level - avg) / avg > tolerance:
                return False
        return True

    def heaviest_bin(self):
        """Find the bin with the highest level."""
        bins = self._silo.bins()
        if not bins:
            return None
        return max(bins, key=lambda b: b.level)

    def lightest_bin(self):
        """Find the bin with the lowest level."""
        bins = self._silo.bins()
        if not bins:
            return None
        return min(bins, key=lambda b: b.level)

    def imbalance_report(self):
        """Generate a report of grain imbalance across bins."""
        avg = self.average_level()
        report = []
        for b in self._silo.bins():
            diff = b.level - avg
            report.append({
                "bin": b.name,
                "level": b.level,
                "deviation": round(diff, 2),
            })
        return sorted(report, key=lambda r: abs(r["deviation"]), reverse=True)
