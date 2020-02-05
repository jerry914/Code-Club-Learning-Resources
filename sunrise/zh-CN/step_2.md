## 创建太阳

让我们首先添加一张太阳的图片并使用一些 CSS 对其定位。



+ 打开这个 trinket：<a href="http://jumpto.cc/web-sunrise" target="_blank">jumpto.cc/web-sunrise</a>。 

    此项目应如下所示：

	![screenshot](images/sunrise-starter.png)

+ 查看你的 `index.html` 文件的 `body` 内部，你会发现天空和海洋的 `div` 元素。

    ```
    <div id="sky">
    </div>
    
    <div id="sea">
    </div>
    ```

+ 太阳的图片已包含在你的项目中。 

    向你的太阳 `div` 内部添加该图片，并包含一个 id，这样你便可以设置其样式：

    ![screenshot](images/sunrise-sun-image.png)

+ 哇哦，图片太大了。转向 `style.css` 并添加 CSS 来设置图片高度：

    ![screenshot](images/sunrise-sun-height.png)

    请注意，宽度会自动更新来使比例保持一致。 

+ 最后，让我们添加一些代码来对太阳进行定位：

    ![screenshot](images/sunrise-sun-position.png)




