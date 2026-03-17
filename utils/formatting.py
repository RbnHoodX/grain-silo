"""Formatting utilities for grain silo display."""


def format_amount(amount, unit="bu"):
    """Format an amount with unit label."""
    if isinstance(amount, float):
        return f"{amount:.2f} {unit}"
    return f"{amount} {unit}"


def format_bin_status(b):
    """Format a bin status string."""
    kind_label = f"[{b.kind}]"
    return f"{b.name:<20} {kind_label:<14} level={b.level}"


def format_header(title, width=50):
    """Format a section header."""
    return f"{'=' * width}\n{title:^{width}}\n{'=' * width}"


def truncate(text, max_length=40):
    """Truncate text to max_length, adding ellipsis if needed."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."
