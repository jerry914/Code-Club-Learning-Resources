## Spaceship explosion

When a hippo touches your spaceship, the spaceship should explode!

--- task ---

Select the `Spaceship` sprite and rename its costume 'normal'.

--- /task ---

--- task ---

Draw another costume of an exploding spaceship, and call the new costume 'hit'.

![screenshot](images/invaders-spaceship-costumes.png)

If you don't want to draw the explosion, you can select the 'Sun' costume from the Scratch library, and then use the **Color a shape** tool to change the costume's colour and face.

![screenshot](images/invaders-sun.png)

--- /task ---

--- task ---

Add some code to your `Spaceship` sprite so that it displays the 'normal' costume when the game starts, and switches to the 'hit' costume when it touches a hippo:

![rocket sprite](images/rocket-sprite.png)

```blocks3
when flag clicked
switch costume to (normal v)
wait until <touching (Hippo1 v)>?
switch costume to (hit v)
```

--- /task ---

--- task ---

Test your code. Make the spaceship collide with a hippo. Does the spaceship change to the 'hit' costume?

--- /task ---

