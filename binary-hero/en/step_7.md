## More custom blocks

The newest section of code is difficult to read, so you're going to use more custom blocks to make it simpler.

--- task ---

Make another block called `clear song`{:class="block3myblocks"} that deletes all items from both lists. Use this block before adding numbers back intothe lists.

![note-sprite](images/note-sprite.png)

```blocks3
define clear song
delete (all v) of [notes v]
delete (all v) of [times v]
```

When you test your code, it should work just as it did before.

```blocks3
define load 'happy birthday'
+clear song ::custom
add [1] to [notes v]
add [5] to [notes v]
```

--- /task ---

--- task ---

So that your code is even easier to read, make another block that allows you to specify a note to be played and a time to play the note at.

[[[generic-scratch3-make-block-parameters]]]

--- hints ---
--- hint ---

Make a block that takes a number as `note`{:class="block3variables"} and a number as `time`{:class="block3variables"} and `adds`{:class="block3variables"} each number to the correct list.

--- /hint ---
--- hint ---

This is what your code should look like:

```blocks3
define Add note (note) at (time) secs
add (note :: custom-arg) to [notes v]
add (time :: custom-arg) to [times v]

define load 'happy birthday'
clear song ::custom
+Add note (1) at (5) secs
+Add note (1) at (5.5) secs
+Add note (3) at (6) secs
+Add note (1) at (7) secs
+Add note (6) at (8) secs
+Add note (5) at (9) secs
```

--- /hint ---
--- /hints ---

--- /task ---
