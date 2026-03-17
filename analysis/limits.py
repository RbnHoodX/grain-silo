"""Limit checking for grain bin levels."""

from config import LOW_LEVEL_THRESHOLD, HIGH_LEVEL_THRESHOLD, CRITICAL_LEVEL_THRESHOLD


class LimitChecker:
    """Checks grain bin levels against configured thresholds."""

    def __init__(self, silo):
        self._silo = silo

    def low_level_bins(self):
        """Find bins below the low-level threshold."""
        return [
            b for b in self._silo.bins()
            if 0 < b.level < LOW_LEVEL_THRESHOLD
        ]

    def high_level_bins(self):
        """Find bins above the high-level threshold."""
        return [
            b for b in self._silo.bins()
            if b.level > HIGH_LEVEL_THRESHOLD
        ]

    def critical_bins(self):
        """Find bins at or below the critical threshold."""
        return [
            b for b in self._silo.bins()
            if 0 < b.level <= CRITICAL_LEVEL_THRESHOLD
        ]

    def check_all(self):
        """Run all limit checks and return a status dict."""
        return {
            "low": [b.name for b in self.low_level_bins()],
            "high": [b.name for b in self.high_level_bins()],
            "critical": [b.name for b in self.critical_bins()],
        }
