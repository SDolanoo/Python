from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snejk = Snake()

screen.listen()
screen.onkey(fun=snejk.left, key="a")
screen.onkey(fun=snejk.right, key="d")
screen.onkey(fun=snejk.up, key="w")
screen.onkey(fun=snejk.down, key="s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snejk.move()




screen.exitonclick()