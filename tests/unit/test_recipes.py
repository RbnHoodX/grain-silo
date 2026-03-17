"""Tests for blend recipes."""

from blends.recipes import BlendRecipe


class TestBlendRecipe:
    def test_create_recipe(self):
        recipe = BlendRecipe("test", {"WHT": 70, "RYE": 30})
        assert recipe.name == "test"

    def test_components_copy(self):
        original = {"WHT": 70, "RYE": 30}
        recipe = BlendRecipe("test", original)
        components = recipe.components
        components["CRN"] = 10
        assert "CRN" not in recipe.components

    def test_total_parts(self):
        recipe = BlendRecipe("test", {"WHT": 60, "CRN": 40})
        assert recipe.total_parts() == 100

    def test_total_parts_empty(self):
        recipe = BlendRecipe("empty", {})
        assert recipe.total_parts() == 0

    def test_proportion(self):
        recipe = BlendRecipe("test", {"WHT": 75, "RYE": 25})
        assert recipe.proportion("WHT") == 0.75
        assert recipe.proportion("RYE") == 0.25

    def test_proportion_missing(self):
        recipe = BlendRecipe("test", {"WHT": 100})
        assert recipe.proportion("CRN") == 0

    def test_proportion_empty(self):
        recipe = BlendRecipe("empty", {})
        assert recipe.proportion("WHT") == 0

    def test_scale(self):
        recipe = BlendRecipe("test", {"WHT": 60, "CRN": 40})
        scaled = recipe.scale(200)
        assert scaled["WHT"] == 120
        assert scaled["CRN"] == 80

    def test_scale_empty(self):
        recipe = BlendRecipe("empty", {})
        assert recipe.scale(100) == {}

    def test_repr(self):
        recipe = BlendRecipe("test", {"WHT": 100})
        r = repr(recipe)
        assert "test" in r
        assert "WHT" in r
