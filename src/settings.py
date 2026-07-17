# ==== Imports ==== #
import json
import os
from pathlib import Path

# ==== Settings File Location ==== #
SETTINGS_FILE = Path(os.environ["APPDATA"]) / "MSFSDiag" / "settings.json"

DEFAULT_SETTINGS = {
    "language": "EN",
    "theme":    "dark",
    "gemini_api_key": "",
}

# ==== Load and Save ==== #
def load_settings() -> dict:
    try:
        return {**DEFAULT_SETTINGS, **json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))}
    except (OSError, json.JSONDecodeError):
        return DEFAULT_SETTINGS.copy()

def save_settings(language: str, theme: str, gemini_api_key: str = "") -> None:
    SETTINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
    SETTINGS_FILE.write_text(
            json.dumps({"language": language, "theme": theme, "gemini_api_key": gemini_api_key}, indent=4),
        encoding="utf-8",
        )

