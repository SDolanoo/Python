from turtle import Turtle
import random
from snake import Snake

number = []
for i in range(-280,300, 20):
    number.append(i)
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.move_food()

    def move_food(self):
        random_x = random.choice(number)
        random_y = random.choice(number)
        self.goto(random_x, random_y)