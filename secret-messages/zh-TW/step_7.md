## 其他字元

一些字元不在字母表中，會造成錯誤。



+ 使用字母表中不存在的一些字元來測試你的程式碼。

	例如，你可以使用 `hi there!!`（你好！！）這條資訊。

	![screenshot](images/messages-extra-characters.png)

	請注意空格和 `!` 字元都被加密為字母“c”！

+ 為解決這個問題，你希望只轉換字母表中的字元。為此，向你的程式碼新增一個 `if`語句，並縮排剩餘程式碼。

	![screenshot](images/messages-if.png)

+ 用同樣的資訊來測試你的程式碼。這次會發生什麼？

	![screenshot](images/messages-if-test.png)

	現在，你的程式碼會跳過不在字母表中的字元。

+ 如果你的程式碼並未對不在字母表中的內容進行加密，而只是使用原來的字元，那就更好了。

	向你的程式碼新增 `else` 語句，這會將原始字元新增到已加密的資訊中。

	![screenshot](images/messages-else.png)

+ 測試你的程式碼。你會看到字母表中的所有字元已被加密，而其他字元則保持原樣！

	![screenshot](images/messages-else-test.png)



