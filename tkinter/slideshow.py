from tkinter import *
from tkinter import filedialog
import os
from PIL import  ImageTk, Image
import time



root= Tk()
root.geometry("800x800")
root.title("Hungry")
root.iconbitmap("images/icon.ico")
imagesList = []

def LookForFolder():
    global imagesList
    imagesList.clear()
    folder_name = filedialog.askdirectory()

    if len(folder_name) ==0:
        print("No folder was selected")
        return

    labelOne.config(text = "Folder Location " + folder_name)

    for images in os.listdir(folder_name):

        if (images.endswith(".jpg") or images.endswith(".png") or  images.endswith(".jpeg") or images.endswith(".gif")):
            img = ImageTk.PhotoImage(Image.open(folder_name + "/" + images).resize((600, 450)))
            imagesList.append(img)

    print(imagesList)
    countdown(len(imagesList))

def countdown(time_sec):
    count= time_sec
    while True:
        mins, secs = divmod(time_sec,60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        print(timeformat, end="/r")
        image.config(image=imagesList[time_sec-1])
        labelTwo.config(text= str(time_sec) + " of " + str(count))
        time.sleep(3)
        time_sec -= 1
        if time_sec == 0:
            time_sec=count

        root.update()
    print("stop")


Browse = Button(root, text="Browse", padx=10, pady=10, command=LookForFolder)
labelOne = Label(root, text="Folder Location", padx=20, pady=20)
image = Label(root, image="", padx=30, pady=30)
labelTwo = Label(root, text="0 of 0", padx=10, pady=10)

Browse.pack()
labelOne.pack()
image.pack()
labelTwo.pack()

root.mainloop()

