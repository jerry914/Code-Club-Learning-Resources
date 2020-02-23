## 多個等級

目前為止，玩家僅需記住五種顏色的序列。讓我們通過新增得分和新增程式碼使玩家需要記住的序列長度隨著玩家得分增加而變得越長，以此完善遊戲。

+ 建立一個名為 `分數`{:class="blockdata"}的新變數。

[[[generic-scratch-add-variable]]]

`分數`{:class="blockdata"}將被用來決定玩家需要記住的序列長度。讓我們從得分（和序列長度） `3` 開始。

+ 在你角色的 `當綠色旗幟被點選`{:class="blockevents"}程式碼的開頭新增一個程式碼塊來將 `分數`{:class="blockdata"}設為 `3`。

現在，你希望 `分數`{:class="blockdata"}來決定序列長度，而非總是建立一個五種顏色的序列。

+ 將角色的 `重複執行`{:class="blockcontrol"}迴圈（適用於建立序列）更改為重複執行 `分數`{:class="blockdata"}次：

```blocks
	重複 (score) 次
  end
```

+ 如果猜對了序列，你應該將分數增加 `1` 來增加下一個序列的長度。__在你知道猜對序列的時候__，向角色的程式碼新增此程式碼塊。

```blocks
  變數 [score v] 改變 (1)
```

--- hints ---
--- hint ---
當你廣播 `勝利` 訊息時，你就知道猜對序列了。
--- /hint ---
--- /hints ---

+ 最後，你需要在生成序列的程式碼周圍新增 `重複執行`{:class="blockcontrol"}迴圈，使得每個等級都建立一個新的序列。你的角色程式碼可能如下所示：

	```blocks
		點選綠旗時
    變數 [score v] 設為 [3]
    重複無限次 
     刪除第 (全部 v) 項 \( [sequence v] \)
     重複 (score) 次 
      新增專案 (隨機取數 (1) 到 (4)) \( [sequence v] \)
      造型換成 (連結串列第 (last v) 項專案\( [sequence v] \) :: list)
      等待 (1) 秒
    end
    等待直到 <(length of [sequence v] :: list) = [0]>
    廣播訊息 [won v] 並等待
    變數 [score v] 改變 (1)
    end
	```

+ 請你的朋友們來測試你的遊戲。請記得在他們開始遊戲之前隱藏 `序列`{:class="blockdata"}列表！
