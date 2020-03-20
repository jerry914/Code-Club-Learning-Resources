## 跑道

您將編寫一個烏龜賽跑的遊戲。首先，此遊戲需要建立一個跑道。

+ 單擊連結<a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>，開啟一個空白的Trinket Python模版。

+ 新增以下程式碼以使用'turtle'模組繪製一條線：
    
    ![截圖](images/race-forward.png)

+ 現在讓我們使用turtle模組來為賽跑繪製跑道標記。
    
    Turtle模組中的`write`函式能在螢幕上繪製文字。
    
    嘗試一下：
    
    ![截圖](images/race-markings1.png)

+ 現在你需要線條上填寫一些數字來建立標記：
    
    ![截圖](images/race-markings2.png)

+ 你注意到你的程式碼有許多的重複嗎？它們唯一不同的地方是輸入的數字。
    
    在Python中有一種更好的方法來寫這樣重複的程式碼。您可以使用`for`迴圈。
    
    使用`for`迴圈來更新你的程式碼：
    
    ![截圖](images/race-for.png)

+ 嗯，這支程式碼列印了從0到4之間的數字。Python中的`range(5)`函式將返回從0到4的五個數字。要讓它返回數字5，您則需要使用`range(6)`：
    
    ![截圖](images/race-range.png)

+ 現在我們可以繪製一些跑道的標記了。turtle模組將從螢幕中央的座標 (0,0) 開始繪製。
    
    現在要將畫筆移動到螢幕的左上方：
    
    ![截圖](images/race-goto.png)

+ 啊，你要先把畫筆抬起來！
    
    ![截圖](images/race-penup.png)

+ 讓我們繪製一些垂直線來建立跑道, 而不是水平線：
    
    ![截圖](images/race-lines.png)
    
    `right(90)`函式使畫筆向右轉90度。將畫筆放下之前，使用`forward(10)`函式前進10步將使線條的起點和數字之間保留一個小的空隙。 線條畫好後，將畫筆抬起並使用`backward(160)`函式向後移動160步，即線條和空隙的總長。

+ 將數字置中，將使介面看起來更整潔：
    
    ![截圖](images/race-center.png)

+ 你還可以加快畫筆的速度，使它畫得更快：
    
    ![截圖](images/race-speed.png)