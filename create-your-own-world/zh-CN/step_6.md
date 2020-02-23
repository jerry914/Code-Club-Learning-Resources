## 标志

让我们向你的世界添加一些标志，以指引玩家的旅程。

+ 你的项目包括一个 `欢迎标志` 子图：

![screenshot](images/world-sign.png)

+ `欢迎标志` 子图只应在房间 1 中可见，因此向 `欢迎标志` 子图添加一些代码以确保实现这一点：

```blocks
	点击绿旗时
  重复无限次 
    如果 <(room) = [1]> 那么 
      显示

      隐藏
    end
  end
```

+ 通过在房间之间移动来测试你的 `欢迎标志` 子图。你的标志只应在房间 1 中可见。

	![screenshot](images/world-sign-test.png)

+ 一个标志如果不能表示点什么，则没有多大用处！添加更多代码，使 `欢迎标志` 子图触碰到 `玩家` 子图时显示一条信息：

```blocks
	点击绿旗时
  重复无限次 
    如果 <(room) = [1]> 那么 
      显示

      隐藏
    end
    如果 <碰到 [player v] ?> 那么 
      说出 [Welcome! Can you get to the treasure?]

      说出 []
    end
  end
```

+ 测试你的 `欢迎标志` 子图 — 现在，`玩家` 子图触碰它时，你应该会看到一条信息。

![screenshot](images/world-sign-test2.png)
