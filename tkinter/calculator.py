from tkinter import *
root=Tk()
root.geometry("300x300")
root.title("My cool Calculator")

def add_items():
    try:
        num_one =float(inputOne.get())
        num_two = float(inputTwo.get())
        total = num_one + num_two
        label_answer["text"] = "Total is: " + str(total)
    except ValueError:
        print("enter a number or make sure there are no spaces")

def sub_items():
    try:
        num_one = float(inputOne.get())
        num_two = float(inputTwo.get())
        total = num_one - num_two
        label_answer["text"] = "Total is: " + str(total)
    except ValueError:
        print("enter a number or make sure there are no spaces")

def divide_items():
    try:
        num_one = float(inputOne.get())
        num_two = float(inputTwo.get())
        total = num_one / num_two
        if num_two == 0:
            print("enter a number that isnt 0")
        label_answer["text"] = "Total is: " + str(total)
    except ValueError:
        print("enter a number or make sure there are no spaces")
    except ZeroDivisionError:
        print("You can not divide by 0")

def mult_items():
    try:
        num_one = float(inputOne.get())
        num_two = float(inputTwo.get())
        total = num_one * num_two
        label_answer["text"] = "Total is: " + str(total)
    except ValueError:
        print("enter a number or make sure there are no spaces")

inputOne = Entry(root, width=13, bg="lightblue", fg="maroon")
inputTwo = Entry(root, width=13, bg="lightyellow", fg="maroon")
Add = Button(root, text="+", width=9, command=add_items)
Sub= Button(root, text="-", width=9, command=sub_items)
div = Button(root, text="/", width=9, command=divide_items)
mult = Button(root, text="*", width=9, command=mult_items)

label_answer=Label(text="Total is: ", fg="purple")

inputOne.grid(row=0, column=0)
inputTwo.grid(row=0, column=1)
Add.grid(row=1, column=0)
Sub.grid(row=1, column=1)
div.grid(row=2, column=0)
mult.grid(row=2, column=1)
label_answer.grid(row=3, column=0, columnspan=2)
root.mainloop()