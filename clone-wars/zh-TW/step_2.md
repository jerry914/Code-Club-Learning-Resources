## 建造太空船

先來製造一艘可以保衛地球的宇宙飛船！

\--- task \---

開啟 Clone wars 這個範例專案。

**線上版：**你可以連結 [rpf.io/clone-wars-on](http://rpf.io/clone-wars-on){:target="_blank"} 以新建專案。

如果你有 Scratch 帳戶，你就可以直接**改編**專案。

**離線版：** 你可以點擊 [rpf.io/p/en/clone-wars-go](http://rpf.io/p/en/clone-wars-go){:target="_blank"} 以下載專案。

如果你需要 Scratch 離線版編輯器，可以連結到 [rpf.io/scratchoff](https://rpf.io/scratchoff){:target="_blank"}。

\--- /task \---

![初始專案](images/starter-project.png)

\--- task \---

為飛船編寫程式，讓它可以在按下<kbd>向左</kbd>鍵時，跟著往左移動：

![飛船角色](images/rocket-sprite.png)

```blocks3
    當 @greenflag 被點擊
    重複無限次
        如果 < (向左 v)鍵被按下？> 那麼
            x 改變 (-4)
        end
    end
```

x 軸指的是舞台的水平方向（左到右側）的位置。 如果你把飛船角色的 x 座標減小，它就會往左移動。 下方的這個積木就是讓飛船往左平移的關鍵：

```blocks3
x 改變 (-4)
```

\--- /task \---

\--- task \---

再添加一些程式到`重複無限次`{:class="block3control"}裡頭，讓飛船能在輸入<kbd>向右</kbd>鍵時往右平移。

\--- hints \---

\--- hint \---

把飛船在 `x` 的位置減去 `4` 可以讓它往左移動，那要怎樣讓飛船往右移動 `4` 點呢？

\--- /hint \---

\--- hint \---

你需要的積木是一樣的，但是給定的數字不同：

```blocks3
x 改變 ()
```

\--- /hint \---

\--- hint \---

這是你要在`重複無限次`{:class="block3control"}迴圈裡要添加的程式：

![飛船角色](images/rocket-sprite.png)

```blocks3
如果 < (向右 v)鍵被按下？> 那麼
    x 改變 (4)
end
```

\--- /hint \---

\--- /hints \---

\--- /task \---

\--- task \---

點擊綠旗開始測試你的專案，看看你能不能用方向鍵讓飛船往左或往右水平移動。

\--- /task \---