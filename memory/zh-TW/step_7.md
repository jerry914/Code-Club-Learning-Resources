## 高分

讓我們來儲存高分，這樣你便能與你的朋友進行比賽。

+ 向你的專案新增兩個名為 `高分`{:class="blockdata"}和 `姓名`{:class="blockdata"}的新變數。

當遊戲因玩家猜錯序列而終止時，你需要檢查他們的分數是否高於當前的高分。如果是，你需要將該分數儲存為高分並儲存玩家的姓名。

+ 向你的玩家子圖新增程式碼來儲存高分。還要詢問玩家的姓名並將其記錄在 `姓名`{:class="blockdata"}變數中。

[[[generic-scratch-high-score]]]

--- hints ---
--- hint ---
你的新程式碼需要遵循以下邏輯：
`遊戲結束` 訊息播放後
`如果` 該 `分數` `>` `高分`
將 `高分` `設定` 為該 `分數`
`詢問` 玩家的姓名
將該 `姓名` `設定` 為 `回答`
--- /hint ---
--- hint ---
你將需要以下程式碼塊：

![Hint for high score](images/hint-high-score.png)

--- /hint ---
--- hint ---
按下紅色按鈕時，你的程式碼應如下所示：

```blocks
	當收到訊息 [red v]
  如果 <(item (1 v) of [sequence v] :: list) = [1]> 那麼 
   刪除第 (1 v) 項 \( [sequence v] \)

   說出 [Game over!] (1) 秒
   如果 <(score) > (high score)> 那麼 
    變數 [high score v] 設為 (score)
    詢問 [High score! What is your name?] 並等待
    變數 [name v] 設為 (詢問的答案)
   end
   停止 [全部 v]
 end
```
--- /hint ---
--- /hints ---

+ 你還將需要對其他三種顏色的角色子圖新增此新程式碼！你是否注意到了四種顏色中每一個的“遊戲結束”程式碼都完全相同嗎？

![screenshot](images/colour-same.png)

如果你需要更改此程式碼的任何一處，例如新增聲音或更改“遊戲結束”訊息，你需要更改四次。這可能會很煩人，並浪費大量時間。

不過，你可以定義你自己的程式碼塊，並在你的專案中重複使用。為此，請點選 `更多程式碼塊`{:class="blockmoreblocks"}，然後點選**製作程式碼塊**。將這個新程式碼塊稱為“遊戲結束”。

![screenshot](images/colour-more.png)

+ 向你建立的程式碼塊新增紅色按鈕相關的 `否則`{:class="blockcontrol"}程式碼塊中的程式碼：

![screenshot](images/colour-make-block.png)

+ 你現在已經編寫了名為 `遊戲結束`{:class="blockmoreblocks"}的新_函式_，並且你可以用在任何地方。將你的新 `遊戲結束`{:class="blockmoreblocks"}程式碼塊拖到按鈕的四個指令碼上。

![screenshot](images/colour-use-block.png)

+ 現在新增一個在按錯按鈕時發出的聲音。你僅需要在你編寫的 `遊戲結束`{:class="blockmoreblocks"}程式碼塊中新增一次此程式碼，無需分別新增四次！

![screenshot](images/colour-cough.png)
