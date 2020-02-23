## 讓鬼動起來

--- task ---

新建一個 Scratch 空白專案。

[[[generic-scratch3-new-project]]]

--- /task ---

--- task ---

添加一個名為 ghost（幽靈）的角色，還有一個合適的舞台背景。

![截圖](images/ghost-ghost.png)

[[[generic-scratch3-sprite-from-library]]]

[[[generic-scratch3-backdrop-from-library]]]

--- /task ---

--- task ---

為 ghost 角色編寫程式，讓它在綠旗被點擊時一會兒出現一會兒消失。

--- hints --- --- hint ---

只要`點一下綠旗`{:class="block3events"}，你的幽靈應該會`隱藏`{:class="block3looks"}持續`1 秒`{:class="block3control"}，然後再`顯示`{:class="block3looks"}持續`1 秒`{:class="block3control"}。 它會在畫面上`不斷的`{:class="block3control"}出沒。

--- /hint --- --- hint ---

這裡是你需要的程式積木：

![幽靈角色](images/ghost-sprite.png)

```blocks3
隱藏

顯示

重複無限次
end

等待 (1) 秒

等待 (1) 秒

當 @greenflag 被點擊
```

--- /hint --- --- hint ---

你的程式看起來應該像這樣：

![幽靈角色](images/ghost-sprite.png)

```blocks3
當 @greenflag 被點擊
重複無限次
隱藏
等待 (1) 秒
顯示
等待 (1) 秒
end
```

--- /hint --- --- /hints ---

--- /task ---

--- task ---

測試並儲存你的專案。

[[[generic-scratch3-saving]]]

--- /task ---