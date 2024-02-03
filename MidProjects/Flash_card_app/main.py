from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# set the data in csv file to a dictionary {'French': 'word1', 'English': 'word2'}
data_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient='records')
else:
    data_dict = data.to_dict(orient='records')


# -------------------------- Flip the card ----------------------------- #
def flip_the_card(x):
    german_word = data_dict[x]['English']
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(main_word, text=german_word, fill="white")
    canvas.itemconfig(card_image, image=back_card_image)


# ------------------------ Change main word --------------------------- #
def show_french_word(bool):
    x = random.randint(0, (len(data_dict) - 1))
    random_french_word = data_dict[x]['French']
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(main_word, text=random_french_word, fill="black")
    canvas.itemconfig(card_image, image=front_card_image)
    window.after(3000, flip_the_card, x)
    if bool is True:
        update_csv(x)


# ---------------------------- UPDATE CSV ------------------------------- #
def update_csv(x):
    data_dict.remove(data_dict[x])
    dataFrame = pandas.DataFrame(data_dict)
    dataFrame.to_csv("data/words_to_learn.csv", index=False)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

# image cards
front_card_image = PhotoImage(file="images//card_front.png")
right_image = PhotoImage(file="images//right.png")
wrong_image = PhotoImage(file="images//wrong.png")
back_card_image = PhotoImage(file="images//card_back.png")
# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=front_card_image)
canvas.grid(column=0, row=0, columnspan=2)
language = canvas.create_text(400, 150, text="French", fill="black", font=("arial", 40, "italic"))
main_word = canvas.create_text(400, 263, text="word", fill="black", font=("arial", 60, "bold"))
# labels

# buttons
right_button = Button(image=right_image, command=lambda: show_french_word(True))
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_image, command=lambda: show_french_word(False))
wrong_button.grid(column=0, row=1)

show_french_word(False)

window.mainloop()
