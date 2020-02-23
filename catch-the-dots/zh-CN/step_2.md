## 创建一个控制器

让我们从创建一个控制器开始，控制器将用来收集小点。



+ 从 <a href="http://jumpto.cc/dots-go" target="_blank">jumpto.cc/dots-go</a> 在线打开“接住小点”Scratch 项目，如果你正使用离线编辑器，则从 <a href="http://jumpto.cc/dots-get" target="_blank">jumpto.cc/dots-get</a> 下载，然后打开。

	你会看到一个控制器子图：

	![screenshot](images/dots-controller.png)
	
	
+ 按下右箭头键时使你的控制器右转：

	```blocks
		点击绿旗时
    重复无限次 
      如果 <[右移 v] 键被按下？> 那么 
        转动CW (3) 度
      end
    end
	```
+ 测试你的控制器 -- 它应该转向右边。



