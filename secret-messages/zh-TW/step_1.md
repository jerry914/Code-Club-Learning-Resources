## 介紹：

你將在本專案中學習如何製作你自己的加密程式，從而在朋友間傳送和接收祕密資訊。本專案與太空日記第 16 頁的“地球到 Principa”活動相關。

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/402256078c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/messages-finished.png">
</div>

### 更多俱樂部領導參考資訊

如果你需要列印本專案，請使用 [適合印表機的版本](https://projects.raspberrypi.org/en/projects/secret-messages/print)。


--- collapse ---
---
title: 俱樂部領導備註
---


## 介紹：
孩子們將在本專案中學習如何製作一個加密程式，從而在朋友間傳送和接收祕密資訊。本專案介紹了對文字字串進行迭代（迴圈）。

## 線上資源

本專案使用 Python 3。我們推薦使用 [trinket](https://trinket.io/）線上編寫 Python。本專案包含以下 Trinket：

+ [新（空白）Python Trinket -- jumpto.cc/python-new](http://jumpto.cc/python-new)

還有一個 trinket 包含已完成專案：

+ [“祕密資訊”已完成 -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

+ [“友情計算器”已完成 -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

## 離線資源
如果希望的話，本專案可[離線完成](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/)。

你可以在“志願者資源”部分中找到已完成專案，其中包含：

+ messages-finished/messages.py
+ messages-finished/friends.py

（以上所有的資源也可以作為專案和志願者 `.zip` 檔案下載。）

## 學習目標
+ 對字串變數進行迭代（迴圈）；
+ `find()` 方法；
+ 取模運算子 (`%`)。

本專案包括 [Raspberry Pi 數字製作課程](http://rpf.io/curriculum) 以下幾個部分的元素：

+ [結合程式設計結構解決問題。](https://www.raspberrypi.org/curriculum/programming/builder)

## 挑戰
+ 使用凱撒密碼 - 手動加密和解密字母和單詞；
+ 可變金鑰 - 允許使用者輸入選定的金鑰；
+ 加密和解密資訊 - 加密和解密完整資訊；
+ 友情計算器 - 將文字迭代應用到新的問題。

## 常見問題
+ 當使用 `find()` 或 `if char in alphabet:` 進行搜尋時，請注意搜尋會區分大小寫。孩子們可以使用：

	```python
	message = input("Please enter a message to encrypt: ").lower()
	```

	在搜尋之前將輸入內容變為小寫。

--- /collapse ---


--- collapse ---
---
title: 專案材料
---
## 專案資源
* [包含所有專案資源的 .zip 檔案](resources/secret-messages-project-resources.zip)
* [線上空白 Python Trinket](http://jumpto.cc/python-new)
* [離線空白 Python 檔案](resources/new-new.py)

## 俱樂部領導資源
* [包含所有已完成專案資源的 .zip 檔案](resources/secret-messages-volunteer-resources.zip)
* [線上已完成 Trinket 專案](https://trinket.io/python/402256078c)
* [secret-messages-finished/messages.py](resources/secret-messages-finished-messages.py)
* [線上已完成“友情計算器”挑戰](https://trinket.io/python/2e852cd687)
* [離線完成“友情計算器”挑戰](resources/friendship-calculator-finished-friends.py)

--- /collapse ---
