## 彩笔

让我们向你的项目添加不同颜色的画笔，并允许用户在它们之间进行选择！



+ 点击你的铅笔子图，点击“造型”并复制你的“蓝色铅笔”造型。

	![screenshot](images/paint-blue-duplicate.png)

+ 将你的新造型重命名为“绿色铅笔”，然后将铅笔颜色变为绿色。

	![screenshot](images/paint-pencil-green.png)

+ 创建两个新子图，你将使用它们来选择蓝色或绿色铅笔。

	![screenshot](images/paint-selectors.png)

+ 点击绿色选择器图标时，你需要向铅笔子图 `广播`{:class="blockevents"}一条消息，告诉它更改自身造型和铅笔颜色。

	为此，首先向绿色选择器图标添加此代码：

	```blocks
		当角色被点击
    广播消息 [green v]
	```

	为创建 `广播`{:class="blockevents"}代码块，点击下箭头并选择“新消息...”。

	![screenshot](images/paint-broadcast.png)

	随后，你可以输入“绿色”来创建你的新消息。

	![screenshot](images/paint-green-message.png)

+ 现在你需要告诉你的铅笔子图在收到消息时做什么。向你的铅笔子图添加此代码：

	```blocks
		当收到消息 [green v]
    造型换成 [pencil-green v]
    笔迹颜色设为 [#00ff00]
	```

	要将铅笔颜色设为绿色，请点击 `设定颜色`{:class="blockpen"}代码块中的彩色盒子，然后点击绿色选择器图标来选择绿色作为你的铅笔颜色。

+ 你现在可以对蓝色铅笔图标进行同样操作，将此代码添加到蓝色选择器子图：

	```blocks
		当角色被点击
    广播消息 [blue v]
	```

	...并向铅笔子图添加此代码：

	```blocks
		当收到消息 [blue v]
    造型换成 [pencil-blue v]
    笔迹颜色设为 [#0000ff]
	```

+ 最后，你需要告诉你的铅笔子图选择何种造型和铅笔颜色，以及在项目开始时清空画面。向铅笔 `当绿色旗帜被点击`{:class="blockevents"}代码（在 `重复执行`{:class="blockcontrol"}循环之前）的开头添加此代码：

	```blocks
		笔迹清除
    造型换成 [blue-pencil v]
    笔迹颜色设为 [#0000ff]
	```

	如果你乐意，你可以使用一个不同颜色的铅笔开始！

+ 测试你的项目。你能否在蓝色和绿色画笔之前切换？

	![screenshot](images/paint-pens-test.png)



