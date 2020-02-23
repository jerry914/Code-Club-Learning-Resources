## Ask the question

Let's ask the player to name the flag for a particular country.

--- task ---

In the flag sprite, `broadcast the message`{:class="block3events"} 'announce country' immediately after the block that clones the flags.

![Flag sprite](images/flag-sprite.png)

```blocks3
when green flag clicked
create flag list :: custom
delete (all v) of [chosen flags v]
repeat (6)
    choose random flag :: custom
end
set [correct answer v] to (item (pick random (1) to (length of [chosen flags v])) of [chosen flags v])
clone flags :: custom
+ broadcast (announce country v)

```

[[[generic-scratch3-broadcast-message]]]

--- /task ---

--- task ---

Add a new sprite of your choice to be your quiz master. The quiz master in the example is the sprite called Abby.

![Abby sprite](images/bear-sprite.png)

--- /task ---

--- task ---

Add some code to the quiz master sprite so that, when the sprite receives the `announce country`{:class="block3events"} broadcast, it tells the player to click on the country name that is stored in the variable `correct answer`{:class="block3variables"}.

![Character sprite](images/char-sprite.png)

--- hints ---
--- hint ---

`When I receive`{:class="block3events"} the broadcast, `say`{:class="block3looks"} 'click on `correct answer`{:class="block3variables"}'.

--- /hint ---

--- hint ---

Here are the code blocks you need:

```blocks3
(join [click on] [])

(correct answer)

say [] for (2) seconds

when I receive [announce country v]
```

--- /hint ---

--- hint ---

This is what your code should look like:

```blocks3
when I receive [announce country v]
say (join [click on] (correct answer :: variables)) for (2) seconds
```

--- /hint ---

--- /hints ---
--- /task ---
