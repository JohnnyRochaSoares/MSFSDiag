# ==== Imports ==== #
from pathlib import Path

# ==== Symlink Validation ==== #
def find_broken_symlinks(folder: Path) -> list[Path]:
    if not folder.exists():
        return []

    return [
        entry for entry in folder.rglob("*")
        if entry.is_symlink() and not entry.exists()
    ]
