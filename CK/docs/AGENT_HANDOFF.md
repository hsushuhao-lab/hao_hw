# CK v0.3 — Agent Handoff

## GOAL

把已可直接試玩的 CK v0.3 Production Slice 推進到 **v0.4 Character Animation & Deployment QA**。不得重構目前已成立的遊戲循環：角色選擇 → 病人點餐 → 備料/切配 → 火候 → 甩鍋 → 上菜 → 結算。

## CURRENT SUCCESS CRITERIA — ALL PASS

1. `index.html` 可由靜態 HTTP server 執行，無 build step。
2. GitHub README 已提供直接試玩連結。
3. 3 位角色可選，且都有被動差異與每單一次的 Ultimate。
4. 6 類病人具有個別訂單與 portrait。
5. 豆腐 / 青蔥具有 timing 切配。
6. 4 階段火候可判定 Perfect / Miss。
7. 最後有獨立甩鍋 timing mini-game。
8. CRAVING / FOCUS、失敗條件、分數與連勝皆成立。
9. 病人具有進場、用餐、離場 CSS 演出。
10. 有 Web Audio 程序式音效與 mute。
11. `tests/smoke_test.py` 覆蓋主要頁面 token、機制函式與 web assets。

## NEXT TASK — v0.4

只做以下項目，完成一項就驗證一項：

- [ ] 三位醫師各製作透明 full-body sprite sheet：idle / prep / cook / serve / ultimate。
- [ ] 三位醫師的入場動畫必須互不相同，不可只改顏色或速度。
- [ ] 6 位病人製作最小 body sprite：walk / sit / eat / leave。
- [ ] 目前 CSS portrait 演出保留作 fallback，不要先刪。
- [ ] 將程序音效保留作 fallback，再補 production SFX / BGM 與獨立音量控制。
- [ ] 手機 390×844、平板 768×1024、桌機 1440×900 實機/瀏覽器 QA。
- [ ] 啟用正式 GitHub Pages 後，以 `https://hsushuhao-lab.github.io/hao_hw/CK/` 做 deploy smoke test。

## NON-GOALS

- 不增加第二道料理。
- 不做多人連線。
- 不擴張成大型醫院地圖。
- 不改資料模型，除非新動畫狀態真的需要。
- 不刪除目前 SVG / CSS fallback，直到新 production asset 已通過部署 QA。

## VISUAL SOURCE OF TRUTH

以 `docs/ART_BIBLE.md`、`assets/concept/` 和現有高解析 release art 為準。核心視覺原則仍是：**同一間診間突然變成料理工作站，而不是一般餐廳。**

## DEPLOYMENT

- Immediate preview: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html`
- Intended GitHub Pages: `https://hsushuhao-lab.github.io/hao_hw/CK/`
- 詳細步驟：`docs/DEPLOYMENT.md`
