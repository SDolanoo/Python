from turtle import Screen
from paddles import Paddles
import time
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
# screen setup
screen.setup(width=700, height=500)
screen.bgcolor("black")
screen.title("PONG Game")
screen.tracer(0)

paddle_p1 = Paddles(0)
paddle_p2 = Paddles(1)
ball = Ball()
scoreboard = Scoreboard()
scoreboard.draw_score()
scoreboard.draw_court()

screen.update()

screen.listen()
# paddles keybinding
screen.onkey(fun=paddle_p1.go_up, key="w")
screen.onkey(fun=paddle_p1.go_down, key="s")
screen.onkey(fun=paddle_p2.go_up, key="Up")
screen.onkey(fun=paddle_p2.go_down, key="Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move_ball()


    if ball.ycor() > 240 or ball.ycor() < -240:
        # call ball bounce logic
        ball.bounce_back(180)

    if ball.xcor() >= 320:
        # if statement used to bounce ball back if collision happen
        if paddle_p2.paddle_body[4].ycor() - 10 <= ball.ycor() <= paddle_p2.paddle_body[0].ycor() + 10:
            # receive the coordinates of each paddle body
            paddle_y_coords = paddle_p2.give_back_body_num()
            # use min function to find the index of the paddle
            closest_index = min(range(len(paddle_y_coords)), key=lambda i: abs(paddle_y_coords[i] - ball.ycor()))
            # list of angles to bounce ball back according to the paddle index
            angles = [135, 155, 180, 205, 225]
            # bounce ball back
            ball.setheading(angles[closest_index])
        else:
            # if the ball doesn't collide with the paddle opposite player get a point, new ball is drawn and reset
            scoreboard.p1_points += 1
            scoreboard.draw_score()
            ball.new_ball(180)
            screen.update()
            time.sleep(2)

    if ball.xcor() <= -320:
        # if statement used to bounce ball back if collision happen
        if paddle_p1.paddle_body[4].ycor() - 10 <= ball.ycor() <= paddle_p1.paddle_body[0].ycor() + 10:
            # receive the coordinates of each paddle body
            paddle_y_coords = paddle_p1.give_back_body_num()
            # use min function to find the index of the paddle
            closest_index = min(range(len(paddle_y_coords)), key=lambda i: abs(paddle_y_coords[i] - ball.ycor()))
            # list of angles to bounce ball back according to the paddle index
            angles = [45, 25, 0, 335, 315]
            # bounce ball back
            ball.setheading(angles[closest_index])
        else:
            # if the ball doesn't collide with the paddle opposite player get a point, new ball is drawn and reset
            scoreboard.p2_points += 1
            scoreboard.draw_score()
            ball.new_ball(0)
            screen.update()
            time.sleep(2)

    if scoreboard.p1_points == 3 or scoreboard.p2_points == 3:
        # if one player score 3 times game will end
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()
