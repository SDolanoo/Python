from turtle import Turtle

starting_positions = [
    [(-330, 40), (-330, 20), (-330, 0), (-330, -20), (-330, -40)],
    [(330, 40), (330, 20), (330, 0), (330, -20), (330, -40)]
                      ]


class Paddles:
    def __init__(self, player_number):
        self.player_num = player_number
        self.paddle_body = []
        self.new_paddle(self.player_num)

    def new_paddle(self, player_num):
        for position in starting_positions[player_num]:
            paddle = Turtle()
            paddle.penup()
            paddle.color("white")
            paddle.shape("square")
            paddle.goto(position)
            self.paddle_body.append(paddle)

    def go_up(self):
        for paddle in self.paddle_body:
            paddle.setheading(90)
            paddle.forward(20)
            print()

    def go_down(self):
        for paddle in self.paddle_body:
            paddle.setheading(270)
            paddle.forward(20)

    def give_back_body_num(self):
        y_cord_list = []
        for body_num in range(len(self.paddle_body)):
            y_coords = self.paddle_body[body_num].ycor()
            y_cord_list.append(y_coords)
        return y_cord_list