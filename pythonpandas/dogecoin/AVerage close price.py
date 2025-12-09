import pandas as pd
df=pd.read_csv("Dogecoin.csv")
average = df["Close"].mean()
print(f"the average close price is{average}")
