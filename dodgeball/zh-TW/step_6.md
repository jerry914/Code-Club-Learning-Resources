## 躲避球

現在你已經使你的角色能夠四處移動，讓我們為你的角色新增一些需要躲避的小球。



+ 建立一個新的小球子圖。你可以選擇任何你喜歡的小球型別。

	![screenshot](images/dodge-balls.png)

+ 重新設定你的小球尺寸，使你的角色能跳過去。試著跳過小球以對其進行測試。 

	![screenshot](images/dodge-ball-resize.png)

+ 向你的小球新增以下程式碼：

	![screenshot](images/dodge-ball-motion.png)

	此程式碼每 3 秒建立一個新的小球克隆體。每個新的小球克隆體都沿頂部平臺移動。

+ 點選旗幟以進行測試。

	![screenshot](images/dodge-ball-test.png)

+ 向你的小球子圖新增更多程式碼，使其跨越所有的 3 個平臺。

	![screenshot](images/dodge-ball-more-motion.png)

+ 最終，你將需要你的角色被小球擊中時的程式碼！向你的小球子圖新增此程式碼：

	```blocks
		當分身產生
    重複無限次 
      如果 <碰到 [Pico walking v] ?> 那麼 
        廣播訊息 [hit v]
      end
    end
	```

+ 你還需要向你的角色新增程式碼，使其在被擊中時返回起始位置：

	```blocks
		當收到訊息 [hit v]
    面朝 (90 v) 度
    定位到 x: (-210) y: (-120)
	```	

+ 測試你的角色，看看它們是否會在被小球擊中時返回起始位置。



