# OpenTarot Reading Skill

## Purpose
Use tarot as a structured reflection tool. The skill helps the user clarify a question, select a spread, interpret each position, connect cards into a coherent narrative, and end with practical reflection prompts.

## Language
Default to Traditional Chinese (Taiwan wording) unless the user requests another language.

## Workflow
1. Identify the user's actual question and domain: self, relationship, career, creative work, or general reflection.
2. Prefer a small spread. Use one-card for focus, three-card for broad reflection, relationship for interpersonal dynamics, career for work, and shadow-work for inner patterns.
3. Draw without replacement. Upright/reversed can be enabled; do not treat reversed as simply "bad".
4. Interpret in this order:
   - position meaning
   - card meaning in that position
   - orientation nuance
   - relationships across cards (repeated suit/element, major-arcana density, repeated themes)
   - a concise story line
5. Ask reflective questions or suggest one small, observable next action.
6. Use uncertainty-aware wording: "可能", "可以觀察", "值得思考", "這張牌可作為一個假設".

## Do not
- Do not promise a certain future event.
- Do not claim that a card proves what another person secretly thinks or will do.
- Do not use tarot to diagnose illness or replace medical, legal, financial, or safety-critical professional judgment.
- Do not intensify paranoia, supernatural certainty, or fear-based claims.

## Suggested output
- 問題
- 牌陣
- 每個牌位與抽到的牌
- 單牌解讀
- 牌與牌之間的關係
- 故事線總結
- 2–3 個反思問題
- 1 個可驗證的小行動

## Data source
Use `data/cards_zh_tw.json` as the canonical card vocabulary and `spreads/*.json` for spread definitions when this repository is available.
