## 誰在太空裡？

你將使用一項提供有關太空實時資訊的 web 服務。讓我們找出目前誰身處太空。 



+ web 服務就像網頁一樣，有一個地址 (url)。但它並不傳回網頁的 HTML，而是傳回資料。 

    在網頁瀏覽器中開啟 <a href="http://api.open-notify.org/astros.json" target="_blank">http://api.open-notify.org/astros.json</a>。 

    你會看到類似於下文的內容：

    ```
    {
      "message": "success", 
      "number": 3, 
      "people": [
        {
          "craft": "ISS", 
          "name": "Yuri Malenchenko"
        }, 
        {
          "craft": "ISS", 
          "name": "Timothy Kopra"
        }, 
        {
          "craft": "ISS", 
          "name": "Timothy Peake"
        }
      ]
    }
    ```

    這些資料是實時的，因此你會看到不同的結果。這種格式被稱作 JSON（念 Jason）。 

+ 讓我們從 Python 呼叫該 web 服務，這樣我們便可以使用該結果。

    開啟這個 trinket：<a href="http://jumpto.cc/iss-go" target="_blank">jumpto.cc/iss-go</a>。 

+ 已經為你匯入了 `urllib.request` 和 `json` 模組。 

    向 `main.py` 新增以下程式碼來將你剛剛使用的 web 地址放入一個變數中：

    ![screenshot](images/iss-url.png)
   
+ 現在讓我們來呼叫 web 服務：

    ![screenshot](images/iss-request.png)


+ 接下來你需要將 JSON 響應結果載入到 Python 資料結構中：

    ![screenshot](images/iss-result.png)


    你會看到類似於下文的內容：

    ```
    {'message': 'success', 'number': 3, 'people': [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]}
    ```

    這是一個有 3 個鍵的 Python 字典：message（資訊）、number（數量）和 people（人物）。 


--- callapse ---
## 在 Pyhton 中使用 名稱:值

這是樂隊成員的字典。名稱是第一部分（例如'john'），及其值是所述第二部分（例如，“rhythm guitar'）。
---
band = {
  'john' : 'rhythm guitar',
  'paul' : 'bass guitar',
  'george' : 'lead guitar',
  'ringo' : 'bass guitar'
	}
---
這是將名稱:值添加到字典的方法：
---
## Add a key:value pair
band['yoko'] = 'vocals'
---
以下是從字典中刪除名稱:值的方法：
---
## Remove a key:value pair
del band['paul']
---
--- /callapse ---


    資訊的“success”（成功）值告訴你請求成功。很好。 

    請注意你會看到不同的結果，具體取決於目前誰在太空中！

+ 現在讓我們以更具可讀性的方式列印出該資訊。 

    首先，讓我們找到太空中的人數並將其列印出來：
  
    ![screenshot](images/iss-number.png)

    `result['number']` 將會列印與結果字典中的鍵“number”（數量）相關的值。示例中這個值為 `3`。 

+ 與“people”（人物）鍵相關的值是字典列表！讓我們把這個值放入變數中，以供你使用：

    ![screenshot](images/iss-people.png)


    你會看到類似於下文的內容： 
    
    ```
    [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]
    ```

+ 現在你需要針對每個宇航員列印出一行。

    你可以在 Python 中使用一個 for 迴圈來進行操作。每執行一次迴圈，都將為一名不同的宇航員將 `p` 設定到一個字典。

    ![screenshot](images/iss-people-1a.png)

+ 隨後你可以查詢“name”（名稱）和“craft”（飛行器）的值

    ![screenshot](images/iss-people-2.png)
  
    你會看到類似於下文的內容：

    ```
    People in Space:  3
    Yuri Malenchenko
    Timothy Kopra
    Timothy Peake
    ```

    你正使用實時資料，因此你的結果將取決於目前在太空中的人數。 



