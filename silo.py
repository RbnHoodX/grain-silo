"""Silo class managing bins and grain pour operations."""

from bin import Bin
from pour import Pour, PourLog


class Silo:
    """Grain silo managing bins and pour operations."""

    def __init__(self):
        self._bins = {}
        self._log = PourLog()

    def create_bin(self, name, kind="standard"):
        if name in self._bins:
            raise ValueError(f"bin {name!r} already exists")
        b = Bin(name, kind)
        self._bins[name] = b
        return b

    def get_bin(self, name):
        return self._bins[name]

    def bins(self):
        return list(self._bins.values())

    def transfer(self, dest_name, source_name, amount, note=""):
        if amount <= 0:
            raise ValueError("amount must be positive")
        dest_bin = self._bins[dest_name]
        source_bin = self._bins[source_name]
        pour = Pour(dest_bin, source_bin, amount, note)
        self._log.record(pour)
        return pour

    def log_entries(self):
        return self._log.pours()

    def volume_summary(self):
        total_in = 0
        total_out = 0
        for pour in self._log.pours():
            total_in += pour.amount
            total_out += pour.amount
        return total_in, total_out
