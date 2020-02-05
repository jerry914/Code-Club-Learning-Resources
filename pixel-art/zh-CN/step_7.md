## 添加调色板

你是否发现如果你出错的话，就无法将像素颜色变回白色这点很烦人？让我们来创建一个调色板，使得你能通过点击来选择画笔颜色，从而解决这个问题。

+ 在 `style.css` 文件的底部添加此代码来创建一个画笔样式：

![screenshot](images/pixel-art-pen.png)

+ 现在使用你刚刚创建的画笔样式来创建一个带有黑白画笔颜色的调色板。向 `<body>` 标记下方的 `index.html` 添加以下代码：

![screenshot](images/pixel-art-palette.png)

`style=` 使你能在你的 HTML 文件内部添加 CSS 代码，在此处也很方便。

我们需要添加代码，使得点击调色板中的一种颜色时，画笔的颜色随之改变。

+ 切换到 `script.js`，然后在文件顶部创建一个名为 `penColour`（画笔颜色）的变量。将变量值设为 `black`（黑色）。

[[[generic-javascript-create-variable]]]

--- hints ---
--- hint ---
在文件顶部添加以下代码：

![screenshot](images/pixel-art-pencolour.png)
--- /hint ---
--- /hints ---

+ 在变量下方创建一个名为 `setPenColour`（设置画笔颜色）的新函数，函数的输入项为 `pen`（画笔）。请查看你已经创建的用来帮助你的 `setPixelColour`（设置像素颜色）函数。

[[[generic-javascript-create-a-function]]]

+ 在 `setPenColour`（设置画笔颜色）函数内部添加代码来将 `penColour`（画笔颜色）变量设为作为输入项提供的 `pen`（画笔）颜色。

![screenshot](images/pixel-art-set-pen.png)

在更改像素颜色时，你还将需要使用 `penColour`（画笔颜色）变量。

+ 将 `setPixelColour`（设置像素颜色）函数更改为使用 `penColour`（画笔颜色）变量而非 `black`（黑色）：

 ![screenshot](images/pixel-art-use-pen.png)

+ 在 `index.html` 文件中添加一些代码，以在调色板中的颜色被点击时调用 `setPenColour`（设置画笔颜色）函数。

![screenshot](images/pixel-art-palette-onclick.png)

+ 测试你能否在黑色和白色之间切换画笔颜色来填充或删除像素。
