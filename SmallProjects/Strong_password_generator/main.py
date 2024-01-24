from tkinter import *
from generator import Generator


window = Tk()
window.title("My password generator")
window.minsize(width=250, height=100)


def get_password(number):
    # function insert generated password into a text box. The User is able to copy the code.
    password = generator.generate_password(int(number))
    password2 = "".join(password)
    text_password.delete('1.0', END)
    text_password.insert(END, f"{password2}")


generator = Generator()
# window setup

label_question = Label(text="How long do you want your password to be?")

entry_state = IntVar()
entry_number = Entry(width=10, textvariable=entry_state)

text_password = Text(height=1, width=20)
text_password.insert(END, "Your new password")

button = Button(text="generate", command=lambda: get_password(entry_number.get()))

label_question.grid(column=0, row=0)
entry_number.grid(column=0, row=1)
text_password.grid(column=0, row=2)
button.grid(column=0, row=3)

window.mainloop()
