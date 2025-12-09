import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dogecoin.csv")
df['Date'] = pd.to_datetime(df['Date'])
df["Price Jump"] = df["Close"] - df["Open"]


plt.figure(figsize=(12, 6))
plt.scatter(df["Date"][::74], df["Price Jump"][::74], label="Price Jump", color="blue")
plt.xlabel("Date")
plt.xticks(df["Date"][::74], rotation=45)
plt.ylabel("Price Jump")
plt.title("Price jump every 74 days")
plt.grid()
plt.show()
