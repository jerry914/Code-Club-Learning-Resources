## 介绍

你将在本项目中学习如何使用 CSS 来创建一个日出动画。

<div class="trinket">
  <iframe src="https://trinket.io/embed/html/abcc0284a3?outputOnly=true&start=result" width="600" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/sunrise-final.png">
</div>

### 更多俱乐部领导参考信息

如果你需要打印本项目，请使用 [适合打印机的版本](https://projects.raspberrypi.org/en/projects/sunrise/print)。


--- collapse ---
---
title: 俱乐部领导备注
---


## 介绍：
孩子们将在本项目中学习如何使用 CSS 将一个简单的场景制作成动画。他们将使用 CSS @keyframes（关键帧）规则来对图片和 div 的各项属性进行动画处理。

## 在线资源

我们推荐使用 [trinket](https://trinket.io/) 来在线编写 HTML & CSS。本项目包含以下 trinket：

+ [“日出”起点](https://trinket.io/html/web-sunrise)

孩子们也可使用该空白 trinket [(jumpto.cc/html-blank)](http://jumpto.cc/html-blank) 来编写自己的 HTML & CSS，或者他们可以使用该 trinket 模板 [(jumpto.cc/html-template)](http://jumpto.cc/html-template)。

还有一个 trinket，其中包含相关挑战的解决方案样例：

+ [“日出”已完成](https://trinket.io/html/abcc0284a3)

## 离线资源
如果愿意的话，本项目可[离线完成](../offline.html)。你可以通过单击此项目的“下载项目材料”链接来访问项目资源。此链接包含一个“项目资源”文件夹，其中包括孩子们离线完成本项目时所需的资源。确保每个孩子都能访问这些资源的副本。此文件夹包括以下文件：

+ template/index.html
+ template/prefix.js
+ template/style.css
+ sunrise/index.html
+ sunrise/style.css
+ sunrise/prefixfree.js
+ sunrise/boat.png
+ sunrise/cloud.png
+ sunrise/helicopter.png
+ sunrise/rainbow.png
+ sunrise/sun.png

你还可以在“志愿者资源”部分中找到本项目挑战的完整版本，其中包含：

+ sunrise-finished/index.html
+ sunrise-finished/style.css
+ sunrise-finished/prefixfree.js
+ sunrise-finished/boat.png
+ sunrise-finished/sun.png
+ sunrise-finished/rainbow.png

## 学习目标
+ 运用 CSS 制作造型和动画：
	+ 引入 `@keyframe`（关键帧）规则来定义动画中的步骤。
	+ 加强属性的使用来定义网页上多个元素的尺寸、形状、位置和颜色。

本项目包括 [Raspberry Pi 数字制作课程](http://rpf.io/curriculum) 以下几个部分的元素：

+ [设计基本的 2D 和 3D 资源](https://www.raspberrypi.org/curriculum/design/creator)。

## 挑战
+ “斜向动画”- 编辑动画的 `@keyframe`（关键帧）属性来使用 left:（左侧）；
+ “完善天空”- 添加更多关键帧并设置 background:（背景）；
+ “更多动画”- 使用多种 CSS 属性对更多图片或元素进行动画处理。 

## 常见问题

+ 本项目使用了 javascript 的 `prefixfree.js` 库，使动画能兼容多个浏览器。如果不使用这个库，那么使用旧版浏览器的孩子则需要针对浏览器声明动画，例如：

```
animation: sky 10s infinite; 		  	//适用于所有新版浏览器
-webkit-animation: sky 10s infinite;  	// 适用于 Webkit 浏览器 (Chrome, Safari...)
-moz-animation: sky 10s infinite;     	// 适用于 Mozilla 浏览器
-o-animation: sky 10s infinite;       	// 适用于 Opera 浏览器
-ms-animation: sky 10s infinite;		// 适用于微软浏览器 
```


--- /collapse ---


--- collapse ---
---
title: 项目材料
---
## 项目资源
* [包含所有项目资源的 .zip 文件](resources/sunrise-project-resources.zip)
* [包含所有“日出”项目资源的在线 Trinket](http://jumpto.cc/web-sunrise)
* [在线 Trinket 模板](http://jumpto.cc/trinket-template)
* [在线空白 Trinket](http://jumpto.cc/trinket-blank)
* [template/index.html](resources/template-index.html)
* [template/style.css](resources/template-style.css)
* [intro/index.html](resources/intro-index.html)
* [intro/style.css](resources/intro-style.css)
* [sunrise/index.html](resources/sunrise-index.html)
* [sunrise/style.css](resources/sunrise-style.css)
* [sunrise/prefixfree.js](resources/sunrise-prefixfree.js)
* [sunrise/sun.png](resources/sunrise-sun.png)
* [sunrise/rainbow.png](resources/sunrise-rainbow.png)
* [sunrise/cloud.png](resources/sunrise-cloud.png)
* [sunrise/boat.png](resources/sunrise-boat.png)
* [sunrise/helicopter.png](resources/sunrise-helicopter.png)

## 俱乐部领导资源
* [包含所有已完成项目资源的 .zip 文件](resources/sunrise-volunteer-resources.zip)
* [在线完整 Trinket 项目](https://trinket.io/html/abcc0284a3)
* [sunrise-finished/index.html](resources/sunrise-finished-index.html)
* [sunrise-finished/style.css](resources/sunrise-finished-style.css)
* [sunrise-finished/prefixfree.js](resources/sunrise-finished-prefixfree.js)
* [sunrise-finished/sun.png](resources/sunrise-finished-sun.png)
* [sunrise-finished/boat.png](resources/sunrise-finished-boat.png)
* [sunrise-finished/rainbow.png](resources/sunrise-finished-rainbow.png)

--- /collapse ---