from tarotflow.deck import TarotDeck
from tarotflow.spreads import load_spread
from tarotflow.interpret import interpret_reading

deck = TarotDeck(seed=2026)
reading = deck.draw_spread(load_spread("three-card"))
print(interpret_reading(reading, "我現在最值得專注的是什麼？"))
