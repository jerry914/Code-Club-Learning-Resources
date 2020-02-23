## 建立一個控制器

讓我們從建立一個控制器開始，控制器將用來收集小點。



+ 從 <a href="http://jumpto.cc/dots-go" target="_blank">jumpto.cc/dots-go</a> 線上開啟“接住小點”Scratch 專案，如果你正使用離線編輯器，則從 <a href="http://jumpto.cc/dots-get" target="_blank">jumpto.cc/dots-get</a> 下載，然後開啟。

	你會看到一個控制器子圖：

	![screenshot](images/dots-controller.png)
	
	
+ 按下右箭頭鍵時使你的控制器右轉：

	```blocks
		點選綠旗時
    重複無限次 
      如果 <[右移 v] 鍵被按下？> 那麼 
        轉動CW (3) 度
      end
    end
	```
+ 測試你的控制器 -- 它應該轉向右邊。



