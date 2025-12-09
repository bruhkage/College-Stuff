from tkinter import *
from PIL import  ImageTk, Image
import random

root= Tk()
root.geometry("600x600")
root.title("Magic 8 Ball")


img1= ImageTk.PhotoImage(Image.open("1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("4.jpg"))
img5 = ImageTk.PhotoImage(Image.open("5.jpg"))
img6 = ImageTk.PhotoImage(Image.open("6.jpg"))
img7 = ImageTk.PhotoImage(Image.open("7.jpg"))
img8 = ImageTk.PhotoImage(Image.open("8.jpg"))
img9 = ImageTk.PhotoImage(Image.open("9.jpg"))
img10 = ImageTk.PhotoImage(Image.open("10.jpg"))
img11 = ImageTk.PhotoImage(Image.open("11.jpg"))
img12 = ImageTk.PhotoImage(Image.open("12.jpg"))
img13 = ImageTk.PhotoImage(Image.open("13.jpg"))
img14 = ImageTk.PhotoImage(Image.open("14.jpg"))
img15 = ImageTk.PhotoImage(Image.open("15.jpg"))

image_number = random.randint(0,14)
image_list = [img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13,img14,img15]
image_canvas = Canvas(root, width=400, height=400)
image_display =  image_canvas.create_image((0,0), image = image_list[11], anchor="nw")

def answer():
    global image_number
    image_number = random.randint(0, 14)
    image_canvas.itemconfig(image_display, image=image_list[image_number])

button = Button(text="Ask", command=answer)
question=Entry()
image_canvas.pack()
button.pack()
question.pack()


root.mainloop()