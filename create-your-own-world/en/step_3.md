## Solid walls

--- task ---

Test your `player` sprite again. Do you see that it can walk through the light grey walls.

![screenshot](images/world-walls.png)

--- /task ---

--- task ---

To fix this, you need to make the `player` sprite move back if it touches a light grey wall. Here's the code you need to add inside your `forever`{:class="block3control"} block below the direction blocks:

![player](images/player.png)

```blocks3
when flag clicked
forever
	if <key (up arrow v) pressed? > then
		point in direction (0)
		move (4) steps
	end
	if <key (left arrow v) pressed? > then
		point in direction (-90)
		move (4) steps
	end
		if <key (down arrow v) pressed? > then
		point in direction (-180)
		move (4) steps
	end
		if <key (right arrow v) pressed? > then
		point in direction (90)
		move (4) steps
	end
+	if < touching color [#BABABA]? > then
	move (-4) steps
	end
end
```

--- /task ---

--- task ---

Try to make the `player` sprite move through a wall. If your new code works, this shouldn't be possible.

![screenshot](images/world-walls-test.png)

--- /task ---
