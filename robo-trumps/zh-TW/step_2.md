## 從檔案讀取機器人資料

從檔案中讀取資訊通常很有用處。你隨後可以更改檔案中的資料，而無須更改你的程式碼。 



+ 開啟這個 trinket：<a href="http://jumpto.cc/trumps-go" target="_blank">jumpto.cc/trumps-go</a>。 

+ 你的啟動器專案包含一個 `cards.txt` 檔案，其中包含機器人相關的資料。 

  點選 `cards.txt` 來檢視資料：

  ![screenshot](images/robotrumps-cards.png)

  每行都有一個機器人的相關資料。資料條目以逗號隔開。 

  每行都包含以下資訊：

  名稱、智慧等級、電池持續時間、圖片檔名稱


+ 讓我們從檔案中讀入資料，以便你使用這些資料。 

  第一步是開啟指令碼中的 `cards.txt` 檔案：
  
  ![screenshot](images/robotrumps-open.png)
  
+ 現在你可以從該檔案讀取資料：

  ![screenshot](images/robotrumps-read.png)
  
+ 你務必要在使用完一份檔案後關閉它：

  ![screenshot](images/robotrumps-close.png)

+ 這樣可將檔案視為一個字串，你需要將其拆分成多個單獨的資料段。 

  首先，你可以將檔案劃分成行列表：

  ![screenshot](images/robotrumps-lines.png)
  
  請仔細檢視輸出內容。列表中有三個專案，每個專案都是檔案中的一行。 
  
+ 現在你可以每次一行來迴圈遍及這些行

  ![screenshot](images/robotrumps-loop.png)
  
+ 將這些行讀入到變數，而非進行列印輸出：

  ![screenshot](images/robotrumps-variables.png)
  
+ 你想隨後能使用這個資料來檢視一個特定機器人的值。讓我們使用機器人的名稱作為字典的鍵。 

  新增一個 `robots` 字典：

  ![screenshot](images/robotrumps-dict.png)
  
+ 現在針對每個機器人向機器人字典新增一個條目。 

  名稱為鍵，值為該機器人的一系列資料。 

  新增以下高亮程式碼：
 
  ![screenshot](images/robotrumps-data.png)
  
  你可以在測試完指令碼之後移除 `print robots`。 


