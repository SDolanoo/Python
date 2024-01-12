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

# key bindings
screen.listen()
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")

game_is_on = True
# let the game on! also update with time.sleep followed by snake.move() for the game to keep moving
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(apple) < 15:
        apple.move_food()
        snake.new_body()
        scoreboard.get_score()
    # detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        print("you lost")
        game_is_on = False
        scoreboard.game_over()
    # detect collision with snake tail
    for body_num in range(len(snake.all_bodies) - 2, 0, -1):
        new_x = snake.all_bodies[body_num].xcor()
        new_y = snake.all_bodies[body_num].ycor()
        if snake.head.xcor() == new_x:
            if snake.head.ycor() == new_y:
                game_is_on = False
                scoreboard.game_over()


screen.exitonclick()