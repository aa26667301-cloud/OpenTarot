from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_DIR.parent

# Prefer editable/repository data while developing; fall back to packaged copies after installation.
DATA_DIR = (REPO_ROOT / "data") if (REPO_ROOT / "data").exists() else (PACKAGE_DIR / "data")
SPREADS_DIR = (REPO_ROOT / "spreads") if (REPO_ROOT / "spreads").exists() else (PACKAGE_DIR / "spreads")
