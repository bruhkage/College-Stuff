from tkinter import *
from PIL import  ImageTk, Image
import  time
timer=0
count=1
correct=0
iheight=400
ilength=500


def start():
    def closeWindow():
        root.destroy()
        window()


    root = Tk()
    root.geometry("280x150")
    root.title("Tkinter Quizz")
    questionLabel = Label(text=f"Press the start button when your ready",font=("Arial,18")).grid(row=0, column=0, columnspan=3)
    button1 = Button(text="Start", width=15, height=5,command=closeWindow).grid(row=1, column=0, columnspan=3)
    root.mainloop()

def finished():
    root = Tk()
    root.geometry("620x550")
    root.title("Finished")
    congrats = ImageTk.PhotoImage(Image.open("congrats.jpg").resize((ilength, iheight)))
    image_canvas = Canvas(root, width=ilength, height=iheight)
    image_display = image_canvas.create_image((0, 0), image=congrats, anchor="nw")
    image_canvas.grid(row=0, column=0, columnspan=3)
    questionLabel = Label(text=f"Congratulations! You got {correct} out of {count} questions correct",font=("Arial,18")).grid(row=1, column=0, columnspan=3)
    root.mainloop()

def window():
    global timer

    root= Tk()
    root.geometry("620x550")
    root.title("Tkinter quizz")
    img1= ImageTk.PhotoImage(Image.open("img1.jpg").resize((ilength,iheight)))
    img2= ImageTk.PhotoImage(Image.open("img2.jpg").resize((ilength,iheight)))
    img3= ImageTk.PhotoImage(Image.open("img3.jpg").resize((ilength,iheight)))
    img4= ImageTk.PhotoImage(Image.open("img4.jpg").resize((ilength,iheight)))
    img5= ImageTk.PhotoImage(Image.open("img5.jpg").resize((ilength,iheight)))

    quizz_data={
            "question1":{
        "image": img1,
        "question": "What is drakes faviourite chord",
        "options":["C Minor","D Minor","A Minor","B Minor"],
        "answer":"A Minor"
        },
            "question2":{
        "image": img2,
        "question": "What is this",
        "options":["Kfc Stacker Meal","Kfc Zinger Meal","Kfc Fillet Burger Meal","Kfc Double Down"],
        "answer":"Kfc Zinger Meal"
        },
        "question3": {
            "image":img3,
            "question": "What is my cats name",
            "options": ["John", "Sparkles", "Hope", "Fluff"],
            "answer": "Fluff"
        },
        "question4": {
        "image": img4,
        "question": "What is the best one piece arc (image not related)",
        "options": ["Marineford", "Ennies Lobby", "Wano", "Egghead"],
        "answer": "Ennies Lobby"
        },

        "question5": {
        "image": img5,
        "question": "What is the most peak persona song",
        "options": ["Whims Of Fate", "Its Going Down Now", "Last Surprise", "Heartbeat Heartbreak"],
        "answer": "Whims Of Fate"
        },

        "question5": {
            "image": img5,
            "question": "What is the most peak persona song",
            "options": ["Whims Of Fate", "Its Going Down Now", "Last Surprise", "Heartbeat Heartbreak"],
            "answer": "Whims Of Fate"
    }
    }



    def answering(answer):

        global count
        global correct
        if answer == quizz_data[f"question{count}"]["answer"] and count <=4:
            correct+=1
            count += 1
            root.destroy()
            window()
        elif answer!=quizz_data[f"question{count}"]["answer"] and count <=4:
            count += 1
            root.destroy()
            window()
        elif answer == quizz_data[f"question{count}"]["answer"] and count == 5:
            correct+=1
            root.destroy()
            finished()
        elif answer != quizz_data[f"question{count}"]["answer"] and count == 5:
            root.destroy()
            finished()


    def countdown(time_left):
        global count
        if time_left > 0:
            timerDisplay.config(text=str(time_left))
            root.after(1000, countdown, time_left - 1)  # Update after 1 second
        else:
            if count <5:
                timerDisplay.config(text="Time's up!")
                root.destroy()
                count+=1
                window()
            else:
                root.destroy()
                finished()

    image_canvas = Canvas(root, width=ilength, height=iheight)
    image_display = image_canvas.create_image((0,0), image = quizz_data[f"question{count}"]["image"], anchor="nw")


    image_canvas.grid(row=0, column=0, columnspan=3)
    questionLabel=Label(text=quizz_data[f"question{count}"]["question"],font=("Arial,18"))
    timerDisplay=Label(font=("Arial,18"))
    button1=Button(text=quizz_data[f"question{count}"]["options"][0],bg="red",width=15,height=5,command=lambda:answering(quizz_data[f"question{count}"]["options"][0]))
    button2=Button(text=quizz_data[f"question{count}"]["options"][1],bg="yellow",width=15,height=5,command=lambda:answering(quizz_data[f"question{count}"]["options"][1]))
    button3=Button(text=quizz_data[f"question{count}"]["options"][2],bg="blue",width=15,height=5,command=lambda:answering(quizz_data[f"question{count}"]["options"][2]))
    button4=Button(text=quizz_data[f"question{count}"]["options"][3],bg="lime",width=15,height=5,command=lambda:answering(quizz_data[f"question{count}"]["options"][3]))
    button1.grid(row=2,column=0)
    button2.grid(row=2,column=1)
    button3.grid(row=2,column=2)
    button4.grid(row=2,column=3)
    questionLabel.grid(row=1, column=0, columnspan=3)
    timerDisplay.grid(row=0, column=3, columnspan=3)

    countdown(5)
    root.mainloop()

start()


