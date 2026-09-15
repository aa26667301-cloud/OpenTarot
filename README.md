# OpenTarot 🔮

**繁體中文優先的開源塔羅反思引擎 + AI Skill。**

OpenTarot 不是「算命保證器」，而是一套可被網站、Bot、AI Agent 或個人筆記工具重複使用的塔羅資料與工作流程。核心重點是：**牌義資料結構、正逆位、牌陣位置、牌與牌的故事線，以及可追蹤的反思問題。**

## v0.1.0 內容

- 78 張塔羅牌繁中資料（22 大牌 + 56 小牌）
- 正位 / 逆位關鍵詞
- 四元素與四牌組欄位
- 5 種內建牌陣：單張、三張、關係、工作、陰影反思
- Python 抽牌引擎，支援 seed 方便測試與重現
- 基礎規則式敘事解讀
- `skills/tarot-reading/SKILL.md`：給 AI Agent 使用的塔羅工作流程
- 單元測試
- MIT License

## 快速開始

```bash
git clone https://github.com/aa26667301-cloud/OpenTarot.git
cd OpenTarot
python -m tarotflow.cli --spread three-card --question "我最近的工作方向要注意什麼？"
```

固定 seed：

```bash
python -m tarotflow.cli --spread career --seed 42
```

列出可用牌陣：

```bash
python -m tarotflow.cli --list-spreads
```

## Python 使用範例

```python
from tarotflow.deck import TarotDeck
from tarotflow.spreads import load_spread
from tarotflow.interpret import interpret_reading

deck = TarotDeck(seed=42)
spread = load_spread("three-card")
reading = deck.draw_spread(spread)
print(interpret_reading(reading, question="我下一步該把力氣放在哪？"))
```

## 資料格式

`data/cards_zh_tw.json` 每張牌包含：

```json
{
  "id": "16-the-tower",
  "arcana": "major",
  "name_en": "The Tower",
  "name_zh_tw": "高塔",
  "keywords_upright": ["突變", "真相揭露", "結構瓦解", "重建"],
  "keywords_reversed": ["延後衝擊", "抗拒改變", "內在震盪", "勉強維持"]
}
```

## 設計原則

1. **反思優先**：文字用「可能、可以觀察、值得思考」而非命定式語氣。
2. **可重用**：資料與抽牌邏輯分離，方便接 Web / App / Bot。
3. **可驗證**：支援 seed，測試與示範可以重現。
4. **不綁牌圖**：Repo 不內建第三方牌面圖片，避免圖像授權爭議。
5. **高風險議題降級**：醫療、法律、財務、人身安全等議題不可用塔羅取代專業判斷。

## 圖像授權提醒

本專案只提供資料與程式，不附第三方塔羅牌圖。若你要加入 Rider–Waite–Smith 或其他牌組圖片，請確認**該特定數位掃描 / 重製檔**的授權狀態；最安全的做法是使用你自己創作或明確標示可再利用的圖像。

## Roadmap

- [ ] 牌與牌組合規則（元素強弱、重複數字、大牌比例）
- [ ] Tarot Journal JSON Schema
- [ ] Web Demo
- [ ] REST API
- [ ] 多語系（EN / JA）
- [ ] 自訂牌陣與自訂牌組
- [ ] AI 解讀評測資料集

## 貢獻

歡迎補充牌義、改善繁中用詞、增加牌陣或提交 UI。請先閱讀 `CONTRIBUTING.md`。

## License

MIT。程式與本專案原創資料可依授權使用；第三方圖像或外部資料仍以各自授權為準。

