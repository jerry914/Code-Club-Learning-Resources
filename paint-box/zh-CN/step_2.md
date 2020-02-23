## 制作铅笔

首先让我们制作一支可用来在工作区绘图的铅笔。



+ 从 <a href="http://jumpto.cc/paint-go" target="_blank">jumpto.cc/paint-go</a> 在线打开“颜料盒”Scratch 项目，如果你正使用离线编辑器，则从 <a href="http://jumpto.cc/paint-get" target="_blank">jumpto.cc/paint-get</a> 下载，然后打开。

	你将会看到铅笔和橡皮擦子图：

	![screenshot](images/paint-starter.png)	

+ 由于你将使用鼠标绘图，因此你希望铅笔能 `重复执行`{:class="blockcontrol"}跟随鼠标移动。向你的铅笔子图添加此代码：

	```blocks
		点击绿旗时
    重复无限次 
    定位到 [mouse pointer v] 位置
    end
	```

+ 通过点击旗帜然后在工作区四处移动鼠标来测试此代码。 

+ 接下来，我们来让你的铅笔进行以下操作：`如果`{:class="blockcontrol"}鼠标被点击，即进行绘图。向你的铅笔子图添加此代码：

	![screenshot](images/paint-pencil-draw-code.png)	

+ 再次测试你的代码。这次，在工作区四处移动铅笔并按住鼠标按钮。你能否使用你的铅笔绘图？

	![screenshot](images/paint-draw.png)
	



