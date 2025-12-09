import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dogecoin.csv")
df= df.loc[df["Close"]>0.1]

plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Close"],color="blue")
plt.xlabel("Date")
plt.xticks(df["Date"], rotation="vertical")
plt.ylabel("Close")
plt.title("Days doge closed higher than 0.1")
plt.grid()
plt.show()
