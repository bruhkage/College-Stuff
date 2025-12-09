import pandas as pd


df = pd.read_csv("cereal.csv")
maxdf=df.nlargest(10,"fat")
mindf=df.nsmallest(10,"fat")
print(mindf)
print(maxdf)