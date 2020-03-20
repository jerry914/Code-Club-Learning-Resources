## 對字母進行加密

讓我們編寫一個 Python 程式來加密單個字元。



+ 開啟空白 Python 模版 Trinket：<a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>。

+ 讓我們將字母表寫出來作為 `alphabet` 變數，而不是將其畫在圓中。

	![screenshot](images/messages-alphabet.png)

+ 字母表中的每個字母都有一個位置，從位置 0 開始。因此，字母“a”在字母表中位於位置 0，“c”位於位置 2。

	![screenshot](images/messages-array.png)

+ 你可以通過在方括號內填寫位置來從 `alphabet` 變數中獲取一個字母。

	![screenshot](images/messages-alphabet-array.png)

	你在測試過之後就可以刪除 `print` 語句。

+ 接下來，你將需要在變數中儲存祕密 `key`。

	![screenshot](images/messages-key.png)

+ 然後，詢問使用者需要加密的字母（被稱為 `character`（字元））。

	![screenshot](images/messages-character.png)

+ 找到該 `character`（字元）的 `position`（位置）。

	![screenshot](images/messages-position.png)

+ 你可以將所儲存的 `position`（位置）列印出來以進行測試。例如，字元“e”位於字母表中的位置 4。

	![screenshot](images/messages-position-test.png)

+ 要加密 `character`（字元），你需要向 `position`（位置）新增 `key`（密鑰）。它隨後會被儲存在 `newPosition` 變數中。

	![screenshot](images/messages-newposition.png)

+ 新增程式碼來列印出新字元的位置。 

	![screenshot](images/messages-newposition-print.png)

+ 測試你的新程式碼。因為你的 `key`（密鑰）是 3，所以應該要把 `position`（位置）加上 3 並儲存在你的 `newPosition` 變數中。

	例如，字母“e”位於位置 4。為了進行加密，你需要加上 `key` (3)，得出 7。

	![screenshot](images/messages-newposition-test.png)

+ 如果你試著加密字母“y”的話，會發生什麼事情呢？

	![screenshot](images/messages-modulus-bug.png)

	請注意 `newPosition` 現在變成 27，但是在字母表中並沒有 27 個字母！

+ 你可以使用 `%` 來告訴新位置，一旦到達位置 26，就返回位置 0。

	![screenshot](images/messages-modulus.png)

+ 最後，你想要列印出新位置的字母。

	例如，向字母“e”新增密鑰得出 7，字母表中位置 7 的字母為“h”。

	![screenshot](images/messages-newcharacter.png)

+ 試試你的程式碼。你還可以移除某些列印語句，只有在最後列印出新字元。

	![screenshot](images/messages-enc-test.png)
