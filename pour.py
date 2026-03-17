"""Pour and PourLog classes for grain movement tracking."""


class Pour:
    """A grain movement entry linking two bins."""

    def __init__(self, dest_bin, source_bin, amount, note=""):
        self._id = 0
        self._dest_bin = dest_bin
        self._source_bin = source_bin
        self._amount = amount
        self._note = note

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def dest_bin(self):
        return self._dest_bin

    @property
    def source_bin(self):
        return self._source_bin

    @property
    def amount(self):
        return self._amount

    @property
    def note(self):
        return self._note

    def __repr__(self):
        return (f"Pour(id={self._id}, dest={self._dest_bin.name!r}, "
                f"source={self._source_bin.name!r}, amount={self._amount})")


class PourLog:
    """Append-only log of grain pour records."""

    def __init__(self):
        self._pours = []
        self._counter = 0

    def record(self, pour):
        self._counter += 1
        pour.id = self._counter
        self._pours.append(pour)
        pour.dest_bin._add_pour(pour)
        pour.source_bin._add_pour(pour)
        return pour

    def pours(self):
        return list(self._pours)
