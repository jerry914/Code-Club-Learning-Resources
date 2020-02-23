## 消失的河马

当宇宙飞船受到撞击时，所有的河马都应消失，并给玩家一个复活机会。

+ 向你的代码添加一个代码块，使宇宙飞船在碰到河马时 `广播` “撞击”消息。

[[[generic-scratch-broadcast-message]]]

--- hints ---
--- hint ---
从 **事件** 选项卡拖出代码块，然后点击下拉菜单并选择 **新消息** 来创建一个 `广播` “撞击”代码块。
--- /hint ---
--- hint ---
你的代码块应如下所示：
```blocks
broadcast [hit v]
```
--- /hint ---
--- hint ---
你的代码应如下所示：

```blocks
点击绿旗时
造型换成 [normal v]
等待直到 <碰到 [Hippo1 v] ?>
造型换成 [hit v]
广播消息 [hit v]
```
--- /hint ---
--- /hints ---

所有的 `河马` 子图克隆体都会收到此消息，因此你现在可以指示它们在宇宙飞船受到撞击时消失。

+ 向 `河马` 子图添加此代码：

```blocks
当收到消息 [hit v]
分身删除
```

+ 开始一局新游戏并故意与一只河马相撞来测试此代码。

![screenshot](images/invaders-hippo-collide.png)

你受到撞击后，河马开始重新出现，但宇宙飞船仍然爆炸了！我们来让宇宙飞船能够在受到撞击后自行复位。

+ 在你所有的代码周围添加 `永远`{:class="blockcontrol"}代码块来重复流程，在末端添加 `等待`{:class="blockcontrol"}代码块以在河马开始再次出现之前添加短暂的停顿。

```blocks
点击绿旗时
重复无限次 
  造型换成 [normal v]
  等待直到 <碰到 [Hippo1 v] ?>
  造型换成 [hit v]
  广播消息 [hit v]
  等待 (1) 秒
end
```

--- challenge ---
### 挑战：生命和分数

玩家此时具备无数条生命。你能否向你的游戏添加 `生命`{:class="blockdata"}、`分数`{:class="blockdata"}甚至 `高分`{:class="blockdata"}代码块？

[[[generic-scratch-high-score]]]
--- /challenge ---
