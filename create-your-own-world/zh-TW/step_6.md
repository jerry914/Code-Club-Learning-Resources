## 告示牌

現在為你的世界添加一些告示牌，引導玩家探索這個世界。

材料包裡已經有個`告示牌`角色了：

![截圖](images/world-sign.png)

\--- task \---

這個`歡迎告示牌`角色應該只會在空間 1 出現，所以我們要添加一些程式：

\--- hints \---

\--- hint \---

`在點擊綠旗時`{:class="block3events"}，`重複不斷`{:class="block3control"}的檢查`所在的空間`{:class="block3variables"}`是不是`{:class="block3control"}空間1，如果是就`顯示`{:class="block3looks"}`歡迎告示牌`，`否則`{:class="block3control"}就`隱藏`{:class="block3looks"}。

\--- /hint \---

\--- hint \---

這裡是你需要的程式積木：

![告示牌](images/sign.png)

```blocks3
<br />如果 <> 那麼
否則
end

<(空間 :: variables) = (1)>

隱藏

顯示

重複無限次
end

當 @greenflag 被點擊

```

\--- /hint \---

\--- hint \---

以下是完整的程式：

![告示牌](images/sign.png)

```blocks3
當 @greenflag 被點擊
重複無限次
    如果 <(空間 :: variables) = (1)> 那麼
        顯示
    否則
        隱藏
    end
end
```

\--- /hint \---

\--- /hints \---

\--- /task \---

\--- task \---

測試在`歡迎告示牌`角色的程式是否正確，你要在兩個空間走動。 告示牌只會出現在空間1這個背景。

![截圖](images/world-sign-test.png)

\--- /task \---

\--- task \---

告示牌啥事都不告訴你，也太遜了對吧？！ 添加一些程式，如果`歡迎告示牌`被`玩家`碰到了，就顯示一些訊息：

![告示牌](images/sign.png)

```blocks3
當 @greenflag 被點擊
重複無限次
如果 <(空間 :: variables) = (1)> 那麼
顯示
否則
隱藏
end
+ 如果 <碰到 (玩家 v)？ > 然後
說出 (歡迎！ 你能得到寶藏嗎？)
否則
說出 ()
end
end
```

\--- /task \---

\--- task \---

再次測試你的`歡迎告示牌`， 當`玩家`碰觸`歡迎告示牌`角色時，你應該會看到一段訊息。

![截圖](images/world-sign-test2.png)

\--- /task \---