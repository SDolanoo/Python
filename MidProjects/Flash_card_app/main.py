from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
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
front_card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_canvas.create_image(400, 263, image=front_card_image)
front_card_canvas.grid(column=0, row=0, columnspan=2)
front_card_canvas.create_text(400, 150, text="German", fill="black", font=("arial", 40, "italic"))
front_card_canvas.create_text(400, 263, text="word", fill="black", font=("arial", 60, "bold"))
# labels

# buttons
right_button = Button(image=right_image)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_image)
wrong_button.grid(column=0, row=1)


window.mainloop()