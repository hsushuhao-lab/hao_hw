# CK — Game Design Document v0.1

## 1. High Concept

**一句話：** 在精神科診間裡，把突然升高的煙癮變成一張麻婆豆腐訂單；玩家必須在 craving 爆表前完成備料、火候與上菜。

核心辨識度不是「料理」，而是**嚴肅診間突然切換為高壓料理站**的視覺與節奏反差。

## 2. Core Loop

1. 病人入場並描述 craving / 口味。
2. 玩家讀取 order ticket。
3. 備料：選取必要材料；錯拿材料增加 craving。
4. 烹調：完成爆香 → 炒肉 → 下豆腐 → 勾芡收汁。
5. 上菜：依時間、火候與 focus 結算。
6. 下一位病人；病人需求逐漸複雜。

## 3. Win / Fail

- **Win:** 在 CRAVING < 100% 時完成訂單。
- **Fail:** CRAVING 到 100%。
- **Score:** 基礎分 + 火候命中 + 剩餘 craving + focus。

## 4. Playable Doctors

### DR. SPEED — 快刀醫師
- 定位：備料型。
- v0.1 技能：每次正確備料 Focus +8。
- 未來：切豆腐 mini-game 的判定速度更快。

### DR. HEAT — 火候醫師
- 定位：烹調型。
- v0.1 技能：最佳火候區加寬。
- 未來：連續 perfect heat 可觸發「大火收汁」。

### DR. STRATEGY — 處方醫師
- 定位：訂單 / 時間管理型。
- v0.1 技能：craving 增長速度降低 18%。
- 未來：可提早看到病人的隱藏 modifier。

## 5. Patient Archetypes

- 焦慮上班族：要求快。
- 熬夜學生：材料排除。
- 長班司機：高辣、多項加料。
- 熱情阿姨：份量型訂單。
- 安靜青年：簡短但精準需求。
- 熟客：後期可改成「跟上次一樣」的記憶題。

NPC 需維持尊重與人性，不用疾病標籤當笑點。

## 6. Difficulty Curve

- Stage 1: 單一病人、固定訂單。
- Stage 2: modifier 增加。
- Stage 3: 病人會中途改單。
- Stage 4: 兩張訂單並行。
- Boss: 候診室連續 5 張掛號單。

## 7. Medical Framing

CK 的核心是喜劇遊戲化。畫面應保留簡短 disclaimer：**麻婆豆腐不是戒菸治療；真實戒菸應依循實證治療與專業建議。**
