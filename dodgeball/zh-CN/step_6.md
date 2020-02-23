## 躲避球

现在你已经使你的角色能够四处移动，让我们为你的角色添加一些需要躲避的小球。



+ 创建一个新的小球子图。你可以选择任何你喜欢的小球类型。

	![screenshot](images/dodge-balls.png)

+ 重新设置你的小球尺寸，使你的角色能跳过去。试着跳过小球以对其进行测试。 

	![screenshot](images/dodge-ball-resize.png)

+ 向你的小球添加以下代码：

	![screenshot](images/dodge-ball-motion.png)

	此代码每 3 秒创建一个新的小球克隆体。每个新的小球克隆体都沿顶部平台移动。

+ 点击旗帜以进行测试。

	![screenshot](images/dodge-ball-test.png)

+ 向你的小球子图添加更多代码，使其跨越所有的 3 个平台。

	![screenshot](images/dodge-ball-more-motion.png)

+ 最终，你将需要你的角色被小球击中时的代码！向你的小球子图添加此代码：

	```blocks
		当分身产生
    重复无限次 
      如果 <碰到 [Pico walking v] ?> 那么 
        广播消息 [hit v]
      end
    end
	```

+ 你还需要向你的角色添加代码，使其在被击中时返回起始位置：

	```blocks
		当收到消息 [hit v]
    面朝 (90 v) 度
    定位到 x: (-210) y: (-120)
	```	

+ 测试你的角色，看看它们是否会在被小球击中时返回起始位置。



