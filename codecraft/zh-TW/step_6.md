## 建立一個新的木材資源

讓我們來建立一個新的木材資源。為此，你將需要在 `variables.py` 檔案中新增一些變數。

+ 首選你需要給你的新資源一個編號。隨後，你就可以在程式碼中使用 `WOOD`（木材）這個詞來代替數字 4。

    ![screenshot](images/craft-wood-const.png)

+ 你應將新的 `WOOD`（木材）資源新增到你的 `resources`（資源）列表。

    ![screenshot](images/craft-wood-resources.png)

+ 你還應為你的資源命名，名稱將顯示在庫存中。

    ![screenshot](images/craft-wood-name.png)

    請注意上文行末的逗號 `,`。

+ 你的資源還需要一張圖片。專案中已包含一張名為 `wood.png` 的圖片，你應該將其新增到 `textures`（材質）詞典。

    ![screenshot](images/craft-wood-texture.png)

+ 新增你的 `inventory`（庫存）中應包含的資源的起始數量。

    ![screenshot](images/craft-wood-inventory.png)

+ 最後，新增將木材放在世界中需要按下的按鍵。 

    ![screenshot](images/craft-wood-placekey.png)

+ 執行你的專案來進行測試。你會看到現在你的庫存中有了一個新的“wood”（木材）資源。

    ![screenshot](images/craft-wood-test.png)

+ 你的世界中沒有木材！為解決這個問題，點選你的 `main.py` 檔案，找到名為 `generateRandomWorld()`（生成隨機世界）的函式。

    ![screenshot](images/craft-wood-random1.png)    

    此程式碼會生成一個 0 到 10 之間的隨機數字，並使用該數字來決定放置哪種資源：

    + 1 或 2 = water（水）
    + 3 或 4 = grass（草）
    + 任何其他數字 = DIRT（泥土）

+ 新增此程式碼，從而每當 `randomNumber`（隨機數字）為 5 時就向你的世界新增木材。

    ![screenshot](images/craft-wood-random2.png)

+ 再次測試你的專案。這次，你會看到你的世界中出現一些木材。

    ![screenshot](images/craft-wood-test2.png)

