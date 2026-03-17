"""Standard grain blend presets."""

from .recipes import BlendRecipe

_STANDARD_BLENDS = {
    "feed_mix": BlendRecipe("feed_mix", {"CRN": 60, "OAT": 25, "BRL": 15}),
    "bread_flour": BlendRecipe("bread_flour", {"WHT": 85, "RYE": 15}),
    "livestock": BlendRecipe("livestock", {"CRN": 50, "SRG": 30, "OAT": 20}),
    "poultry": BlendRecipe("poultry", {"CRN": 40, "WHT": 30, "MLT": 20, "OAT": 10}),
}


def get_standard_blend(name):
    """Get a standard blend recipe by name."""
    if name not in _STANDARD_BLENDS:
        raise KeyError(f"unknown standard blend: {name!r}")
    return _STANDARD_BLENDS[name]


def list_standard_blends():
    """List all available standard blend names."""
    return sorted(_STANDARD_BLENDS.keys())
