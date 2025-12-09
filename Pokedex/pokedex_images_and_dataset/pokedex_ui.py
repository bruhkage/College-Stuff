# just to show how to make the UI work for practice

from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.geometry("800x600")
root.title("[Your Name & ID] - PokeDex 2024")

# set up the background image from the app and assign it to the window
PokeDex_display= ImageTk.PhotoImage(Image.open("UI-Image.png"))
Image_background = Canvas(root,width=800,height=600)
Image_background.create_image(0,0,image=PokeDex_display,anchor="nw")

# set up the scroll bar and align it with the window
scroll_bar = Scrollbar(root)
scroll_bar.pack(side= RIGHT, fill = Y )
listbox = Listbox(root, bg="#ff9966", yscrollcommand= scroll_bar.set)
scroll_bar.config(command= listbox.yview)

# a random set of numbers inside of a list
random_list = [1,2,3,4,5,6,7,23,13,456745,3432,467,723,3,5,34564,21465456,32233,
               1,2,3,4,5,6,7,23,13,456745,3432,467,723,3,5,34564,21465456,32233,
               1,2,3,4,5,6,7,23,13,456745,3432,467,723,3,5,34564,21465456,32233
               ]

# load all of the files from the pokemons folder and store them inside of a list
imglist = [file for file in os.listdir("pokemons")]

# adding the items from the list to the list box
for i in random_list:
    listbox.insert("end", i)
    
# click event thats linked to the list box items
def update_ui(event):
    active = listbox.get(listbox.curselection())  # get item user selects from listbox
    #print(active)
    pokemon_name.config(text=str(active))
    
    # get the index of the list item
    index = listbox.curselection()[0]
    #print(index)
    
    Pokemon = ImageTk.PhotoImage(Image.open("pokemons/" + imglist[index]).resize((150, 150)))
    #print(imglist[index])
    
    # below we need to configure the label to display the image
    # you will need both of the lines to display the image
    image.config(image=Pokemon)
    image.image = Pokemon
    
    # display the hp on the hp_text label
    hp_text.config(text=str(index))
    
    
# matplotlib chart buttons, change the text to name of the charts such as top 5, lowest 5 etc
button_1 = Button(root, text="Chart 1")
button_2 = Button(root, text="Chart 2")
button_3 = Button(root, text="Chart 3")
button_4 = Button(root, text="Chart 4")



# label for the names, HP, Defense etc
pokemon_name = Label(root, text="Pokemon Name", fg="white", bg="black", font="Arial 11")

hp_text = Label(root, text="00", font="Arial 9")
attack_text = Label(root, text="00", font="Arial 9")


# pokemon image
image = Label(root, image="", background="black")


# placing the items to the window
pokemon_name.place(x=95, y=280, width=209, height=36)
hp_text.place(x=70, y=395)
attack_text.place(x=160, y=395)


listbox.place(x=453, y=153, width=315, height=387)
Image_background.pack(fill="both",expand=True)
image.place(x=100, y=165, width=200, height=100)


# chart buttons
button_1.place(x=610, y=30)
button_2.place(x=680, y=30)
button_3.place(x=610, y=60)
button_4.place(x=680, y=60)



# assigning the click event using bind
listbox.bind("<<ListboxSelect>>", update_ui)
# This line makes the listbox appear
root.mainloop()
