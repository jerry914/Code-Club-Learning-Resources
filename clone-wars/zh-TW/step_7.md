## 消失的河馬

當宇宙飛船受到撞擊時，所有的河馬都應消失，並給玩家一個復活機會。

+ 向你的程式碼新增一個程式碼塊，使宇宙飛船在碰到河馬時 `廣播` “撞擊”訊息。

[[[generic-scratch-broadcast-message]]]

--- hints ---
--- hint ---
從 **事件** 選項卡拖出程式碼塊，然後點選下拉選單並選擇 **新訊息** 來建立一個 `廣播` “撞擊”程式碼塊。
--- /hint ---
--- hint ---
你的程式碼塊應如下所示：
```blocks
broadcast [hit v]
```
--- /hint ---
--- hint ---
你的程式碼應如下所示：

```blocks
點選綠旗時
造型換成 [normal v]
等待直到 <碰到 [Hippo1 v] ?>
造型換成 [hit v]
廣播訊息 [hit v]
```
--- /hint ---
--- /hints ---

所有的 `河馬` 子圖克隆體都會收到此訊息，因此你現在可以指示它們在宇宙飛船受到撞擊時消失。

+ 向 `河馬` 子圖新增此程式碼：

```blocks
當收到訊息 [hit v]
分身刪除
```

+ 開始一局新遊戲並故意與一隻河馬相撞來測試此程式碼。

![screenshot](images/invaders-hippo-collide.png)

你受到撞擊後，河馬開始重新出現，但宇宙飛船仍然爆炸了！我們來讓宇宙飛船能夠在受到撞擊後自行復位。

+ 在你所有的程式碼周圍新增 `永遠`{:class="blockcontrol"}程式碼塊來重複流程，在末端新增 `等待`{:class="blockcontrol"}程式碼塊以在河馬開始再次出現之前新增短暫的停頓。

```blocks
點選綠旗時
重複無限次 
  造型換成 [normal v]
  等待直到 <碰到 [Hippo1 v] ?>
  造型換成 [hit v]
  廣播訊息 [hit v]
  等待 (1) 秒
end
```

--- challenge ---
### 挑戰：生命和分數

玩家此時具備無數條生命。你能否向你的遊戲新增 `生命`{:class="blockdata"}、`分數`{:class="blockdata"}甚至 `高分`{:class="blockdata"}程式碼塊？

[[[generic-scratch-high-score]]]
--- /challenge ---
