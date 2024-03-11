import tkinter as tk
from tkinter import messagebox, ttk
from file_operator import FileOperator

THEME_COLOR = "#375362"
FONT = ("Arial", 20)


class BankGui(tk.Tk):

    def __init__(self, file_operator: FileOperator):
        super().__init__()
        self.file_op = file_operator


class MainPage(BankGui):

    def __init__(self, file_operator: FileOperator):
        BankGui.__init__(self, file_operator)
        self.main_page_setup()

    def main_page_setup(self):
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
            self.user_is_logged_in(str(username))
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
            self.file_op.register_user(data)

    def user_is_logged_in(self, username: str):
        self.destroy()
        LoggedInUser(file_operator=self.file_op, user=username)


class LoggedInUser(BankGui):

    def __init__(self, file_operator: FileOperator, user: str):
        BankGui.__init__(self, file_operator)
        self.user = user
        self.logged_in_page_setup()
        self.mainloop()

    def logged_in_page_setup(self):
        self.title("BankApp")
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

    def withdraw_money_clicked(self):
        def withdraw_button_clicked():
            withdraw_amount = float(withdraw_spinbox.get())
            self.file_op.minus_balance(self.user, withdraw_amount)

        # new window setup
        withdraw_window = tk.Toplevel()
        withdraw_window.title("Withdraw")
        withdraw_window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Label
        withdraw_label = tk.Label(withdraw_window, text="How much money do you want to withdraw", fg="white",
                                  bg=THEME_COLOR)
        withdraw_label.grid(row=0, column=0)
        # Spinbox
        current_value = tk.StringVar()
        withdraw_spinbox = tk.Spinbox(withdraw_window, from_=50, to=500,
                                      values=("50", "100", "150", "200", "300", "400", "500"),
                                      textvariable=current_value, wrap=True, state="readonly")
        withdraw_spinbox.grid(row=1, column=0)
        # Button
        withdraw_button = tk.Button(withdraw_window, text="Withdraw", command=withdraw_button_clicked)
        withdraw_button.grid(row=2, column=0)

    def deposit_money_clicked(self):
        def deposit_button_clicked():
            deposit_amount = float(deposit_spinbox.get())
            self.file_op.add_balance(self.user, deposit_amount)

        # new window setup
        deposit_window = tk.Toplevel()
        deposit_window.title("Deposit")
        deposit_window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Label
        deposit_label = tk.Label(deposit_window, text="How much money do you want to deposit", fg="white",
                                 bg=THEME_COLOR)
        deposit_label.grid(row=0, column=0)
        # Spinbox
        current_value = tk.StringVar()
        deposit_spinbox = tk.Spinbox(deposit_window, from_=50, to=500,
                                     values=("50", "100", "150", "200", "300", "400", "500"),
                                     textvariable=current_value, wrap=True, state="readonly")
        deposit_spinbox.grid(row=1, column=0)
        # Button
        deposit_button = tk.Button(deposit_window, text="Deposit", command=deposit_button_clicked)
        deposit_button.grid(row=2, column=0)

    def transfer_money_clicked(self):
        def transfer_button_clicked():
            transfer_amount = float(transfer_spinbox.get())
            transfer_person = transfer_combobox.get()
            if len(transfer_combobox.get()) == 0:
                messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
            else:
                if messagebox.askquestion("Confirmation",
                                          f"Are you sure you want to transfer {transfer_amount} to"
                                          f" {transfer_person}?"):
                    self.file_op.minus_balance(self.user, transfer_amount)
                    self.file_op.add_balance(transfer_person, transfer_amount)
                    print("money transferred")

        # new window setup
        transfer_window = tk.Toplevel()
        transfer_window.title("Deposit")
        transfer_window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Label
        transfer_label = tk.Label(transfer_window, text="How much money do you want to transfer", fg="white",
                                  bg=THEME_COLOR)
        transfer_label.grid(row=0, column=0)
        username_label = tk.Label(transfer_window, text="To who do you want to transfer", fg="white",
                                  bg=THEME_COLOR)
        username_label.grid(row=2, column=0)
        # Spinbox
        current_value = tk.StringVar()
        transfer_spinbox = tk.Spinbox(transfer_window, from_=50, to=500,
                                      values=("50", "100", "150", "200", "300", "400", "500"),
                                      textvariable=current_value, wrap=True, state="readonly")
        transfer_spinbox.grid(row=1, column=0)
        # Combobox
        x = tk.StringVar()
        transfer_combobox = ttk.Combobox(transfer_window, width=27, textvariable=x, state="readonly")
        data = self.file_op.get_all_users()
        data.remove(self.user)
        transfer_combobox['values'] = data
        transfer_combobox.grid(row=3, column=0)
        # Button
        transfer_button = tk.Button(transfer_window, text="Deposit", command=transfer_button_clicked)
        transfer_button.grid(row=4, column=0)

    def log_out_clicked(self):
        self.destroy()
        MainPage(file_operator=self.file_op)

#file = FileOperator()
#log = LoggedInUser(file, "Dolan")