## Add a score

The player should score a point every time Flappy makes it through a gap between pipes.

--- task ---

Make a new variable **for all sprites** and call it `score`{:class="block3variables"}.

[[[generic-scratch3-add-variable]]]

--- /task ---

Each 'Pipes' sprite clone should `wait until`{:class="block3control"} Flappy has flown past and then increase the `score`{:class="block3variables"}.

--- task ---

First, `set score to 0`{:class="block3variables"} when the game begins:

![pipes sprite](images/pipes-sprite.png)

```blocks3
when green flag clicked
+ set [score v] to [0]
set size to (200) %
hide
forever 
  create clone of (myself v)
  wait (2) seconds
end
```

--- /task ---

--- task ---

Then add the following code to the `Pipes` sprite:

![pipes sprite](images/pipes-sprite.png)

```blocks3
when I start as a clone
wait until <>
```

--- /task ---

--- task ---

Add more code so that, when Flappy's `x` position is greater than the pipe clone's `x` position, the `score`{:class="block3variables"} increases by `1` and a sound of your choice plays.

You could use the 'pop' sound if you want, or add a sound from the library, for example 'bird'.

--- hints ---

--- hint ---

You need to `wait until`{:class="block3control"} `Flappy's x position`{:class="block3sensing"} is `greater than (>)`{:class="block3operators"} the `x position`{:class="block3motion"} of `Pipes`.  

![pipes sprite](images/pipes-sprite.png)

```blocks3
when I start as a clone
+ wait until <>
```

Then `change score by 1`{:class="block3variables"} and `play a sound`{:class="block3sound"}. 

--- /hint ---

--- hint ---

Use these blocks in the correct order:

![pipes sprite](images/pipes-sprite.png)

```blocks3
when I start as a clone
wait until <>

play sound (pop v)

change [score v] by (1)

[x position v] of (Flappy v)

x position

() > ()
```

--- /hint ---

--- hint ---

Your code should look like this:

![pipes sprite](images/pipes-sprite.png)

```blocks3
when I start as a clone
wait until <([x position v] of (Flappy v)) > (x position)>
change [score v] by (1)
play sound (pop v)
```

--- /hint ---

--- /hints ---

--- /task ---

--- task ---

Test your code and make sure you score a point every time Flappy gets through a gap between pipes. Check whether the `score`{:class="block3variables"} is set to `0` when you start a new game.

--- /task ---
