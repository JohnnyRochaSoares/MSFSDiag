# ==== Imports ==== #
from dataclasses import dataclass, field
from pathlib import Path

from config import (
    MANIFEST_FILENAME,
    LAYOUT_FILENAME,
    REQUIRED_MANIFEST_FIELDS,
)
from core.manifest_parser import read_manifest, validate_manifest
from core.json_validator import is_valid_json

# ==== Addon Report ==== #
@dataclass
class AddonReport:
    addon_name:     str
    has_manifest:   bool = False
    has_layout:     bool = False
    invalid_json:   bool = False
    missing_fields: list[str] = field(default_factory=list)

# ==== Addon Analysis ==== #
def analyze_addon(addon_path: Path) -> AddonReport:
    report = AddonReport(addon_name=addon_path.name)

    manifest_path = addon_path / MANIFEST_FILENAME
    layout_path   = addon_path / LAYOUT_FILENAME

    report.has_manifest = manifest_path.exists()
    report.has_layout   = layout_path.exists()

    if report.has_manifest:
        if not is_valid_json(manifest_path):
            report.invalid_json = True
        else:
            manifest = read_manifest(addon_path)
            if manifest is not None:
                report.missing_fields = validate_manifest(manifest)

    return report
