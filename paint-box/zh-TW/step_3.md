## 彩筆

讓我們向你的專案新增不同顏色的畫筆，並允許使用者在它們之間進行選擇！



+ 點選你的鉛筆子圖，點選“造型”並複製你的“藍色鉛筆”造型。

	![screenshot](images/paint-blue-duplicate.png)

+ 將你的新造型重新命名為“綠色鉛筆”，然後將鉛筆顏色變為綠色。

	![screenshot](images/paint-pencil-green.png)

+ 建立兩個新子圖，你將使用它們來選擇藍色或綠色鉛筆。

	![screenshot](images/paint-selectors.png)

+ 點選綠色選擇器圖示時，你需要向鉛筆子圖 `廣播`{:class="blockevents"}一條訊息，告訴它更改自身造型和鉛筆顏色。

	為此，首先向綠色選擇器圖示新增此程式碼：

	```blocks
		當角色被點選
    廣播訊息 [green v]
	```

	為建立 `廣播`{:class="blockevents"}程式碼塊，點選下箭頭並選擇“新訊息...”。

	![screenshot](images/paint-broadcast.png)

	隨後，你可以輸入“綠色”來建立你的新訊息。

	![screenshot](images/paint-green-message.png)

+ 現在你需要告訴你的鉛筆子圖在收到訊息時做什麼。向你的鉛筆子圖新增此程式碼：

	```blocks
		當收到訊息 [green v]
    造型換成 [pencil-green v]
    筆跡顏色設為 [#00ff00]
	```

	要將鉛筆顏色設為綠色，請點選 `設定顏色`{:class="blockpen"}程式碼塊中的彩色盒子，然後點選綠色選擇器圖示來選擇綠色作為你的鉛筆顏色。

+ 你現在可以對藍色鉛筆圖示進行同樣操作，將此程式碼新增到藍色選擇器子圖：

	```blocks
		當角色被點選
    廣播訊息 [blue v]
	```

	...並向鉛筆子圖新增此程式碼：

	```blocks
		當收到訊息 [blue v]
    造型換成 [pencil-blue v]
    筆跡顏色設為 [#0000ff]
	```

+ 最後，你需要告訴你的鉛筆子圖選擇何種造型和鉛筆顏色，以及在專案開始時清空畫面。向鉛筆 `當綠色旗幟被點選`{:class="blockevents"}程式碼（在 `重複執行`{:class="blockcontrol"}迴圈之前）的開頭新增此程式碼：

	```blocks
		筆跡清除
    造型換成 [blue-pencil v]
    筆跡顏色設為 [#0000ff]
	```

	如果你樂意，你可以使用一個不同顏色的鉛筆開始！

+ 測試你的專案。你能否在藍色和綠色畫筆之前切換？

	![screenshot](images/paint-pens-test.png)



