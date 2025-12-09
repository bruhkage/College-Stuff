import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
dates = df.columns.values.tolist()
dates.remove("Produce")
item_name = "Apple"
df2 = df.loc[(df["Produce"] == item_name)]
df2 = df.loc[:, "01/01/2023":"05/01/2023"]
print(df2)



print(dates)