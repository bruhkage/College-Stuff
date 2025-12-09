import pandas as pd

df = pd.read_csv("cereal.csv")
matching=df.loc[df["rating"]>=30].copy()
matching = matching.nlargest(20,"rating")
print(matching)