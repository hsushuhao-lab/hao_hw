# Craving Kitchen (CK) — v0.3 Production Slice

[▶ **直接試玩 CK v0.3**](https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html)  
[🎨 **原始主美術 Concept Art**](https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html)  
[🧩 **角色動畫 / Art Bible**](https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art.html)  
[📦 **最終交班入口**](./docs/00_START_HERE.md)  
[🤖 **MASTER AGENT PROMPT**](./docs/MASTER_AGENT_PROMPT.md)

> 診間麻婆豆腐料理小遊戲：病人 craving 上升時，玩家操作三位可選醫師，接單、備料、切配、掌握火候、甩鍋並上菜。

## Current status

**v0.3 Production Slice — COMPLETE / PLAYABLE / HANDOFF READY**

已成立的 regression baseline：

`選醫師 → 病人進場 → 點餐 → 診間切換 Cooking Mode → 備料/切配 → 四階段火候 → 甩鍋 → 上菜 → 病人用餐 → 結算 → 離場 → 下一位`

Failure：`CRAVING >= 100%`。

## v0.3 已完成

- 3 位可選醫師，角色被動能力與主動 **Ultimate** 均不同。
- 6 類病人與多種訂單偏好。
- 診間 → Cooking Mode 場景轉換。
- 豆腐 / 青蔥 timing 切配。
- 4 階段火候判定 + Perfect Heat VFX。
- 甩鍋收尾 mini-game。
- 病人進場 → 點餐 → 用餐 → 離場演出。
- DR. SPEED：閃電備料。
- DR. HEAT：下一次火候必定 Perfect。
- DR. STRATEGY：降低 Craving 並恢復 Focus。
- Web Audio 程序音效、mute、鍵盤 Space timing / U Ultimate。
- 線上美術 gallery、GDD、Art Bible、asset index、scene/game flow、deployment notes、regression test、final handoff、next-agent master prompt。
- **五張實際製作的主美術 concept sheets 已正式上 GitHub**：醫師角色、診間配置、Cooking Mode、料理材料/道具、病人 NPC。

## 線上內容

### Play
https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html

### Original concept art — production visual source of truth
https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art-original.html

實際圖片位於：

```text
assets/art/
  doctor_concepts.jpg
  clinic_layout.jpg
  cooking_mode.jpg
  props.jpg
  patient_npcs.jpg
```

### Animation Art Bible / SVG gameplay assets
https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/art.html

### GitHub source
https://github.com/hsushuhao-lab/hao_hw/tree/ck-game/CK

### Intended GitHub Pages
https://hsushuhao-lab.github.io/hao_hw/CK/

GitHub Pages 仍需在 repository Settings → Pages 啟用 publishing source；raw.githack 目前可直接試玩與瀏覽美術。

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
```

## Public art boundary

GitHub 公開版本現在包含 **本專案生成的衍生遊戲 concept art**，但不公開原始真人照片。五張 JPEG concept sheets 是 production visual source of truth；既有 SVG 則作為遊戲執行、角色動畫與 fallback 資產。兩者用途不得混淆。

核心規則：**Same Clinic, Different Mode**。Cooking Mode 必須仍能辨識原始診間，不得改造成一般餐廳。

## 下一版 v0.4

1. 三位醫師 transparent full-body sprite sheet：entrance / idle / prep / cut / cook / serve / ultimate。
2. 三位醫師入場與 Ultimate 必須明顯不同。
3. 六位病人 walk / sit / order / eat / leave body animation。
4. 正式 BGM / SFX；Web Audio 保留 fallback。
5. 390×844、768×1024、1440×900 手動 QA。
6. GitHub Pages 原生部署驗證。

**不要增加第二道料理，直到第一道麻婆豆腐的角色動畫與部署 QA 達到 production quality。**