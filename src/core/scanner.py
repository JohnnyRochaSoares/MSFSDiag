# ==== Imports ==== #
from dataclasses import dataclass
from pathlib import Path

from config import (
    MSFS2020_USER_CFG,
    MSFS2024_USER_CFG_STEAM,
    MSFS2024_USER_CFG_STORE,
    MANIFEST_FILENAME,
    LAYOUT_FILENAME,
)

# ==== MSFS Installation ==== #
@dataclass
class MsfsInstallation:
    version:          str
    user_cfg:         Path
    community_folder: Path | None = None

# ==== Version Detection === #
def detect_installations() -> list[MsfsInstallation]:
    installations = []

    if MSFS2020_USER_CFG.exists():
        installations.append(MsfsInstallation(
            version  = "2020",
            user_cfg = MSFS2020_USER_CFG,
        ))

    # Steam tem prioridade, Store como fallback
    if MSFS2024_USER_CFG_STEAM.exists():
        installations.append(MsfsInstallation(
            version  = "2024",
            user_cfg = MSFS2024_USER_CFG_STEAM,
        ))
    elif MSFS2024_USER_CFG_STORE.exists():
        installations.append(MsfsInstallation(
            version  = "2024",
            user_cfg = MSFS2024_USER_CFG_STORE,
        ))

    return installations

# ==== Community Folder Detection ==== #
def find_community_folder(installation: MsfsInstallation) -> Path | None:
    try:
        text = installation.user_cfg.read_text(encoding="utf-8")
    except OSError:
        return None

    for line in text.splitlines():
        if line.startswith("InstalledPackagesPath"):
            raw_path = line.split('"')[1]
            return Path(raw_path) / "Community"

    return None

# ==== Add-on Listing ==== #
def list_addons(community_folder: Path) -> list[Path]:
    if not community_folder.exists():
        return []

    return [
        entry for entry in community_folder.iterdir()
        if entry.is_dir()
    ]
