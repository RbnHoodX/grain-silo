"""Grain blend recipe definitions."""


class BlendRecipe:
    """A grain blend recipe specifying proportions of different grain types."""

    def __init__(self, name, components):
        self._name = name
        self._components = dict(components)

    @property
    def name(self):
        return self._name

    @property
    def components(self):
        return dict(self._components)

    def total_parts(self):
        """Return the total number of parts in this blend."""
        return sum(self._components.values())

    def proportion(self, grain_type):
        """Return the proportion (0-1) of a grain type in this blend."""
        total = self.total_parts()
        if total == 0:
            return 0
        return self._components.get(grain_type, 0) / total

    def scale(self, target_total):
        """Scale the recipe to a target total amount."""
        total = self.total_parts()
        if total == 0:
            return {}
        factor = target_total / total
        return {k: round(v * factor, 2) for k, v in self._components.items()}

    def __repr__(self):
        return f"BlendRecipe(name={self._name!r}, components={self._components})"
