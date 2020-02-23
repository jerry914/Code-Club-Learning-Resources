## Adding a score

Let's make things more interesting by keeping score.

--- task ---

To keep the player's score, you need a place to put it. Create a new `variable`{:class="block3variables"} called `score`{:class="block3variables"}.

[[[generic-scratch3-add-variable]]]

--- /task ---

--- task ---

When a new game is started (by clicking the flag), you should set the player's score to 0. Add this code to the top of the balloon's `when flag clicked`{:class="block3events"} code:

![balloon sprite](images/balloon-sprite.png)

```blocks3
when flag clicked
+ set [score v] to [0]
show
switch costume to (balloon1-a v)
```

--- /task ---

--- task ---

Whenever a balloon is popped, you need to add 1 to the score:

![balloon sprite](images/balloon-sprite.png)

```blocks3
when this sprite clicked
switch costume to (burst v)
start sound (pop v)
wait (0.3) seconds
+change [score v] by (1)
hide
```

--- /task ---

--- task ---

Run your program again and click the balloon. Does your score change?

--- /task ---

