"""Search utilities for grain silo data."""


def find_pours_by_note(silo, note):
    """Find all pours with a matching note."""
    return [p for p in silo.log_entries() if p.note == note]


def find_bins_by_kind(silo, kind):
    """Find all bins of a given kind."""
    return [b for b in silo.bins() if b.kind == kind]


def find_empty_bins(silo):
    """Find all bins with zero level."""
    return [b for b in silo.bins() if b.level == 0]


def find_largest_pour(silo):
    """Find the pour with the largest amount."""
    entries = silo.log_entries()
    if not entries:
        return None
    return max(entries, key=lambda p: p.amount)


def count_pours_per_bin(silo):
    """Count the number of pours involving each bin."""
    counts = {}
    for b in silo.bins():
        counts[b.name] = len(b.pours())
    return counts
