--- challenge ---
## 挑战：改进的重力
你的游戏中有另外一个小错误：如果角色的_任何_部位触碰到蓝色平台 - 即使是其头部，重力便不会将你的角色往下拉！你可以通过一路向上攀爬梯子然后向左移动来对其进行测试。

![screenshot](images/dodge-gravity-bug.png)

你能否修复这个错误？为此，你需要赋予你的角色不同颜色的裤子（在_所有_造型上）...

![screenshot](images/dodge-trousers.png)

...然后将代码： 

```blocks
	<碰到颜色 [#0000FF] ?>
```

替换为：

```blocks
	<颜色 [#00FF00] 碰到颜色 [#0000FF] ?>
```

请记得测试你的改进之处来确保你修复了这个问题！




--- /challenge ---
