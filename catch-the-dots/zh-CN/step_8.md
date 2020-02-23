## 高分

让我们来保存高分，使玩家能了解他们的成绩有多好。



+ 创建一个被称作 `高分`{:class="blockdata"} 的新变量。

+ 在你的工作区上点击，并创建一个被称作 `查看高分`{:class="blockmoreblocks"} 的新自定义模块。

	![screenshot](images/dots-custom-1.png)

+ 在游戏结束之前，加入你的新自定义模块。

	![screenshot](images/dots-custom-2.png)

+ 向你的自定义模块添加代码， `如果`{:class="blockcontrol"} 当前分数是到目前为止为最高分，则将该 `分数`{:class="blockdata"} 储存为 `高分`{:class="blockdata"}： 

	```blocks
		定义 (check high score)
    如果 <(score) > (high score)> 那么 
      变量 [high score v] 设为 (score)
    end
	```

+ 测试你所添加的代码。玩你的游戏来检查 `高分`{:class="blockdata"} 是否已正确更新。



