from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class CardDraw:
    id: str
    name_zh_tw: str
    name_en: str
    orientation: str
    keywords: list[str]
    arcana: str
    suit: Optional[str] = None
    element: Optional[str] = None

@dataclass(frozen=True)
class PositionedCard:
    position_id: str
    position_label: str
    prompt: str
    card: CardDraw

@dataclass(frozen=True)
class Reading:
    spread_id: str
    spread_name: str
    cards: list[PositionedCard]
