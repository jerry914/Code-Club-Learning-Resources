## Flying your helicopter

Let's use the arrow keys to fly your helicopter.

--- task ---

Let's start by coding your helicopter to move up when the up arrow is pressed.

![helicopter sprite](images/helicopter-sprite.png)

```blocks3
when [up arrow v] key pressed
change y by (5)
```

--- /task ---

--- task ---

Test your code and you'll see that your helicopter's `y`{:class="block3motion"} position (up/down) changes whenever the up arrow is pressed.

--- /task ---

--- task ---

To have your helicopter move more smoothly, you can instead add code to move upwards inside your helicopter's `forever`{:class="block3motion"} loop.

![helicopter sprite](images/helicopter-sprite.png)

```blocks3
when I receive [start v]
forever
next costume
+ if <key [up arrow v] pressed ?> then
change y by (5)
end
end

-when [up arrow v] key pressed
-change y by (5)
```

--- /task ---

--- task ---

You can also code your helicopter to move to the left when the left arrow is pressed. This time you'll need to change the helicopter's `x`{:class="block3motion"} postition by `-5`.

![helicopter sprite](images/helicopter-sprite.png)

```blocks3
when I receive [start v]
forever
next costume
if <key [up arrow v] pressed ?> then
change y by (5)
end
+if <key [left arrow v] pressed ?> then
change x by (-5)
end
end
```

--- /task ---

--- task ---

Now code your helicopter to respond to the down and right arrow keys.

--- hints ---

--- hint ---

Copy the code you used to make the helicopter move up and left, changing the `keys`{:class="block3sensing"} used and `x`{:class="block3motion"} & `y`{:class="block3motion"} values

--- /hint ---

--- hint ---

You will need these blocks:

![helicopter sprite](images/helicopter-sprite.png)

```blocks3
if <> then

end

change y by (-5)

change x by (5)

<key [right arrow v] pressed ?>
```

--- /hint ---

--- hint ---

Your code should look like this:

![helicopter sprite](images/helicopter-sprite.png)

```blocks3
when I receive [start v]
forever
next costume
if <key [up arrow v] pressed ?> then
change y by (5)
end
if <key [left arrow v] pressed ?> then
change x by (-5)
end
+if <key [down arrow v] pressed ?> then
change y by (-5)
end
+if <key [right arrow v] pressed ?> then
change x by (5)
end
end
```

--- /hint ---

--- /hints ---

--- /task ---
