# Clinic Kitchen 2.0 — R2 verified 2D prototype

目前版本明確標示為2D／CSS功能原型，不是3D建模或美術成品。

上方WASD／方向鍵移動，E檢視附近物件；下方備料、開火、下鍋、翻炒、盛盤。R清空全部探索及料理狀態。窄螢幕僅驗證版面，尚未提供觸控移動。

R2修好上下區同屏、窄螢幕鏡頭、缺料／未翻炒也可盛盤及重置不完整，加入24項實際Chromium行為測試。

## 測試
```sh
cd CK
python tests/smoke_test.py
python -m pip install playwright==1.57.0
python -m playwright install chromium
python -m http.server 8000 --bind 127.0.0.1
# 第二個terminal
python tests/browser_qa.py --base-url http://127.0.0.1:8000/
```
離線可用 --inline；此模式不代表HTTP／CDN驗證。

完整素材、私人附件分流及新repo權限狀態見 [R2_MIGRATION.md](docs/R2_MIGRATION.md)。新repo未確認可存取；本次只更新現有main。完整二進位美術在另份R2下載封包，不在此原型tree。

[試玩main](https://raw.githack.com/hsushuhao-lab/hao_hw/main/CK/index.html)

下一步為真正3D診間—備料—後廚與單一病人任務，不以CSS裝飾或CI綠燈代替遊戲／美術完成。
