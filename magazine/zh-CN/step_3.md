## 创建栏目

网站通常使用多个栏目。让我们来为你的杂志创建一个两栏布局。



+ 首先创建两个栏目 `div`。

	向 `index.html` 添加高亮的 HTML：

	![screenshot](images/magazine-columns.png)

+ 现在设置栏目 div 的样式，使得一栏浮动到左侧，另一栏浮动到右侧。

	![screenshot](images/magazine-columns-style.png)

	每个栏目的宽度应小于 50% 来留出内边距。

	你将需要向栏目添加一些内容来查看效果。

+ 让我们向栏目 2 的顶部添加一张猫咪图片。

	![screenshot](images/magazine-kitten.png)

	请注意将猫咪图片放在页面第二栏的半边。

	但图片有点大！

+ 让我们使用 `max-width: `（最大宽度）来使图片适应其容器。

	向 `style.css` 添加以下样式。

	![screenshot](images/magazine-img-width.png)

	这将应用到你在杂志中使用的所有图片，不仅仅是猫咪图片。

+ 现在向图片添加一个 `photo`（照片）类，使得你能设置其样式：

	![screenshot](images/magazine-photo.png)

+ 然后添加阴影和旋转来设置图片样式，使图片跃出页面：

	![screenshot](images/magazine-photo-style.png)

	进行一些更改直至你对成果满意。


