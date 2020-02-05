## 设置标题样式

让我们来完善 `<h1>` 标题的样式。



+ 向图片 CSS 的下方添加以下代码：

	```
	h1 {

	}
	```

	这就是你将向 `<h1>` 主标题添加 CSS 属性的地方。

+ 要更改 `<h1>` 标题的字体，在花括号之间添加以下代码：

	```
	font-family: Impact;
	```

+ 你还可以更改标题的尺寸：

	```
	font-size: 50pt;
	```

+ 	你是否注意到了 `<h1>` 标题和其周围内容之间的间隔很大？

	![screenshot](images/wanted-h1-margin.png)

	这是因为标题周围有一个边距。边距指元素（在这里是一个标题）与其周围的其他内容之间的间距。

	你可以使用以下代码来缩小边距：

	```
	margin: 10px;
	```

	![screenshot](images/wanted-h1-margin-small.png)

+ 你还可以为你的标题添加下划线：

	```
	text-decoration: underline;
	```

