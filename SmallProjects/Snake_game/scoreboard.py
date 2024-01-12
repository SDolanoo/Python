from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        self.count = 0
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0,280)
        self.write(f"Score: {self.count}", False, align="center")
        self.shapesize(2, 2)

    def get_score(self):
        self.count += 1
        self.clear()
        self.write(f"Score:{self.count}", False, align="center")