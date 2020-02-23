## 坚固的墙壁

+ 再次测试你的 `玩家` 子图，你可能会注意到他们能够穿过浅灰色的墙壁。

![screenshot](images/world-walls.png)

+ 为修复这个问题，你应该在 `玩家` 子图碰到浅灰色墙壁时使其往回移动。以下是你将需要在方向代码块下方的 `永远`{:class="blockcontrol"}代码块内部添加的代码：

```blocks
	如果 <碰到颜色 [#BABABA] ?> 那么 
  移动 (-4) 点
  end
```

+ 测试这个新代码：将 `玩家` 子图移动到墙壁下方，然后看看你是否能让它们向上移动到墙中。如果你的代码生效，就不会出现这种情况。

![screenshot](images/world-walls-test.png)
