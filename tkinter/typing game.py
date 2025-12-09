import random
from tkinter import *
root= Tk()
root.geometry("300x300")
root.title("Typing Game")
colours=["red", "black", "purple", "green", "brown", "blue", "silver", "orange", "gold", "lightyellow", "maroon"]
correct=0
incorrect=0
userInput = ""
colour=""

def EnterPressed(event):
    global correct
    global incorrect
    if inputBox.get() == colour:
        correct+=1
    else:
        incorrect+=1
    Rungame()

def Rungame():
    global colour
    colour=random.choice(colours)
    text= random.choice(colours)
    colour_label.config(text=text, fg=colour)
    score_label["text"] = "Correct " + str(correct) + "--Incorrect: " + str(incorrect)
    inputBox.delete(0, END)

inputBox = Entry(root, bg="lightyellow", fg="black", justify=CENTER)
score_label = Label(root, text="Correct: 0 -- Incorrect: 0", fg="red", pady=10)
colour_label = Label(root, text="ColourName", fg="red", pady=10)
instruction_label = Label(root, text="What colour is the text? Press enter to check", fg="purple", pady=5)

score_label.pack()
instruction_label.pack()
colour_label.pack()
inputBox.pack()
root.bind("<Return>", EnterPressed)
Rungame()
root.mainloop()
