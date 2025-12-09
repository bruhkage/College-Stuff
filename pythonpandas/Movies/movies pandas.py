
import  pandas as pd
import matplotlib.pyplot as plt
df1=pd.read_csv("movies.csv")
df2=pd.read_csv("ratings.csv")
df3=pd.read_csv("links.csv")
df = pd.merge(df1, df2, on="movieId")
df = pd.merge(df, df3, on="movieId")
df.to_csv("Movies_Combined.csv")

df= df.dropna()
df.reset_index()
df["timestamp"] = pd.to_datetime(df["timestamp"],unit="s")
print(df["title"].value_counts().nlargest(10))
#top_titles = df["title"].value_counts().nlargest(10)
#plt.bar(top_titles.index, top_titles.values)
#plt.xticks(rotation=45, ha="right")
#plt.show()
#print(df["timestamp"].to_string())
print(df["rating"].mean())

df["average rating"] = df.groupby("title")["rating"].transform("mean")
rating_counts = df.groupby("title").size()
highrated = rating_counts[rating_counts > 50].index
highrated = df[df["title"].isin(highrated)]
highrated = highrated.groupby("title")["average rating"].max().reset_index()
print(highrated.nlargest(10,"average rating").to_string())

top10ratings = highrated.nlargest(10,"average rating")
top10ratings = df[df["title"].isin(top10ratings["title"])]
#plt.bar(top10ratings["title"], top10ratings["average rating"], color="skyblue")
#plt.xticks(rotation=45, ha="right")
#plt.show()

df["Year"] = df["title"].str.extract(r'\((\d+)\)$')
years_count = df.groupby("Year")["rating"].mean.reset_index()
years = years_count[years_count].index
print(years)
years= df[df["Year"].isin(years)]

print(years.groupby("Year")["rating"].transform("mean"))