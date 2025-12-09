#Joshua O'Connor 24003462
import random#imports random for randomly selecting types
from tkinter import * #imports tkinter for making the window

import pandas as pd #imports panda for reading and editing the excel file
from PIL import ImageTk, Image, ImageGrab  # imported to make using images easier
import os#imported for file handling (reading files and file directorys)
import matplotlib.pyplot as plt#imported for making charts


df = pd.read_excel(os.path.join("pokedex_images_and_dataset", "dataset_pokemon_task.xlsx"))#puts the excel file containing all the pokemon's information into a dataframe (series of lists kinda)
#removes pokemon from the dataframe who do not have an image to link to
df=df.drop(index=33)
df=df.drop(index=49)
df=df.drop(index=819)
df=df.drop(index=821)
df=df.drop(index=822)
df=df.drop(index=823)
df=df.drop(index=825)
df=df.drop(index=826)
df=df.drop(index=1025)


for rows in range(len(df)):#starts a for loop that loops through the entire df

#code that fixes the order of the pokedex (images were desynced)
    if "Galarian" in df.iloc[rows, df.columns.get_loc("Pokemon")] and rows not in [105,106,107,650,651,652,653,654,655,656,657] :#looks for all pokemon with "Galarian" in there name except for the exceptions listed (their indexes in the df are use instead of their names)
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]#swaps there postiton in the pokedex with the pokemon above them


    if "Galarian"  in df.iloc[rows, df.columns.get_loc("Pokemon")]  and rows in [105,106,107,651,652,653,654,655,656,657]:#targets all the pokemon who were excluded last time
        df.iloc[rows - 2], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 2]#swaps them up by 2 instead of one (moving them up by one was not enough to correct them)


    if "Mega " in df.iloc[rows, df.columns.get_loc("Pokemon")] and rows not in [7,8,192,193]:#same as before but with pokemon with "Mega " in there name instead (targets all mega pokemon)
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]


    if "Alolan" in df.iloc[rows, df.columns.get_loc("Pokemon")] :#same as before but with alolan pokemon
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]

    if "Mega " in df.iloc[rows, df.columns.get_loc("Pokemon")] and rows in [105,106,107]:#for some reason these ones have to be moved individually not sure why
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]

    if "Attack " in df.iloc[rows, df.columns.get_loc("Pokemon")] or "Defense " in df.iloc[rows, df.columns.get_loc("Pokemon")]:#swaps deoxys' forms to be in the right order
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]
    if "Sandy Cloak" in  df.iloc[rows, df.columns.get_loc("Pokemon")]:#you probaly get the point now. swaps again
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]

    if "Fan " in  df.iloc[rows, df.columns.get_loc("Pokemon")] or "Mow " in  df.iloc[rows, df.columns.get_loc("Pokemon")]:#more swapping (the rotom forms were a nightmare)
        df.iloc[rows - 4], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 4]

    if "Heat " in  df.iloc[rows, df.columns.get_loc("Pokemon")]:
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]

    if "Rotom"  in  df.iloc[rows, df.columns.get_loc("Pokemon")] and rows in [569]:
        df.iloc[rows - 3], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 3]

    #now targeting individual pokemon :(

    if "Black"  in  df.iloc[rows, df.columns.get_loc("Pokemon")]:
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]

    if "Blade Forme"   in  df.iloc[rows, df.columns.get_loc("Pokemon")]:
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]

    if "Ash"   in  df.iloc[rows, df.columns.get_loc("Pokemon")]:
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]

    if "10% Forme" in df.iloc[rows, df.columns.get_loc("Pokemon")]:
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]

    if "Complete Forme"   in  df.iloc[rows, df.columns.get_loc("Pokemon")]:
        df.iloc[rows - 2], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 2]
    if "Mane" in  df.iloc[rows, df.columns.get_loc("Pokemon")]:
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]
    if "Wing" in  df.iloc[rows, df.columns.get_loc("Pokemon")]:
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]
    if "Eternamax" in df.iloc[rows, df.columns.get_loc("Pokemon")]:
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]
    if "Crowned" in df.iloc[rows, df.columns.get_loc("Pokemon")]:
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]
    if "Ice Rider" in df.iloc[rows, df.columns.get_loc("Pokemon")]:
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]

#finally free from that


def PokemonCard():#creates a pokemon card (read this fuction last otherwise things wont make sense)
    root.destroy()#destroys the pokedex window
    win = Tk()#creates a window and assigns it to a variable
    win.title("Joshua O'Connor 24003462 Pokemon Card Maker 2024")#sets the window title
    win.geometry("747x1008")#sets the window size

    #sets the background of the window using an image canvas
    background1 = ImageTk.PhotoImage(Image.open("pokemon-card-generator/pokemon-card.jpg"))
    image1_canvas = Canvas(win, width=747, height=1038)
    image1_display = image1_canvas.create_image((0, 0), image=background1, anchor="nw",bg=None)
    image1_canvas.pack()


    #function that updates the information of the pokemon
    def statsupdate():
        #code for displaying the type image (tried to use the function but it kept giving me weird errors)
        type = Selected["Type"].to_string(index=False)
        type_image = ImageTk.PhotoImage(Image.open(f"pokedex_images_and_dataset/poken_types/{type}.png").resize((65, 75)))
        typeimage2.config(image=type_image)
        typeimage2.image = type_image

        index = Selected.index[0]#grabs the index of the pokemon
        image_path = df.loc[index, "Image_Path"]#finds the image path of the selcted pokemon

        #same code used for displaying the pokemon image as before
        if image_path and os.path.exists(image_path):
            card_image = ImageTk.PhotoImage(Image.open(image_path).resize((200, 200)))  # Resize as needed
            cardimage.config(image=card_image)
            cardimage.image = card_image  # Store the image reference

        #updates the information of the labels
        hp["text"] = Selected["HP"].to_string(index=False)
        name["text"] = Selected["Pokemon"].to_string(index=False)
        attack["text"] = Selected["Attack"].to_string(index=False)
        defence["text"] = Selected["Defence"].to_string(index=False)
        speed["text"] = Selected["Speed"].to_string(index=False)
        Sp_Defence["text"] = Selected["Sp. Defense"].to_string(index=False)
        Sp_Attack["text"] = Selected["Sp. Attack"].to_string(index=False)

    #creating the labels
    cardimage = Label(image="", background="black")
    cardimage.place(x=265, y=245)

    typeimage2 = Label(win, image="", background="black")
    typeimage2.place(x=38, y=88)

    name = Label(text=df["Pokemon"][0], font="Arial 9")
    name.place(x=275, y=565, width=209, height=36)

    hp = Label(text=df["HP"][0], font="Arial 20")
    hp.place(x=175, y=635)

    attack = Label(text=df["Attack"][0], font="Arial 20")
    attack.place(x=375, y=635)

    defence = Label(text=df["Defence"][0], font="Arial 20")
    defence.place(x=575, y=635)

    speed = Label(text=df["Speed"][0], font="Arial 20")
    speed.place(x=575, y=740)

    Sp_Defence = Label(text=df["Sp. Defense"][0], font="Arial 20")
    Sp_Defence.place(x=375, y=740)

    Sp_Attack = Label(text=df["Sp. Attack"][0], font="Arial 20")
    Sp_Attack.place(x=175, y=740)

    #runs the statsupdate function
    statsupdate()

    #function that screenshots the window
    def TakeScreenshot():
        #finds exact location of window
        x = win.winfo_rootx()#finds the x cordinate of the window
        y = win.winfo_rooty()#fins the y cordinate of the window

        #finds size of window
        width = win.winfo_width()#finds the width
        height = win.winfo_height()#sets the height
        screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))#takes a screenshot of the window using the cordinates and size
        pokemon=Selected["Pokemon"].to_string(index=False)#saves the pokemons name ot a variable (makes it easier to use)
        screenshot.save(f"{pokemon}.png")#saves the screenshot as a png file

    jpg=Button(text="Save to PNG",command=TakeScreenshot,font="Arial 12")#button that runs the screenshot function
    jpg.place(x=325, y=840)
    win.mainloop()#runs the window






root=Tk()#creates the window and assigns it to the root variable
root.title("Joshua O'Connor 24003462 Pokedex 2024")#sets the windows title
root.geometry("800x600")#sets the windows size


imglist = [file for file in os.listdir("pokedex_images_and_dataset/pokemons") if file.endswith(".png")]#looks through the pokemons folder for any pngs and then adds them to a list
df["Image_Path"] = [f"pokedex_images_and_dataset/pokemons/{imglist[i]}" for i in range(len(df))]#creates a new column in the df called image path and assigns each pokemon the path to their image (bassicaly adding images to the df)


df["Type"] = df.apply(lambda _: random.choice(["Dark", "Fire", "Fairy", "Steel", "Grass", "Water", "Ice","Dragon", "Psychic", "Poison", "Ground", "Rock","Electric", "Flying", "Normal", "Ghost", "Bug", "Fighting"]), axis=1)#assigns each pokemon a new random type (stays consistent when the program is running but resets if u rerun the program


#event that handles pulling up and displaying the information of the pokemon u clicked on
def clickedPokemon(event):
    global clicked#creates clicked as a global variable as it will be used elsewhere in the code
    global Selected#same for selected

    if event==1:#checks if the variable event = 1 (only equals one if you hit the random pokemon button)
        randomindex = random.randint(0,1025)#selects a random index (selecting a random pokemon)
        Selected = df.iloc[[randomindex]]#creates a new df with only that pokemon

    else:#(this happens if you just clicked on the pokemon in the list box)
        clicked = listbox.get(listbox.curselection())#stores the pokemon u clicked on
        Selected = df[df["Pokemon"] == clicked]#makes a new df with only the pokemon u clicked on
    print(Selected)#prints selected (good for debugging and finding the index)
    type_display()#runs the function that deals with displaying the type image


    index = Selected.index[0]#assigns the index of the selcted pokemon to a variable
    image_path = df.loc[index, "Image_Path"]#using the stored index finds the image path of the pokemon

    if image_path and os.path.exists(image_path):#if it finds a valid image path
        pokemon_image = ImageTk.PhotoImage(Image.open(image_path).resize((150, 150)))#creates a new image canvas containing the pokemons image and sets it size
        pokemonimage.config(image=pokemon_image)#assigns that new image canvas to a tkinter label so it can be displayed
        pokemonimage.image = pokemon_image

    # pulls the selected pokemons stats and assigns them to the stat labels
    hp["text"] = Selected["HP"].to_string(index=False)
    name["text"] = Selected["Pokemon"].to_string(index=False)
    attack["text"] = Selected["Attack"].to_string(index=False)
    defence["text"] = Selected["Defence"].to_string(index=False)
    speed["text"] = Selected["Speed"].to_string(index=False)
    Sp_Defence["text"] = Selected["Sp. Defense"].to_string(index=False)
    Sp_Attack["text"] = Selected["Sp. Attack"].to_string(index=False)

    Pokecard["command"] = PokemonCard#if the user has selected a pokemon it makes it so the pokemon card button has a command (stops users from trying ot make a card with no selected pokemon)

#function that deals with displaying the type image
def type_display():
    type=Selected["Type"].to_string(index=False)#assigns the randomly selected type for the selected pokemon into a variable (just makes it easier to work with)
    type_image = ImageTk.PhotoImage(Image.open(f"pokedex_images_and_dataset/poken_types/{type}.png").resize((75, 85)))#creates a new image canvas containg the type image
    typeimage.config(image=type_image)#assigns the canvas to a tkinter label
    typeimage.image = type_image

#sets the background image using an image canvas

Pokedex_Background =  ImageTk.PhotoImage(Image.open("pokedex_images_and_dataset/UI-Image.png"))
image_canvas = Canvas(root, width=800, height=600)
image_display = image_canvas.create_image((0,0), image=Pokedex_Background, anchor="nw")
image_canvas.pack()

scroll_bar = Scrollbar(root)#creates a scrollbar (will let the user scroll up and down in the listbox we're gonna make)
scroll_bar.pack(side= RIGHT, fill = Y )#adds it to the right window
listbox = Listbox(root, bg="#ff9966", yscrollcommand= scroll_bar.set)#creates a list box which is gonna contain all the pokemon (user will be able to click on any of them)
scroll_bar.config(command= listbox.yview)

#function that allows the user to seach through the listbox using a searchbar
def pokemon_search(event):
    listbox.delete(0, END)#clears the listbox (used for reseting searches)
    if searchbar.get() == "":#checks if the searchbar is blank
        for pokemon in df["Pokemon"]:
            listbox.insert(END, pokemon)#adds all pokemon into the listbox
    else:
        searched_df = df[df["Pokemon"].str.contains(searchbar.get(), case=False, na=False)]#checks what the user has put in the searchbox
        for pokemon in searched_df["Pokemon"]:
            listbox.insert(END, pokemon)#adds all pokemon that contain what the user searched

#function that manges displaying all the charts
def charts(chartNumber):
    df1=pd.read_excel(os.path.join("pokedex_images_and_dataset", "dataset_pokemon_task.xlsx"))#creates a new df (using the original one causes conflicts with the listbox)
    if chartNumber ==1:#first chart displays pokemon with top 10 attack
        df1 = df1.nlargest(10, "Attack")#finds the 10 pokemon with the largest attack stat
        plt.figure(figsize=(12, 6))#sets the size of the chart
        plt.bar(df1["Pokemon"], df1["Attack"])#makes a bar chart with th pokemon and their attack stat
        plt.xlabel("Pokemon")
        plt.ylabel("Attack")
        plt.xticks(rotation=22.25, ha="right")#rotates the pokemons names so they all fit
        plt.grid()
        plt.show()#shows the chart
    if chartNumber ==2:#same are the rest as before but with diffrent stats
        df1 = df1.nlargest(10, "HP")#
        print(df1.to_string())
        plt.figure(figsize=(12, 6))
        plt.bar(df1["Pokemon"], df1["HP"])
        plt.xlabel("Pokemon")
        plt.ylabel("HP")
        plt.xticks(rotation=22.25, ha="right")
        plt.grid()
        plt.show()
    if chartNumber ==3:
        df1 = df1.nlargest(10, "Defence")
        print(df1.to_string())
        plt.figure(figsize=(12, 6))
        plt.bar(df1["Pokemon"], df1["Defence"])
        plt.xlabel("Pokemon")
        plt.ylabel("Defence")
        plt.xticks(rotation=22.25, ha="right")
        plt.grid()
        plt.show()
    if chartNumber ==4:
        df = df1.nlargest(10, "Sp. Defense")
        print(df.to_string())
        plt.figure(figsize=(12, 6))
        plt.bar(df["Pokemon"], df["Sp. Defense"])
        plt.xlabel("Pokemon")
        plt.ylabel("Sp. Defence")
        plt.xticks(rotation=22.25, ha="right")
        plt.grid()
        plt.show()

    if chartNumber == 5:
        df1 = df1.nlargest(10, "Sp. Attack")
        print(df1.to_string())
        plt.figure(figsize=(12, 6))
        plt.bar(df1["Pokemon"], df1["Sp. Attack"])
        plt.xlabel("Pokemon")
        plt.ylabel("Sp. Attack")
        plt.xticks(rotation=22.25, ha="right")
        plt.grid()
        plt.show()

    if chartNumber == 6:
        df1 = df1.nlargest(10, "Speed")
        print(df1.to_string())
        plt.figure(figsize=(12, 6))
        plt.bar(df1["Pokemon"], df1["Speed"])
        plt.xlabel("Pokemon")
        plt.ylabel("Speed")
        plt.xticks(rotation=22.25, ha="right")
        plt.grid()
        plt.show()

    if chartNumber == 7:
        df1 = df1.nlargest(10, "Total")
        print(df1.to_string())
        plt.figure(figsize=(12, 6))
        plt.bar(df1["Pokemon"], df1["Total"])
        plt.xlabel("Pokemon")
        plt.ylabel("Total")
        plt.xticks(rotation=22.25, ha="right")
        plt.grid()
        plt.show()

#adds all pokemon to the lsitbox (used for when the program is first ran)
for pokemon in df["Pokemon"]:
    listbox.insert("end", pokemon)
listbox.place(x=453, y=153, width=315, height=387)#places the listbox at thr right of the window

pokemonimage = Label(root, image="", background="black")#label that the pokemon image is assigned to
pokemonimage.place(x=100, y=165, width=200, height=100)

typeimage= Label(root, image="",background="black")#label that contains the type image
typeimage.place(x=275,y=45)


#labels that contains names and stats (need to be placed before they're values can be changed)
name = Label(text=df["Pokemon"][0], font="Arial 9")
name.place(x=95, y=280, width=209, height=36)


hp = Label(text=df["HP"][0], font="Arial 9")
hp.place(x=70, y=395)

attack = Label(text=df["Attack"][0], font="Arial 9")
attack.place(x=160, y=395)

defence = Label(text=df["Defence"][0], font="Arial 9")
defence.place(x=250, y=395)

speed = Label(text=df["Speed"][0], font="Arial 9")
speed.place(x=335, y=395)

Sp_Defence = Label(text=df["Sp. Defense"][0], font="Arial 9")
Sp_Defence.place(x=310, y=430)

Sp_Attack = Label(text=df["Sp. Attack"][0], font="Arial 9")
Sp_Attack.place(x=140, y=430)

searchbar=Entry(font="Arial 14")#creates the searchbar
searchbar.place(x=500, y=550)
listbox.bind("<<ListboxSelect>>", clickedPokemon)#when you click on a pokemon in the listbox it runs the clickedPokemon function
searchbar.bind("<Return>",pokemon_search)#when you press enter on the window it will run the search function

randompokemon=Button(text="Random",command=lambda: clickedPokemon(1))
randompokemon.place(x=725,y=550)

attackchart=Button(text="Attack Chart",padx=2,command=lambda: charts(1))#button that when pressed displays the first chart
attackchart.place(x=610, y=10)

#same with the other charts
defencechart=Button(text="Defence Chart",padx=2,command=lambda: charts(3))
defencechart.place(x=690, y=10)


spdefchart=Button(text="Sp. Def Chart",padx=2,command=lambda: charts(4))
spdefchart.place(x=690, y=40)

spattchart=Button(text="Sp. Att Chart",padx=2,command=lambda: charts(5))
spattchart.place(x=610, y=40)

hpchart=Button(text="HP Chart",padx=11,command=lambda: charts(2))
hpchart.place(x=610, y=67)

speedchart=Button(text="Speed Chart",padx=9,command=lambda: charts(6))
speedchart.place(x=690, y=67)

totalchart=Button(text="Total",padx=9,command=lambda: charts(7))
totalchart.place(x=550, y=10)

Pokecard=Button(text="PokeCard",padx=9)#makes a button that when pressed rusn the pokecard function
Pokecard.place(x=450, y=10)

root.mainloop()#runs the window


