## Make Flappy fall

Now add a sprite called Flappy and create code it so Flappy falls down the Stage. In the next step, you will add the code to make Flappy fly when you press a key.

--- no-print ---

![flappy falling animation](images/flappy-falling.gif)

--- /no-print ---

--- task ---

Add a new sprite that has two costumes, for 'wings up' and 'wings down', and name it `Flappy`.

The parrot sprite is a good choice.

![parrot sprite](images/flappy-sprite.png)

--- /task ---

Flappy needs to be smaller.

--- task ---

Add code to `set Flappy's size to 25%`{:class="block3looks"} `when the green flag is clicked`{:class="block3events"}.

![parrot sprite](images/flappy-sprite.png)

```blocks3
when green flag clicked
set size to (25) %
```

--- /task ---


When the game starts, Flappy needs to be just left of the centre of the Stage, at coordinates `-50, 0`. 

![flappy shown at the start position](images/flappy-starting-position.png)

--- task ---

Add code to make Flappy `go to the x and y`{:class="block3motion"} starting position of `x: -50`{:class="block3motion"} and `y: 0`{:class="block3motion"}.

![parrot sprite](images/flappy-sprite.png)

```blocks3
when green flag clicked
set size to (25) %
+ go to x: (-50) y: (0)
```

[[[generic-scratch3-set-coordinates]]]

--- /task ---

--- task ---

Now make Flappy keep falling down the Stage by `forever`{:class="block3control"} `changing the sprite's y position by -3`{:class="block3motion"}.

![parrot sprite](images/flappy-sprite.png)

```blocks3
when green flag clicked
set size to (25) %
go to x: (-50) y: (0)
+ forever 
    change y by (-3)
end
```

--- /task ---

--- task ---

Test your code to make sure Flappy starts in the middle of the screen and falls to the bottom. When you drag Flappy to the top of the Stage, the sprite should fall again.

--- /task ---
