import tkinter as tk
from tkinter import messagebox
from file_operator import FileOperator

THEME_COLOR = "#375362"
FONT = ("Arial", 20)


class MainPage(tk.Tk):

    def __init__(self, file_operator: FileOperator):
        super().__init__()
        self.file_op = file_operator

        self.logged_in = False

        self.title("BankApp")
        self.config(padx=20, pady=20, bg=THEME_COLOR)
        # Canvas
        self.main_canvas = tk.Canvas(width=200, height=200, bg="white")
        self.text = self.main_canvas.create_text(100, 100, width=190, text="Create an account or login", font=FONT)
        self.main_canvas.grid(row=0, column=0, columnspan=2)
        # Buttons
        self.login_button = tk.Button(text="Login", command=self.login_clicked)
        self.login_button.grid(row=3, column=0, sticky=tk.EW)
        self.register_button = tk.Button(text="Register", command=self.register_clicked)
        self.register_button.grid(row=3, column=1)
        # Entries
        self.username_entry = tk.Entry()
        self.username_entry.grid(row=1, column=1)
        self.password_entry = tk.Entry()
        self.password_entry.config(show="*")
        self.password_entry.grid(row=2, column=1)
        # Labels
        self.username_label = tk.Label(text="Username", fg="white", bg=THEME_COLOR)
        self.username_label.grid(row=1, column=0)
        self.password_label = tk.Label(text="Password", fg="white", bg=THEME_COLOR)
        self.password_label.grid(row=2, column=0)
        self.mainloop()

    def login_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.file_op.check_credentials(username, password):
            # messagebox.showinfo(title="You are logged in.", message="You are logged in.")
            self.logged_in = True
            self.user_is_logged_in()
        else:
            messagebox.showinfo(title="Invalid credentials", message="Invalid credentials, forgot password?, "
                                                                     "maybe use it as red label popup")

    def register_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        data = {
            "username": [f"{username}"],
            "password": [f"{password}"],
            "balance": [0.0]
        }

        if len(username) <= 0 and len(password) <= 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        else:
            self.file_op.register_or_create_user(data)

    def user_is_logged_in(self):
        if self.logged_in:
            self.withdraw()
            #LoggedInUser()

class LoggedInUser(tk.Tk):

    def __init__(self, file_operator: FileOperator, user: str):
        super().__init__()
        self.user = user
        self.file_op = file_operator
        self.config(padx=20, pady=20, bg=THEME_COLOR)
        # Canvas
        self.main_canvas = tk.Canvas(width=200, height=200, bg="white")
        self.text = self.main_canvas.create_text(100, 100, width=190, text="This is logged in page", font=FONT)
        self.main_canvas.grid(row=0, column=0, rowspan=4)
        # Buttons
        self.withdraw_money_button = tk.Button(text="Withdrawmoney", command=self.withdraw_money_clicked)
        self.withdraw_money_button.grid(row=0, column=1)
        self.deposit_money_button = tk.Button(text="Deposit money", command=self.deposit_money_clicked)
        self.deposit_money_button.grid(row=1, column=1)
        self.transfer_money_button = tk.Button(text="Transfer money", command=self.transfer_money_clicked)
        self.transfer_money_button.grid(row=2, column=1)
        self.log_out_button = tk.Button(text="Log out", command=self.log_out_clicked)
        self.log_out_button.grid(row=3, column=1)

        self.mainloop()



    def withdraw_money_clicked(self):
        pass
        # make it in toplevel https://www.geeksforgeeks.org/python-tkinter-toplevel-widget/?ref=lbp
        # use scale widget for amount https://www.geeksforgeeks.org/python-tkinter-scale-widget/?ref=lbp
        # or use spinbox
        # input = input("how much?")
        # self.file_op.minus_balance(self.user, amount=input)

    def deposit_money_clicked(self):
        pass
        # make it in toplevel https://www.geeksforgeeks.org/python-tkinter-toplevel-widget/?ref=lbp
        # use scale widget for amount https://www.geeksforgeeks.org/python-tkinter-scale-widget/?ref=lbp
        # or use spinbox
        # input = input("how much?")
        # self.file_op.add_balance(self.user, amount=input)

    def transfer_money_clicked(self):
        pass
        # make it in toplevel, https://www.geeksforgeeks.org/python-tkinter-toplevel-widget/?ref=lbp
        # use scale widget for amount https://www.geeksforgeeks.org/python-tkinter-scale-widget/?ref=lbp
        # or use spinbox
        # use combobox for users in data.csv https://www.geeksforgeeks.org/combobox-widget-in-tkinter-python/?ref=lbp
        # input = input("how much?")
        # to_who = input("to who?")
        # self.file_op.add_balance(to_who, amount=input)
        # self.file_op.minus_balance(self.user, amount=input)

    def log_out_clicked(self):
        pass
        # message box "are you sure?"
        # go back to main page