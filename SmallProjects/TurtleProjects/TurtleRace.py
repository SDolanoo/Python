import random
from turtle import Turtle, Screen

#setting up screen, prompt for user to make a bet, list of colors to make turtles
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle wil win the race? Enter a color: \n"
                                                          "red/ blue/ gold/ brown/ purple/ black")
colors = ["red", "blue", "gold", "brown", "purple", "black"]
y_position = [-70, -40, -10, 20, 50, 80]

#list of turtles to append to with for loop
all_turtles = []
#for loop to make new objects- turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

race_is_on = False

if user_bet:
    race_is_on = True
#while loop for race to be on. Stop and choose winner according to first turtle and made bet.
while race_is_on is True:
    for turtle in all_turtles:
        move = random.randint(0,20)
        turtle.forward(move)
        if turtle.xcor() >= 150:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Your turtle ({winning_color}) made it to the finish line first! You've won!")
            else:
                print(f"Your turtle ({user_bet}) didn't make it. You lost the bet.")


screen.exitonclick()