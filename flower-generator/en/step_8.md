## Flower patterns

You can also use your `draw flower`{:class="block3myblocks"} block to create neat flower patterns. 

--- task ---

Create a flower or a combination of flowers that you like. Here's an example:

![flower sprite](images/flower-sprite.png)

```blocks3
when [p v] key pressed
erase all
go to x: (-150) y: (100)
draw flower (150) (80) (7) :: custom
draw flower (130) (35) (20) :: custom
```

--- /task ---

--- task ---

Press <kbd>p</kbd> to see your flower. The example looks like this:

![a flower pattern](images/flower-for-pattern-example.png)  

--- /task ---

Before you can create your pattern, you should clear the Stage of any leftover flowers.

--- task ---

Click on the `erase all` block in the Pen tab.

```blocks3
erase all
```

--- /task ---

--- task ---

Right-click on the Flower sprite and `hide`{:class="block3looks"} it so it doesn't appear on the Stage. (You can `show`{:class="block3looks"} the sprite again if you need to see where it is.)

--- /task ---

--- task ---

Now draw a row of these flowers across the top of the Stage. Here is some example code, in which you might need to adjust the numbers so it works with your flower:

![flower sprite](images/flower-sprite.png)

```blocks3
when [p v] key pressed
erase all
go to x: (-150) y: (100)
repeat (4) 
  draw flower (150) (80) (7) :: custom
  draw flower (130) (35) (20) :: custom
  change x by (100)
end
```

--- /task ---

--- task ---

Press `p` to see a row of flowers: 

![4 flowers in a row](images/flower-pattern-row-example.png)

--- /task ---

--- task ---

Add another loop to create more rows of flowers. This example adds a `repeat 3`{:class="block3control"} loop to create three rows. 

![flower sprite](images/flower-sprite.png)

```blocks3
when [p v] key pressed
erase all
go to x: (-150) y: (100)
repeat (3) 
  repeat (4) 
    draw flower (150) (80) (7) :: custom
    draw flower (130) (35) (20) :: custom
    change x by (100)
  end
  set x to (-150)
  change y by (-100)
end
```
 
--- /task ---

--- task ---

Press <kbd>p</kbd> to create a grid of flowers: 

![a 4 x 4 grid of flowers](images/flower-pattern-rows-example.png)

--- /task ---

Do you want to speed up the drawing of the flowers? 

--- task ---

Right-click on the `draw flower`{:class="block3myblocks"} definition block and then click on **edit**. Click on the **Run without screen refresh** box. 

![turn no refresh option off](images/flower-no-refresh.png)

Now the flowers get drawn more quickly. 

--- /task ---

You can also change the colour of the Stage.

--- task ---

Click on **Choose a backdrop**, and then click on **Paint**. Create an orange backdrop by using the Fill tool in Bitmap mode. 

![paint new backdrop](images/flower-orange-backdrop.png)

If you use orange for the backdrop and the Flower sprite, then the numbers for different colours will match for the sprite and the backdrop. 

--- /task ---

--- task ---

Now you can use the `set colour effect`{:class="block3looks"} on the Stage to change the colour of the backdrop.

![stage sprite](images/stage-sprite.png)

```blocks3
when [p v] key pressed
set [color v] effect to (30)
```

--- /task ---

--- task ---

Try to create a pattern you like. 

Here's an example: 
 
![flowers on a green background](images/flower-pattern-background.png)
 
--- /task ---

When you put it all together, you can create an amazing effect:

![animation of lots of flowers](images/flower-gen-example.gif)
