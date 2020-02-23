## Random obstacle

At the moment, the obstacle sprite always appears in the same place on the screen, so it's very easy to avoid. To make the game more challenging, obstacles should appear in a different position every time.

--- task ---

Make a variable called `obstacle_x`{:class="block3variables"}.

[[[generic-scratch3-add-variable]]]

--- /task ---

--- task ---

At the start of the `forever loop`{:class="block3control"}, `set obstacle_x`{:class="block3variables"} to a `random number`{:class="block3operators"}.

![obstacle sprite](images/obstacle_sprite.png)

```blocks3
when green flag clicked
forever 
+   set [obstacle_x v] to (pick random (-200) to (200))
    go to x: (0) y: (-180)
    show
    glide (1) secs to x: (0) y: (180)
    hide
    wait (1) seconds
end
```


--- /task ---

--- task ---

Use the `obstacle_x`{:class="block3variables"} variable in the `go to`{:class="block3motion"} block and the `glide`{:class="block3motion"} block.

![obstacle sprite](images/obstacle_sprite.png)

```blocks3
when green flag clicked
forever 
    set [obstacle_x v] to (pick random (-200) to (200))
    go to x: (obstacle_x :: variables +) y: (-180)
    show
    glide (1) secs to x: (obstacle_x :: variables +) y: (180)
    hide
    wait (1) seconds
end
```

--- /task ---