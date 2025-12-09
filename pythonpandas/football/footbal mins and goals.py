import pandas as pd

df = pd.read_excel("EPL_20_21.xlsx")

df["Mins Per Match"] = df["Mins"] / df["Matches"]
df["Goals per Match"] = df["Goals"] / df["Matches"]
print(df.to_string())
