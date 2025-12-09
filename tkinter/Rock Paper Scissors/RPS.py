from tkinter import *
from PIL import  ImageTk, Image
import random

root= Tk()
root.geometry("500x350")
root.title("Rock Paper Scissors")

paper_img=ImageTk.PhotoImage(Image.open("paper.png"))
rock_img=ImageTk.PhotoImage(Image.open("rock.png"))
scissors_img=ImageTk.PhotoImage(Image.open("scissor.png"))


player=0


image_list = [paper_img,rock_img,scissors_img]
image_canvas = Canvas(root, width=206, height=206)

def rock():
    global player
    player=2

def paper():
    global player
    player=1

def scissors():
    global player
    player=3

def play():
    cpu = random.randint(1, 3)
    image_number = cpu
    image_display = image_canvas.create_image((0, 0), image=image_list[image_number-1], anchor="nw")

    if cpu == player:
        result["text"] = "It is a draw"

    elif cpu == 1 and player == 2: #cpu win   paper beats rock
        result["text"] = "You lose"

    elif cpu == 2 and player ==1:#player win paper beats rock
        result["text"] = "You win"

    elif cpu == 3 and player == 1: #cpu win scissors beats paper
        result["text"] = "you lose"

    elif cpu == 1 and player == 3:#player win scissors beats paper
        result["text"] = "You win"

    elif cpu == 2 and player == 3:#cpu wins rock beats scissors
        result["text"] = "You lose"

    elif cpu== 3 and player == 2:#player wins rock beats scissors
        result["text"] = "You win"

    if player == 1:
        player_text="Paper"

    elif player== 2:
        player_text="Rock"

    elif player ==3:
        player_text="Scissors"

    if cpu ==1:
        cpu_text="Paper"

    elif cpu==2:
        cpu_text="Rock"

    elif cpu==3:
        cpu_text="Scissors"

    picked["text"] = "You picked " + player_text + " and the cpu picked " + cpu_text


image_canvas.grid(row=0, column=0, columnspan=3)
result=Label(text="Pick an option")
Rock=Button(text="Rock", width=20, command=rock).grid(row=3, column=0)
Paper=Button(text="Paper", width=20, command=paper).grid(row=3, column=1)
Scissors=Button(text="Scissors",width=20, command=scissors).grid(row=3, column=2)
Play=Button(text="Rock Papers Scissors Shoot",width=30, command=play).grid(row=4, column=0, columnspan=3)
picked=Label(text="")
picked.grid(row=1, column=0, columnspan=3)
result.grid(row=2, column=0, columnspan=3)

#if start==True:
root.mainloop()
