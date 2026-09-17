# CK v0.1 — Agent Handoff

## GOAL

把目前 CK vertical slice 推進到 **可公開試玩的 v0.2**，但不得破壞已完成的 v0.1 game loop：角色選擇 → 病人點餐 → 備料 → 火候 → 上菜 → 結算。

## CURRENT SUCCESS CRITERIA

1. `index.html` 可由靜態 server 直接啟動。
2. 3 位角色都可選，且技能差異有實際數值效果。
3. 隨機產生 6 類病人之一。
4. 正確/錯誤備料會改變 Focus / Craving。
5. 4 個火候步驟皆可判定成功/失敗。
6. Craving 到 100% 會結束該單。
7. 成功上菜會計分並可進下一位病人。

## NEXT TASK — v0.2

**不要先重構。** 先完成下列可驗證任務：

- [ ] 新增真正的 `TitleScene` 入場動畫。
- [ ] 把醫師 portrait 換成透明角色 sprite，不再依賴 concept-sheet crop。
- [ ] 新增病人從門口進場 → 坐下 → 點餐 → 吃完離場動畫。
- [ ] 備料拆成至少「切豆腐」和「切蔥」兩個 timing mini-game。
- [ ] Perfect Heat 觸發 0.4–0.8 秒 VFX。
- [ ] 加入音效 mute 控制。
- [ ] 建立 GitHub Pages deploy workflow。

## NON-GOALS

- 不增加第二道料理。
- 不做多人連線。
- 不做大型醫院地圖。
- 不重寫成重型 framework，除非現有結構阻礙明確需求。

## VISUAL SOURCE OF TRUTH

先看 `docs/ART_BIBLE.md` 與 `assets/concept/`。Cooking Mode 必須仍看得出原本是診間，不能改成一般餐廳。
