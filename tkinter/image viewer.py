from tkinter import *
from PIL import  ImageTk, Image
root= Tk()
root.geometry("410x420")
root.title("My Cool Image Viewer")
root.iconbitmap("images/icon.ico")
img1= ImageTk.PhotoImage(Image.open("images/01.jpg"))
img2= ImageTk.PhotoImage(Image.open("images/02.jpg"))
img3= ImageTk.PhotoImage(Image.open("images/03.jpg"))
img4= ImageTk.PhotoImage(Image.open("images/04.jpg"))
img5= ImageTk.PhotoImage(Image.open("images/05.jpg"))
image_number = 0
image_list = [img1,img2,img3,img4,img5]
image_canvas = Canvas(root, width=400, height=350)
image_display = image_canvas.create_image((0,0), image = image_list[image_number], anchor="nw")

def foward():
    global image_number
    if image_number < len(image_list) - 1:
        image_number += 1
    else:
        image_number = 0
    image_canvas.itemconfig(image_display, image=image_list[image_number])
    info_text["text"] = "Image " + str(image_number + 1) + " of " + str(len(image_list))

def backward():
    global image_number
    if image_number <= len(image_list) - 1 and image_number > 0 :
        image_number -=1
    elif image_number <= 0:
        image_number = 4
    image_canvas.itemconfig(image_display, image=image_list[image_number])
    info_text["text"] = "Image " + str(image_number + 1) + " of " + str(len(image_list))

button_next = Button(root, text=">>", width=10, bg="lightgreen", command=foward)
button_back = Button(root, text="<<", width=10, bg="lightgreen", command=backward)
button_exit = Button(root, text="exit", command=root.quit, width=10, bg="plum")
info_text = Label(root,text="Image" + str(image_number + 1) + " of " + str(len(image_list)), font=("Arial, 14"), bg="lightyellow", fg="maroon")
image_canvas.grid(row=0, column=0, columnspan=3)
button_next.grid(row=1, column=2)
button_back.grid(row=1, column=1)
button_exit.grid(row=1, column=0)
info_text.grid(row=2, column=0, columnspan=3)

root.mainloop()
