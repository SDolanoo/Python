from turtle import Screen
from paddles import Paddles
import time
from ball import Ball

screen = Screen()
screen.setup(width=700, height=500)
screen.bgcolor("black")
screen.title("PONG Game")
screen.tracer(0)

paddle_p1 = Paddles(0)
paddle_p2 = Paddles(1)
ball = Ball()

screen.update()

screen.listen()
screen.onkey(fun=paddle_p1.go_up, key="w")
screen.onkey(fun=paddle_p1.go_down, key="s")
screen.onkey(fun=paddle_p2.go_up, key="Up")
screen.onkey(fun=paddle_p2.go_down, key="Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move_ball()


    if ball.ycor() > 240 or ball.ycor() < -240:
        # call ball bounce logic
        ball.bounce_back(180)


    if ball.xcor() >= 320:
        if paddle_p2.paddle_body[4].ycor() -10 <= ball.ycor() <= paddle_p2.paddle_body[0].ycor() +10:
            paddle_y_coords = paddle_p2.give_back_body_num()
            closest_index = min(range(len(paddle_y_coords)), key=lambda i: abs(paddle_y_coords[i] - ball.ycor()))
            angles = [135, 155, 180, 205, 225]
            ball.setheading(angles[closest_index])
        else:
            game_is_on = False

    if ball.xcor() <= -320:
        if paddle_p1.paddle_body[4].ycor() -10 <= ball.ycor() <= paddle_p1.paddle_body[0].ycor() +10:
            paddle_y_coords = paddle_p1.give_back_body_num()
            closest_index = min(range(len(paddle_y_coords)), key=lambda i: abs(paddle_y_coords[i] - ball.ycor()))
            angles = [45, 25, 0, 335, 315]
            ball.setheading(angles[closest_index])
        else:
            game_is_on = False










screen.exitonclick()