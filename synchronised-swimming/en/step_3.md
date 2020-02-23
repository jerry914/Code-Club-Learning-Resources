## Changing costume

Hmm, this would look better if the cat sprite changed direction when it turns left. 

--- task ---

Click on 'Costumes' and delete the 'cat flying-a' costume.

![costumes tab and delete icon highlighted on costume](images/swim-delete-a.png) 

--- /task ---

--- task ---

Rename the remaining costume from 'cat flying-b' to 'right'. 

![name right highlighted in costumes tab](images/swim-costume-right.png)

--- /task ---

--- task ---

Right-click on the costume and choose duplicate to create a copy. 

![costume menu with duplicate highlighted](images/swim-costume-duplicate.png)

--- /task ---

--- task ---

Click 'Flip Horizontal' to reverse the copy and then name it 'left'. 

Your costumes should look like this:

![new costume facing left with flip icon and name highlighted](images/swim-costume-left.png)

--- /task ---

--- task ---

Click 'Code' to return to your code and add blocks to change the costume when the direction is changed. 

![swimmer sprite](images/swimmer-sprite.png)

```blocks3
when [left arrow v] key pressed
+switch costume to (left v)
turn ccw (15) degrees

when [right arrow v] key pressed
+switch costume to (right v)
turn cw (15) degrees
```

--- /task ---

--- task ---

Test your code by swimming around the stage using the arrow keys. 

![sprite facing left](images/swim-test-left.png)

--- /task ---
