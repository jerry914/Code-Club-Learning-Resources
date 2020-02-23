--- challenge ---

## Challenge: manual control
Instead of the ball moving left and right automatically, can you allow your player to control the ball with the `a` and `d` keys?

To do this you’ll need to remove the code for moving the ball left and right.

```blocks3
when green flag clicked
forever
	go to x:(-200) y:(-140)
	repeat until <key (space v) pressed?>
-		move (10) steps
-		if on edge, bounce
	end
	repeat (15)
		change y by (10)
	end
	if <touching (goalie v)> then
		start sound (rattle v)
		broadcast (save v)
	else
		start sound (cheer v)
		broadcast (goal v)
	end
end
```

You can then add code to move the ball when the keys are pressed. Here are some code blocks to help you:

```blocks3
change x by (-5)

if <> then 
end

<key (a v) pressed>
```

--- /challenge ---
