from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps

    reps = 0
    window.after_cancel(timer)
    label_timer.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        # if it's the 2nd/4th/6th rep:
        count_down(short_break_sec)
        label_timer.config(text="Break time!!!", fg=RED)
    elif reps % 8 == 0:
        # if it's the 8th rep
        count_down(long_break_sec)
        label_timer.config(text="Work time!!!", fg=PINK)
    else:
        # if it's the 1t/3rd/5th/7th rep:
        count_down(work_sec)
        label_timer.config(text="Work time!!!", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label_timer.grid(column=1, row=0)

check_mark = Label(text="", fg=GREEN,bg=YELLOW)
check_mark.grid(column=1, row=4)

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=3)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=3)




window.mainloop()