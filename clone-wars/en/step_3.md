## Lightning bolts

Now you are going to give the spaceship the ability to fire lightning bolts!

--- task ---

Add the `Lightning` sprite from the Scratch library.  

[[[generic-scratch3-sprite-from-library]]]

--- /task ---

--- task ---

When the game starts, the `Lightning` sprite should be hidden until the spaceship fires its laser cannons.

Add this code to the `Lightning` sprite:

![lightning sprite](images/lightning-sprite.png)

```blocks3
when green flag clicked
hide
```

--- /task ---

At the moment, the lightning bolt is really big compared to the spaceship!

--- task ---

Below the code that the `Lightning` sprite already has, add some blocks to make the sprite smaller and to turn it upside down.

![lightning sprite](images/lightning-sprite.png)

```blocks3
set size to (25) %
point in direction (-90)
```

Now it looks like it fires pointy end–first out of the spaceship.

--- /task ---

--- task ---

Add some new code to the `Spaceship` sprite to create a new clone of the lightning bolt if the <kbd>space</kbd> key is pressed.

--- hints ---

--- hint ---

`When the green flag is clicked`{:class="block3events"}, keep checking `forever`{:class="block3control"} `if`{:class="block3control"} the `space key is pressed`{:class="block3sensing"}, and in that case `create a clone of the Lightning`{:class="block3control"} sprite.	

--- /hint ---

--- hint ---

Here are the blocks you need:

```blocks3
if <> then
end

forever
end

create clone of (Lightning v)

<key (space v) pressed?>

when flag clicked
```

--- /hint ---

--- hint ---

Here is what your new code should look like:

![rocket sprite](images/rocket-sprite.png)

```blocks3
when flag clicked
forever
	if <key (space v) pressed?> then
		create clone of (Lightning v)
	end
end
```

--- /hint ---

--- /hints ---

--- /task ---

--- task ---

Whenever the game creates a `Lightning` sprite clone, the clone should appear and then move upwards until it reaches the top of the Stage. Then the clone should disappear.

Add this code to the `Lightning` sprite so that clones of it move upwards until they touch the edge of the Stage, and then they get deleted.

![lightning sprite](images/lightning-sprite.png)

```blocks3
	when I start as a clone
	go to (Spaceship v)
    show
	repeat until <touching (edge v) ?>
		change y by (10)
	end
	delete this clone
```

--- /task ---

--- task ---

Press the <kbd>space</kbd> key to test whether the lightning bolt moves correctly.

--- /task ---

