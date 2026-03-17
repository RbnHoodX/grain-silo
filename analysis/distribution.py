"""Distribution analysis for grain across bin types."""


class DistributionReport:
    """Reports on grain distribution patterns."""

    def __init__(self, silo):
        self._silo = silo

    def by_bin_kind(self):
        """Group bins by kind and sum their levels."""
        groups = {}
        for b in self._silo.bins():
            if b.kind not in groups:
                groups[b.kind] = 0
            groups[b.kind] += b.level
        return groups

    def top_loaded(self, n=3):
        """Return the n most heavily loaded bins."""
        bins = sorted(self._silo.bins(), key=lambda b: b.level, reverse=True)
        return bins[:n]

    def empty_bins(self):
        """Return bins with zero load."""
        return [b for b in self._silo.bins() if b.level == 0]

    def summary(self):
        """Generate a distribution summary dict."""
        bins = self._silo.bins()
        if not bins:
            return {"count": 0, "total": 0, "min": 0, "max": 0}
        levels = [b.level for b in bins]
        return {
            "count": len(bins),
            "total": sum(levels),
            "min": min(levels),
            "max": max(levels),
        }
