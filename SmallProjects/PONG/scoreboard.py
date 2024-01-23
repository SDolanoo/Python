from turtle import Turtle

FONT = ("Times New Roman", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        self.p1_points = 0
        self.p1_cords = (-20, 210)
        self.p2_points = 0
        self.p2_cords = (20, 210)
        super().__init__()
        # classic Turtle setup
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 210)
        self.shapesize(2, 2)

    def draw_score(self):
        # function to draw a score updating itself each time a player scores
        self.clear()
        self.goto(self.p1_cords)
        self.write(self.p1_points, False, align="center", font=FONT)
        self.goto(self.p2_cords)
        self.write(self.p2_points, False, align="center", font=FONT)
        self.draw_court()

    def draw_court(self):
        # function to draw a line to split the court
        self.goto(0, -260)
        self.setheading(90)
        for i in range(30):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)
        self.penup()

    def game_over(self):
        # everything has to end at some point
        self.goto(0,0)
        if self.p1_points == 3:
            self.p1_points = "PLAYER 1"
            self.write(f"!!!GAME OVER {self.p1_points} WINS!!!", False, align="center", font=FONT)
        elif self.p2_points == 3:
            self.p2_points = "PLAYER 2"
            self.write(f"!!!GAME OVER {self.p2_points} WINS!!!", False, align="center", font=FONT)