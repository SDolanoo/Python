from turtle import Turtle
starting_positions = [(0,0), (-20,0), (-40,0)]
class Snake:

    def __init__(self):
        self.all_bodies = []
        self.make_snake()
        self.head = self.all_bodies[0]
    def make_snake(self):
        # make snake body based on predefined list of positions
        for position in starting_positions:
            new_snake_body = Turtle()
            new_snake_body.penup()
            new_snake_body.shape("square")
            new_snake_body.color("white")
            new_snake_body.goto(position)
            self.all_bodies.append(new_snake_body)

    def move(self):
        # move the snake body on the screen. Second body part follows head, third part follows second and so on.
        for body_num in range(len(self.all_bodies) - 1, 0, -1):
            new_x = self.all_bodies[body_num - 1].xcor()
            new_y = self.all_bodies[body_num - 1].ycor()
            self.all_bodies[body_num].goto(new_x, new_y)
        self.all_bodies[0].forward(20)

    def new_body(self):
        # make a new part of the body
        new_snake_body = Turtle()
        new_snake_body.penup()
        new_snake_body.shape("square")
        new_snake_body.color("white")
        for body_num in range(len(self.all_bodies) - 1, 0, -1):
            new_x = self.all_bodies[body_num - 1].xcor()
            new_y = self.all_bodies[body_num - 1].ycor()
            new_snake_body.goto(new_x, new_y)
        self.all_bodies.append(new_snake_body)

    def up(self):
        # snake head go up
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        # snake head go down
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        # snake head go left
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        # snake head go right
        if self.head.heading() != 180:
            self.head.setheading(0)
