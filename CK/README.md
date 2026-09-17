# Craving Kitchen (CK) — v0.4.1 Corrected Art Build

[▶ **直接試玩 CK**](https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html)  
[🎨 **正式美術 Source of Truth**](https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html)  
[📦 **交班入口**](./docs/00_START_HERE.md)  
[🤖 **MASTER AGENT PROMPT**](./docs/MASTER_AGENT_PROMPT.md)

> 診間麻婆豆腐料理小遊戲：病人 craving 上升時，玩家操作三位可選醫師，接單、備料、切配、掌握火候、甩鍋並上菜。

## Current status

**v0.4.1 ART CORRECTION — CORRECTED CANONICAL ART PUBLISHED / RUNTIME BOUND TO APPROVED ART**

先前 v0.4 的主要問題是：文件雖宣告了正確美術方向，但 runtime 仍讀取舊的 `assets/art/*.jpg` 與 legacy SVG，因此線上畫面與核准的五張美術設計不一致。

v0.4.1 已修正這個治理錯誤。

## 唯一正式美術 Source of Truth

以下五張 WebP 是目前 CK 最高優先級視覺準則：

```text
assets/art_direction/source_of_truth/
  doctor_concepts.webp
  clinic_layout.webp
  cooking_mode.webp
  props_station.webp
  patient_npcs.webp
```

這五張直接來自本輪核准的正確美術設計，保留 4:3 完整構圖並以 WebP 提供線上遊戲使用。

### 視覺核心

**Same Clinic, Different Flavors.**

- 仍然是同一個門診診間。
- Cooking Mode 是料理元素「侵入」診間，而不是改造成一般餐廳。
- 角色、病人、材料、UI 語言、色彩與場景都以五張正式 concept sheets 為準。
- Legacy SVG 只能作 fallback / 程式相容資產，不再具有 production art authority。

## v0.4.1 修正內容

- 發布五張正確 canonical WebP artwork。
- `src/art-direction.js` 改成直接讀取 `assets/art_direction/source_of_truth/*.webp`。
- Hero 直接使用正式 `cooking_mode.webp`。
- Clinic / Cooking stage 會被 runtime 強制導向正式場景。
- Doctor selection cards 由正式 doctor concept sheet 產生可見角色圖，不再顯示舊 portrait SVG。
- Doctor presence / doctor stage 由正式 doctor sheet 顯示。
- Patient card / patient stage 由正式 patient NPC sheet 顯示。
- 遊戲內 Art Gallery 強制使用正式五張 WebP。
- `art-original.html` 已改成 canonical art gallery。
- 文件、handoff、asset index 與 regression gate 同步改成正確資產治理。

## Core gameplay baseline

`選醫師 → 病人進場 → 點餐 → 診間切換 Cooking Mode → 備料/切配 → 四階段火候 → 甩鍋 → 上菜 → 病人用餐 → 結算 → 離場 → 下一位`

Failure：`CRAVING >= 100%`。

遊戲仍保留：

- 3 位可選醫師與不同 passive / Ultimate。
- 6 類病人與不同訂單偏好。
- 豆腐 / 青蔥 timing 切配。
- 4 階段火候判定。
- final wok toss。
- CRAVING / FOCUS 雙資源。
- Web Audio / BGM / volume mixer。

## 線上入口

- Play: https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html
- Approved art: https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html
- GitHub: https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK

Repository 目前 `has_pages=false`，因此原生 GitHub Pages 尚未啟用；raw.githack 為目前直接試玩入口。

## 開發規則

後續任何 AGENT 必須：

1. 先讀 `docs/00_START_HERE.md`。
2. 把五張 canonical WebP 視為最高美術 authority。
3. 不得再以 `assets/concept/*.svg`、`assets/characters/*.svg` 或 `assets/portraits/*.svg` 宣稱 production-final art。
4. 不增加第二道料理，直到麻婆豆腐的 production character/prop assets 完成。
5. 不把診間改造成 generic restaurant。

## Regression commands

```bash
cd CK
python tests/smoke_test.py
node --check src/data.js
node --check src/game.js
node --check src/art-direction.js
python -m http.server 8000
```

遊戲中的麻婆豆腐為喜劇世界觀設定，並非戒菸治療或醫療建議。
