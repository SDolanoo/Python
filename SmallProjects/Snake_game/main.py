from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
apple = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(apple) < 15:
        apple.move_food()
        snake.new_body()
        scoreboard.get_score()
    if snake.head.xcor() == 300:
        print("you lost")



screen.exitonclick()