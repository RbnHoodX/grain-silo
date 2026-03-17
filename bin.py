"""Grain bin that tracks its level from pour log entries."""


class Bin:
    """A grain bin that tracks its level from pour log entries.

    The level is always computed from pours -- never stored directly.
    This guarantees the level is always consistent with the pour log.
    """

    def __init__(self, name, kind="standard"):
        self._name = name
        self._kind = kind
        self._pours = []

    @property
    def name(self):
        return self._name

    @property
    def kind(self):
        return self._kind

    @property
    def level(self):
        total = 0
        for pour in self._pours:
            if pour.dest_bin is self:
                total += pour.amount
            elif pour.source_bin is self:
                total -= pour.amount
        return total

    def _add_pour(self, pour):
        self._pours.append(pour)

    def pours(self):
        return list(self._pours)

    def __repr__(self):
        return f"Bin(name={self._name!r}, kind={self._kind!r})"
