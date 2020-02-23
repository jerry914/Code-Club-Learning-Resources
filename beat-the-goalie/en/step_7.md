## Control the goalie

It's far too easy to score a goal! Let's allow a second player to try and save goals.

--- task ---

Click on your __Goalie__ sprite and add this code to change the goalie's x position when the left arrow is pressed.

![goalie sprite](images/goalie-sprite.png)

```blocks3
when [left arrow v] key pressed
change x by (-10)
```

--- /task ---

--- task ---

Press the left arrow to test your new code. Your goalie should move to the left.

![screenshot](images/goalie-move-left-test.png)

--- /task ---

--- task ---

Use blocks similar to the ones above to make the __Goalie__ move to the right `when the right arrow key is pressed`{:class="block3events"}.

--- hints ---

--- hint ---

Add blocks to your code so `when the right arrow key is pressed`{:class="block3events"}, the __Goalie's__ `x position is changed by 10`{:class="block3motion"}.

--- /hint ---

--- hint ---

You will need these blocks:

```blocks3
change x by (10)

when [right arrow v] key pressed
```

--- /hint ---

--- hint ---

Your code should look like this:

![goalie sprite](images/goalie-sprite.png)

```blocks3
when [right arrow v] key pressed
change x by (10)
```

--- /hint ---

--- /hints ---

--- /task ---
