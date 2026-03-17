"""Aggregation utilities for grain silo data."""


def sum_amounts(pours):
    """Sum the amounts of a list of pours."""
    return sum(p.amount for p in pours)


def group_by_note(pours):
    """Group pours by their note field."""
    groups = {}
    for p in pours:
        if p.note not in groups:
            groups[p.note] = []
        groups[p.note].append(p)
    return groups


def average_amount(pours):
    """Calculate the average amount across a list of pours."""
    if not pours:
        return 0
    return sum_amounts(pours) / len(pours)
