import turtle
import pandas

# screen and turtle setup
screen = turtle.Screen()
screen.title("I.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()
def write_state(x, y):
    # function to write state's name on the guessed state
    timmy.goto(x, y)
    timmy.write(f"{answer_state}", False, align="center")


# reading pandas file
states = pandas.read_csv("50_states.csv")

count = 0

while True:
    # while loop for continuous game
    answer_state = screen.textinput(title="Guess the State",
                                    prompt=f"What's another state's name \n"
                                           f"Your score is {count}/50").title()
    # getting the state name, x and y coordinates to use it in for loop to search if user guessed correctly
    state_answer = states[states.state == answer_state]
    x_cor = round(state_answer["x"[0]], 1)
    y_cor = round(state_answer["y"[0]], 1)
    for state_name in states.state:
        if answer_state == state_name:
            write_state(int(x_cor), int(y_cor))
            count += 1
        else:
            continue


# TODO 1. use csv to check answer against all of the states ✔️
# TODO 2. make input a capital name  ✔️
# TODO 3. written state's name should appear on the state's location✔️
# TODO 4. if wrong nothing happens✔️
# TODO 5. keep track of correct guesses ✔️
# TODO 6. work with and use the data✔️