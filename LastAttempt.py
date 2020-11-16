import tkinter
from tkinter import *

## Set up Functionality:
def roll_a_die():
    import random
    faces = [1,2,3,4,5,6]
    faceValue = random.choice(faces)
    return(faceValue)

die_pos_1_x = 300
die_pos_2_x = 400
die_pos_3_x = 500
die_pos_4_x = 600
die_pos_5_x = 700 
die_pos_y = 200


def score_calculator():
    die_output = entry.get()
    die_output = list(die_output)
    score = 0
    if aces.get() == 1:
        for face in die_output:
            if face == '1':
                score = score + int(face)
    if twos.get() == 1:
        for face in die_output:
            if face == '2':
                score = score + int(face)
    if threes.get() == 1:
        for face in die_output:
            if face == '3':
                score = score + int(face)
    if fours.get() == 1:
        for face in die_output:
            if face == '4':
                score = score + int(face)
    if fives.get() == 1:
        for face in die_output:
            if face == '5':
                score = score + int(face)
    if sixes.get() == 1:
        for face in die_output:
            if face == '6':
                score = score + int(face)

    if threekind.get() == 1 or fourkind.get() == 1 or fullhouse.get() == 1 or small.get() == 1 or large.get() == 1 or yahtzee.get() == 1 or chance.get() == 1:
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        count6 = 0 
        for face in die_output:
            if face == '1':
                count1 += 1
            if face == '2':
                count2 += 1
            if face == '3':
                count3 += 1
            if face == '4':
                count4 += 1
            if face == '5':
                count5 += 1
            if face == '6':
                count6 += 1
        die_counts = [count1, count2, count3, count4, count5, count6]

    if threekind.get() == 1:
        if 3 in die_counts:
            for face in die_output:
                score += int(face)
    if fourkind.get() == 1:
        if 4 in die_counts:
            for face in die_output:
                score += int(face)
    if fullhouse.get() == 1:
        if 2 in die_counts and 3 in die_counts:
            score += 25
    if small.get() == 1:
        if die_counts[0]>= 1 and die_counts[1]>= 1 and die_counts[2] >= 1 or die_counts[1]>= 1 and die_counts[2]>= 1 and die_counts[2] >= 1 or die_counts[2]>= 1 and die_counts[3]>= 1 and die_counts[4] >= 1:
            score += 30
    if large.get()  == 1:
        for count in die_counts:
            if die_counts[1] == 1 and die_counts[2] == 1 and die_counts[3] == 1 and die_counts[4] == 1:
                score = 0
                if die_counts[0] == 1 or die_counts[5] ==1:
                    score += 40
    if yahtzee.get() == 1:
        if 5 in die_counts:
            score += 50
    if chance.get() == 1:
        for die in die_output:
            score += int(die)


    score_text = "SCORE: " + str(score)
    Label(game, text = score_text, bg = "black", fg = "white", font = "Helvetica 55 bold", padx = 400, pady = 200).place(anchor = CENTER, x = 500, y = 300) 

def roll_Three():
    if die1.get() == 1:
        dice1 = roll_a_die()
        Label(game, text = dice1, bg = "black", fg = "white", font = "Helvetica 55 bold").place(anchor = CENTER, x = die_pos_1_x, y = die_pos_y)
    if die2.get() == 1:
        dice2 = roll_a_die()
        Label(game, text = dice2, bg = "black", fg = "white", font = "Helvetica 55 bold").place(anchor = CENTER, x = die_pos_2_x, y = die_pos_y)
    if die3.get() == 1:
        dice3 = roll_a_die()
        Label(game, text = dice3, bg = "black", fg = "white", font = "Helvetica 55 bold").place(anchor = CENTER, x = die_pos_3_x, y = die_pos_y)
    if die4.get() == 1:
        dice4 = roll_a_die()
        Label(game, text = dice4, bg = "black", fg = "white", font = "Helvetica 55 bold").place(anchor = CENTER, x = die_pos_4_x, y = die_pos_y)
    if die5.get() == 1:
        dice5 = roll_a_die()
        Label(game, text = dice5, bg = "black", fg = "white", font = "Helvetica 55 bold").place(anchor = CENTER, x = die_pos_5_x, y = die_pos_y)
    Roll_One = Button(game, text = "ROLL ONE", bd = 5, state = DISABLED, command = roll_One, fg = "white", bg = "black", font = "Helvetica 20 bold").place(anchor = CENTER, x = 300, y = 400)
    Roll_Two = Button(game, text = "ROLL TWO", state = DISABLED, command = roll_Two, bd = 5, fg = "white", bg = "black", font = "Helvetica 20 bold").place(anchor = CENTER, x = 503, y = 400)
    Roll_Three = Button(game, text = "ROLL THREE", state = DISABLED, command = roll_Three, bd = 5, fg = "white", bg = "black", font = "Helvetica 20 bold").place(anchor = CENTER, x = 725, y = 400)
    Get_Score = Button(game, text = "PICK A CATEGORY TO CALCULATE THE SCORE", command = score_calculator, fg = "white", bg = "black", font = "Helvetica 20 bold", padx = 10, pady = 5).place(anchor = CENTER, x = 500, y = 400)


def roll_Two():
    if die1.get() == 1:
        dice1 = roll_a_die()
        Label(game, text = dice1, bg = "black", fg = "white", font = "Helvetica 55 bold").place(anchor = CENTER, x = die_pos_1_x, y = die_pos_y)
    if die2.get() == 1:
        dice2 = roll_a_die()
        Label(game, text = dice2, bg = "black", fg = "white", font = "Helvetica 55 bold").place(anchor = CENTER, x = die_pos_2_x, y = die_pos_y)
    if die3.get() == 1:
        dice3 = roll_a_die()
        Label(game, text = dice3, bg = "black", fg = "white", font = "Helvetica 55 bold").place(anchor = CENTER, x = die_pos_3_x, y = die_pos_y)
    if die4.get() == 1:
        dice4 = roll_a_die()
        Label(game, text = dice4, bg = "black", fg = "white", font = "Helvetica 55 bold").place(anchor = CENTER, x = die_pos_4_x, y = die_pos_y)
    if die5.get() == 1:
        dice5 = roll_a_die()
        Label(game, text = dice5, bg = "black", fg = "white", font = "Helvetica 55 bold").place(anchor = CENTER, x = die_pos_5_x, y = die_pos_y)    
    Roll_One = Button(game, text = "ROLL ONE", bd = 5, state = DISABLED, command = roll_One, fg = "white", bg = "black", font = "Helvetica 20 bold").place(anchor = CENTER, x = 300, y = 400)
    Roll_Two = Button(game, text = "ROLL TWO", state = DISABLED, command = roll_Two, bd = 5, fg = "white", bg = "black", font = "Helvetica 20 bold").place(anchor = CENTER, x = 503, y = 400)
    Roll_Three = Button(game, text = "ROLL THREE", state = NORMAL, command = roll_Three, bd = 5, fg = "white", bg = "black", font = "Helvetica 20 bold").place(anchor = CENTER, x = 725, y = 400)


def roll_One():
    dice1 = roll_a_die()
    Label(game, text = dice1, bg = "black", fg = "white", font = "Helvetica 55 bold").place(anchor = CENTER, x = die_pos_1_x, y = die_pos_y)
    dice2 = roll_a_die()
    Label(game, text = dice2, bg = "black", fg = "white", font = "Helvetica 55 bold").place(anchor = CENTER, x = die_pos_2_x, y = die_pos_y)
    dice3 = roll_a_die()
    Label(game, text = dice3, bg = "black", fg = "white", font = "Helvetica 55 bold").place(anchor = CENTER, x = die_pos_3_x, y = die_pos_y)
    dice4 = roll_a_die()
    Label(game, text = dice4, bg = "black", fg = "white", font = "Helvetica 55 bold").place(anchor = CENTER, x = die_pos_4_x, y = die_pos_y)
    dice5 = roll_a_die()
    Label(game, text = dice5, bg = "black", fg = "white", font = "Helvetica 55 bold").place(anchor = CENTER, x = die_pos_5_x, y = die_pos_y)
    Roll_One = Button(game, text = "ROLL ONE", bd = 5, state = DISABLED, command = roll_One, fg = "white", bg = "black", font = "Helvetica 20 bold").place(anchor = CENTER, x = 300, y = 400)
    Roll_Two = Button(game, text = "ROLL TWO", state = NORMAL, command = roll_Two, bd = 5, fg = "white", bg = "black", font = "Helvetica 20 bold").place(anchor = CENTER, x = 503, y = 400)


## Entry Page

root = Tk()
root.title("Welcome to ... YAHTZEE!")
root.geometry('%dx%d+%d+%d' % (1000, 600, 20, 0))
root.configure(background = "dark red")

def close_window():
    root.destroy()


# entry_frame = Frame(root).pack()
Welcome_title = Label(root, text =  "WELCOME TO", fg = "white", bg = "dark red", font = "Helvetica 38 bold italic").place(anchor = CENTER, x = 500, y = 200)
Yahtzee_title = Label(root, text =  "YAHTZEE!", fg = "white", bg = "dark red", font = "Helvetica 70 bold italic").place(anchor = CENTER, x = 500, y = 300)
Start_Playing = Button(root, text = "LET'S ROLL", bd = 5, command = close_window, bg = "white", fg = "black", font = "Helvetica 20 bold").place(anchor = CENTER, x = 500, y = 425)

root.mainloop()



## Set up GUI:
game = Tk()
game.title("YAHTZEE!")
game.geometry('%dx%d+%d+%d' % (1000, 600, 20, 0))
game.configure(background = "dark red")

Roll_One = Button(game, text = "ROLL ONE", bd = 5, command = roll_One, bg = "black", fg = "white", font = "Helvetica 20 bold").place(anchor = CENTER, x = 300, y = 400)
Roll_Two = Button(game, text = "ROLL TWO", state = DISABLED, bd = 5, fg = "white", bg = "black", font = "Helvetica 20 bold").place(anchor = CENTER, x = 503, y = 400)
Roll_Three = Button(game, text = "ROLL THREE", state = DISABLED, bd = 5, fg = "white", bg = "black", font = "Helvetica 20 bold").place(anchor = CENTER, x = 725, y = 400)

Label(game, text = "WHICH DIE DO YOU WANT TO ROLL AGAIN?", fg = "black", bg = "white", font = "Helvetica 18 bold").place(anchor = CENTER, x = 500, y = 300)
die1 = IntVar()
Checkbutton(game, text = "1", variable = die1, onvalue = 1, offvalue = 0).place(x=310, y = 330)
die2 = IntVar()
Checkbutton(game, text = "2", variable = die2, onvalue = 1, offvalue = 0).place(x=405, y = 330)
die3 = IntVar()
Checkbutton(game, text = "3", variable = die3, onvalue = 1, offvalue = 0).place(x=495, y = 330)
die4 = IntVar()
Checkbutton(game, text = "4", variable = die4, onvalue = 1, offvalue = 0).place(x=585, y = 330)
die5 = IntVar()
Checkbutton(game, text = "5", variable = die5, onvalue = 1, offvalue = 0).place(x=680, y = 330)

Label(game, text = "ENTER YOUR FINAL ROLL", font = "Helvetica 12 bold", fg = "black", bg = "white").place(x = 280, y = 439)
entryText = StringVar()
entry = Entry(game, bg = "white", font = "Helvetica 12 bold", fg = "black", textvariable = entryText)
entry.place(x= 500, y = 440)

# Left Side
aces = IntVar()
Checkbutton(game, text = "ACES", variable = aces, onvalue = 1, offvalue = 0).place(x = 50, y = 480)
twos = IntVar()
Checkbutton(game, text = "TWOS", variable = twos, onvalue = 1, offvalue = 0).place(x = 150, y = 480)
threes = IntVar()
Checkbutton(game, text = "THREES", variable = threes, onvalue = 1, offvalue = 0).place(x = 250, y = 480)
fours = IntVar()
Checkbutton(game, text = "FOURS", variable = fours, onvalue = 1, offvalue = 0).place(x = 50, y = 545)
fives = IntVar()
Checkbutton(game, text = "FIVES", variable = fives, onvalue = 1, offvalue = 0).place(x = 150, y = 545)
sixes = IntVar()
Checkbutton(game, text = "SIXES", variable = sixes, onvalue = 1, offvalue = 0).place(x = 250, y = 545)

# Right Side
threekind = IntVar()
Checkbutton(game, text = "THREE OF A KIND", variable = threekind, onvalue = 1, offvalue = 0).place(x = 450, y = 480)
fourkind = IntVar()
Checkbutton(game, text = "FOUR OF A KIND", variable = fourkind, onvalue = 1, offvalue = 0).place(x = 610, y = 480)
fullhouse = IntVar()
Checkbutton(game, text = "FULL HOUSE", variable = fullhouse, onvalue = 1, offvalue = 0).place(x = 770, y = 480)
small = IntVar()
Checkbutton(game, text = "SMALL STRAIGHT", variable = small, onvalue = 1, offvalue = 0).place(x = 450, y = 545)
large = IntVar()
Checkbutton(game, text = "LARGE STRAIGHT", variable = large, onvalue = 1, offvalue = 0).place(x = 590, y = 545)
chance = IntVar()
Checkbutton(game, text = "CHANCE", variable = chance, onvalue = 1, offvalue = 0).place(x = 730, y = 545)
yahtzee = IntVar()
Checkbutton(game, text = "YAHTZEE", variable = yahtzee, onvalue = 1, offvalue = 0).place(x = 830, y = 545)


game.mainloop()





#https://www.python-course.eu/tkinter_entry_widgets.php
#https://stackoverflow.com/questions/10727131/why-is-tkinter-entrys-get-function-returning-nothing
#https://pythonbasics.org/tkinter-checkbox/
#https://www.delftstack.com/howto/python-tkinter/how-to-change-tkinter-button-state/
