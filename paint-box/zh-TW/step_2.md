## 製作鉛筆

首先讓我們製作一支可用來在工作區繪圖的鉛筆。



+ 從 <a href="http://jumpto.cc/paint-go" target="_blank">jumpto.cc/paint-go</a> 線上開啟“顏料盒”Scratch 專案，如果你正使用離線編輯器，則從 <a href="http://jumpto.cc/paint-get" target="_blank">jumpto.cc/paint-get</a> 下載，然後開啟。

	你將會看到鉛筆和橡皮擦子圖：

	![screenshot](images/paint-starter.png)	

+ 由於你將使用滑鼠繪圖，因此你希望鉛筆能 `重複執行`{:class="blockcontrol"}跟隨滑鼠移動。向你的鉛筆子圖新增此程式碼：

	```blocks
		點選綠旗時
    重複無限次 
    定位到 [mouse pointer v] 位置
    end
	```

+ 通過點選旗幟然後在工作區四處移動滑鼠來測試此程式碼。 

+ 接下來，我們來讓你的鉛筆進行以下操作：`如果`{:class="blockcontrol"}滑鼠被點選，即進行繪圖。向你的鉛筆子圖新增此程式碼：

	![screenshot](images/paint-pencil-draw-code.png)	

+ 再次測試你的程式碼。這次，在工作區四處移動鉛筆並按住滑鼠按鈕。你能否使用你的鉛筆繪圖？

	![screenshot](images/paint-draw.png)
	



