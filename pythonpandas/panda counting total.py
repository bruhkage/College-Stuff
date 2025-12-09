import pandas as pd

df = pd.read_csv("cereal.csv")
print(df["type"].value_counts())
highdf