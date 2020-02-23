## 多个等级

目前为止，玩家仅需记住五种颜色的序列。让我们通过添加得分和添加代码使玩家需要记住的序列长度随着玩家得分增加而变得越长，以此完善游戏。

+ 创建一个名为 `分数`{:class="blockdata"}的新变量。

[[[generic-scratch-add-variable]]]

`分数`{:class="blockdata"}将被用来决定玩家需要记住的序列长度。让我们从得分（和序列长度） `3` 开始。

+ 在你角色的 `当绿色旗帜被点击`{:class="blockevents"}代码的开头添加一个代码块来将 `分数`{:class="blockdata"}设为 `3`。

现在，你希望 `分数`{:class="blockdata"}来决定序列长度，而非总是创建一个五种颜色的序列。

+ 将角色的 `重复执行`{:class="blockcontrol"}循环（适用于创建序列）更改为重复执行 `分数`{:class="blockdata"}次：

```blocks
	重复 (score) 次
  end
```

+ 如果猜对了序列，你应该将分数增加 `1` 来增加下一个序列的长度。__在你知道猜对序列的时候__，向角色的代码添加此代码块。

```blocks
  变量 [score v] 改变 (1)
```

--- hints ---
--- hint ---
当你广播 `胜利` 消息时，你就知道猜对序列了。
--- /hint ---
--- /hints ---

+ 最后，你需要在生成序列的代码周围添加 `重复执行`{:class="blockcontrol"}循环，使得每个等级都创建一个新的序列。你的角色代码可能如下所示：

	```blocks
		点击绿旗时
    变量 [score v] 设为 [3]
    重复无限次 
     删除第 (全部 v) 项 \( [sequence v] \)
     重复 (score) 次 
      新增项目 (随机取数 (1) 到 (4)) \( [sequence v] \)
      造型换成 (链表第 (last v) 项项目\( [sequence v] \) :: list)
      等待 (1) 秒
    end
    等待直到 <(length of [sequence v] :: list) = [0]>
    广播消息 [won v] 并等待
    变量 [score v] 改变 (1)
    end
	```

+ 请你的朋友们来测试你的游戏。请记得在他们开始游戏之前隐藏 `序列`{:class="blockdata"}列表！
