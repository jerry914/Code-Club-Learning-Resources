--- challenge ---
## 挑戰：顯示太空站

除了太空人的名字，該 web 服務還提供他們所在的太空站（如 ISS。）

你能否新增到你的指令碼，使其還能列印出太空人所在的太空站。 

範例：

```
People in Space:  3
Yuri Malenchenko in ISS
Timothy Kopra in ISS
Timothy Peake in ISS
```
--- hints ---
--- hint ---
你需要在迴圈 `for p in people:` 中新增程式碼來印出狀態。你可以藉由用逗號分隔來印出多個項目。
--- /hint ---
--- hint ---
你使用`p[name]`來取得`name`的值 - 那你要如何取得`craft`的值？
--- /hint ---
--- hint ---
更改你的迴圈，讓它看起來像這樣：
---
for p in people:
  print(p['name'], ' in ', p['craft'])
---
--- /hint ---


--- /hint ---

--- /hints ---


--- /challenge ---