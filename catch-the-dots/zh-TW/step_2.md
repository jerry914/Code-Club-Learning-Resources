## 做個控制器

先創建一個控制器，玩家要使用這個控制器來收集點點。

\--- task \---

開啟 Catch the dots 這個範例專案。

**線上版：**你可以連結 [rpf.io/dots-on](http://rpf.io/dots-on){:target="_blank"} 以新建專案。

如果你有 Scratch 帳戶，你就可以直接**改編**專案。

**離線版：** 你可以點擊 [rpf.io/p/en/catch-the-dots-go](http://rpf.io/p/en/catch-the-dots-go){:target="_blank"} 以下載專案。

如果你需要 Scratch 離線版編輯器，可以連結到 [rpf.io/scratchoff](http://rpf.io/scratchoff){:target="_blank"}。

\--- /task \---

你應該會看到一個控制器的造型：

![截圖](images/dots-controller.png)

\--- task \---

為控制器寫個程式，在玩家按鍵盤的向右鍵時，控制器會向右旋轉。

![控制器角色](images/controller-sprite.png)

```blocks3
    當 @greenflag 被點擊
    重複無限次
        如果 < (向右 v)鍵被按下？> 那麼
            右轉 @turnright (3) 度
        end
    end
```

\--- /task \---

\--- task \---

測試你的程式。 當你按下向右鍵時，控制器應該會向右旋轉。

\--- /task \---

\--- task \---

在控制器上添加程式，讓玩家按向左鍵時，控制器會向左旋轉。

![控制器角色](images/controller-sprite.png)

\--- hints \---

\--- hint \---

是什麼程式在檢查向右鍵是否被按下，並讓角色向右旋轉的。 複製這個程式，把它改成檢查向左鍵是否被按下，並讓角色向左旋轉，如何，你做得到嗎？

\--- /hint \---

\--- hint \---

這裡是你需要的程式積木：

```blocks3
< (向左 v)鍵被按下？>

左轉 @turnright (3) 度

如果 <> 那麼
end
```

\--- /hint \---

\--- hint \---

你的程式看起來應該像這樣：

```blocks3
    當 @greenflag 被點擊
    重複無限次
        如果 < (向右 v)鍵被按下？> 那麼
            右轉 @turnright (3) 度
        end

+       如果 < (向左 v)鍵被按下？> 那麼
            左轉 @turnright (3) 度
       end 
    end
```

\--- /hint \---

\--- /hints \---

\--- /task \---