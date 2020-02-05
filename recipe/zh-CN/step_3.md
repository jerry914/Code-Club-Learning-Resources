## 原料

让我们列出你的食谱所需的原料。



+ 打开此 trinket 模板：[jumpto.cc/html-template](http://jumpto.cc/html-template){:target="_blank"}.

	此项目应如下所示：

	![screenshot](images/recipe-starter.png)

+ 就您的原料列表而言，你将使用__无序列表__，其中要运用 `<ul>` 标记。转向模板第 8 行并添加以下 HTML，用你自己食谱的名称替代 `<h1>` 标题中的文本：

```
<h1>Banana Milkshake</h1>

<h3>Ingredients:</h3>

<ul>

</ul>
```

+ 查看你的网页，你会看到两个标题。

![screenshot](images/recipe-headings.png)

但你现在还无法看到你的列表，因为你还未向其添加任何列表项目！

+ 下一步是使用 `<li>` 标记向你的列表中添加列表项目。在你的 `<ul>` 标记内部添加以下代码：

```
<li>1 banana</li>
```
![screenshot](images/recipe-ul.png)

因为你的列表是无序的，因此列表项目旁边并无编号，只有项目符号。

