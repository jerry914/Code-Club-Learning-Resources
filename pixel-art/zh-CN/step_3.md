## 创建像素网格

让我们创建一个你能用来创作像素艺术的像素网格。

网格看起来像一张表格。表格包含多个行，行包含代表像素的单元格。

+ 打开 [启动器 trinket](http://jumpto.cc/web-pixel)。

此项目应如下所示：

![screenshot](images/pixel-starter.png)

首先，让我们编写一些代码来创建一张背景为黑色的表格，然后将白色像素放在里面。

+ 将此代码添加到 `index.html` 文件的 `<body>` 中来创建一个 `<div>`：

![screenshot](images/pixel-art-art.png)

`<div>` 是一个不可见的盒子，你可以为其赋予 **style**（样式）。此 `<div>` 的 ID 为 `art`（艺术），你需要它来向盒子添加样式。

+ 现在转向 `style.css` 文件，然后向名为 `art`（艺术）的 `<div>` 添加表格样式。

![screenshot](images/pixel-art-style.png)

由此创建一个有边界的表格，并在网格内部设置间距。

现在看起来还不是十分有趣，因此你需要在里面放入多行像素。

+ 返回你的 `index.html` 文件并在 `art`（艺术）盒子**内部**添加一行三个像素。如果你想节省时间，你可以输入第一行，然后将其复制粘贴来创建其他行。

![screenshot](images/pixel-art-row.png)

请注意你在此处使用的是 **class**（类）而非 ID 来设置 div 的样式。这是因为有很多 div，所以类更加好用。

+ 切换到 `style.css` 文件，然后向各行和每行内的像素添加以下样式：

![screenshot](images/pixel-art-row-style.png)

现在你的像素将在网格中排列成行，周围环绕着黑线。

+ 在你的 `index.html` 文件中，再添加两行像素来创建一个 3×3 的像素网格。你可以再次使用复制和粘贴来节省时间。

--- hints ---
--- hint ---
找到带有 `row`（行）类的 `<div>` 标记并复制，包括其中标示为 `pixel`（像素）的三行，直至并包括其对应的 `</div>` 标记。

立即将此代码粘贴到你刚刚复制的像素区域下方，用于创建另一行。再次重复此操作，由此可获得三行，每行三个像素。

你可以查看右侧的结果区域来检查你的表格是否正确无误。
--- /hint ---
--- hint ---
你的代码应如下所示：

![screenshot](images/pixel-art-grid-3.png)
--- /hint ---
--- /hints ---
