"""Command-line interface for grain silo management."""

import sys
from silo import Silo
from config import BIN_KINDS, GRAIN_TYPES


def create_default_silo():
    """Create a silo with default bin configuration."""
    silo = Silo()
    silo.create_bin("MAIN-1")
    silo.create_bin("MAIN-2")
    silo.create_bin("RESERVE-1", "reserve")
    silo.create_bin("OVERFLOW", "overflow")
    return silo


def format_bin_status(b):
    """Format a single bin status line."""
    return f"  {b.name:<20} {b.kind:<12} level={b.level}"


def format_silo_report(silo):
    """Format a full silo status report."""
    lines = ["=== Silo Status Report ===", ""]
    lines.append(f"Bins: {len(silo.bins())}")
    lines.append(f"Log entries: {len(silo.log_entries())}")
    lines.append("")

    lines.append("Bin Status:")
    for b in silo.bins():
        lines.append(format_bin_status(b))
    lines.append("")

    total_in, total_out = silo.volume_summary()
    lines.append(f"Total volume in:  {total_in}")
    lines.append(f"Total volume out: {total_out}")

    return "\n".join(lines)


def print_grain_types():
    """Print available grain type codes."""
    print("Available grain types:")
    for code, name in sorted(GRAIN_TYPES.items()):
        print(f"  {code}: {name}")


def print_bin_kinds():
    """Print available bin kinds."""
    print("Available bin kinds:")
    for kind in BIN_KINDS:
        print(f"  {kind}")


def main():
    """Main CLI entry point."""
    silo = create_default_silo()

    if len(sys.argv) < 2:
        print(format_silo_report(silo))
        return

    command = sys.argv[1]

    if command == "types":
        print_grain_types()
    elif command == "kinds":
        print_bin_kinds()
    elif command == "status":
        print(format_silo_report(silo))
    else:
        print(f"Unknown command: {command}")
        print("Usage: cli.py [status|types|kinds]")
        sys.exit(1)


if __name__ == "__main__":
    main()
