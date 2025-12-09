import time
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Whatwewatchedjan24.csv')
df["Hours Viewed"] = df["Hours Viewed"].apply(lambda x : x.replace(',','')) #replace the , in the numbers
df["Hours Viewed"] = pd.to_numeric(df["Hours Viewed"],errors='coerce')# ensure the hours viewed column is numeric not text
df["Views"] = df["Views"].apply(lambda x : x.replace(',','')) #replace the , in the numbers
df["Views"] = pd.to_numeric(df["Views"],errors='coerce')

def mainMenu():
    time.sleep(1)
    print("-----------------------------------------------------")
    print("Welcome to the Netflix viewing analyser")
    print("-----------------------------------------------------")
    print("Please choose your option:")
    print("1: Find viewing figures by series or movie name")
    print("2: Show top 10 series or movie by hours viewed")
    print("3: Show top 10 series or movie by total views")
    print("4: Calculate Total hours viewed")
    print("5: Print graph of Title versus hours viewed and views for top 10")

    choice = input()
    try:
        choice=int(choice)
        if choice not in [1,2,3,4,5,6]:
            raise Exception("Not a valid option")
        else:
            if choice ==1:
                show=chooseByNameMenu()
                viewingFiguresByName(show)
            elif choice ==2:
                showTop10ByHoursViewed()
            elif choice ==3:
                showTop10ByTotalViews()
            elif choice ==4:
                calculateTotalHoursViewed()
            elif choice ==5:
                viewGraph()
    except Exception as e:
        print("error choice must be a number shown")
        print(" ")
        print(e)
        mainMenu()


def chooseByNameMenu():
    print("-----------------------------------------------------")
    print("Please enter your movie or show name:")
    namesList=df["Title"].unique().tolist()
    print(namesList)
    name=input("Enter")
    if namesList.str.contains(name):
        print("Movie or Show not in data set")
    else:
        return name


def viewingFiguresByName(show):
    amountOfHours=df.loc[df["Title"]==show].copy()
    print(amountOfHours[["Title","Hours Viewed","Views"]])

def showTop10ByHoursViewed():
    newdf=df.nlargest(10, "Hours Viewed")
    print(newdf.to_string())

def showTop10ByTotalViews():
    newdf = df.nlargest(10, "Views")
    print(newdf.to_string())

def calculateTotalHoursViewed():
    print(df["Hours Viewed"].sum())

def viewGraph():
    top10views=df.nlargest(10, "Views")
    plt.figure(figsize=(13, 6))
    plt.xticks(rotation=45, ha='right')
    plt.bar(top10views["Title"],top10views["Views"])
    plt.show()

    top10hviews = df.nlargest(10, "Hours Viewed")
    plt.figure(figsize=(13, 6))
    plt.xticks(rotation=45, ha='right')
    plt.bar(top10hviews["Title"], top10hviews["Hours Viewed"])
    plt.show()



mainMenu()

