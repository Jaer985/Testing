from random import randint
from time import sleep
import turtle
from random import choice

# Set up the screen
screen = turtle.Screen()
screen.setup(800, 600)

# Set up the turtle
t = turtle.Turtle()
t.shape("turtle")
while True:
    B = randint(5, 50)  # Random length of the line
    C = [-90, -75, -60, -45, -30, 30, 45, 60, 75, 90]  # List of random angles
    t.right(choice(C))  # Move turtle in a random direction
    t.forward(B)  # Draw the line with random length
    sleep(1)  # Pause for 1 second

    # Add some color variation
    if randint(0, 1):
        t.color("red")
    else:
        t.color("blue")

# Make sure to close the turtle graphics window when you're done
screen.mainloop()
