# ==== Imports ==== #
import json
from pathlib import Path

from config import (
    MANIFEST_FILENAME,
    REQUIRED_MANIFEST_FIELDS,
)

# ==== Manifest Reading ==== #
def read_manifest(addon_path: Path) -> dict | None:
    manifest_path = addon_path / MANIFEST_FILENAME

    if not manifest_path.exists():
        return None

    try:
        with open(manifest_path, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None

# ==== Manifest Validation ==== #
def validate_manifest(manifest: dict) -> list[str]:
    missing = []

    for field in REQUIRED_MANIFEST_FIELDS:
        if field not in manifest:
            missing.append(field)

    return missing
