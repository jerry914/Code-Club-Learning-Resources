## 出錯

有時可能會出錯，因此讓我們來向你的專案新增一個“清除”按鈕和一個橡皮擦！



+ 讓我們新增一個按鈕來清空工作區。為此，向工作區新增“X-block”字母子圖並將其變為紅色。

	![screenshot](images/paint-x.png)

+ 向你的新取消按鈕新增程式碼，使其在被點選時清空工作區。

	```blocks
		當角色被點選
    筆跡清除
	```

	請注意你無需傳送訊息來清空工作區，因為任何子圖都能做到！

+ 你可能注意到了你的鉛筆子圖包含一個橡皮擦造型：

	![screenshot](images/paint-eraser-costume.png)
	

+ 你的專案還包含一個橡皮擦選擇器子圖，右鍵單擊並選擇“顯示”。你的工作區應如下所示：

	![screenshot](images/paint-eraser-stage.png)

+ 你隨後可以向橡皮擦選擇器子圖新增程式碼，告訴鉛筆切換為橡皮擦。

	```blocks
		當角色被點選
    廣播訊息 [eraser v]
	```

+ 鉛筆收到此訊息時，你可以通過將鉛筆造型切換為橡皮擦來建立一個橡皮擦，並將鉛筆顏色變為與工作區同樣的顏色！

	```blocks
		當收到訊息 [eraser v]
    造型換成 [eraser v]
    筆跡顏色設為 [#FFFFFF]
	```

+ 測試你的專案，看看你能否在工作區進行清空和擦除。

	![screenshot](images/paint-erase-test.png)

+ 鉛筆還有一個問題 - 你可以在工作區的任何地方進行繪圖，包括選擇器圖示附近！

	![screenshot](images/paint-draw-problem.png)

	為解決這個問題，你必須告訴鉛筆只能在滑鼠被點選_和_滑鼠的 y 座標大於 -120（`滑鼠的 y 座標`）時進行繪圖，語句如下所示：

	![screenshot](images/pencil-gt-code.png)

+ 測試你的專案，你現在應該無法在選擇器模組附近進行繪圖。

	![screenshot](images/paint-fixed.png)



