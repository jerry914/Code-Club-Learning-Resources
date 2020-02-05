## 彩色编码贴纸

渐变指从一种颜色逐渐向另一种颜色变换。渐变可用来创建炫酷效果。你将使用它们来创建可在网页上使用的贴纸。 

+ 打开这个 trinket：<a href="http://jumpto.cc/web-stickers" target="_blank">jumpto.cc/web-stickers</a>。 

	此项目应如下所示：

	![screenshot](images/stickers-starter.png)

+ 让我们制作一张“I <3 Coding”的贴纸。 

	运用带 `sticker`（贴纸）类的 `<div>` 和 `coding`（编码）id，使你能设置其样式： 

	![screenshot](images/stickers-coding-error.png)


+ 嗯，你是否注意到出现了一个错误？这是因为“<”在 HTML 中属于特殊字符。你需要使用特殊代码 `&lt;` 而非“<”。 

	更新你的代码来使用 `&lt;`，从而消除错误。 

	![screenshot](images/stickers-coding-fixed.png)

	`<br>` 指另起一行。 

+ 现在我们来让贴纸看起来更加有趣。 

	切换到 `style.css` 文件。你会看到已为你提供了 `.sticker`（贴纸）类。由此在页面上布设贴纸并使其内容居中。 

	请记住。你向你的贴纸添加了 id `coding`（编码）。在 `style.css` 的底部添加以下代码来设置文本样式：

	![screenshot](images/stickers-coding-font.png)

+ 现在你可以为贴纸的背景添加渐变效果。线性渐变指沿着一条直线从一种颜色向另一种颜色变换。

	此渐变将从顶部的红色变为底部的洋红色。向你的 `coding`（编码）样式添加该渐变代码：

	![screenshot](images/stickers-coding-gradient.png)

+ 你可以通过添加内边距和圆角来完善渐变结果。 

	添加以下高亮代码：

	![screenshot](images/stickers-coding-padding.png)

	`padding`（内边距）样式分别在顶部和底部添加 50 像素、在左侧和右侧添加 30 像素的内边距。 




