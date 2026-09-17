# Craving Kitchen (CK) — v0.4 Art Alignment Build

[▶ **直接試玩 CK v0.4**](https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html)  
[🎨 **正式主美術 Concept Art**](https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html)  
[🧩 **角色動畫 / Art Bible**](https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art.html)  
[📦 **最終交班入口**](./docs/00_START_HERE.md)  
[🤖 **MASTER AGENT PROMPT**](./docs/MASTER_AGENT_PROMPT.md)

> 診間麻婆豆腐料理小遊戲：病人 craving 上升時，玩家操作三位可選醫師，接單、備料、切配、掌握火候、甩鍋並上菜。

## Current status

**v0.4 ART ALIGNMENT — PLAYABLE / APPROVED VISUAL DIRECTION APPLIED**

核心流程維持不變：

`選醫師 → 病人進場 → 點餐 → 診間切換 Cooking Mode → 備料/切配 → 四階段火候 → 甩鍋 → 上菜 → 病人用餐 → 結算 → 離場 → 下一位`

Failure：`CRAVING >= 100%`。

## Approved visual source of truth

2026-09-17 已正式鎖定以下五張設計稿為 CK 最高優先級美術準則：

```text
assets/art_direction/source_of_truth/
  doctor_concepts.jpg
  clinic_layout.jpg
  cooking_mode.jpg
  props_station.jpg
  patient_npcs.jpg
```

視覺關鍵詞：

**stylized 2.5D arcade illustration / warm / bright / semi-realistic / clinic × cooking / sticky notes / recipe prescriptions / order tickets**

核心規則：**Same Clinic, Different Flavors.** Cooking Mode 必須仍能辨認原本診間，不得改造成一般餐廳或商業廚房。

既有 `assets/characters/`、`assets/portraits/` 與 `assets/concept/*.svg` 目前僅作 gameplay placeholder / fallback，不代表 production-final 美術品質。

## v0.4 已修正

- 首頁 Hero 改用正式 Cooking Mode 主視覺。
- 診間 gameplay stage 改用正式 `clinic_layout.jpg`。
- Cooking Mode 轉場後改用正式 `cooking_mode.jpg`。
- 遊戲內 Art Gallery 改讀正式五張 concept sheets。
- 新增 `art-direction.css`，統一 Navy / Cream / Sky Blue / Warm Yellow / Chili Red / Scallion Green 色系。
- Doctor cards、order panel、patient card、phase tabs、ingredients、gallery 全面改成便條紙 / 訂單 / 處方箋式視覺語言。
- 新增 `src/art-direction.js`，在不重構 gameplay logic 的情況下把場景資產橋接到正式美術。
- `docs/ART_BIBLE.md` 升級為 Approved Art Bible v0.4。

## 遊戲已完成內容

- 3 位可選醫師，角色被動能力與主動 Ultimate 均不同。
- 6 類病人與多種訂單偏好。
- 診間 → Cooking Mode 場景轉換。
- 豆腐 / 青蔥 timing 切配。
- 4 階段火候判定 + Perfect Heat VFX。
- 甩鍋收尾 mini-game。
- 病人進場 → 點餐 → 用餐 → 離場演出。
- Web Audio 程序音效、mute、鍵盤 Space timing / U Ultimate。

## 線上內容

### Play
https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html

### Approved concept art
https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html

### GitHub source
https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK

### Intended GitHub Pages
https://hsushuhao-lab.github.io/hao_hw/CK/

GitHub Pages 需在 repository Settings → Pages 啟用 publishing source；raw.githack 可立即試玩。

## Handoff documents

依序閱讀：

1. [`docs/00_START_HERE.md`](./docs/00_START_HERE.md)
2. [`docs/FINAL_HANDOFF.md`](./docs/FINAL_HANDOFF.md)
3. [`docs/MASTER_AGENT_PROMPT.md`](./docs/MASTER_AGENT_PROMPT.md)
4. [`docs/SCENE_AND_GAME_FLOW.md`](./docs/SCENE_AND_GAME_FLOW.md)
5. [`docs/ONLINE_ASSET_INDEX.md`](./docs/ONLINE_ASSET_INDEX.md)
6. [`docs/ART_BIBLE.md`](./docs/ART_BIBLE.md)
7. [`docs/GDD.md`](./docs/GDD.md)
8. [`PROGRESS.md`](./PROGRESS.md)

## 本機執行

```bash
cd CK
python -m http.server 8000
```

開啟 `http://localhost:8000`。

Regression gate：

```bash
python tests/smoke_test.py
node --check src/data.js
node --check src/game.js
node --check src/art-direction.js
```

## Public art boundary

GitHub 公開版本只包含遊戲衍生美術，不公開原始真人照片。正式 concept sheets 是視覺 source of truth；legacy SVG 僅作執行與 fallback。

## 下一階段

1. 依 approved doctor concepts 製作三位醫師透明 production sprites。
2. 依 patient NPC sheet 製作六位病人的 production body states。
3. 把 props sheet 拆成真正可互動 ingredient / station assets。
4. 保留目前 gameplay loop，不增加第二道料理。
5. 完成 390×844、768×1024、1440×900 實機視覺 QA。

**先把第一道麻婆豆腐做到 production-quality，再擴內容。**
