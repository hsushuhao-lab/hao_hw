# CK v0.6 — Realistic Clinic-Kitchen Rebuild

**STATUS: ACTIVE REBUILD / FIRST REALISTIC ENVIRONMENT PUBLISHED**

The previous concept-sheet bridge was useful for art governance but did not feel like a believable game. v0.6 starts a deliberate rebuild around a realistic outpatient consultation room that is physically converted into a compact mapo-tofu workstation.

Current v0.6 changes:
- high-detail production clinic environment is now loaded by the runtime;
- gameplay stage is larger and less card-like;
- clinical workstation, wash area, prep cart and wok zone are spatially identified inside one room;
- UI is quieter and more physical/clinical; rounded cartoon-card treatment is reduced;
- the approved semi-realistic doctor/patient concept art remains identity authority while dedicated production character sheets are prepared;
- the gameplay loop remains playable during the rebuild.

**Non-negotiable target:** believable clinic first + improvised kitchen second; refined semi-realistic people; no generic restaurant; no flat/Q-style final characters.

# Craving Kitchen (CK) — v0.4.2 Art Closeout

[▶ **直接試玩 CK**](https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html)  
[🎨 **正式美術 Source of Truth**](https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html)  
[📦 **交班入口**](./docs/00_START_HERE.md)  
[🤖 **MASTER AGENT PROMPT**](./docs/MASTER_AGENT_PROMPT.md)

> 診間麻婆豆腐料理小遊戲：病人 craving 上升時，玩家操作三位可選醫師，接單、備料、切配、掌握火候、甩鍋並上菜。

## Current status

**v0.4.2 ART CLOSEOUT — CANONICAL ART ONLINE / RUNTIME BOUND / LEGACY ART FALLBACK ONLY**

本版修正先前最大的治理錯誤：文件、美術頁與 runtime 現在全部指向同一組正式美術，不再由舊 `assets/art/*.jpg` 或 legacy SVG 決定視覺風格。

## 唯一正式美術 Source of Truth

```text
assets/art_direction/source_of_truth/
  doctor_concepts.avif
  clinic_layout.avif
  cooking_mode.avif
  props_station.avif
  patient_npcs.avif
```

這五張圖是 CK 的最高視覺 authority：

- `doctor_concepts.avif`：三位可選醫師的造型、服裝、道具與筆觸。
- `clinic_layout.avif`：同一個診間的空間基準。
- `cooking_mode.avif`：診間進入 Cooking Mode 後的正式氣氛與工作站配置。
- `props_station.avif`：麻婆豆腐材料、器具、備料站與 prescription/order-ticket 語言。
- `patient_npcs.avif`：六位病人 archetype 的正式視覺。

核心規則：**Same Clinic, Different Flavors.** Cooking Mode 是料理元素侵入同一診間，不得改造成 generic restaurant 或 commercial kitchen。

## Runtime art policy

`src/art-direction.js` 與 `art-direction.css` 直接讀取 `assets/art_direction/source_of_truth/*.avif`。

既有：

- `assets/art/`
- `assets/concept/`
- `assets/characters/`
- `assets/portraits/`

全部降級為 **legacy compatibility / gameplay fallback**，不得再標示為 production-final art。

## Core gameplay baseline

`選醫師 → 病人進場 → 點餐 → 診間切換 Cooking Mode → 備料/切配 → 四階段火候 → 甩鍋 → 上菜 → 病人用餐 → 結算 → 離場 → 下一位`

Failure：`CRAVING >= 100%`。

目前保留：

- 3 位可選醫師與不同 passive / Ultimate。
- 6 類病人與不同訂單偏好。
- 豆腐 / 青蔥 timing 切配。
- 4 階段火候判定。
- final wok toss。
- CRAVING / FOCUS 雙資源。
- Web Audio / BGM / volume mixer。

## Art closeout rules

1. 新增 production asset 時必須能追溯到五張 canonical sheets。
2. 主角、病人與場景不得重新發明畫風。
3. UI 使用 navy / cream / sky blue / warm yellow / chili red / scallion green，搭配 rounded card、sticky note、order ticket、recipe prescription。
4. 文字使用 HTML/CSS 真文字，不使用圖像中的 AI pseudo-text 作正式 UI。
5. 不增加第二道料理，直到麻婆豆腐的 production character / patient / prop assets 完成。

## 線上入口

- Play: https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html
- Approved art: https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html
- GitHub: https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK

Repository 目前未啟用原生 GitHub Pages，因此 raw.githack 為直接試玩入口。

## Regression commands

```bash
cd CK
python tests/smoke_test.py
node --check src/data.js
node --check src/game.js
node --check src/art-direction.js
python -m http.server 8000
```

遊戲中的麻婆豆腐為喜劇世界觀設定，不是戒菸治療或醫療建議。
