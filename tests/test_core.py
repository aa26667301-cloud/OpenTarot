import unittest
from tarotflow.deck import TarotDeck
from tarotflow.spreads import load_spread, list_spreads

class CoreTests(unittest.TestCase):
    def test_deck_has_78_cards(self):
        self.assertEqual(len(TarotDeck(seed=1).cards), 78)

    def test_draw_is_unique(self):
        cards = TarotDeck(seed=1).draw(10)
        self.assertEqual(len({c.id for c in cards}), 10)

    def test_seed_is_reproducible(self):
        a = TarotDeck(seed=42).draw(3)
        b = TarotDeck(seed=42).draw(3)
        self.assertEqual([(x.id, x.orientation) for x in a], [(x.id, x.orientation) for x in b])

    def test_three_card_spread(self):
        spread = load_spread("three-card")
        reading = TarotDeck(seed=7).draw_spread(spread)
        self.assertEqual(len(reading.cards), 3)
        self.assertEqual([x.position_id for x in reading.cards], ["past", "present", "advice"])

    def test_builtin_spreads(self):
        self.assertTrue({"one-card","three-card","relationship","career","shadow-work"}.issubset(set(list_spreads())))

if __name__ == "__main__":
    unittest.main()
