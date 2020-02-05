## 绚丽的机器人贴纸 

你可以使用图片来制作渐变贴纸。如果你使用背景透明的图片，渐变效果就会显现出来。 

你还可以创建向不同方向延伸的渐变。 

+ 使用 `firerobot.png` 图片向 `index.html` 添加一个贴纸：

	![screenshot](images/stickers-fire-html.png)

	你可以调整 `height`（高度）来调整图片大小，宽度也会自动改变。 

+ 线性渐变通常从顶部向底部延伸，但你可以使用 `to`（朝向）来更改方向。例如：`to top`（朝向顶部）、`to left`（朝向左侧）或 `to right`（朝向右侧）。

	就对角渐变而言，你可以给出两个方向。以下示例使用了 `to bottom left`（朝向左下方）。

	向 `style.css` 添加以下样式来为你的新机器人贴纸添加一个对角渐变和绚丽的边框：

	![screenshot](images/stickers-fire-gradient.png)

	请注意，你可以使用 `outline`（轮廓）来在通常的边框外部创建另一个边框。 
	`outline-offset`（轮廓偏移）在边框和轮廓之间添加了空白。 

+ 让我们为此贴纸添加一些文本。 

	向 `index.html` 添加一个包含文本“ROBOTS”（机器人）的 `<span>`，并赋予其一个 id。 

	![screenshot](images/stickers-fire-span.png)

+ 如果你使其变大并放置，文本效果会更好。 

	要放置文本，你将需要向 `#greensticker` 添加 `position: relative;` 并向 `#greentext` 添加 `position: absolute`。`制作一个机器人`项目中对定位进行了详细介绍。 

	向 `style.css` 添加以下代码：

	![screenshot](images/stickers-fire-text-style.png)

+ 为制作最后的扭曲效果，让我们使用 `transform: rotate` 来旋转文本。

	![screenshot](images/stickers-fire-rotate.png)

	尝试更改文本旋转的角度值。 




