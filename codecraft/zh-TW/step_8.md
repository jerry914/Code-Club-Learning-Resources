## 利用木材製作木板

讓我們建立一個可以使用木材製作的新木板資源。

+ 首先，向你的遊戲新增一個新的 `PLANK`（木板）變數。

    ![screenshot](images/craft-plank-const.png)

+ 向你的遊戲新增一個新的 `PLANK`（木板）變數。

    ![screenshot](images/craft-plank-resources.png)

+ 將該資源命名為 `'plank'`（木板）。

    ![screenshot](images/craft-plank-names.png)

+ 為你的 `PLANK`（木板）資源提供一張圖片。專案中已包含一張 `plank.png` 圖片，但如果你願意的話，你可以建立你自己的圖片。

    ![screenshot](images/craft-plank-textures.png)

+ 向你的庫存新增木板。

    ![screenshot](images/craft-plank-inventory.png)

+ 設定一個放置木板的按鍵。

    ![screenshot](images/craft-plank-placekeys.png)

+ 由於該資源可被製作出來，你需要建立一個製作規則，即 1 塊木板可由 3 個木材塊製成。向 `crafting`（製作）字典新增此程式碼。 

    ![screenshot](images/craft-plank-crafting.png)

+ 最後，你需要設定製作新木板的按鍵。

    ![screenshot](images/craft-plank-craftkeys.png)

+ 要測試你的新木板資源，將一些木材塊聚集起來，然後利用這些木材塊製作一些木板。你隨後可以在你的世界中放置新木板。

    ![screenshot](images/craft-plank-test.png)



