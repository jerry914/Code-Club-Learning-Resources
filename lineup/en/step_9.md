## Finish the game

--- task ---

To finish the game, [find and download an image of a stage curtain](https://www.google.co.uk/search?q=stage+curtain&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjKg9O1k8_VAhXSL1AKHe1HDMIQ_AUICigB&biw=1362&bih=584){:target="_blank"}.

Import this image as a sprite.

[[[generic-scratch3-add-sprite-from-file]]]

--- /task ---

--- task ---

Position the new curtain sprite at `x:0 y:0`{:class="block3motion"}, and then change its size so that it fills the screen. Make sure it is visible.

```blocks3
when flag clicked
go to x: (0) y: (0)
set size to (110) %
show
```

--- /task ---

--- task ---

Then, in the scripts for your character sprite, add a `broadcast`{:class="block3events"} with the message 'curtain up' to the end of the `when flag clicked`{:class="block3events"} script.

```blocks3
when flag clicked
erase all
generate positions (4) (10) ::custom
stamp sprites (4) (10) ::custom
go to x: (0) y: (0)
go to front
set size to (100) %
say [Find me] for (2) seconds
go back (1) layers
set size to (40) %
go to x: (item (1 v) of [x_positions v]) y: (item (1 v) of [y_positions v])
+broadcast (curtain up v)
```

--- /task ---

--- task ---

When the curtain sprite receives the `broadcast`{:class="block3events"}, the sprite needs to move upwards for 10 seconds so that it looks like the curtain is raised to reveal the stamps. Then the curtain should drop again, so the curtain sprite needs to move downwards.

--- no-print ---

It should look like this:

![demo 2](images/demo_2.gif)

--- /no-print ---

Try to do this by yourself, and use the hints if you need help.

--- hints --- 
--- hint ---

For the curtain sprite, you need a script that does the following things:
  1. When the curtain sprite receives the `broadcast`{:class="block3events"}
  1. Bring the curtain sprite to the `front`{:class="block3looks"}
  1. `Wait`{:class="block3control"} a little bit while the character sprite costumes get stamped
  1. `Glide`{:class="block3motion"} the curtain sprite upwards so it ends up near the top of the Stage
  1. `Hide`{:class="block3looks"} the curtain
  1. Start a loop that counts down for 10 seconds
  1. When the time is over, `show`{:class="block3looks"} the curtain sprite
  1. `Glide`{:class="block3motion"} the curtain sprite back to its original position
  
--- /hint --- 
--- hint ---

Here are the blocks you need:

```blocks3
go to front

show

hide

glide (1) secs to x: (0) y: (0)

glide (1) secs to x: (0) y: (0)

set [timer v] to []

change [timer v] by ()

wait () secs

wait () secs

repeat ()
end
when I receive [curtain up v]
```

--- /hint --- 
--- hint ---

 This is the completed script:
 
 ```blocks3
when I receive [curtain up v]
go to front
wait (1) seconds
glide (1) secs to x: (0) y: (300)
hide
set [timer v] to [10]
repeat (10)
wait (1) seconds
change [timer v] by (-1)
end
show
glide (1) secs to x: (0) y: (0)
```

--- /hint --- 
--- /hints ---
--- /task ---

The very last part is to let the player know if they've won.

--- task ---

In the scripts for the the character sprite, add code so that, when the sprite is clicked, the sprite says `You've found me`{:class="block3looks"}, and all the scripts in the game stop.
	
```blocks3
when this sprite clicked
say [You found me]
stop [all v]
```

--- /task ---

