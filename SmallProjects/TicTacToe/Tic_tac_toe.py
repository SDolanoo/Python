from tkinter import *
import random
from tkinter.messagebox import *

def choose_winner(row,column):
    global currentplayer

    if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
        label.config(text=(currentplayer + ' player wins'))
        showinfo('Game ended', currentplayer + ' player wins')
        return True
    elif buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
        label.config(text=(currentplayer + ' player wins'))
        showinfo('Game ended', currentplayer + ' player wins')
        return True
    elif buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        label.config(text=(currentplayer + ' player wins'))
        showinfo('Game ended', currentplayer + ' player wins')
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        label.config(text=(currentplayer + ' player wins'))
        showinfo('Game ended', currentplayer + ' player wins')
        return True

def restart_game():
    global currentplayer

    currentplayer = random.choice(players)

    label.config(text=(currentplayer + "'s turn"))

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", state=ACTIVE)

def next_turn(row,column): #currentplayer > input > switch player
    global currentplayer, count

    if currentplayer == "x":
        buttons[row][column].config(text='X',state=DISABLED)
        count -= 1
        if choose_winner(row, column) is True:
            return
        else:
            currentplayer = players[1]
            label.config(text=(currentplayer+"'s turn"))
    elif currentplayer=="o":
        buttons[row][column].config(text='O',state=DISABLED)
        count -= 1
        if choose_winner(row,column) is True:
            return
        else:
            currentplayer = players[0]
            label.config(text=(currentplayer+"'s turn"))

    if count <= 0:
        label.config(text=("It's a tie"))
        return


window = Tk()
window.geometry("500x600")
players = ("x", "o")
currentplayer = random.choice(players)
window.config(bg='yellow')
count = 9

buttons=[[],
         [],
         []]

label=Label(window, text=currentplayer+"'s turn", font=("Comic Sans", 20))
label.pack(side=TOP)

restartbutton=Button(window, text='Restart', command=restart_game, width=15, height=2)
restartbutton.pack(side=TOP)

frame=Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row].append(Button(frame, text=(""),command=lambda row=row, column=column: next_turn(row, column),width=20, height=10))
        buttons[row][column].grid(row=row,column=column) #"sample"+str(row)+str(column)

window.mainloop()