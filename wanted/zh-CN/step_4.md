## 设置图片样式

让我们来完善海报中的图片样式。



+ 此时，你的 `<img>` 标记并无任何 CSS 属性，那就让我们来添加一些！

	首先，在 CSS 的下方向你的 div 添加以下代码：

	```
	img {

	}
	```

	![screenshot](images/wanted-img-css.png)

+ 我们现在可以在 `` 花括号之间添加图片的 CSS 属性。

	例如，在花括号之间添加以下代码来设置图片宽度：

	```
	width: 100px;
	```

	你会看到图片的尺寸改变，宽度变为 100 像素。

	![screenshot](images/wanted-img-width.png)

+ 你还可以用以下代码在图片周围添加边框：

	```
	border: 1px solid black;
	```

+ 你是否注意到了图片与边框之间并无太多的间隙？

	![screenshot](images/wanted-img-border.png)

	你可以通过在图片周围添加一些内边距来解决这个问题：

	```
	padding: 10px;
	```

	内边距是内容（在这里为一张图片）与其边框之间的空间。

	![screenshot](images/wanted-img-padding.png)

	如果你将内边距更改为 `50px`，你认为会发生什么？

