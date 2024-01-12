from turtle import Turtle
FONT = ("Times New Roman", 24, "normal")
class Scoreboard(Turtle):
    # scoreboard subclass
    def __init__(self):
        self.count = 0
        super().__init__()
        # classic Turtle setup
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.count}", False, align="center", font=FONT)
        self.shapesize(2, 2)

    def get_score(self):
        # counts number of food eaten by snake and refreshes score on the board
        self.count += 1
        self.clear()
        self.write(f"Score:{self.count}", False, align="center", font=FONT)

    def game_over(self):
        # everything has to end at some point
        self.goto(0,0)
        self.write(f"!!!GAME OVER, BITCH!!!", False, align="center", font=FONT)
