import json
import random
from .paths import DATA_DIR
from .models import CardDraw, PositionedCard, Reading

class TarotDeck:
    def __init__(self, seed=None, reversal_rate: float = 0.5):
        if not 0 <= reversal_rate <= 1:
            raise ValueError("reversal_rate must be between 0 and 1")
        self.rng = random.Random(seed)
        self.reversal_rate = reversal_rate
        self.cards = json.loads((DATA_DIR / "cards_zh_tw.json").read_text(encoding="utf-8"))
        if len(self.cards) != 78:
            raise RuntimeError(f"Expected 78 cards, got {len(self.cards)}")

    def draw(self, count: int = 1) -> list[CardDraw]:
        if count < 1 or count > len(self.cards):
            raise ValueError("count must be between 1 and 78")
        chosen = self.rng.sample(self.cards, count)
        result = []
        for raw in chosen:
            reversed_ = self.rng.random() < self.reversal_rate
            orientation = "reversed" if reversed_ else "upright"
            keywords = raw["keywords_reversed"] if reversed_ else raw["keywords_upright"]
            result.append(CardDraw(
                id=raw["id"], name_zh_tw=raw["name_zh_tw"], name_en=raw["name_en"],
                orientation=orientation, keywords=list(keywords), arcana=raw["arcana"],
                suit=raw.get("suit"), element=raw.get("element")
            ))
        return result

    def draw_spread(self, spread: dict) -> Reading:
        positions = spread["positions"]
        drawn = self.draw(len(positions))
        placed = [
            PositionedCard(position_id=pos["id"], position_label=pos["label_zh_tw"],
                           prompt=pos["prompt"], card=card)
            for pos, card in zip(positions, drawn)
        ]
        return Reading(spread_id=spread["id"], spread_name=spread["name_zh_tw"], cards=placed)
