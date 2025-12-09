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
AmountLabel = Label(text=f"Enter The amount of money you want to invest", font=("Arial,18")).grid(row=3, column=2,)
AmountEntry = Entry()
AmountEntry.grid(row=4, column=2)
ProfitLable = Label(text=f"", font=("Arial,18"))
ProfitLable.grid(row=6, column=2)

def AmountMade():
    global  AmountEntry
    global DateEnter
    date = df.loc[df["Date"] == DateEnter.get()]
    ValueOnDate = date["Close"]
    ValueOnDate = float(date["Close"].values[0])
    AmountBrought =  int(AmountEntry.get()) / ValueOnDate
    print(AmountBrought)
    peak = df["Close"].max()
    print(peak)
    PeakValue = peak * AmountBrought
    profit = PeakValue - int(AmountEntry.get())
    print(profit)
    #profit=profit.to_string(index=False)
    ProfitLable["text"] = f"You would have made £{profit:,.2f}"

CalculateButton = Button(text="Calculate",command=lambda:AmountMade()).grid(row=5,column=2)




root.mainloop()