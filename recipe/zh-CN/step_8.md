## 最后润色

让我们再添加一点 HTML 和 CSS 来完善你的网页。



+ 你可以使用 `<hr>` 标记在食谱结尾处添加一条水平线。

![screenshot](images/recipe-hr.png)

请注意，此标记就像 `<img>` 标记一样，没有结束标记。

+ 你刚刚添加的横线与你网页其他部分的样式并不相配。让我们通过添加一些 CSS 代码来解决这个问题：

```
hr {
    height: 2px;
    border: none;
    background-color: tomato;
}
```

![screenshot](images/recipe-hr-css.png)

+ 你甚至可以运用以下 CSS 代码来更改项目编号的外观：

```
ul {
    list-style-type: square;
}
```

![screenshot](images/recipe-ul-css.png)

