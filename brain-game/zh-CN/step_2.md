## 创建问题

让我们从创建随机问题供玩家回答开始。



+ 启动一个新的 Scratch 项目，删除猫子图，使项目清空。你可以在 <a href="http://jumpto.cc/scratch-new" target="_blank">jumpto.cc/scratch-new</a> 找到在线 Scratch 编辑器。

+ 为你的游戏选择一个角色和背景。你可以选择任何你喜欢的！示例：

	![screenshot](images/brain-setting.png)

+ 创建 2 个被称作 `数字 1`{:class="blockdata"} 和 `数字 2`{:class="blockdata"} 的新变量。这些变量将储存要进行相乘的 2 个数字。

	![screenshot](images/brain-variables.png)

+ 向你的角色添加代码，将这些变量均设置为 2 和 12 之间的 `随机`{:class="blockoperators"} 数字。

	```blocks
		点击绿旗时
		变量 [number 1 v] 设为 (随机取数 (2) 到 (12))
		变量 [number 2 v] 设为 (随机取数 (2) 到 (12))
	```

+ 随后，你可以让玩家给出答案，并告知其答案正确与否。

	```blocks
		点击绿旗时
		变量 [number 1 v] 设为 (随机取数 (2) 到 (12))
		变量 [number 2 v] 设为 (随机取数 (2) 到 (12))
		询问 (字串组合 (number 1) 和 (字串组合 [ x ] 和 (number 2))) 并等待
		如果 <(answer) = ((number 1) * (number 2))> 那么 
  			说出 [yes! :)] (2) 秒

  			说出 [nope :(] (2) 秒
		end
	```

+ 通过正确回答一个问题和错误回答一个问题，对你的项目进行充分测试。

+ 围绕此代码添加一个 `永远`{:class="blockcontrol"} 循环，以询问玩家大量问题。

+ 使用被称作 `时间`{:class="blockdata"} 的变量，在工作区上创建一个倒数计时器。如果你需要帮助，“魔鬼克星”项目有制作计时器的说明（在第 5 步）！

+ 再次测试你的项目 - 你应该能够持续提出问题，直到时间结束。



