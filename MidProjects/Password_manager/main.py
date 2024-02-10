from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [i for i in "0123456789!@#$%^&*-_+=,<.>/?;:`~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    password = []
    for n in range(12):
        password.append(random.choice(letters))
    password2 = "".join(password)
    password_entry.delete(0, END)
    password_entry.insert(END, f"{password2}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        #is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUsername: {username} "
        #                                              f"\nPassword: {password} \nIs it ok to save?")
        try:
            with open("data.json", 'r') as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                # saving updated data
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", 'w') as file:
                # saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ------------------------ BROWSE USER DATA --------------------------- #
def browse_user_data():
    website = (website_entry.get())
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            searched_website = data[website]
    except FileNotFoundError:
        messagebox.showerror(title="Hello", message="There is no data in the manager. \n"
                                                   "First You need to add data to be able to browse it.")
        pass
    except KeyError:
        messagebox.showerror(title="Hello", message="There is either: No website You try to find or You misspelled it.")
    else:
        username = searched_website['username']
        password = searched_website['password']
        messagebox.showinfo(title="Your data", message=f"Username: {username}\n Password: {password}")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()
username_entry = Entry(width=50)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "sdolazinski@gmail.com")
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons
browse_button = Button(text="Browse", width=14, command=browse_user_data)
browse_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()