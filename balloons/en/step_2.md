## Animating a balloon

--- task ---

Open a new Scratch project.

**Online**: open a [new online Scratch project](http://rpf.io/scratch-new){:target="_blank"}.

If you have a Scratch account you can make a copy by clicking **Remix**.

**Offline**: open a new project in the offline editor.

If you need to download and install the Scratch offline editor, you can find it at [rpf.io/scratchoff](http://rpf.io/scratchoff){:target="_blank"}.

--- /task ---

--- task ---

Delete the cat sprite.

--- /task ---

--- task ---

Add in a new balloon sprite, and a suitable stage backdrop.

![backdrop and balloon sprite](images/balloons-balloon.png)

--- /task ---


--- task ---

Add this code to your balloon, so that it bounces around the screen:

![balloon sprite](images/balloon-sprite.png)

```blocks3
	when flag clicked
	go to x:(0) y:(0)
	point in direction (45 v)
	forever
		move (1) steps
		if on edge, bounce
	end
```

--- /task ---

--- task ---

Test out your balloon. Does it move too slowly? Change the numbers in your code if you want to speed it up a bit.

--- /task ---

--- task ---

Did you also notice that your balloon flips as it moves around the screen?

![balloon upside down](images/balloons-flip.png)

Balloons don't move like this! To fix this, click on the balloon sprite icon, and then click the direction.

In the 'rotation style' section, click 'Do not rotate' to stop the balloon rotating.

![rotation style option](images/balloons-lock-annotated.png)

--- /task ---

--- task ---

Test your program again to see if the problem is fixed.

--- /task ---
