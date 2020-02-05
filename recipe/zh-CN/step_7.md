## 颜色！

让我们向你的食谱网页添加一些颜色。



+ 你已经学过如何向网页添加彩色文本。向你的 `style.css` 文件内部添加以下代码，使网站正文内的所有文本变为蓝色：

```
body {
    color: blue;
}
```

![screenshot](images/recipe-blue.png)

+ 你的浏览器知道 `blue`（蓝色）、`yellow`（黄色）甚至 `lightgreen`（浅绿色）之类的颜色，但你是否知道你的浏览器其实知道 140 多种不同颜色的__名称__？

有一张所有颜色名称的列表可供你使用：[jumpto.cc/colours](http://jumpto.cc/colours)，其中包括 `tomato`（番茄色）、​`firebrick`（砖红色）和 `peachpuff`（桃红色）等颜色名称。

将文本颜色从 `blue`（蓝色）变为 `tomato`（番茄色）。

![screenshot](images/recipe-tomato.png)

+ 你的浏览器知道 140 种颜色的名称，但实际上却知道超过 1600 万种颜色的__色值__！


为告诉浏览器显示哪种颜色，你只需要告知其使用的红色、绿色和蓝色色值。

红色、绿色和蓝色的色值被定义为 `0` 到 `255` 之间的数值。

![screenshot](images/recipe-rgb-img.png)

向网页正文的 CSS 添加以下代码来显示一个浅黄色背景：

```
background: rgb(250,250,210);
```

![screenshot](images/recipe-rgb.png)

+ 如果你喜欢，你可以使用__十六进制代码__来告诉浏览器显示哪种颜色。这与上文 `rgb()` 代码的工作方式类似，但十六进制代码总是以 `#` 开头，并使用 `00` 到 `ff` 之间的十六进制“数字”来表示红色、绿色和蓝色色值。

![screenshot](images/recipe-hex-img.png)

使用以下十六进制代码替代 CSS 中的 `rgb()` 代码：

```
background: #fafad2;
```

![screenshot](images/recipe-hex.png)

你会看到与之前相同的浅黄色！



