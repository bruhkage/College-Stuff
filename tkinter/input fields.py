from tkinter import *
root=Tk()
root.geometry("400x300")

def ClickButton():
    if len(inputField.get()) ==0:
        labelOne = Label(root, text="hello what is your name", fg="purple", pady=20).grid(row=1, column=0)
    else:
        labelOne = Label(root, text="hello" + inputField.get(), fg="purple", pady=20).grid(row=1, column=0)

inputField=Entry(root, width=50, bg="lightblue", fg="maroon")
inputField.grid(row=1,column=1)
click=Button(root,text="click me", padx=50, pady=50, command=ClickButton, bg="gold",font=("Arial, 14")).grid(row=0, column=1)
labelOne =Label(root,text="???", fg="purple", pady=20).grid(row=1, column=0)
root.mainloop()