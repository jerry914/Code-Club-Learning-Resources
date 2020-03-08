## 太空河馬來啦

現在，你要加入試圖破壞飛船的太空河馬大軍。

\--- task \---

使用範例庫中的 Hippo1 作為新角色，用圖像編輯器的工具把它**縮小**一點，重新命名為`河馬`，和`飛船`的尺寸差不多就行了。

![截圖](images/invaders-hippo.png)

\--- /task \---

\--- task \---

把`河馬`的迴轉方式設定成**左-右**。

[[[generic-scratch3-sprite-rotation-style]]]

\--- /task \---

\--- task \---

寫個程式，讓`河馬`在遊戲啟動前先藏起來。

![河馬角色](images/hippo-sprite.png)

```blocks3
當 @greenflag 被點擊
隱藏
```

\--- /task \---

\--- task \---

在舞台上寫個程式，讓`河馬`大軍不斷襲擊飛船，每隔幾秒鐘，就有河馬分身出現。

\--- hints \---

\--- hint \---

在`點擊綠旗`{:class="block3events"}後，`重複不斷`{:class="block3control"}的`等個`{:class="block3control"}`2 到 4 秒的時間`{:class="block3operators"}就`建立河馬的分身`{:class="block3control"}。

\--- /hint \---

\--- hint \---

這裡是你需要的程式積木：

```blocks3
重複無限次
end

建立 (河馬 v) 的分身

隨機取數 (2) 到 (4)

當 @greenflag 被點擊

等待 () 秒
```

\--- /hint \---

\--- hint \---

你的程式看起來應該像這樣：

![舞台角色](images/stage-sprite.png)

```blocks3
當 @greenflag 被點擊
重複無限次
    等待 (隨機取數 (2) 到 (4)) 秒
    建立 (河馬 v) 的分身
end
```

\--- /hint \---

\--- /hints \---

\--- /task \---

每次有新的河馬分身時，應該出現在舞台頂部隨機的一個`水平`位置，而且每個分身都應該有自己的速度。

\--- task \---

建立一個名為`速度`{：class =“block3variables”}的新變數，只有`河馬`能使用這個變數。

[[[generic-scratch3-add-variable]]]

如果你的操作正確，變數旁邊會附加角色的名稱，如下所示：

![截圖](images/invaders-var-test.png)

\--- /task \---

\--- task \---

當每次`河馬`分身產生時，就給它一個隨機的速度還有初始位置，接著在畫面上出現。

```blocks3
當分身產生
變數 [速度 v] 設為 (隨機取數 (2) 到 (4))
定位到 x:(隨機取數 (-220) 到 (220)) y:(150)
顯示
```

\--- /task \---

\--- task \---

測試你的程式，是不是每隔幾秒就有隻新的河馬分身出現？

\--- /task \---

不過目前河馬是不會動的。

\--- task \---

每個河馬分身應該要隨機的移動，除非它被飛船發射的雷電擊中，要實現的話，請把以下程式安排到`河馬`現有程式的最後：

```blocks3
重複直到 <碰到 (閃電 v)？>
    移動 (速度 :: variables) 點
    右轉 @turnright (隨機取數 (-10) 到 (10)) 度
    碰到邊緣就反彈
end
分身刪除
```

\--- /task \---

\--- task \---

再次測試你的程式，你應該會看到，每隔幾秒就出現一個新的河馬分身，而分身會以不同的速度移動。

\--- no-print \---

![截圖](images/hippo-clones.gif)

\--- /no-print \---

\--- /task \---

\--- task \---

現在試試宇宙飛船的雷電炮，如果發射的閃電擊中河馬，河馬會消失嗎？

\--- /task \---