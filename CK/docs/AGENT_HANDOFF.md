# CK v0.4.2 — Agent Handoff

## GOAL

接手已完成美術治理收尾的 CK v0.4.2，推進到 **v0.5 Production Asset Extraction & Animation**。不得改寫已成立的核心循環：角色選擇 → 病人點餐 → 備料/切配 → 火候 → 甩鍋 → 上菜 → 結算。

## CURRENT BASELINE

已成立：

1. 靜態 `index.html` 可直接執行，無 build step。
2. 3 位醫師可選，passive 與 Ultimate 不同。
3. 6 類病人具有不同訂單。
4. 豆腐 / 青蔥 timing 切配。
5. 4 階段火候判定。
6. final wok-toss mini-game。
7. CRAVING / FOCUS、失敗條件、分數、連勝。
8. 病人進場 / 用餐 / 離場狀態。
9. Web Audio SFX / BGM / mixer。
10. canonical art runtime bridge 已上線。

## ONLY VISUAL SOURCE OF TRUTH

```text
assets/art_direction/source_of_truth/
  doctor_concepts.avif
  clinic_layout.avif
  cooking_mode.avif
  props_station.avif
  patient_npcs.avif
```

所有舊 `assets/concept/`、`assets/portraits/`、`assets/characters/`、`assets/art/` 都只能作 compatibility fallback。

核心原則：**Same Clinic, Different Flavors.** 同一診間被料理元素侵入，不是一般餐廳。

## NEXT TASK — v0.5

依序完成：

- [ ] DR. SPEED production vertical slice：entrance / idle / prep / cut / cook / serve / ultimate / fail / victory。
- [ ] 經視覺審核鎖定角色比例、臉型、眼鏡、髮型、白袍與筆觸。
- [ ] DR. HEAT、DR. STRATEGY 套用同一 production standard。
- [ ] 六位病人製作 walk / sit / order-react / eat / leave production body sets。
- [ ] 從 `props_station.avif` 製作透明 ingredient / cookware / ticket / prescription assets。
- [ ] legacy SVG/CSS fallback 保留到 replacement 通過 online QA。
- [ ] 390×844、768×1024、1440×900 QA。

## NON-GOALS

- 不增加第二道料理。
- 不做多人連線。
- 不擴張成大型醫院地圖。
- 不把診間改成商業廚房。
- 不把 legacy SVG 當新 production art 的畫風參考。
- 不在 replacement 驗證前刪除 fallback。

## REGRESSION

```bash
cd CK
python tests/smoke_test.py
node --check src/data.js
node --check src/game.js
node --check src/art-direction.js
python -m http.server 8000
```

## LINKS

- Play: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html`
- Approved art: `https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html`
- Repository: `https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK`

正式執行細節以 `MASTER_AGENT_PROMPT.md` 為準。
