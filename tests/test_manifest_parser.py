# ==== Imports ==== #
import pytest
from pathlib import Path

from src.core.manifest_parser import read_manifest, validate_manifest

# ==== validate_manifest tests ==== #
def test_validate_manifest_all_fields_present():
    manifest = {
        "title":                "My Addon",
        "manufacturer":         "Me",
        "version":              "1.0.0",
        "minimum_game_version": "1.0.0",
        "content_type":         "SCENERY",
        "dependencies":         [],
    }
    missing = validate_manifest(manifest)
    assert missing == []

def test_validate_manifest_missing_fields():
    manifest = {"title": "My Addon"}
    missing = validate_manifest(manifest)
    assert "manufacturer" in missing
    assert "version" in missing
    assert "minimum_game_version" in missing
    assert "content_type" in missing
    assert "dependencies" in missing

def test_validate_manifest_empty():
    missing = validate_manifest({})
    assert len(missing) == 6

# ==== read_manifest tests ==== #
def test_read_manifest_missing_file(tmp_path):
    result = read_manifest(tmp_path / "nonexistent")
    assert result is None

def test_read_manifest_valid(tmp_path):
    addon = tmp_path / "my-addon"
    addon.mkdir()
    (addon / "manifest.json").write_text(
        '{"title": "Test", "version": "1.0.0"}',
        encoding="utf-8"
    )
    result = read_manifest(addon)
    assert result is not None
    assert result["title"] == "Test"