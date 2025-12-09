import time
from tkinter import *
root=Tk()
root.geometry("300x300")

clicked=0.0
autoclick=0.0


def clickbutton():
    global clicked
    global autoclick
    clicked+=1
    click["text"]=clicked
    print(autoclick)
    if clicked == 50:
        labeltwo["text"] = "congrats you reached 50"
    else:
        labeltwo["text"] = ""

def buyautoclick():
    global autoclick
    global clicked
    if  clicked >= 1:
        autoclick+=1
        clicked-=1
        click["text"] = clicked



def autoclick_increase():
    global autoclick
    global clicked
    if clicked > 0:
        time.sleep(1)
        clicked += autoclick
        click["text"] = clicked



autoclick_increase()
click=Button(root,text="0", padx=50, pady=50, command=clickbutton, bg="gold",font=("Arial, 14"))
buyauto=Button(root,text="Buy autoclick (50)", padx=50, pady=50, command=buyautoclick)
labeltwo = Label(root, text="")
click.pack()
labeltwo.pack()
buyauto.pack()


root.mainloop()
