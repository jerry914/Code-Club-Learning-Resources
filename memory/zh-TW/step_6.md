## 最高紀錄

把得分記錄下來，看看你和朋友誰有超強記憶力。

\--- task \---

添加名為 `最高分`{:class="block3variables"} 和 `姓名`{:class="block3variables"} 兩個變數到你的專案。

\--- /task \---

當玩家弄錯順序時，遊戲結束，結束時檢查得分是不是目前的最高分。 如果是，就記錄得分，並儲存玩家的姓名。

\--- task \---

為角色添加記錄`最高分`{:class="block3variables"}的程式。 還要詢問玩家的姓名，把它儲存在`名稱`{:class="block3variables"}變數裡。

[[[generic-scratch3-high-score]]]

\--- hints \---

\--- hint \---

你的新程式要依這個模式安排：

在`遊戲結束`{:class="block3looks"} 的訊息廣播後， `如果`{:class="block3control"}玩家的`得分`{:class="block3variables"}數`大於`{:class="block3operators"} 目前的`最高分`{:class="block3variables"}，那麼 `設定`{:class="block3variables"}變數`最高分`{:class="block3variables"}為`得分`{:class="block3variables"} `詢問`{:class="block3sensing"}玩家叫什麼名字 `設定`{:class="block3variables"}變數`名稱`{:class="block3variables"}為`詢問的答案`{:class="block3sensing"}

\--- /hint \---

\--- hint \---

這裡是你需要的程式積木：

![芭蕾舞者](images/ballerina.png)

```blocks3
如果 <> 那麼
end

(得分)

(得分)

() > (50)

詢問的答案

(最高分)

詢問 (你最高分，貴姓大名？) 並等待

變數 [得分 v] 設為 ()

變數 [名稱 v] 設為 () 
```

\--- /hint \---

\--- hint \---

當你點擊紅色按鈕時的程式應該會像這樣：

![芭蕾舞者](images/ballerina.png)

```blocks3
當收到訊息 (紅色 v)
如果 <((序列 v) 的第 (1) 項) = (1)> 那麼
    演奏節拍 ( (1)軍鼓 v) (0.25) 拍
    刪除 [序列 v] 的第 (1) 項
否則
    說出 (遊戲結束！) 持續 (1) 秒
    如果 <((得分)) = ((最高分))> 那麼
        變數 [最高分 v] 設為 (得分)
        詢問 (你最高分， 貴姓大名？) 並等待
        變數 [名稱 v] 設為 (詢問的答案)
    end
    停止 [全部 v]
end
```

\--- /hint \---

\--- /hints \---

\--- /task \---

接著，你必須把這樣的程式寫進其它三個顏色按鈕的角色當中！很麻煩對吧？！

你注意到了嗎？這四個顏色按鈕上，為「遊戲結束」安排的程式都完全一樣，對吧？

![芭蕾舞者](images/ballerina.png)

```blocks3
說出 (遊戲結束！) 持續 (1) 秒
如果 <((得分)) = ((最高分))> 那麼
    變數 [最高分 v] 設為 (得分)
    詢問 (你最高分， 貴姓大名？) 並等待
    變數 [名稱 v] 設為 (詢問的答案)
end
停止 [全部 v]
```

假設你有天突然想重新安排遊戲結束時的程式，比方說加入一個音效、一段文字，那麼就要同時修改四個地方，那很煩人，很浪費時間，對吧？

所以，如果你可以有個自己的積木，叫做「遊戲結束」，那麼你只要修改一次，在任何地方就能重複使用。

\--- task \---

切換到`函式積木`{:class="block3myblocks"}類，點擊**建立一個積木**，命名為`遊戲結束r`{:class="block3myblocks"}。

\--- /task \---

\--- task \---

把剛剛`紅色`{:class="block3events"}按鈕中`否則`{:class="block3control"}區段的程式複製並安排到`遊戲結束`{:class="block3myblocks"}積木的下面，像這樣：

![芭蕾舞者](images/ballerina.png)

```blocks3
定義 遊戲結束
說出 (遊戲結束！) 持續 (1) 秒
如果 <((得分)) = ((最高分))> 那麼
    變數 [最高分 v] 設為 (得分)
    詢問 (你最高分，
 貴姓大名？) 並等待
    變數 [名稱 v] 設為 (詢問的答案)
end
停止 [全部 v]
```

\--- /task \---

\--- task \---

現在你可以移除`紅色`{:class="block3events"}按鈕中`否則`{:class="block3control"}區段的程式，改成`遊戲結束`{:class="block3myblocks"}：

![芭蕾舞者](images/ballerina.png)

```blocks3
當收到訊息 (紅色 v)
如果 <((序列 v) 的第 (1) 項) = (1)> 那麼
    演奏節拍 ( (1)軍鼓 v) (0.25) 拍
    刪除 [序列 v] 的第 (1) 項
否則
    遊戲結束 :: custom
end
```

\--- /task \---

\--- task \---

測試你自己做的函式積木，看看在答錯顏色序列時，是不是會進入遊戲結束的程式。

\--- /task \---

建立一個像`遊戲結束`{:class="block3myblocks"}的積木，在程式設計中叫做一個**函式（function）**，在編程時，如果你發現有些程式不斷重複在使用，就可以建立`函式積木`{:class="block3myblocks"}，就可以方便日後的修改或維護。

\--- task \---

現在你可以在`收到其它顏色訊息`{:class="block3events"}事件下的`否則`{:class="block3control"}區段，放入`遊戲結束`{:class="block3myblocks"}這個函式積木。 像收到`藍色`{:class="block3events"}訊息的程式應該會是這樣：

![芭蕾舞者](images/ballerina.png)

```blocks3
當收到訊息 (藍色 v)
如果 <((序列 v) 的第 (1) 項) = (2)> 那麼
    演奏節拍 ( (2) 低音鼓 v) (0.25) 拍
    刪除 [序列 v] 的第 (1) 項
否則
    遊戲結束 :: custom
end
```

\--- /task \---

\--- task \---

現在我們來為按錯按鈕時製造一點音效。 你只要修改自己建立的`遊戲結束`{:class="block3myblocks"}積木就可以了，比起一次要修改四個地方，是不是來得輕鬆多了呢！

![芭蕾舞者](images/ballerina.png)

```blocks3
定義 遊戲結束
播放音效 (Cough1 v)
說出 (遊戲結束！) 持續 (1) 秒
如果 <((得分)) = ((最高分))> 那麼
    播放音效 (Trumpet1 v)
    變數 [最高分 v] 設為 (得分)
    詢問 (你最高分，
 貴姓大名？) 並等待
    變數 [名稱 v] 設為 (詢問的答案)
end
停止 [全部 v]
```

\--- /task \---