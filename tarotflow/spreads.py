import json
from pathlib import Path
from .paths import SPREADS_DIR

def list_spreads() -> list[str]:
    return sorted(p.stem for p in SPREADS_DIR.glob("*.json"))

def load_spread(spread_id: str) -> dict:
    path = SPREADS_DIR / f"{spread_id}.json"
    if not path.exists():
        raise ValueError(f"Unknown spread: {spread_id}. Available: {', '.join(list_spreads())}")
    return json.loads(path.read_text(encoding="utf-8"))
