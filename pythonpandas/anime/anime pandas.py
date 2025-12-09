


import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("anime-filteredUpdated.csv")

def  top10Rating():
    global df
    df=df.sort_values("Score",ascending=False)
    df=df.head(10)
    topten=df.groupby("Name",sort=False)["Score"].max()
    print(topten)

def top10Popularity():
    global df
    df = df.sort_values("Popularity", ascending=True)
    df = df.head(10)
    print(df.to_string())

def averageScore():
    global df
    averagescore=df["Score"].mean()
    df = df.sort_values("Popularity", ascending=True)
    df = df.head(10)
    top10Average=df["Score"].mean()
    print(f"The average score of all anime is {averagescore:.2f} while the average for the top 10 most popular anime is {top10Average:.2f}")

def popular_AiringvsFinished():
    global df
    choice=input("1)Top 10 popular(Airing)\n2)Top 10 popular(Finished)\n")
    while True:
        if choice =="1":
            df=df.loc[df["Status"]=="Currently Airing"]
            df = df.sort_values("Popularity", ascending=True)
            print(df.head(10).to_string())
            break
        if choice =="2":
            df=df.loc[df["Status"]=="Finished Airing"]
            df = df.sort_values("Popularity", ascending=True)
            print(df.head(10).to_string())
            break
        else:
            print("Invalid Choice")


def PopularityvsScore():
    global df
    popular = df.sort_values("Popularity", ascending=True)
    popular = popular.head(10)
    names = popular["Name"]
    score = popular["Score"]
    popularity = popular["Popularity"]
    plt.yticks([1,2,3,4,5,6,7,8,9,10])

    plt.plot(names, popularity, label="Popularity", marker="o")
    plt.plot(names, score, label="Score", marker="o")
    plt.xlabel("Anime")
    plt.ylabel("Score")
    plt.title("Popular Anime(Popularity vs Score)")
    plt.legend()
    plt.xticks(rotation=45, ha="right")
    plt.show()

def genreCount():
    global df
    action=df.loc[df["Genres"].str.contains("Action")]
    adventure=df.loc[df["Genres"].str.contains("Adventure")]
    scifi=df.loc[df["Genres"].str.contains("Sci-Fi")]
    drama=df.loc[df["Genres"].str.contains("Drama")]
    comedy=df.loc[df["Genres"].str.contains("Comedy")]
    romance=df.loc[df["Genres"].str.contains("Romance")]
    print(f"Action:{len(action)} \nAdventure:{len(adventure)} \nSci-Fi:{len(scifi)} \nDrama:{len(drama)} \nComedy:{len(comedy)} \nRomance:{len(romance)}")

def genreAverageScore():
    global df
    action = df.loc[df["Genres"].str.contains("Action")]
    adventure = df.loc[df["Genres"].str.contains("Adventure")]
    scifi = df.loc[df["Genres"].str.contains("Sci-Fi")]
    drama = df.loc[df["Genres"].str.contains("Drama")]
    comedy = df.loc[df["Genres"].str.contains("Comedy")]
    romance = df.loc[df["Genres"].str.contains("Romance")]

    action=action["Score"].mean()
    adventure=adventure["Score"].mean()
    scifi=scifi["Score"].mean()
    drama=drama["Score"].mean()
    comedy=comedy["Score"].mean()
    romance=romance["Score"].mean()

    genres = ["Action", "Adventure", "Sci-Fi", "Drama", "Comedy", "Romance"]
    scores = [action, adventure, scifi, drama, comedy, romance]

    plt.bar(genres, scores)
    plt.xlabel("Genres")
    plt.ylabel("Average Score")
    plt.title("Average Scores by Genre")
    plt.show()

def trends():
    global df
    df=df.loc[df["Genres"].str.contains("Ecchi")]
    print(df.to_string())

option = input("1)Top 10 anime(Rating)\n2)Top 10 anime(Popularity)\n3)Average Score Vs Top 10 Average Score\n4)Popular Airing vs Popular Finished\n5)Popular Anime(Popularity vs Score)\n6)Genre Count\n7)Average Score of Genres\n")
if option == "1":
    top10Rating()
if option == "2":
    top10Popularity()
if option == "3":
    averageScore()
if option == "4":
    popular_AiringvsFinished()
if option =="5":
    PopularityvsScore()
if option =="6":
    genreCount()
if option =="7":
    genreAverageScore()
if option =="8":
    trends()