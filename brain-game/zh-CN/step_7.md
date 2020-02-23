## 添加图形

你的角色不仅仅能向玩家说 `是！:)` 或 `不是 :(` ，让我们来添加一些图形，使玩家了解他们的表现如何。

+ 创建一个被称作“结果”的新子图，其中包含一个“对号”和一个“错号”装扮。

	![screenshot](images/brain-result.png)

+ 更改你角色的代码，使其不是告诉玩家做得如何，而是播放 `正确`{:class="blockevents"} 和 `错误`{:class="blockevents"} 消息。

	![screenshot](images/brain-broadcast-answer.png)

+ 你现在可以使用这些消息显示“对号”或“错号”装扮。向你的新“结果”子图添加此代码：

	![screenshot](images/brain-show-answer.png)

+ 再次测试你的游戏。你每次回答问题正确时就能看到一个对号，回答错误时为一个错号！

	![screenshot](images/brain-test-answer.png)

+ 你是否注意到了 `我收到正确时`{:class="blockevents"} 和 `我收到错误时`{:class="blockevents"} 的代码几乎一样？让我们来创建一个函数，使你更容易更改你的代码。

	在你的“结果”子图上点击 `更多模块`{:class="blockmoreblocks"}，然后点击“制作模块”。创建一个被称作 `制作动画`{:class="blockmoreblocks"} 的新函数。

	![screenshot](images/brain-animate-function.png)

+ 你随后可以将动画代码添加进你的新动画函数中，然后仅使用两次函数：

	![screenshot](images/brain-use-function.png)

+ 现在，如果你想让对号和错号显示更长或更短时间，你只需对你的代码做出一处改动。试一试吧！

+ 你可以更改你的动画函数，让对号和错号渐现，而不是仅仅显示和隐藏。

	```blocks
		定义 (animate)
		效果 [虚像 v] 设为 (100)
		显示
		重复 (25) 次 
  			效果 [虚像 v] 改变 (-4)
		end
		隐藏
	```



