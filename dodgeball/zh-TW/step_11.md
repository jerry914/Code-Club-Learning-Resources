## 挑戰：更多生命

目前的遊戲設計中，角色在被擊中時會回到一開始的位置。 你可以給角色有 3 點的`生命`{:class="block3variables"}，讓角色在被擊中時扣 1 點生命嗎？ 遊戲的運作方式可以像這樣：

+ 每次遊戲開始，角色有 3 點生命值。
+ 每當角色被擊中，它就會失去 1 點生命，**並且**返回到初始位置。
+ 如果沒有生命值，遊戲就以失敗結束。