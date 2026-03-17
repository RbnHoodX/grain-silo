"""Grain blend mixing utilities."""


class BlendMixer:
    """Mixes grain blends according to recipes."""

    def __init__(self, recipe):
        self._recipe = recipe

    @property
    def recipe(self):
        return self._recipe

    def calculate_amounts(self, total_volume):
        """Calculate the amount of each grain type for a given total volume."""
        return self._recipe.scale(total_volume)

    def validate_stock(self, available):
        """Check if available stock can fulfill the blend at given amounts."""
        needed = self._recipe.components
        missing = {}
        for grain_type, amount in needed.items():
            avail = available.get(grain_type, 0)
            if avail < amount:
                missing[grain_type] = amount - avail
        return missing

    def mix_report(self, total_volume):
        """Generate a human-readable mix report."""
        amounts = self.calculate_amounts(total_volume)
        lines = [f"Blend: {self._recipe.name}", f"Total: {total_volume}"]
        for grain_type, amount in sorted(amounts.items()):
            pct = (amount / total_volume * 100) if total_volume > 0 else 0
            lines.append(f"  {grain_type}: {amount} ({pct:.1f}%)")
        return "\n".join(lines)
