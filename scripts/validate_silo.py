"""Validate silo state consistency."""

from silo import Silo


def validate_silo(silo):
    """Run consistency checks on a silo instance."""
    errors = []

    total_in, total_out = silo.volume_summary()
    if total_in != total_out:
        errors.append(f"volume mismatch: in={total_in} out={total_out}")

    for b in silo.bins():
        pour_count = len(b.pours())
        if pour_count < 0:
            errors.append(f"bin {b.name}: negative pour count")

    log_ids = [p.id for p in silo.log_entries()]
    if log_ids != sorted(log_ids):
        errors.append("log entries not in order")

    if len(set(log_ids)) != len(log_ids):
        errors.append("duplicate pour IDs found")

    return errors


if __name__ == "__main__":
    silo = Silo()
    silo.create_bin("A")
    silo.create_bin("B", "overflow")
    silo.transfer("A", "B", 100)
    errors = validate_silo(silo)
    if errors:
        print("Validation errors:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("Silo validation passed")
