## 高分

讓我們來儲存高分，使玩家能瞭解他們的成績有多好。



+ 建立一個被稱作 `高分`{:class="blockdata"} 的新變數。

+ 在你的工作區上點選，並建立一個被稱作 `檢視高分`{:class="blockmoreblocks"} 的新自定義模組。

	![screenshot](images/dots-custom-1.png)

+ 在遊戲結束之前，加入你的新自定義模組。

	![screenshot](images/dots-custom-2.png)

+ 向你的自定義模組新增程式碼， `如果`{:class="blockcontrol"} 當前分數是到目前為止為最高分，則將該 `分數`{:class="blockdata"} 儲存為 `高分`{:class="blockdata"}： 

	```blocks
		定義 (check high score)
    如果 <(score) > (high score)> 那麼 
      變數 [high score v] 設為 (score)
    end
	```

+ 測試你所新增的程式碼。玩你的遊戲來檢查 `高分`{:class="blockdata"} 是否已正確更新。



