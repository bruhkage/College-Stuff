import pandas as pd
df=pd.read_csv("Dogecoin.csv")

CloseMax = df.loc[df["Close"] == df["Close"].max()]
print(CloseMax.to_string())