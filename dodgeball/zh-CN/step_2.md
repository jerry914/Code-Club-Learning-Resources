## 角色移动

让我们首先创建一个可左右移动并可攀爬梯子的角色。



+ 从 <a href="http://jumpto.cc/dodge-go" target="_blank">jumpto.cc/dodge-go</a> 在线打开“躲避球”Scratch 项目，如果你正使用离线编辑器，则从 <a href="http://jumpto.cc/dodge-get" target="_blank">jumpto.cc/dodge-get</a> 下载，然后打开。

	该项目包含一个带有平台的背景：

	![screenshot](images/dodge-background.png)

+ 添加一个新的子图，该子图将成为你的角色。你最好选择一个带有多种造型的子图，这样你能使其看起来像是在行走。

	![screenshot](images/dodge-characters.png)

+ 让我们使用箭头键使你的角色到处移动。当玩家按下右箭头键时，你希望你的角色朝向右侧、移动几步并变换为下一套造型：

	```blocks
		点击绿旗时
    重复无限次 
      如果 <[右移 v] 键被按下？> 那么 
        面朝 (90 v) 度
        移动 (3) 点
        造型换成下一个
      end
    end
	```

+ 通过点击旗帜然后按住右箭头键来测试你的角色。你的角色是否向右移动？你的角色看起来是否正在行走？

	![screenshot](images/dodge-walking.png)

+ 为使你的角色向左移动，你需要在你的 `重复执行`{:class="blockcontrol"}循环内部添加另一个 `如果`{:class="blockcontrol"}代码块，来使你的角色左移。

+ 测试你的新代码来确保其正常运行。你的角色是否在向左行走时上下颠倒？

	![screenshot](images/dodge-upside-down.png)

	如果是，你可以通过点击角色子图上的 `(i)`{:class="blocksensing"} 图标修复这个错误，然后点击左右箭头。

	![screenshot](images/dodge-left-right.png)

	或者，如果你愿意的话，你可以在你角色脚本的开始位置添加此代码块：

	```blocks
    回转方式设为 [左-右 v]
	```

+ 为攀爬粉色梯子，你的角色应该在每次按下上箭头时略微上移，并且触碰到正确的颜色。将此代码添加进你角色的 `重复执行`{:class="blockcontrol"}循环中：

	```blocks
		如果 <<[上移 v] 键被按下？> 且 <碰到颜色 [#FF69B4] ?>> 那么 
      y 改变 (4)
    end
	```

+ 测试你的角色 - 你能否攀爬粉色梯子并到达关卡的终点？

	![screenshot](images/dodge-test-character.png)



