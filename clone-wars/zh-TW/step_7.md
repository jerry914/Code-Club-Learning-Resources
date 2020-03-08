## 太空河馬走囉

在飛船爆炸時，所有的河馬都應該撤退，這樣玩家才有機會捲土重來。

\--- task \---

添加程式到飛船裡，讓它在`碰到河馬`{:class="block3sensing"}時，`廣播`{:class="block3events"}「被擊中」的訊息。

![飛船角色](images/rocket-sprite.png)

```blocks3
當 @greenflag 被點擊
造型換成 (正常 v)
等待直到 <碰到 (河馬 v)？>
造型換成 (爆炸 v)

+ 廣播訊息 (被擊中 v)
```

\--- /task \---

\--- task \---

`河馬`和它的所有分身都會收到「被擊中」的訊息，你就可以讓收到訊息的`河馬`大軍撤退囉：

![河馬角色](images/hippo-sprite.png)

```blocks3
當收到訊息 (被擊中 v)
分身刪除
```

\--- /task \---

\--- task \---

檢查新程式，點擊綠旗後讓飛船和其中一隻河馬分身撞在一起，看看是不是如預期那樣的運作。

![截圖](images/invaders-hippo-collide.png)

\--- /task \---

飛船爆炸後，新的`河馬`分身還是不斷來襲，我們需要在爆炸後讓飛船有時間自我修復。

\--- task \---

在`飛船`角色的程式最後面添加`等待`{:class="block3control"}積木，在河馬再次入侵前有一小段暫停的時間。 接著，用`重複無限次`{:class="block3control"}積木包住程式，讓程式不斷的重複執行。

![飛船角色](images/rocket-sprite.png)

```blocks3
當 @greenflag 被點擊
造型換成 (正常 v)
等待直到 <碰到 (河馬 v)？>
造型換成 (爆炸 v)
廣播訊息 (被擊中 v)

+ 等待 (1) 秒
end
```

\--- /task \---