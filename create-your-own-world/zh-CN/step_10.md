## 收集硬币

你的 `玩家` 子图在探索世界的同时，还可以收集硬币。

+ 向你的项目添加一个名为 `硬币`{:class="blockdata"}的新变量。

+ 右键点击 `硬币` 子图并选择 **显示**。

![screenshot](images/world-coins.png)

+ 向你的 `硬币` 子图添加代码使其仅出现在房间 1 内。

+ 向你的 `硬币` 子图添加代码，从而在 `玩家` 子图触碰到 `硬币` 子图将其“拾取”时，`硬币`{:class="blockdata"}变量便会增加 `1`。

	```blocks
		点击绿旗时
    点击绿旗时
    等待直到 <碰到 [player v] ?>
    变量 [coins v] 改变 (1)
    停止 [角色的其他程序 v]
    隐藏
	```

	需要 `停止子图中的其他脚本`{:class="blockcontrol"} 代码，这样在收集硬币后，`硬币` 子图将停止在房间 1 中显示。

+ 你还将需要添加代码。以在游戏开始时将你的 `硬币`{:class="blockdata"}变量设为 `0`。

+ 测试你的项目 — 收集一枚硬币应使你的 `硬币` 数量变为 `1`。

--- challenge ---
### 挑战：更多硬币
你能否向你的游戏添加更多硬币？硬币可以分布在不同的房间，一些硬币甚至可由巡逻的敌人看守！

--- /challenge ---
