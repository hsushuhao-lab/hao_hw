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
- 無 build system、無外部套件；可直接用靜態 HTTP server 執行

## 執行

在 `CK/` 目錄：

```bash
python -m http.server 8000
```

瀏覽器開啟 `http://localhost:8000`。

## GitHub 分支內容

```text
assets/
  concept/      # 5 張輕量 SVG web fallback：角色、診間、Cooking Mode、道具、病人
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
PROGRESS.md
```

完整 release ZIP 另外保留高解析概念美術與角色 / 病人 portrait crops；GitHub 工作分支使用 SVG fallback，讓 prototype 維持輕量且可直接靜態執行。

## 遊戲定位

CK 是荒謬喜劇式的 arcade cooking game，不是醫療模擬器。遊戲中的「麻婆豆腐分散煙癮」是世界觀設定，不應被解讀為戒菸療法或醫療建議。

## 下一版目標（v0.3）

1. 把概念圖拆成正式透明 sprite / animation。
2. 完整病人：進門 → 坐下 → 點餐 → 用餐 → 離場動畫。
3. 把勾芡與甩鍋拆成獨立 mini-game。
4. 每位醫師增加專屬入場動畫與 ultimate skill。
5. 補上 production SFX / BGM。
6. 建立公開 deployment。
