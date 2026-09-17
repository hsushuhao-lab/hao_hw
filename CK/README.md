# Craving Kitchen (CK) — v0.3 Production Slice

[▶ **直接試玩 CK v0.3**](https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html)

> 診間麻婆豆腐料理小遊戲：病人 craving 上升時，玩家操作三位可選醫師，接單、備料、切配、掌握火候、甩鍋並上菜。

## v0.3 已完成

- 3 位可選醫師，角色能力與主動 **Ultimate** 均不同。
- 6 類病人與多種訂單偏好。
- 診間 → Cooking Mode 場景轉換。
- 豆腐 / 青蔥 timing 切配。
- 4 階段火候判定 + Perfect Heat VFX。
- 新增 **甩鍋收尾 mini-game**。
- 病人進場 → 點餐 → 用餐 → 離場演出。
- DR. SPEED：閃電備料；DR. HEAT：下一次火候必定 Perfect；DR. STRATEGY：降低 Craving 並恢復 Focus。
- Web Audio 程序音效、mute、鍵盤 Space timing / U Ultimate。
- GitHub web build 使用輕量 SVG 角色 / 病人 portraits；完整 release ZIP 保留高解析概念美術。

## 直接試玩

GitHub branch 的靜態內容以 raw.githack 提供瀏覽器預覽：

**https://raw.githack.com/hsushuhao-lab/hao_hw/ck-game/CK/index.html**

正式 GitHub Pages 網址預留為：

**https://hsushuhao-lab.github.io/hao_hw/CK/**

GitHub Pages 需在 repository Settings → Pages 將 publishing source 啟用後才會生效；目前上方 raw.githack 連結可立即試玩。

## 本機執行

```bash
cd CK
python -m http.server 8000
```

開啟 `http://localhost:8000`。

## 專案結構

```text
assets/
  concept/      # 5 張主要美術概念圖
  portraits/    # 3 位醫師 + 6 位病人角色裁切
src/
  data.js       # 角色、Ultimate、病人、材料、料理流程
  game.js       # 遊戲狀態與互動
styles.css
index.html
docs/
  GDD.md
  ART_BIBLE.md
  ASSET_MANIFEST.md
  AGENT_HANDOFF.md
  DEPLOYMENT.md
tests/smoke_test.py
PROGRESS.md
```

## 遊戲定位

CK 是荒謬喜劇式 arcade cooking game，不是醫療模擬器。麻婆豆腐分散煙癮屬虛構遊戲設定，不代表戒菸療法或醫療建議。

## 下一版 v0.4

1. 角色透明 sprite / expression sheet，取代 portrait overlay。
2. 三位醫師各自不同的入場與 Ultimate 動畫。
3. 病人完整 body walk / sit / eat / leave sprite animation。
4. 正式 BGM / SFX 與音量控制。
5. GitHub Pages 正式部署與手機實機 QA。
