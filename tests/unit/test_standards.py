"""Tests for standard blend presets."""

import pytest
from blends.standards import get_standard_blend, list_standard_blends


class TestStandardBlends:
    def test_list_blends(self):
        blends = list_standard_blends()
        assert "feed_mix" in blends
        assert "bread_flour" in blends

    def test_get_feed_mix(self):
        recipe = get_standard_blend("feed_mix")
        assert recipe.name == "feed_mix"
        components = recipe.components
        assert "CRN" in components

    def test_get_bread_flour(self):
        recipe = get_standard_blend("bread_flour")
        assert "WHT" in recipe.components

    def test_get_unknown_raises(self):
        with pytest.raises(KeyError):
            get_standard_blend("mystery")

    def test_total_parts(self):
        recipe = get_standard_blend("feed_mix")
        assert recipe.total_parts() == 100

    def test_proportion(self):
        recipe = get_standard_blend("feed_mix")
        assert recipe.proportion("CRN") == 0.6
