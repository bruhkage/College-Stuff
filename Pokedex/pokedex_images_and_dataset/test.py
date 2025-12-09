import random
import os
from tkinter import *
import pandas as pd
from PIL import ImageTk, Image
import matplotlib.pyplot as plt


# Read and clean the dataset
df = pd.read_excel("dataset_pokemon_task.xlsx")
df = df.drop(index=[33, 49, 819, 821, 822, 823, 825, 826, 1025])  # Clean up rows based on indices

# Reorder DataFrame based on specific conditions
for rows in range(len(df)):
    pokemon_name = df.iloc[rows, df.columns.get_loc("Pokemon")]

    # Adjust row ordering based on specific Pokemon names and conditions
    if "Galarian" in pokemon_name and rows not in [105, 106, 107, 650, 651, 652, 653, 654, 655, 656, 657]:
        df.iloc[rows - 1], df.iloc[rows] = df.iloc[rows], df.iloc[rows - 1]
    # More conditional reordering (same as the original code)...

# Prepare the 'Image_Path' column
df['Image_Path'] = df['Pokemon'].apply(lambda pokemon: f"pokemons/{pokemon}.png" if f"{pokemon}.png" in os.listdir("pokemons") else None)

# Tkinter setup
root = Tk()
root.title("Joshua O'Connor 24003462 Pokedex 2024")
root.geometry("800x600")

# Background Image (ensure it has a proper reference)
Pokedex_Background = ImageTk.PhotoImage(Image.open("UI-Image.png"))
image_canvas = Canvas(root, width=800, height=600)
image_display = image_canvas.create_image((0, 0), image=Pokedex_Background, anchor="nw")
image_canvas.pack()

# Listbox for searching Pokémon
scroll_bar = Scrollbar(root)
scroll_bar.pack(side=RIGHT, fill=Y)
listbox = Listbox(root, bg="#ff9966", yscrollcommand=scroll_bar.set)
scroll_bar.config(command=listbox.yview)

# Function for displaying a Pokémon's information and image
def clickedPokemon(event):
    global clicked
    clicked = listbox.get(listbox.curselection())  # Get the selected Pokémon
    Selected = df[df["Pokemon"] == clicked]  # Select relevant row
    print(Selected)
    type_display()

    # Retrieve the Pokémon's image path
    index = df[df["Pokemon"] == clicked].index[0]
    image_path = df.loc[index, "Image_Path"]

    if image_path and os.path.exists(image_path):
        pokemon_image = ImageTk.PhotoImage(Image.open(image_path).resize((150, 150)))  # Resize as needed
        pokemonimage.config(image=pokemon_image)
        pokemonimage.image = pokemon_image  # Store the image reference

        # Create canvas to display the Pokémon image
        width, height = pokemonimage.width(), pokemonimage.height()
        canvas = Canvas(root, bg="blue", width=width, height=height)
        canvas.pack()
        canvas.create_image(0, 0, image=pokemon_image, anchor=NW)

    # Display other stats like HP, Attack, etc.
    hp["text"] = Selected["HP"].to_string(index=False)
    name["text"] = Selected["Pokemon"].to_string(index=False)
    attack["text"] = Selected["Attack"].to_string(index=False)
    defence["text"] = Selected["Defence"].to_string(index=False)
    speed["text"] = Selected["Speed"].to_string(index=False)
    Sp_Defence["text"] = Selected["Sp. Defense"].to_string(index=False)
    Sp_Attack["text"] = Selected["Sp. Attack"].to_string(index=False)


# Function to display Pokémon Type image
def type_display():
    global clicked
    Selected = df[df["Pokemon"] == clicked]
    pokemon_type = Selected["Type"].iloc[0]

    # Display the correct type image based on the Pokémon type
    type_image = ImageTk.PhotoImage(Image.open(f"poken_types/{pokemon_type}.png").resize((200, 75)))  # Resize as needed
    typeimage.config(image=type_image)
    typeimage.image = type_image  # Store the image reference


# Populate Listbox with Pokémon names
for pokemon in df["Pokemon"]:
    listbox.insert("end", pokemon)

listbox.place(x=453, y=153, width=315, height=387)

# Labels to display Pokémon image and stats
pokemonimage = Label(root, image="", background="black")
pokemonimage.place(x=100, y=165, width=200, height=100)

typeimage = Label(root, image="")
typeimage.place(x=100, y=295, width=200, height=75)

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

# Searchbar and functionality
searchbar = Entry(font="Arial 14")
searchbar.place(x=500, y=550)

# Bindings for events
listbox.bind("<<ListboxSelect>>", clickedPokemon)

# Search Function
def pokemon_search(event):
    listbox.delete(0, END)
    if searchbar.get() == "":
        for pokemon in df["Pokemon"]:
            listbox.insert(END, pokemon)
    else:
        searched_df = df[df["Pokemon"].str.contains(searchbar.get(), case=False, na=False)]
        for pokemon in searched_df["Pokemon"]:
            listbox.insert(END, pokemon)

searchbar.bind("<Return>", pokemon_search)

# Buttons for charts
attackchart = Button(text="Attack Chart", padx=2, command=lambda: charts(1))
attackchart.place(x=610, y=10)

defencechart = Button(text="Defence Chart", padx=2, command=lambda: charts(3))
defencechart.place(x=690, y=10)

spdefchart = Button(text="Sp. Def Chart", padx=2, command=lambda: charts(4))
spdefchart.place(x=690, y=40)

spattchart = Button(text="Sp. Att Chart", padx=2, command=lambda: charts(5))
spattchart.place(x=610, y=40)

hpchart = Button(text="HP Chart", padx=11, command=lambda: charts(2))
hpchart.place(x=610, y=67)

speedchart = Button(text="Speed Chart", padx=9, command=lambda: charts(6))
speedchart.place(x=690, y=67)

totalchart = Button(text="Total", padx=9, command=lambda: charts(7))
totalchart.place(x=550, y=10)

# Run Tkinter event loop
root.mainloop()
