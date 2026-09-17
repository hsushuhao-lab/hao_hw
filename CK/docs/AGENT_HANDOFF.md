# CK v0.2 — Agent Handoff

## GOAL

把目前已通過 smoke test 的 CK v0.2 推進到 **可公開試玩的 v0.3 production slice**，但不得破壞既有流程：角色選擇 → 病人點餐 → 備料/切配 → 火候 → 上菜 → 結算。

## CURRENT SUCCESS CRITERIA — ALL PASS

1. `index.html` 可由靜態 server 啟動。
2. 3 位角色都可選，技能差異有實際數值效果。
3. 隨機產生 6 類病人之一。
4. 正確/錯誤備料會改變 Focus / Craving。
5. 豆腐與青蔥可進入三次 timing 切配挑戰。
6. 4 個火候步驟皆可判定成功/失敗，Perfect 會顯示 VFX。
7. Craving 到 100% 會結束該單。
8. 成功上菜會計分、記錄連勝並進下一位病人。
9. 病人有進場/離場動畫。
10. 有程序式音效與 mute 控制。

## NEXT TASK — v0.3

**不要重構既有可玩的 game loop。** 先完成下列可驗證任務：

- [ ] 三位醫師各自有透明 full-body sprite 與 idle / prep / cook / serve 動畫。
- [ ] 病人有門口進場 → 坐下 → 點餐 → 用餐 → 離場的 body animation。
- [ ] 將勾芡與甩鍋拆成獨立 mini-game；切豆腐維持現有 timing 核心。
- [ ] 每位醫師新增一個專屬入場動畫與一個 ultimate skill。
- [ ] 將程序音效替換/補強為 production SFX：出票、切菜、炒鍋、服務鈴、craving 警報。
- [ ] 建立可公開試玩的 deployment。

## NON-GOALS

- 不增加第二道料理。
- 不做多人連線。
- 不擴張成大型醫院地圖。
- 不因為『順便』而改寫目前資料模型或 UI 架構。

## VISUAL SOURCE OF TRUTH

先看 `docs/ART_BIBLE.md` 與 `assets/concept/`。Cooking Mode 必須仍清楚看得出原本是診間，不能改成一般餐廳。
