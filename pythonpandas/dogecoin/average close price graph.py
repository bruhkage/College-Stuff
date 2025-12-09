import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dogecoin.csv")
#newdf=df

df["Date"] = pd.to_datetime(df["Date"])

print(df)
df.set_index("Date", inplace=True,drop=False)
average_close = df["Close"].resample("28D").mean()
#date=df["Date"].resample("28D").mean()
#date= pd.to_datetime(date)
#print(average_close)

plt.figure(figsize=(12, 6))
plt.plot( average_close,color="blue")
plt.xlabel("Date")
plt.ylabel("Average Close")
plt.title("AVerage Close price every 28 days")
plt.grid()
plt.show()
