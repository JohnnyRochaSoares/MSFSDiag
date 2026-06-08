# ==== Imports ==== #
import pytest
from pathlib import Path

from src.core.analyzer import analyze_addon

# ==== Analyze_Addon Tests ==== #
def test_analyze_addon_no_manifest(tmp_path):
    addon = tmp_path / "my-addon"
    addon.mkdir()
    report = analyze_addon(addon)
    assert report.has_manifest == False
    assert report.has_layout == False

def test_analyze_addon_invalid_json(tmp_path):
    addon = tmp_path / "my-addon"
    addon.mkdir()
    (addon / "manifest.json").write_text(
        "this is not json",
        encoding="utf-8"
    )
    report = analyze_addon(addon)
    assert report.has_manifest == True
    assert report.invalid_json == True

def test_analyze_addon_missing_fields(tmp_path):
    addon = tmp_path / "my-addon"
    addon.mkdir()