## 收集小點

讓我們來新增一些小點，供玩家使用控制器收集。



+ 建立一個被稱作“紅色”的新子圖。此子圖應為一個紅色小點。

	![screenshot](images/dots-red.png)

+ 向你的“紅色”小點子圖新增此指令碼，從而每隔幾秒建立一個新的複製點：

	```blocks
		點選綠旗時
    隱藏
    等待 (2) 秒
    重複無限次 
      分身 [自己 v] 建立
      等待 (隨機取數 (5) 到 (10)) 秒
    end
	```

+ 建立每個複製點時，你想使其出現在工作區 4 個角中的一處。

	![screenshot](images/dots-start.png)

	為此，首先建立一個被稱作 `起始位置`{:class="blockdata"}的新列表，並點選 `(+)` 新增值 `-180` 和 `180`。

	![screenshot](images/dots-list.png)

+ 你可以使用這 2 個列表專案選擇工作區的任何一個角。向“小點”子圖新增此程式碼，使得每個新的複製點向一個隨機角移動，然後緩慢移向控制器。

	```blocks
		當分身產生
    當分身產生
    定位到 x: (連結串列第 (random v) 項專案\( [start positions v] \) :: list) y: (連結串列第 (random v) 項專案\( [start positions v] \) :: list)
    面朝 [controller v] 向
    顯示
    重複直到 <碰到 [controller v] ?> 
      移動 (1) 點
    end
	```

	上面的程式碼選擇 `-180` 或 `180` 作為 x _和_ y 座標，這意味著每個複製點起始於工作區的一個角。

+ 測試你的專案。你會看到大量紅色小點出現在畫面的各個角，並朝控制器緩慢移動。

	![screenshot](images/dots-red-test.png)

+ 建立 2 個被稱作 `生命`{:class="blockdata"} 和 `分數`{:class="blockdata"} 的新變數。

+ 向你的工作區新增程式碼以將遊戲開始時的 `生命`{:class="blockdata"} 設為 3， `分數`{:class="blockdata"} 設為 0。

+ 你需要向紅色小點的 `我作為複製點開始時`{:class="blockcontrol"} 程式碼的末端新增程式碼，這樣如果顏色匹配，則玩家的 `分數`{:class="blockdata"} 增加 1，如果顏色不匹配，則玩家減少 1 條 `生命`{:class="blockdata"}。

	```blocks
		移動 (5) 點
    移動 (5) 點
    如果 <碰到顏色 [#FF0000] ?> 那麼 
      變數 [score v] 改變 (1)
      播放音效 [pop v]

      變數 [lives v] 改變 (-1)
      播放音效 [laser1 v]
    end
    分身刪除
	```

+ 向你的工作區指令碼末端新增此程式碼，這樣在玩家失去所有生命時遊戲結束：

	```blocks
		等待直到 <(lives) < [1]>
    停止 [全部 v]
	```

+ 測試你的遊戲，以確保此程式碼按預期執行。



