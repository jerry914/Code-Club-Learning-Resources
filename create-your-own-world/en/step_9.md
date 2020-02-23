## Challenge: add an enemy

If you want, you can also add patrolling enemies to your game. If the `player` sprite touches an enemy, the game ends.

+ Your game already contains an `enemy` sprite. Add code to the `enemy` sprite so that it only appears in room 2.

+ Add code to move the `enemy` sprite and to end the game if the `enemy` sprite touches the `player` sprite. It's easier to do this in separate code blocks. Here's how your `enemy` sprite code might look:

```blocks3
when flag clicked
forever
if <(room :: variables)=[2]> then
show
else
hide

when flag clicked
forever
if <touching (player v)?> then
stop [all v]

when flag clicked
go to x: (170) y:(0)
forever
repeat (130)
change x by (-1)
end
repeat (130)
change x by (1)
```

+ Test out your new code to make sure that:
	+ The `enemy` sprite only visible in room 2
	+ The `enemy` sprite patrols the room
	+ The game ends if the `player` sprite touches the `enemy` sprite

Can you create another `enemy` sprite in room 3 that patrols up and down through the gap in the wall?

![screenshot](images/world-enemy2.png)

