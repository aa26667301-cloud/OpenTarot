# AGENTS.md

## Project
OpenTarot is a Traditional-Chinese-first open-source tarot reflection engine.

## Rules
- Keep the 78-card dataset structurally valid.
- Prefer dependency-free Python for the core engine.
- Do not add copyrighted card images unless the license is explicit and compatible.
- Use reflective, probabilistic language; do not claim deterministic future prediction.
- For medical, legal, financial, or safety-critical questions, clearly separate tarot reflection from professional advice.
- Add or update tests when changing draw logic, spread loading, or interpretation structure.

## Validation
Run: `python -m unittest discover -s tests -v`
