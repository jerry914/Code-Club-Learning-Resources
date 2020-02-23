## 对你的世界进行编码

我们来让 `玩家` 子图穿过房门进入其他房间。

你的项目包含其他房间的背景：

![screenshot](images/world-backdrops.png)

+ 创建一个名为 `房间`{:class="blockdata"}的“适用所有子图”的新变量，来追踪 `玩家` 子图所在的房间。

[[[generic-scratch-add-variable]]]

![screenshot](images/world-room.png)

+ 当 `玩家` 子图碰到第一个房间的橙色房门时，应显示下一个背景，然后 `玩家` 子图应返回工作区的左边。将此代码添加进 `玩家` 子图的 `永远`{:class="blockcontrol"}循环：

```blocks
	如果 <碰到颜色 [#F2A24A] ?> 那么 
    背景换成 [next backdrop v]
    定位到 x: (-200) y: (0)
    变量 [room v] 改变 (1)
  end
```

+ 向你的 `玩家` 子图代码（`永远`{:class="blockcontrol"}循环上方）的**开头**添加此代码，以确保点击旗帜时所有内容都被重置：

	```blocks
		变量 [room v] 设为 (1)
    定位到 x: (-200) y: (0)
    背景换成 [room1 v]
	```

+ 点击旗帜并使你的 `玩家` 子图移动到橙色房门上。你的子图是否移向了下一个画面？`room`{:class="blockdata"}（房间）变量是否变为 `2`？

![screenshot](images/world-room-test.png)

--- challenge ---
### 挑战：移向先前的房间

+ 你能否使你的 `玩家` 子图在碰到黄色房门时移向先前的房间？为此你需要的代码与你之前为移向下一个房间而添加的代码十分相似。

--- /challenge ---
