from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("gold")
        self.setheading(0)

    def new_ball(self, direction):
        # function for setting a ball in the middle and set the
        # heading direction to opposite direction of scoring player
        self.goto(0, 0)
        self.setheading(direction)

    def move_ball(self):
        # function to move the ball ahead
        self.forward(20)

    def bounce_back(self, angle):
        # ball bounce off the wall logic idk how I figured this out
        direction = angle - self.heading()
        newer_direction = direction + angle
        self.setheading(newer_direction)