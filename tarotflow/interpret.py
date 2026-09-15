from collections import Counter
from .models import Reading

ORIENTATION = {"upright": "正位", "reversed": "逆位"}
ELEMENT_ZH = {"fire": "火", "water": "水", "air": "風", "earth": "土"}

def _pattern_notes(reading: Reading) -> list[str]:
    notes = []
    major_count = sum(1 for p in reading.cards if p.card.arcana == "major")
    if major_count >= max(2, len(reading.cards) // 2 + 1):
        notes.append("大牌比例偏高：這次反思可能更像是在碰觸核心課題，而不只是日常小事件。")
    elements = [p.card.element for p in reading.cards if p.card.element]
    if elements:
        counts = Counter(elements)
        elem, n = counts.most_common(1)[0]
        if n >= 2:
            notes.append(f"{ELEMENT_ZH.get(elem, elem)}元素重複出現：可觀察這個主題是否在不同位置以不同形式重演。")
    reversed_count = sum(1 for p in reading.cards if p.card.orientation == "reversed")
    if reversed_count > len(reading.cards) / 2:
        notes.append("逆位偏多：與其急著對外行動，可以先檢查內在阻力、延遲或尚未整合的部分。")
    return notes

def interpret_reading(reading: Reading, question: str | None = None) -> str:
    lines = [f"# {reading.spread_name}"]
    if question:
        lines += [f"問題：{question}", ""]
    for item in reading.cards:
        c = item.card
        kw = "、".join(c.keywords[:4])
        lines.append(f"## {item.position_label}｜{c.name_zh_tw}（{ORIENTATION[c.orientation]}）")
        lines.append(f"牌位提問：{item.prompt}")
        lines.append(f"關鍵詞：{kw}")
        lines.append(f"反思：在「{item.position_label}」這個位置，可先從「{c.keywords[0]}」與「{c.keywords[1]}」觀察目前情境，而不是把牌當成固定結果。")
        lines.append("")
    notes = _pattern_notes(reading)
    if notes:
        lines.append("## 牌面關係")
        lines.extend(f"- {n}" for n in notes)
        lines.append("")
    sequence = " → ".join(f"{x.card.name_zh_tw}：{x.card.keywords[0]}" for x in reading.cards)
    lines += ["## 故事線", sequence, "", "## 行動式反思",
              "把這次牌面當作假設：哪一個關鍵詞最符合現況？哪一個最不符合？接下來 24–72 小時內，有什麼小行動可以驗證你的理解？",
              "", "> OpenTarot 用於自我探索與創意反思，不取代醫療、法律、財務或人身安全等專業判斷。"]
    return "\n".join(lines)
