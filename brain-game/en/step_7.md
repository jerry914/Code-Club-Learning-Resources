## Add graphics

At the moment, the character sprite just says `yes! :)` or `no :(` to the player's answers. Add some graphics to let the player know whether their answer is correct or incorrect.

--- task ---

Create a new sprite called 'Result', and give it a 'tick/check' and a 'cross' costume.

![Sprite with tick and cross costumes](images/brain-result.png)

--- /task ---

--- task ---

Change your character sprite's code so that, instead of saying something to the player, it `broadcasts`{:class="block3events"} the messages 'correct' or 'wrong'.

![Character sprite](images/giga-sprite.png)

```blocks3
if <(answer) = ((number 1)*(number 2))> then
- say [yes! :)] for (2) seconds
+ broadcast (correct v)
else
- say [nope :(] for (2) seconds
+ broadcast (wrong v)
end
```

--- /task ---

--- task ---

Now you can use these messages to `show`{:class="block3looks"} the 'tick' or 'cross' costume. Add the following code to the 'Result' sprite:

![Result sprite](images/result-sprite.png)

```blocks3
    when I receive [correct v]
    switch costume to (tick v)
    show
    wait (1) seconds
    hide

    when I receive [wrong v]
    switch costume to (cross v)
    show
    wait (1) seconds
    hide

    when flag clicked
    hide
```

--- /task ---

--- task ---

Test your game again. You should see the tick whenever you answer a question correctly, and the cross whenever you answer incorrectly!

![Tick for correct, cross for wrong answer](images/brain-test-answer.png)

--- /task ---

Can you see that the code for `when I receive correct`{:class="block3events"} and `when I receive wrong`{:class="block3events"} is nearly identical?

So you can change your code more easily, you are going to create a custom block.

--- task ---

Select the 'Result' sprite. Then click on `My Blocks`{:class="block3myblocks"}, and then on **Make a Block**. Create a new block and call it `animate`{:class="block3myblocks"}.

![Result sprite](images/result-sprite.png)

![Create a block called animate](images/brain-animate-function.png)

--- /task ---

--- task ---

Move the code to `show`{:class="block3looks"} and `hide`{:class="block3looks"} the 'Result' sprite into the `animate`{:class="block3myblocks"} block:

![Result sprite](images/result-sprite.png)

```blocks3
define animate
show
wait (1) seconds
hide
```

--- /task ---

--- task ---

Make sure you have removed the `show`{:class="block3looks"} and `hide`{:class="block3looks"} blocks below **both** of the `switch costume`{:class="block3looks"} blocks.

Then add the `animate`{:class="block3myblocks"} block below both of the `switch costume`{:class="block3looks"} blocks. Your code should now look like this:

![Result sprite](images/result-sprite.png)

```blocks3
    when I receive [correct v]
    switch costume to (tick v)
    animate:: custom

    when I receive [wrong v]
    switch costume to (cross v)
    animate:: custom
```

--- /task ---

Because of the custom `animate`{:class="block3myblocks"} block, you now only need to make one change to your code if you want to show the 'Result' sprite's costumes a longer or shorter time.

--- task ---

Change your code so that the 'tick' or 'cross' costumes display for 2 seconds.

--- /task ---

--- task ---

Instead of `showing`{:class="block3looks"} and `hiding`{:class="block3looks"} the 'tick' or 'cross' costumes, you could change your `animate`{:class="block3myblocks"} block so that the costumes fade in.

![Result sprite](images/result-sprite.png)

```blocks3
	define animate
	set [ghost v] effect to (100)
	show
	repeat (25)
		change [ghost v] effect by (-4)
	end
	hide
```

--- /task ---

Can you improve the animation of the 'tick' or 'cross' graphics? You could add code to make the costumes fade out as well, or you could use other cool effects:

![screenshot](images/brain-effects.png)
