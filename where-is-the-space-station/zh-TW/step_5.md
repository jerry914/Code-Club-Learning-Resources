## ISS 何時會到達上空？

你還可以呼叫另一個 web 服務來找出 ISS 下次會在何時執行到一個特定位置的上空。 

讓我們找出 ISS 下次什麼時候處於美國休斯頓航天中心的上空，其緯度為 29.5502，經度為 95.097。
  
 

+ 首先讓我們在地圖上的這些座標處繪製一個點：

    ![screenshot](images/iss-houston.png)

+ 現在讓我們獲取 ISS 下次到達上空的日期和時間。 

    與之前一樣，我們可以通過在 web 瀏覽器的位址列裡輸入 url 來呼叫 web 服務：<a href="http://api.open-notify.org/iss-pass.json" target="_blank">http://api.open-notify.org/iss-pass.json</a>
  
    你會看到一個錯誤：

    ![screenshot](images/iss-pass-error.png)

+ 這項 web 服務將緯度和經度作為輸入項，因此我們必須將它們加入我們使用的 url 中。

    輸入項新增在 `?` 後面並使用 `&` 隔開。 

    如下所示，向 url 新增 `lat` 和 `lon` 輸入項：<a href="http://api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1" target="_blank">http://api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1</a>
  
    ![screenshot](images/iss-passtimes.png)
  
    響應結果包括多個經過時間，我們只需檢視第一個時間。該時間以標準時間格式給出，你需要在 Python 中將其轉化為可讀的時間。

+ 現在讓我們來從 Python 呼叫 web 服務：向你的指令碼末尾新增以下程式碼：

    ![screenshot](images/iss-passover.png)

+ 現在讓我們從結果中獲得第一次經過的時間。

    新增以下程式碼：

    ![screenshot](images/iss-print-pass.png)


+ 該時間以時間戳的形式給出，因此我們需要 Python 時間模組，使我們能將其列印為可讀的格式並將其轉化為當地時間。讓我們使用海龜寫出經過該點的時間。 

+ 在你的指令碼頂部新增一行 `import time`：

    ![screenshot](images/iss-time.png)

+ `time.ctime()` 函式將該時間轉化為你能使用海龜寫出的可讀格式： 

    ![screenshot](images/iss-pass-write.png)
 
    （你可以移除或者註釋掉 `print` 行。）



