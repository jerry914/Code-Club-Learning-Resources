## 隨機字元

讓我們來建立一支程式，它可以幫我們的密碼產生隨機的字元。



+ 開啟 Trinket 的線上編輯器 <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>. 
+ 建立一張字元清單，儲存在叫做`chars`變數中 。

	![screenshot](images/passwords-chars.png)

+ 要隨機的選擇字元，你需要 `import`（匯入）  `random`（亂數） 模組.

	![screenshot](images/passwords-import.png)

+ 現在你可以隨機的從字元清單中選取字元，並且將它儲存在名為 `password`的變數中。

	![screenshot](images/passwords-choose.png)

+ 最後，你可以在螢幕上印出（非常短的！）密碼。

	![screenshot](images/passwords-print.png)

+ 按下'run'來測試你的程式碼。你可以看到一個隨機的字元出現在螢幕上。

	![screenshot](images/passwords-test-letters.png)

	如果以執行幾次你的程式，你會發現螢幕出現不同的字元。

+ 只有字母的密碼並不安全。新增一些數字到變數 `chars` 。

	![screenshot](images/passwords-numbers.png)

+ 再次嘗試執行幾次你的程式碼，你應該會看到有些時候會選到數字。



