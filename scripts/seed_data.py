"""Seed a silo with sample data for development and testing."""

from silo import Silo


def seed_silo():
    """Create a silo with sample bins and pours."""
    silo = Silo()

    silo.create_bin("WHEAT-1")
    silo.create_bin("WHEAT-2")
    silo.create_bin("CORN-1")
    silo.create_bin("CORN-2")
    silo.create_bin("INTAKE", "overflow")
    silo.create_bin("STAGING", "temporary")

    silo.transfer("WHEAT-1", "INTAKE", 5000, "initial load")
    silo.transfer("WHEAT-2", "INTAKE", 3000, "initial load")
    silo.transfer("CORN-1", "INTAKE", 8000, "initial load")
    silo.transfer("CORN-2", "INTAKE", 4000, "initial load")

    silo.transfer("STAGING", "WHEAT-1", 500, "quality check")
    silo.transfer("WHEAT-1", "STAGING", 450, "return after check")
    silo.transfer("CORN-2", "CORN-1", 1000, "rebalance")

    return silo


if __name__ == "__main__":
    silo = seed_silo()
    print(f"Created silo with {len(silo.bins())} bins")
    print(f"Log entries: {len(silo.log_entries())}")
    for b in silo.bins():
        print(f"  {b.name}: level={b.level}")
