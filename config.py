"""Configuration constants for grain silo management."""

# Default bin settings
DEFAULT_BIN_KIND = "standard"
MAX_BIN_NAME_LENGTH = 50
MIN_POUR_AMOUNT = 1

# Bin kind options
BIN_KINDS = ("standard", "overflow", "reserve", "temporary")

# Volume thresholds
LOW_LEVEL_THRESHOLD = 100
HIGH_LEVEL_THRESHOLD = 10000
CRITICAL_LEVEL_THRESHOLD = 50

# Report settings
DEFAULT_REPORT_FORMAT = "text"
SUPPORTED_FORMATS = ("text", "csv", "json")
MAX_REPORT_ENTRIES = 1000

# Grain type codes
GRAIN_TYPES = {
    "WHT": "wheat",
    "CRN": "corn",
    "BRL": "barley",
    "OAT": "oats",
    "RYE": "rye",
    "SRG": "sorghum",
    "MLT": "millet",
    "RCE": "rice",
}

# Season codes
SEASONS = {
    "SPR": "spring",
    "SUM": "summer",
    "FAL": "fall",
    "WIN": "winter",
}

# Quality grades
QUALITY_GRADES = ("prime", "choice", "select", "standard", "utility")
