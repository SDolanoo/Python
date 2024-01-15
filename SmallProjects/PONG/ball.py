from turtle import Turtle
import random
from paddles import Paddles
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("gold")
        self.set_direction()

    def move_ball(self):
        self.forward(20)

    def set_direction(self):
        self.setheading(0)

    def bounce_back(self, angle):
        # ball bounce off the wall logic idk how I figured this out
        direction = angle - self.heading()
        newer_direction = direction + angle
        self.setheading(newer_direction)