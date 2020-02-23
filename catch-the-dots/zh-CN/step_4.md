## 收集小点

让我们来添加一些小点，供玩家使用控制器收集。



+ 创建一个被称作“红色”的新子图。此子图应为一个红色小点。

	![screenshot](images/dots-red.png)

+ 向你的“红色”小点子图添加此脚本，从而每隔几秒创建一个新的复制点：

	```blocks
		点击绿旗时
    隐藏
    等待 (2) 秒
    重复无限次 
      分身 [自己 v] 建立
      等待 (随机取数 (5) 到 (10)) 秒
    end
	```

+ 创建每个复制点时，你想使其出现在工作区 4 个角中的一处。

	![screenshot](images/dots-start.png)

	为此，首先创建一个被称作 `起始位置`{:class="blockdata"}的新列表，并点击 `(+)` 添加值 `-180` 和 `180`。

	![screenshot](images/dots-list.png)

+ 你可以使用这 2 个列表项目选择工作区的任何一个角。向“小点”子图添加此代码，使得每个新的复制点向一个随机角移动，然后缓慢移向控制器。

	```blocks
		当分身产生
    当分身产生
    定位到 x: (链表第 (random v) 项项目\( [start positions v] \) :: list) y: (链表第 (random v) 项项目\( [start positions v] \) :: list)
    面朝 [controller v] 向
    显示
    重复直到 <碰到 [controller v] ?> 
      移动 (1) 点
    end
	```

	上面的代码选择 `-180` 或 `180` 作为 x _和_ y 坐标，这意味着每个复制点起始于工作区的一个角。

+ 测试你的项目。你会看到大量红色小点出现在画面的各个角，并朝控制器缓慢移动。

	![screenshot](images/dots-red-test.png)

+ 创建 2 个被称作 `生命`{:class="blockdata"} 和 `分数`{:class="blockdata"} 的新变量。

+ 向你的工作区添加代码以将游戏开始时的 `生命`{:class="blockdata"} 设为 3， `分数`{:class="blockdata"} 设为 0。

+ 你需要向红色小点的 `我作为复制点开始时`{:class="blockcontrol"} 代码的末端添加代码，这样如果颜色匹配，则玩家的 `分数`{:class="blockdata"} 增加 1，如果颜色不匹配，则玩家减少 1 条 `生命`{:class="blockdata"}。

	```blocks
		移动 (5) 点
    移动 (5) 点
    如果 <碰到颜色 [#FF0000] ?> 那么 
      变量 [score v] 改变 (1)
      播放音效 [pop v]

      变量 [lives v] 改变 (-1)
      播放音效 [laser1 v]
    end
    分身删除
	```

+ 向你的工作区脚本末端添加此代码，这样在玩家失去所有生命时游戏结束：

	```blocks
		等待直到 <(lives) < [1]>
    停止 [全部 v]
	```

+ 测试你的游戏，以确保此代码按预期运行。



