## Dodging balls

Your character can move and jump now, so it's time to add some balls that the character has to avoid.

--- task ---

Create a new ball sprite. You can choose any type of ball you like.

![screenshot](images/dodge-balls.png)

--- /task ---

--- task ---

Resize the ball sprite so that the character can jump over it. Try making the character jump over the ball to test whether the ball is the right size.

![screenshot](images/dodge-ball-resize.png)

--- /task ---

--- task ---

Add this code to your ball sprite:

![ball sprite](images/ball_sprite.png)

```blocks3
when green flag clicked
hide
forever 
  wait (3) seconds
  create clone of (myself v)
end
```

```blocks3
when I start as a clone
go to x: (160) y: (160)
show
repeat (22) 
  change y by (-4)
end
repeat (170) 
  change x by (-2)
  turn ccw (6) degrees
end
repeat (30) 
  change y by (-4)
end
delete this clone
```

This code creates a new clone of the ball sprite every three seconds. Each new clone moves along the top platform and then drops.

--- /task ---

--- task ---

Click the flag to test the game.

![screenshot](images/dodge-ball-test.png)

--- /task ---

--- task ---

Add more code to your ball sprite so that clones of it move across all three platforms.

![screenshot](images/dodge-ball-more-motion.png)

--- hints ---

--- hint ---

Repeat the code blocks you used to move the ball sprite clone across the first platform. You need to change the `x`{:class="block3motion"}, `y`{:class="block3motion"}, and `repeat`{:class="block3control"} numbers so that the clones follow the platforms correctly.

--- /hint ---

--- hint ---

These are the blocks you need. Make sure you add them in the correct order.

![ball sprite](images/ball_sprite.png)

```blocks3
repeat (170) 
  change x by (-2)
  turn ccw (6) degrees
end

repeat (180) 
  change x by (2)
  turn cw (6) degrees
end

repeat (30) 
  change y by (-4)
end
```

--- /hint ---

--- hint ---

The code for your ball sprite clones should look like this:

![ball sprite](images/ball_sprite.png)

```blocks3
when I start as a clone
go to x: (160) y: (160)
show
repeat (22) 
  change y by (-4)
end
repeat (170) 
  change x by (-2)
  turn ccw (6) degrees
end
repeat (30) 
  change y by (-4)
end
repeat (180) 
  change x by (2)
  turn cw (6) degrees
end
repeat (30) 
  change y by (-4)
end
repeat (170) 
  change x by (-2)
  turn ccw (6) degrees
end
delete this clone
```

--- /hint ---

--- /hints ---

--- /task ---

--- task ---

Now add some code blocks to broadcast (send) a message if your character gets hit by a ball!

Add this code to your ball sprite:

![ball sprite](images/ball_sprite.png)

```blocks3
	when I start as a clone
	forever
		if < touching (Pico walking v)? > then
			broadcast (hit v)
		end
	end
```

--- /task ---

--- task ---

Finally, add code blocks to your character sprite to make it move back to its starting position when it receives the `hit` message:

![pico walking sprite](images/pico_walking_sprite.png)

```blocks3
	when I receive [hit v]
	point in direction (90)
	go to x: (-210) y: (-120)
```	

--- /task ---

--- task ---

Test out your code. Check whether the character moves back to the start after touching a ball.

--- /task ---

