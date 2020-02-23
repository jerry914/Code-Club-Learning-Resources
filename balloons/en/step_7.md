## Lots of balloons

Popping 1 balloon isn't much of a game, so let's add lots more!

One simple way to get lots of balloons is just to right-click on the balloon sprite and click **duplicate**. This is OK if you only want a few, but what if you need 20? or 100? Are you really going to click **duplicate** that many times?

A much better way of getting lots of balloons is to _clone_ the balloon sprite.

--- task ---

Drag your balloon `when flag clicked`{:class="block3events"} code to a new `when I start as a clone`{:class="block3control"} control block.

![balloon sprite](images/balloon-sprite.png)

```blocks3
when flag clicked
set [score v] to [0]
-show
-switch costume to (balloon1-a v)
-point in direction (pick random (-90) to (180))
-go to x:(pick random (-150) to (150)) y:(pick random (-150) to (150))
-change [color v] effect by (pick random (0) to (200))
-forever
-	move (1) steps
-	if on edge, bounce
-end

+when I start as a clone
show
switch costume to (balloon1-a v)
point in direction (pick random (-90) to (180))
go to x:(pick random (-150) to (150)) y:(pick random (-150) to (150))
change [color v] effect by (pick random (0) to (200))
forever
	move (1) steps
	if on edge, bounce
end
```

--- /task ---

--- task ---

Add code to create 20 balloon clones to the `when flag clicked`{:class="block3events"} code.

![balloon sprite](images/balloon-sprite.png)

```blocks3
when flag clicked
set [score v] to [0]
+hide
+repeat (20)
create clone of (myself v)
end
```

--- /task ---

--- task ---

You should also replace the `hide`{:class="block3looks"} block in the balloon-clicking script with a `delete this clone`{:class="block3control"} block.

![balloon sprite](images/balloon-sprite.png)

```blocks3
when this sprite clicked
switch costume to (burst v)
start sound (pop v)
wait (0.3) seconds
change [score v] by (1)
-hide
+delete this clone
```

--- /task ---


--- task ---

Test your project! Now when the flag is clicked, your main balloon sprite will hide and then clone itself 20 times. When each of these 20 clones is started, they will each bounce around the screen randomly, just as they did before. See if you can pop the 20 balloons!

--- /task ---

