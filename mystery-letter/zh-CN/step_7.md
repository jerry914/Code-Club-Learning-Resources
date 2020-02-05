## 创建一个新类 

让我们创建一个看起来像从漫画书上剪切下来的样式。<a href="http://jumpto.cc/web-fonts" target="_blank">jumpto.cc/web-fonts</a> 提供了大量可免费使用的字体。 



+ 在 __style.css__ 文件中添加一个 `comic`（漫画）类。在 ​`magazine2`（杂志 2）后面比较合适。请不要忘记类名称前面的小点。 

![screenshot](images/letter-comic1.png)

如果你收到一个警告说“The Rule is empty”（规则为空），请不要担心；你接下来会解决这个问题。

+ 现在向漫画 CSS 类添加一些 CSS。如果你喜欢，你可以使用不同的颜色。在 <a href="http://jumpto.cc/colours" target="_blank">jumpto.cc/colours</a> 有大量颜色的列表。

![screenshot](images/letter-comic2.png)

+ 将漫画样式用在 HTML 文件内的某些 `<span>` 标记中，并测试你的页面：

![screenshot](images/letter-comic-output.png)

+ 现在你可以添加一个有趣的字体。打开一个新的浏览器选项卡或窗口。前往 <a href="http://jumpto.cc/web-fonts" target="_blank">jumpto.cc/web-fonts</a> 并搜索 __'bangers'__：

![screenshot](images/letter-fonts1.png)

+ 点击 Quick-use（快速使用）按钮：

![screenshot](images/letter-fonts2.png)

+ 将加载一个新的页面。向下滚动，直至你看到：

![screenshot](images/letter-fonts-link.png)

然后复制高亮代码。 

+ 将你刚刚从谷歌字体复制的 `<link>` 代码粘贴到你网页的 `<head>` 中：

![screenshot](images/letter-fonts-head.png)

这让你能在你的网页中使用 Bangers 字体。 

+ 返回到谷歌字体，继续向下滚动页面，然后复制 font-family 代码：

![screenshot](images/letter-fonts-bangers.png)

+ 现在返回 trinket 中的 __'style.css'__ 文件，并将 font-family 代码粘贴到漫画样式中：

![screenshot](images/letter-fonts-comic.png)

+ 测试你的网页。效果应如下所示： 

![screenshot](images/letter-fonts-output.png)



