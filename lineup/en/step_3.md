## Create a grid

You are going to create a grid of stamped costumes:

![stamps in grid](images/stamp_grid.png)
	
To do this you need to know the `x`{:class="block3motion"} and `y`{:class="block3motion"} coordinates of where each stamp should be placed.

--- task ---

First, create a new block called `generate positions`{:class="block3myblocks"}. The block needs to have two 'number input' parameters. Call the two parameters `rows`{:class="block3myblocks"} and `columns`{:class="block3myblocks"}.

The values of these parameters will decide how many rows and columns your grid has.

[[[generic-scratch3-make-block]]]

```blocks3
define generate positions (rows)(columns)
```

--- /task ---

--- task ---

Create two lists, and call one of them `x_positions`{:class="block3variables"} and the other `y_positions`{:class="block3variables"}. These lists are for storing the `x`{:class="block3motion"} and `y`{:class="block3motion"} coordinates for the stamps.

--- /task ---

--- task ---

Inside your `generate positions`{:class="block3myblocks"} block, add blocks to delete all the items from both lists, so that each time the game starts, the lists are empty.

```blocks3
define generate positions (rows)(columns)
+ delete [all v] of [y_positions v]
+ delete [all v] of [x_positions v]
```

--- /task ---

--- task ---

Next, create two variables, and call one of them `x_pos`{:class="block3variables"} and the other `y_pos`{:class="block3variables"}.

--- /task ---

The `x_positions`{:class="block3variables"} list should contain ten numbers in total, and these should start at `-200`{:class="block3variables"} and go up to `200`{:class="block3variables"}.

For now, the `y_positions`{:class="block3variables"} list can just contain the number `-150`{:class="block3variables"} ten times, so that the grid only has one row.

--- task ---

Start by adding code to the `generate positions`{:class="block3myblocks"} block to set the `y_pos`{:class="block3variables"} variable to `-150`{:class="block3variables"} and the `x_pos`{:class="block3variables"} variable to `-200`{:class="block3variables"}. This is the location of the first stamped sprite.

```blocks3
define generate positions (rows)(columns)
delete [all v] of [y_positions v]
delete [all v] of [x_positions v]
+ set [y_pos v] to [-150]
+ set [x_pos v] to [-200]
```

--- /task ---

--- task ---

Next, add a `repeat`{:class="block3control"} loop to put coordinates into the lists.

The `repeat`{:class="block3control"} loop should run once for every column you want the grid to have.

The `generate positions`{:class="block3myblocks"} block takes `columns`{:class="block3myblocks"} as an input, so you can use `columns`{:class="block3myblocks"} for the `repeat`{:class="block3control"} loop.

```blocks3
define generate positions (rows)(columns)
delete [all v] of [y_positions v]
delete [all v] of [x_positions v]
set [y_pos v] to [-150]
set [x_pos v] to [-200]
+ repeat (columns :: custom-arg)
```

--- /task ---
	
Within the `repeat`{:class="block3control"} loop, add the values of `x_pos`{:class="block3variables"} and `y_pos`{:class="block3variables"} into the lists. Then you need to increase the value of `x_pos`{:class="block3variables"} by a little. How much should the value of `x_pos`{:class="block3variables"} increase by?

This is how to figure it out:
  - `x_pos`{:class="block3variables"} starts out with the value `-200`{:class="block3variables"}
  - The final time the loop `repeat`{:class="block3control"} runs, `x_pos`{:class="block3variables"} should reach the value `200`{:class="block3variables"}
  - That's a total increase of `400`{:class="block3variables"}
  - The first `x_pos`{:class="block3variables"} value is for the first column on the grid, and how many columns there are is determined by the `columns`{:class="block3myblocks"} input

So after the first `x_pos`{:class="block3variables"} value is added, each time around the loop, the value of `x_pos`{:class="block3variables"} should increase by `400 / (columns - 1)`{:class="block3operators"}

--- task ---

Add in the code that will add all the `x_pos`{:class="block3variables"} and `y_pos`{:class="block3variables"} values into the `x_positions`{:class="block3variables"} and `y_positions`{:class="block3variables"} lists.
	
--- hints --- 
--- hint ---

Within the loop, you need to add `x_pos`{:class="block3variables"} to the `x_positions`{:class="block3variables"} list, and add the `y_pos`{:class="block3variables"} to the `y_positions`{:class="block3variables"} list.
Then `x_pos`{:class="block3variables"} variable needs to increase by `400 / (columns -1)`{:class="block3operators"} each time the loop repeats.

--- /hint --- 
--- hint ---

This shows the additional blocks you need to add into your script.

```blocks3
define generate positions (rows)(columns)
delete [all v] of [y_positions v]
delete [all v] of [x_positions v]
set [y_pos v] to [-150]
set [x_pos v] to [-200]
repeat (columns :: custom-arg)
end

(x_pos)
(y_pos)

add () to [x_positions v]

add () to [y_positions v]

change [x_pos v] by ()
(columns ::custom
() / () 
() - ()
```

--- /hint --- 
--- hint ---

Here is the completed script for the `generate positions`{:class="block3myblocks"} block:

```blocks3
define generate positions (rows)(columns)
delete [all v] of [y_positions v]
delete [all v] of [x_positions v]
set [y_pos v] to [-150]
set [x_pos v] to [-200]
repeat (columns :: custom-arg)
+ add (x_pos) to [x_positions v]
+ add (y_pos) to [y_positions v]
+ change [x_pos v] by ((400) / ((columns :: custom-arg) - (1)
```

--- /hint --- 
--- /hints ---
--- /task ---
