import argparse
from .deck import TarotDeck
from .spreads import load_spread, list_spreads
from .interpret import interpret_reading

def main():
    parser = argparse.ArgumentParser(description="OpenTarot - 繁中開源塔羅反思引擎")
    parser.add_argument("--spread", default="three-card", help="牌陣 id")
    parser.add_argument("--question", default=None, help="反思問題")
    parser.add_argument("--seed", type=int, default=None, help="固定隨機種子，方便重現")
    parser.add_argument("--no-reversals", action="store_true", help="停用逆位")
    parser.add_argument("--list-spreads", action="store_true", help="列出可用牌陣")
    args = parser.parse_args()
    if args.list_spreads:
        for s in list_spreads(): print(s)
        return
    deck = TarotDeck(seed=args.seed, reversal_rate=0 if args.no_reversals else 0.5)
    reading = deck.draw_spread(load_spread(args.spread))
    print(interpret_reading(reading, question=args.question))

if __name__ == "__main__":
    main()
