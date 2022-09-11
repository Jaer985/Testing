from random import randint
from time import sleep
import turtle
from random import choice

while True:
    B = randint(5,50)
    C = [-90,-75,-60,-45,-30,30,45,60,75,90]
    turtle.right(choice(C))
    turtle.forward(B)
    sleep(1)