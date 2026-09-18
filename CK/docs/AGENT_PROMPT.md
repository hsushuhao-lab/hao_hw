# AGENT 執行指令 — Clinic Kitchen R2

先讀 CK/README.md、docs/R2_MIGRATION.md。本repo是原型修復與交班來源；完整source R2包另外含七張美術原圖、閱覽頁、候選圖、manifest與推送腳本。

## 目前真實狀態
這是一個CSS／DOM 2D原型，不是3D建模。R2新增24項Chromium行為檢查；它們只涵蓋版面、移動、食材與翻炒條件、關火、盛盤、重置。上方站點與下方料理目前獨立運作，沒有病人問診—處方—搬運—第一口。不得用舊版的PASS宣稱替代檢查。

## 分支與發布
僅在main工作，不另建feature branch，不force push。新repo預定hsushuhao-lab/clinic-kitchen-2，目前未確認可存取。不能把舊repo更新稱為新repo發布成功。遇403／404要停在相應權限步驟；不得用舊repo token繞過建立／管理權限。
完整下載包在新repo根目錄使用src/main.js；此舊repo使用CK/src/main.js。不能把整包root覆蓋到hao_hw根目錄。

## 先跑回歸
```sh
cd CK
python tests/smoke_test.py
python -m pip install playwright==1.57.0
python -m playwright install chromium
python -m http.server 8000 --bind 127.0.0.1
# 第二個terminal
python tests/browser_qa.py --base-url http://127.0.0.1:8000/
```
離線inline模式不是HTTP／CDN驗證。看1440×900、768×1024、390×844截圖，不能只看語法檢查或HTTP 200。

## 已核准的遊戲／美術規格
上方主角移動與探索，下方備料／煮菜。前半真實診間，中間清潔與備料過渡，後半固定存在的廚房。三區真正在同一空間，人物需走得過去。不是魔法換背景，也不是普通餐廳。
精緻寫實成人比例，不能Q版、扁平SVG、emoji或貼照片冒充模型。先DR.SPEED：黑髮、透明框眼鏡、白袍、淺色內搭；正反側與3/4設定；實際模型、骨架、材質；idle/walk/sit/talk/pickup/carry/prep/cook/serve。一次先驗收一位，之後才做藍襯衫的DR.HEAT與圓框眼鏡／米色內搭／綠口罩元素的DR.STRATEGY。不得從真人照片推論姓名或真人能力。
每位角色、每個場景、每項食材分別製作與交檔。完整PNG是視覺參考，不是可貼滿整個畫面充當實機遊戲的素材。候選WebP只是舊圖，不是完成的模型。最新寫實UI board與最新使用者要求優先於舊圖裡Q版與醫療功效標語。

## 第一條可玩鏈
一位病人入座 → 問需求 → 寫料理訂單與列印 → 走到後廚 → 冰箱／櫃子取材 → 豆腐／蔥蒜備料 → 炒鍋料理 → 盛飯盛菜 → 托盤端回 → 病人第一口 → 反應結算。
只有一位主角、一位病人、一碗麻婆豆腐；驗收前不加第二道菜與無關功能。

## 工程規則
先提出最小即時3D引擎與部署方案，再實作有幾何、碰撞、材質和光線的診間—過渡區—後廚。不是再改CSS標題。
每個bug先建立能重現的測試；保持R2缺豆腐／翻炒次數／關火／全重置／二次遊玩／窄螢幕回歸。上方站點與下方操作必須共享任務狀態。料理需看到食材與鍋內變化，不再只是串多條timing bar。
原稿以完整解碼、尺寸、SHA-256驗證，不用幾KB門檻冒充完整性。CI、視覺驗收、完整素材上傳與新repo建立分開報告。

## 隱私
原始真人照片、舊ZIP、歷史QA在private-history封包，不上傳本公開repo，不部署到靜態網站。來源不明不自行指定開源授權。

## 回報
精確main SHA、實際修改、測試結果、同一SHA的CI、各尺寸截圖、真正開過的試玩網址、模型／素材manifest、尚未完成項目。沒有看過實機就不能稱為試玩；只有原型bugfix不能稱為精緻3D遊戲完成。
