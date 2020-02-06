--- challenge ---

## Challenge: Counting Down
Can you create a __new__ timer, that counts down to 0? Here's how your new timer should work:

+ Pressing buttons A and B together should reset your `timer` to 0

	![screenshot](images/clock-challenge-1.png)

+ Pressing button B should add 1 to your timer. Press it 10 times to create a 10 second timer. 

	![screenshot](images/clock-challenge-2.png)

+ Pressing button A should take 1 from your `time` variable until it gets to 0. This means you'll need a `while` loop that runs as long as the `time` is greater than (`>`) 0.

	![screenshot](images/clock-challenge-3.png)
	
## Accurate timer
Have you noticed that the timer isn't very accurate! This is because it takes time to display and scroll numbers on the micro:bit. 

Try adjusting the pause to improve the timing. You can use an `if/else` block to have shorter delays for bigger numbers that take longer to scroll. 



--- /challenge ---