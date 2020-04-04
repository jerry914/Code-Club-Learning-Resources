## 一組隨機的密碼

單一個字元的密碼並不是非常有用 - 讓我們改寫你的程式來創造更長的密碼。



+ 要創造一組密碼，我們一次需要隨機增加一個字元。

	要開始之前，你的變數 `password` 必須是空的。在你的程式碼中加入下行：

	![screenshot](images/passwords-empty.png)

+ 你想要隨機的選擇字元十次。要做到這個，加入下列程式碼：

	![screenshot](images/passwords-repeat.png)

+ 你還需要縮排 (前進) 這行來隨機選取字元，如此一來這個步驟就可以重複十次。

	按下 'tab' 鍵來進行縮排。

	![screenshot](images/passwords-indent.png)

+ 每一次你需要使用 `+=` 來 __加入__ 新的字元到密碼中。

	![screenshot](images/passwords-add.png)

+ 測試你的新密碼，你應該可以看到一組包含十個字元的密碼。

	![screenshot](images/passwords-10-test.png)



