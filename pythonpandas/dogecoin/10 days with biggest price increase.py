import pandas as pd
df=pd.read_csv("Dogecoin.csv")
df["Price Jump"] = df["Close"] - df["Open"]

print(df["Price Jump"].nlargest(10).to_string())
