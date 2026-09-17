# Craving Kitchen (CK) — v0.2 Vertical Slice

> 一款發生在診間的麻婆豆腐料理小遊戲：病人煙癮突然升高，玩家操作三位可選醫師，在有限時間內完成病人指定的麻婆豆腐訂單，利用備料與料理任務把注意力拉回當下。

## v0.2 已完成

- 3 位可選角色：DR. SPEED / DR. HEAT / DR. STRATEGY
- 6 類病人 NPC 與不同點餐偏好
- 診間 → Cooking Mode 場景切換
- 備料 mini-game：正確材料 / 錯誤材料懲罰
- 豆腐 / 青蔥切配 timing mini-game
- 火候 mini-game：4 個烹調步驟與 timing 判定 + Perfect Heat VFX
- CRAVING / FOCUS 雙資源
- 訂單結算、分數、連勝
- 病人進場 / 離場動畫、診間切換閃光
- Web Audio 程序音效與 mute 控制
- 5 張主要概念美術＋角色/病人 portrait crops
- 無 build system、無外部套件；可直接用靜態 HTTP server 執行

## 執行

```bash
python -m http.server 8000
```

瀏覽器開啟 `http://localhost:8000`。

## 目錄

```text
assets/
  concept/      # 角色、診間、Cooking Mode、道具、病人概念圖
  portraits/    # 遊戲介面用角色/病人裁切圖
src/
  data.js       # 角色、病人、材料、料理流程資料
  game.js       # 遊戲狀態與互動
styles.css      # UI / responsive layout
index.html      # 單頁遊戲入口
docs/
  GDD.md
  ART_BIBLE.md
  ASSET_MANIFEST.md
  AGENT_HANDOFF.md
tests/
  smoke_test.py
```

## 遊戲定位

CK 是荒謬喜劇式的 arcade cooking game，不是醫療模擬器。遊戲中的「麻婆豆腐分散煙癮」是世界觀設定，不應被解讀為戒菸療法或醫療建議。

## 下一版目標（v0.3）

1. 把概念圖拆成正式可動 sprite / animation。
2. 做真正的點餐動畫與候診隊列。
3. 加入豆腐切割、勾芡、甩鍋三種獨立 mini-game。
4. 每位醫師增加專屬入場動畫與 ultimate skill。
5. 音效：印表機出票、炒鍋、切菜、服務鈴、craving 警報。
6. GitHub Pages / deployment workflow。
