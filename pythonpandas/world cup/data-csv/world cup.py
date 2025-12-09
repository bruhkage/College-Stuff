import pandas as pd
import matplotlib as plt
df=pd.read_csv("goals.csv")



def goalsPerTeam():
    global df
    while True:
        team=input("Enter the team name: ")
        df=df.loc[df["team_name"]==team]
        if df.empty:
            print("Enter A Valid Team\n")
        else:
            break
    print(f"{team} got {len(df)} goals")

def top10goals():
    global df
    print(df["team_name"].value_counts().head(10))

choice = input("1)Goals Per Team\n2)Top 10 countries(goals)\n3)")
if choice == "1":
    goalsPerTeam()
if choice == "2":
    top10goals()