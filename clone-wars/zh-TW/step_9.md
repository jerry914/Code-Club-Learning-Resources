## 還有宇宙蝙蝠

為了讓遊戲更有難度，你將創建一個向飛船扔橘子的蝙蝠。

![一隻蝙蝠朝飛船扔橘子](images/bat-oranges.png)

\--- task \---

在範例庫中找到 `Bat` 作為角色，重新命名成「蝙蝠」，然後把迴轉樣式設定成 **左-右**。

\--- /task \---

\--- task \---

讓`蝙蝠`在舞台最上方`移動`{:class="block3motion"}，讓它只能`不斷的`{:class="block3control"}左右平移。

![蝙蝠角色](images/bat-sprite.png)

```blocks3
當 @greenflag 被點擊
尺寸設為 (50) %
重複無限次
    移動 (10) 點
    碰到邊緣就反彈
end
```

別忘了要測試你的程式。

\--- /task \---

切換到蝙蝠角色的造型頁籤，你會發現牠有四種不同的造型：

![截圖](images/invaders-bat-costume.png)

\--- task \---

使用`造型換成下一個`{:class="block3looks"}積木，讓蝙蝠在移動時拍打翅膀。

\--- hints \---

\--- hint \---

蝙蝠每一次移動後，就把`造型換成下一個`{:class="block3looks"}然後`等待`{:class="block3control"}一小段時間。

\--- /hint \---

\--- hint \---

你會用到這些積木：

```blocks3
等待 (0.3) 秒

造型換成下一個
```

\--- /hint \---

\--- hint \---

你的程式應該會像這樣：

```blocks3
當 @greenflag 被點擊
尺寸設為 (50) %
重複無限次
移動 (10) 點
碰到邊緣就反彈

+ 造型換成下一個
+ 等待 (0.3) 秒
end
```

\--- /hint \---

\--- /hints \---

\--- /task \---

現在讓蝙蝠扔橘子！

\--- task \---

從範例庫中選取 `Orange` 當作角色，然後我們把它的名稱改成「橘子」。

![截圖](images/invaders-orange.png)

\--- /task \---

\--- task \---

為蝙蝠添加程式，在`點擊綠旗`{:class="block3events"}後，`蝙蝠`會`重複不斷的`{:class="block3control"}`等待`{:class="block3control"}一段`隨機`{:class="block3operators"}的時間，比方說 `5 到 10`{:class="block3operators"} 秒，然後開始創建`橘子`的`分身`{:class="block3control"}。

![蝙蝠角色](images/bat-sprite.png)

```blocks3
當 @greenflag 被點擊
重複無限次
    等待 (隨機取數 (5) 到 (10)) 秒
    建立 (橘子 v) 的分身
end
```

\--- /task \---

\--- task \---

為`橘子`寫個程式，在每次分身被建立時，就從`蝙蝠`的位置往下丟，直到橘子移動到舞台底部分身才刪除。

![橘子角色](images/orange-sprite.png)

```blocks3
    當 @greenflag 被點擊
    隱藏

    當分身產生
    定位到 (蝙蝠 v) 位置
    顯示
    重複直到 <碰到 (邊緣 v)？>
        y 改變 (-4)
    end
    分身刪除
```

\--- /task \---

\--- task \---

在`橘子`角色上多加個程式，讓`橘子`的分身在擊中`飛船`時，分身也會消失，讓玩家有機會重置：

![橘子角色](images/orange-sprite.png)

```blocks3
    當收到訊息 (被擊中 v)
    分身刪除
```

\--- /task \---

\--- task \---

修改`飛船`的程式，讓它在撞到`河馬`和`橘子`時都會「爆炸」：

![飛船角色](images/rocket-sprite.png)

```blocks3
    等待直到 <<碰到 (河馬 v)？> 或 <碰到 (蝙蝠 v)？>>
```

\--- /task \---

\--- task \---

測試你的遊戲，如果飛船被掉下來的橘子打到會怎樣？

\--- /task \---