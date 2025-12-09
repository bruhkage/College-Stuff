import pandas as pd

df = pd.read_csv("cereal.csv")
print(df.loc[0])
print("\n \n")
print(df.loc[[0,1]])