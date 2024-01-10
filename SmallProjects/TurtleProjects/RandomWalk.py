from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pensize(10)
timmy.speed(10)

angle = [0, 90, 180, 270]
colors = ["saddle brown", "dark green", "lime green", "lawn green", "forest green"]

screen = Screen()
screen.colormode(255)

for i in range(300):
    timmy.pencolor(choice(colors))
    timmy.setheading(choice(angle))
    timmy.forward(40)




screen.exitonclick()