# R2 重製、測試與移轉

本輪修復的是現行2D原型和交班包，不是完成3D遊戲。原型仍只有CSS／DOM人物與場景。

## 已確認並修正的缺陷
1. 下方料理區原本位於桌面首屏之外；現在上方移動、下方料理同屏。
2. 窄螢幕原本主角在畫面外；修正鏡頭定位。
3. 舊版沒有豆腐、沒有翻炒仍可盛盤；現在必要材料為豆腐、絞肉、豆瓣醬、蒜，需開火並翻炒三次。新材料加入後重新計次。
4. R原本只重置人物；現在清空探索、選料、備料、鍋內材料、火焰、翻炒和盛盤狀態。

## 測試範圍
新增24項Chromium行為檢查：1440×900、768×1024、390×844版面、人物可見性、鍵盤移動、不誤捲頁、配方缺料、翻炒次數、關火、重置與第二次遊玩。
本機測試使用inline載入真實原始碼，因本機瀏覽器的localhost HTTP受環境政策阻擋；不能把inline測試稱為CDN測試。本repo CI另從HTTP載入相同檔案並保存截圖與source hashes。CI成功與否以同一commit的run為準，不以文件宣告為準。

## 完整材料包
本輪下載用 source R2 包另外包含七張原始PNG、七張1200px閱覽JPEG、六張舊候選WebP，共20張圖，全部完整解碼並檢查SHA-256與尺寸。原圖檔名doctor_concepts、clinic_layout、cooking_mode、props_station、patient_npcs、art_bible_poster、realistic_ui_board。
這些完整二進位素材仍在移轉封包，並沒有因本次原型程式推送而自動進入本repo。真人參考照、舊ZIP與歷史QA另在private-history封包，不發布至此公開repo。

## 新repository的真實狀態
預定hsushuhao-lab/clinic-kitchen-2，本輪get_repo回傳404，未列於connector授權清單。不能判定是尚未建立或尚未授權；未宣稱成功建立。之前建立流程因403失敗，本輪未重跑它。
本次可寫入的目的地為現有hao_hw/main，只推原型修復、測試和文字交班；不建立分支、不force push、不刪其他專案。
完整source包附tools/publish_main.py，供使用者本機授權的GitHub CLI建立private目的地並push main，驗證遠端SHA。不得將旧repo token當成新repo管理權限。

## 下一步製作
依已確認的前診間／中過渡備料／後廚，以及上方移動／下方料理規格，製作真正3D環境、DR.SPEED模型、一位病人、問診—處方—取材—烹調—端回—第一口任務。設定圖不是模型，現有CSS不代表精緻寫實美術已完成。
