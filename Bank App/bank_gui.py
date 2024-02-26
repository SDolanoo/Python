import tkinter as tk
THEME_COLOR = "#375362"
FONT = ("Arial", 20)

class Gui(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("BankApp")
        self.config(padx=20, pady=20, bg=THEME_COLOR)
        # Canvas
        self.main_canvas = tk.Canvas(width=200, height=200, bg="white")
        self.text = self.main_canvas.create_text(100, 100, width=190, text="Create an account or login", font=FONT)
        self.main_canvas.grid(row=0, column=0, columnspan=2)
        # Buttons
        self.login_button = tk.Button(text="Login")
        self.login_button.grid(row=3, column=0, sticky=tk.EW)
        self.register_button = tk.Button(text="Register")
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




gui = Gui()