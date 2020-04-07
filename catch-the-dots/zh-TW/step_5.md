## 增加難度

現在，你要讓困難度隨著玩家遊戲時間變長而提高。 你可以藉由點點出現的頻率來提高難度。

\--- task \---

建立一個新的`變數`{:class="block3variables"}，命名為「延遲」。

![舞台角色](images/stage-sprite.png)

\--- /task \---

\--- task \---

移至舞台的程式區，然後寫個新程式，先設定`延遲`{:class="block3variables"} 變數為 `8`，然後在遊戲運行過程中慢慢的減少`延遲`{:class="block3variables"}的值。

![舞台角色](images/stage-sprite.png)

```blocks3
    當 @greenflag 被點擊
    變數 [延遲 v] 設為 (8)
    重複直到 <(延遲) = (2)>
        等待 (10) 秒
        變數 [延遲 v] 改變 (-0.5)
    end
```

\--- /task \---

記得嗎？這個程式和先前創建倒數計時器所使用的程式十分類似！

接下來，在紅點、黃點、藍點角色的程式中使用`延遲`{:class="block3variables"}變數。

\--- task \---

移除原來在建立分身之後等待隨機秒數的程式。 把等待的秒數改成`延遲`{:class="block3variables"}變數：

![截圖](images/all-dots.png)

```blocks3
<br />-   等待 (隨機取數 (5) 到 (10)) 秒
等待 (延遲 :: variables) 秒
```

注意三個點點角色都要替換。

\--- /task \---

\--- task \---

測試遊戲，檢查隨著遊戲時間的增加，點點是否更快的出現。

+ 這對三個顏色的點點都有效嗎？
+ 確定`延遲`{:class="block3variables"}變數的值變得愈來愈小了嗎？

\--- /task \---