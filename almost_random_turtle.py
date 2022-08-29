from random import randint
from time import sleep
import turtle
from random import choice

while True:
    B = randint(5,25)
    C = [-90,-45,45,90]
    turtle.forward(B)
    turtle.right(choice(C))