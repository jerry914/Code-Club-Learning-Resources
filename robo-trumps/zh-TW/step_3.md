## 顯示資料

現在你可以用更有趣的方式來顯示機器人資料。 

讓我們顯示一張帶有圖片及機器人智慧和實用性資料的機器人王牌卡。 

你完成此步驟以後，你將能夠如下所示來顯示機器人：

![screenshot](images/robotrumps-example.png)




+ 詢問使用者他們想看到哪個機器人：

  ![screenshot](images/robotrumps-choose.png)
  
+ 如果機器人存在於字典中，則查詢其資料：

  ![screenshot](images/robotrumps-if.png)
  
  輸入一個機器人的名稱來測試你的程式碼。

  
+ 如果機器人不存在，會出現一個錯誤：

  ![screenshot](images/robotrumps-else.png)
  
 輸入字典中不存在的機器人名稱來測試你的程式碼。

+ 現在你要使用 Python turtle來顯示機器人資料。 

  在你的指令碼頂部匯入海龜庫，並設定畫面和 turtle：

  ![screenshot](images/robotrumps-turtle.png)

+ 現在新增程式碼來使 turtle 列印出機器人的名稱：

  ![screenshot](images/robotrumps-name.png)
  
+ 嘗試更改 `style` 變數直至你對文字滿意。 
  
  除了 `Arial`，你還可以嘗試：`Courier`、`Times` 或 `Verdana`。 
  
  將 `14` 更改為不同的數字來更改字型大小。 
  
  你可以將 `bold`（粗體）更改為 `normal`（正常）或 `italic`（斜體）。 
  
+ 將機器人的統計資料列表儲存在變數中，而不是將其列印輸出：

  ![screenshot](images/robotrumps-stats.png)
  
+ 你現在可以將機器人的統計資料作為列表中的專案進行訪問：

  + `stats[0]` 指智慧
  + `stats[1]` 指電池
  + `stats[2]` 指圖片名稱
  
  新增程式碼來顯示智慧和電池統計資料：
  
  ![screenshot](images/robotrumps-stats-2.png)
   
  
+ 噢天哪！統計資料全都堆在了一起。你將需要新增程式碼來移動 turtle ：

   ![screenshot](images/robotrumps-stats-3.png)

+ 最後，讓我們新增機器人圖片來完成顯示。 

  從 `cards.txt` 讀取資料時，你將需要新增一行來註冊圖片：
  
  ![screenshot](images/robotrumps-register.png)
     
+ 然後新增程式碼來定位和標記圖片：

  ![screenshot](images/robotrumps-image.png)
  
+ 輸入一個機器人然後再輸入另一個來測試你的程式碼，你會看到他們相互疊加在一起！

  你需要在顯示一個機器人之前清空螢幕： 

  ![screenshot](images/robotrumps-clear.png)



