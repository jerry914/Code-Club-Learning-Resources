## 收集金幣

讓`玩家`角色能夠在你的世界四處找尋並收集金幣。

\--- task \---

添加一個新的變數到專案，名為`金幣`{:class="block3variables"}。

\--- /task \---

\--- task \---

選擇`金幣`角色，然後在角色面版選擇**顯示**。

![截圖](images/coin.png)

\--- /task \---

\--- task \---

為`金幣`角色寫個程式，讓它只出現在空間1裡頭。

![截圖](images/coin.png)

```blocks3
當 @greenflag 被點擊
重複無限次
如果 <(空間 :: variables) = (1)> 那麼
顯示
否則
隱藏
end
```

\--- /task \---

\--- task \---

再添加一些程式到`金幣`角色，`玩家`只要碰到`金幣`角色就可以把它收集起來，金幣就會`消失不見`{:class="block3looks"}，然後`金幣`{:class="block3variables"}的收集數就會加 `1`{:class="block3variables"}。

![金幣](images/coin.png)

```blocks3
當 @greenflag 被點擊
等待直到 <碰到 (玩家 v)？>
變數 [金幣 v] 改變 (1)
隱藏
停止 [這個物件的其它程式 v]
```

`停止這個物件的其它程式`{:class="block3control"}這個積木是很重要的，它可以讓`金幣`在被收集後不再出現在空間1裡。

\--- /task \---

\--- task \---

接著要添加的程式，是要讓初始化遊戲的金幣數，也就是讓`金幣`{:class="block3variables"}這個變數在每次遊戲開始重新設定回 `0`{:class="block3variables"}。

![舞台](images/stage.png)

```blocks3
當 @greenflag 被點擊
變數 [金幣 v] 設為 (0)
```

\--- /task \---

\--- task \---

測試你的遊戲。 收集金幣時，`金幣`數應該會變成 `1`{:class="block3variables"}。

\--- /task \---