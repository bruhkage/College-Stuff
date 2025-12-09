from tkinter import *
import pandas as pd
df=pd.read_csv("Dogecoin.csv")






root = Tk()
root.geometry("250x250")
root.title("DogeCoin Calculator")
TitleLabel = Label(text=f"DogeCoin Calculator", font=("Arial,18")).grid(row=0, column=0,  columnspan=3)
DateLabel = Label(text=f"Enter The Date You Brought It On", font=("Arial,18")).grid(row=1, column=2,)
DateEnter = Entry()
DateEnter.grid(row=2, column=2)
AmountLabel = Label(text=f"Enter The amount you brought", font=("Arial,18")).grid(row=3, column=2,)
AmountEntry = Entry()
AmountEntry.grid(row=4, column=2)
ProfitLable = Label(text=f"", font=("Arial,18"))
ProfitLable.grid(row=6, column=2)

def AmountMade():
    global  AmountEntry
    global DateEnter
    date = df.loc[df["Date"] == DateEnter.get()]
    ValueOnDate = date["Close"]
    OriginalValue = ValueOnDate * int(AmountEntry.get())
    peak = df["Close"].max()
    print(peak)
    PeakValue = peak * int(AmountEntry.get())
    print(PeakValue)
    print(OriginalValue)
    profit = PeakValue - OriginalValue
    profit = profit.to_string(index=False)
    print(profit)
    ProfitLable["text"] = f"You would of made £{profit}"

CalculateButton = Button(text="Calculate",command=lambda:AmountMade()).grid(row=5,column=2)




root.mainloop()