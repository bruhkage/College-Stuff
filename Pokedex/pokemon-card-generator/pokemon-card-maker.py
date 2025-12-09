from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageFont


root = Tk()
root.title("Pokemon Card Maker App")
root.geometry("610x460")

image = ImageTk.PhotoImage(Image.open("006MS8.png").resize((200,200)))
type_image = ImageTk.PhotoImage(Image.open("Bug.png").resize((60,70)))
name = "Charizard"

pokeMonImage = Image.open("006MS8.png")
pokeMonImageSize = (200,200)
pokeMonImage = pokeMonImage.resize(pokeMonImageSize)
pokeMonImage = pokeMonImage.convert("RGBA")


newImage = Image.open("Bug.png")
newSize = (90,100)
newImage = newImage.resize(newSize)

def MakeCard():
    im = Image.open("pokemon-card.jpg")
    im.paste(newImage,(25,77), mask=newImage)
    im.paste(pokeMonImage,((im.width - pokeMonImage.width) // 2, 250), mask=pokeMonImage)
    canvas = ImageDraw.Draw(im)
    font = ImageFont.truetype("nova.ttf", 60)
    strip_width = 720
    text_width, text_height = canvas.textsize(name, font)
    print(text_width)
    name_location = ((strip_width-text_width)//2, 525)   
    canvas.text(name_location, name, fill="white", font=font, stroke_width=4, stroke_fill='black')
    font2 = ImageFont.truetype("nova.ttf", 30)
    hp_location = (180,635)
    canvas.text(hp_location, hp_label.cget("text"), fill="white", font=font2, stroke_width=2, stroke_fill='black')
    attack_location = (370,635)
    canvas.text(attack_location, attack_label.cget("text"), fill="white", font=font2, stroke_width=2, stroke_fill='black')
    defense_location = (570,635)
    canvas.text(defense_location, defense_label.cget("text"), fill="white", font=font2, stroke_width=2, stroke_fill='black')
    sp_attack_location = (180,740)
    canvas.text(sp_attack_location, sp_attack_label.cget("text"), fill="white", font=font2, stroke_width=2, stroke_fill='black')
    sp_defense_location = (370,740)
    canvas.text(sp_defense_location, sp_defense_label.cget("text"), fill="white", font=font2, stroke_width=2, stroke_fill='black')
    speed_location = (570,740)
    canvas.text(speed_location, speed_label.cget("text"), fill="white", font=font2, stroke_width=2, stroke_fill='black')
    im.show()
    #im.save("ppooppkkee.jpg")
    


imageLabel = Label(root, image=image)
typeImage = Label(root, image=type_image)

hp_label = Label(root, text="10")
attack_label = Label(root, text="20")
defense_label = Label(root, text="30")
sp_attack_label = Label(root, text="40")
sp_defense_label = Label(root, text="50")
speed_label = Label(root, text="60")
type_label = Label(root, text="Fire")
button = Button(root, text="Change", width=20, height=2, bg="purple", fg="white", command=MakeCard)

imageLabel.pack()
attack_label.pack()
defense_label.pack()
sp_attack_label.pack()
sp_defense_label.pack()
speed_label.pack()
type_label.pack()
typeImage.pack()
button.pack()


root.mainloop()