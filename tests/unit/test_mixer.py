"""Tests for blend mixer."""

from blends.recipes import BlendRecipe
from blends.mixer import BlendMixer


class TestBlendMixer:
    def test_calculate_amounts(self):
        recipe = BlendRecipe("test", {"WHT": 60, "CRN": 40})
        mixer = BlendMixer(recipe)
        amounts = mixer.calculate_amounts(200)
        assert amounts["WHT"] == 120
        assert amounts["CRN"] == 80

    def test_recipe_property(self):
        recipe = BlendRecipe("test", {"WHT": 100})
        mixer = BlendMixer(recipe)
        assert mixer.recipe.name == "test"

    def test_validate_stock_sufficient(self):
        recipe = BlendRecipe("test", {"WHT": 60, "CRN": 40})
        mixer = BlendMixer(recipe)
        missing = mixer.validate_stock({"WHT": 100, "CRN": 100})
        assert missing == {}

    def test_validate_stock_insufficient(self):
        recipe = BlendRecipe("test", {"WHT": 60, "CRN": 40})
        mixer = BlendMixer(recipe)
        missing = mixer.validate_stock({"WHT": 30, "CRN": 100})
        assert "WHT" in missing
        assert missing["WHT"] == 30

    def test_validate_stock_missing_type(self):
        recipe = BlendRecipe("test", {"WHT": 60, "CRN": 40})
        mixer = BlendMixer(recipe)
        missing = mixer.validate_stock({"WHT": 100})
        assert "CRN" in missing

    def test_mix_report(self):
        recipe = BlendRecipe("test", {"WHT": 60, "CRN": 40})
        mixer = BlendMixer(recipe)
        report = mixer.mix_report(200)
        assert "test" in report
        assert "Total: 200" in report


class TestBlendMixerEdgeCases:
    def test_empty_recipe(self):
        recipe = BlendRecipe("empty", {})
        mixer = BlendMixer(recipe)
        assert mixer.calculate_amounts(100) == {}

    def test_single_component(self):
        recipe = BlendRecipe("pure", {"WHT": 100})
        mixer = BlendMixer(recipe)
        amounts = mixer.calculate_amounts(500)
        assert amounts["WHT"] == 500
