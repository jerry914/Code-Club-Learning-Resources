## 第 3 步：判定

你可以對你的聊天機器人進行程式設計，從而基於你對其問題的回覆，來判定說什麼或做什麼。

+ 你能否使聊天機器人提出“你好嗎？”的問題，並對其進行編碼，使其只有__在__使用者回答“是”的時候回覆“很高興聽到這句話！”？

    為適當地測試你的新程式碼，你需要測試__兩次__，一次使用答案“是”，另一次使用答案“不”。

    如果你回答“是”，你的聊天機器人應回覆“很高興聽到這句話！”，但如果你回答“不”，便無回覆。

    ![Testing a chatbot reply](images/chatbot-if-test.png)

--- hints ---
--- hint ---
你的聊天機器人說完“嗨”之後，現在還應該__詢問__“你好嗎？”。__如果__你回答“是”，那麼聊天機器人應該__說__“很高興聽到這句話！”。
--- /hint ---
--- hint ---
以下是你將另外需要的程式碼塊：
![Blocks for a chatbot reply](images/chatbot-if-blocks.png)
--- /hint ---
--- hint ---
你的程式碼應如下所示：
![Code for a chatbot reply](images/chatbot-if-code.png)
--- /hint ---
--- /hints ---

+ 此時，如果你回答“不”，你的聊天機器人將什麼都不會說。你能否更改你的聊天機器人，使其在你對其問題回答“不”時也回覆“噢不！”。

    測試並儲存。現在，你的聊天機器人應在你回答“不”時說“噢不！”。事實上，如果你回答除“是”之外的任何內容，它都會說“噢不！”（`if/else`程式碼塊中的__else__意為__否則__）。

    ![Testing a yes/no reply](images/chatbot-if-else-test.png)

--- hints ---
--- hint ---
現在，__如果__你回答“是”，你的聊天機器人應說“很高興聽到這句話！”，但如果你回答__其他__內容，就會說“噢不！”。
--- /hint ---
--- hint ---
以下是你將需要使用的程式碼塊：
![Blocks for a yes/no reply](images/chatbot-if-else-blocks.png)
--- /hint ---
--- hint ---
你的程式碼應如下所示：
![Code for a yes/no reply](images/chatbot-if-else-code.png)
--- /hint ---
--- /hints ---

+ 你可以將任何程式碼放進`if/else`程式碼塊中，並非只有使你的聊天機器人說話的程式碼。如果你點選聊天機器人的**Costume**（造型）選項卡，你會看到其不止有一種造型。

    ![chatbot costumes](images/chatbot-costume-view.png)

+ 你能否更改聊天機器人的造型以匹配你的回覆？

    測試並儲存。你會看到聊天機器人的面部表情會根據你的回答改變。

    ![Testing a changing costume](images/chatbot-costume-test.png)

--- hints ---
--- hint ---
現在，你的聊天機器人還應根據收到的答案__切換造型__。
--- /hint ---
--- hint ---
以下是你將需要使用的程式碼塊：
![Blocks for a changing costume](images/chatbot-costume-blocks.png)
--- /hint ---
--- hint ---
你的程式碼應如下所示：
![Code for a changing costume](images/chatbot-costume-code.png)
--- /hint ---
--- /hints ---

+ 你是否注意到了你的聊天機器人造型與你上次跟它說話時所變更的造型相同？你能否解決這個問題？

    ![Costume bug](images/chatbot-costume-bug-test.png)

    測試並儲存：執行你的程式碼並輸入“不”，使你的聊天機器人看起來不開心。當你再次執行程式碼時，你的聊天機器人應在詢問你的名字之前變回笑臉。

    ![Testing a costume fix](images/chatbot-costume-fix-test.png)

--- hints ---
--- hint ---
__點選子圖__時，你的聊天機器人應首先__切換造型__，變為笑臉。
--- /hint ---
--- hint ---
以下是你將需要新增的程式碼塊：
![Blocks for a costume fix](images/chatbot-costume-fix-blocks.png)
--- /hint ---
--- hint ---
你的程式碼應如下所示：
![Code for a costume fix](images/chatbot-costume-fix-code.png)
--- /hint ---
--- /hints ---

--- challenge ---
## 挑戰：更多判定

對你的聊天機器人進行程式設計來提出另一個問題 - 用“是”或“不”回答的問題。你能否使你的聊天機器人對回答做出反應？

![screenshot](images/chatbot-joke.png)
--- /challenge ---
