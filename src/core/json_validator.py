# ==== Imports ==== #
import json
from pathlib import Path

# ==== JSON Validation ==== #
def is_valid_json(path: Path) -> bool:
    try:
        with open(path, encoding="utf-8") as f:
            json.load(f)
        return True
    except (json.JSONDecodeError, OSError):
        return False
