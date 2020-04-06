## 隨機顏色

+ 開啟此Trinket: [trinket.io/python/5c2f5a25cf](https://trinket.io/python/08aff680d1){:target="_blank"}。

+ 你可以通過表明你想要的紅色、綠色和藍色色值（在 0 到 255 之間選擇）來設定海龜的顏色。
    
    新增以下程式碼來獲得一隻紫色海龜：
    
    ![截圖](images/modern-purple.png)
    
    紫色是通過混合紅色和藍色而得到的。

--- collapse ---

title: "Error - bad color sequence: (150, 0, 150)"


當你執行程式碼時是否遇到`bad color sequence: (150, 0, 150)`這個錯誤。

這是因為Trinket使用了與其他Python編輯器不同的顏色模式。 可以通過更改`colormode`（顏色模式）至`255`解決這個問題 。

```python
from turtle import *

colormode(255)

shape("turtle")
color(150,0,150)
```

--- /collapse ---

+ 嘗試一些不同的數字以獲得不同的顏色。
    
    請記住，每個數字只能在0到255之間。

+ 如何選擇隨機顏色？
    
    修改你的程式碼，為紅色，綠色和藍色值選擇一個介於0到255之間的隨機數：
    
    ![截圖](images/modern-random-colour.png)

+ 重複點選“Run”可以獲得不同顏色的烏龜。

+ 這很有趣，但你每次想要為一隻海龜設定隨機顏色時，都要記住這段程式碼並重新輸入，而且這樣不便於閱讀。
    
    在 Python 中，可以用 `def`來定義一個隨機設定海龜顏色的函式，以便我們隨時呼叫。
    
    你已經呼叫過函式，`color()`和`randint()`就是已為你定義好功能的函式。
    
    讓我們把隨機顏色的程式碼放入 def 定義的函式中：
    
    ![截圖](images/modern-colour-function.png)
    
    請確保你在函式內縮排程式碼。 函式通常放在指令碼的頂部，跟在imports後面。

+ 如果你現在點選“Run”執行你的程式碼卻沒有得到一個隨機顏色的海龜。 那是因為你定義了函式，但尚未呼叫它。

+ 新增一行程式碼以呼叫新函式：
    
    ![截圖](images/modern-call-colour.png)
    
    注意，新程式碼更容易理解，因為複雜的部分都在函式內。 現在就很容易理解`randomcolour()`做了什麼。