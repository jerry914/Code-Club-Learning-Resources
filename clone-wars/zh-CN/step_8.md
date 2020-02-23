## 果蝠

为使游戏难度增加，让我们来制作一种向宇宙飞船扔橙子的果蝠。

+ 添加一个 `蝙蝠` 子图，并将其旋转方式设为仅 **左右**旋转。

+ 使 `蝙蝠` 子图 `永远`{:class="blockcontrol"}横跨工作区顶部从一边向另一边 `移动`{:class="blockmotion"}。请记得测试你的代码。

![screenshot](images/invaders-bat.png)

--- hints ---
--- hint ---
点击旗帜时，`蝙蝠` 子图应永远
- 移动 10 步
- 如果它到达边缘，则返回
--- /hint ---
--- hint ---
以下是你将需要的代码：

```blocks
点击绿旗时
重复无限次 
  移动 (10) 点
  碰到边缘就反弹
end
```
--- /hint ---
--- /hints ---

如果你观察蝙蝠的造型，你会发现它已经具备两种不同的造型：

![screenshot](images/invaders-bat-costume.png)

+ 运用 `下一个造型`{:class="blocklooks"}代码块来使蝙蝠边移动边扇动翅膀。

--- hints ---
--- hint ---
蝙蝠移动以后，就会显示 `下一个造型`{:class="blocklooks"}，然后稍微 `等待`{:class="blockcontrol"}一会。
--- /hint ---
--- hint ---
以下是你将需要的代码：

```blocks
造型换成下一个
等待 (0.3) 秒
```
--- /hint ---
--- hint ---
以下为已添加新代码的完整代码：

```blocks
点击绿旗时
重复无限次 
  移动 (10) 点
  碰到边缘就反弹
  造型换成下一个
  等待 (0.3) 秒
end
```
--- /hint ---
--- /hints ---

现在我们来让蝙蝠扔橙子。

+ 从 Scratch 库中添加新的 `橙子` 子图。

![screenshot](images/invaders-orange.png)

+ 向你的蝙蝠添加代码，使得点击旗帜时，其等待 5 至 10 秒间的任意时间，然后创建一个 `橙子` 子图的克隆体。

--- hints ---
--- hint ---
查看你在创建 `闪电` 子图时所写的代码。你现在需要的代码与其十分相似，但橙子并不是在你按下**空格**键时出现的，而是在你 `等待`{:class="blockcontrol"}`5-10`{:class="blockoperators"}秒钟之后出现的。
--- /hint ---
--- hint ---
`点击旗帜时`{:class="blockcontrol"}，`蝙蝠` 子图应
`永远`{:class="blockcontrol"}
- `等待`{:class="blockcontrol"}`5-10`{:class="blockoperators"}秒之间的 `任意`{:class="blockoperators"}时间
- 为 `橙子` 子图 `创建一个克隆体`{:class="blockcontrol"}
--- /hint ---
--- hint ---
以下是你将需要的代码：

```blocks
点击绿旗时
重复无限次 
  等待 (随机取数 (5) 到 (10)) 秒
  分身 [Orange v] 建立
end
```
--- /hint ---
--- /hints ---

+ 点击你的 `橙子` 子图并添加一些代码，使每个 `橙子` 子图克隆体下降，从 `蝙蝠` 子图开始朝工作区底部降落。

--- hints ---
--- hint ---
你需要的此代码与 `闪电` 子图内部的代码几乎相同，但 `橙子` 子图应 `前往`{:class="blockmotion"} `蝙蝠` 子图的位置，并且其应该使用 `改变 y 坐标`{:class="blockcontrol"}代码块来向下移动，而非向上。
--- /hint ---
--- hint ---
以下是你将需要的代码：

```blocks
	点击绿旗时
隐藏

当分身产生
定位到 [Bat1 v] 位置
显示
重复直到 <碰到 [边缘 v] ?> 
  y 改变 (-4)
end
分身删除

```
--- /hint ---
--- /hints ---


+ 向 `橙子` 子图添加更多代码，使得 `宇宙飞船` 子图在受撞击时，它也会消失，并给玩家一个复位的机会：

```blocks
	当收到消息 [hit v]
  分身删除
```

+ 你还需要修改你的 `宇宙飞船` 子图中的代码，使其在碰到 `河马` 子图或 `橙子` 子图时受撞击：

```blocks
	等待直到 <<碰到 [Hippo1 v] ?> 或 <碰到 [Orange v] ?>>
```

+ 测试你的游戏。如果你被一个掉落的橙子击中会发生什么？
