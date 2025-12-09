import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dogecoin.csv")
close00 = df.loc[df["Close"]<=0.1]
#close01= df.loc[df["Close"]>0.1 & (df["Close"] <= 0.2)]
close01= df.loc[(df["Close"]>0.1) & (df["Close"] <= 0.2)]
close02= df.loc[(df["Close"]>0.2) & (df["Close"] <= 0.3)]
close03= df.loc[(df["Close"]>0.3) & (df["Close"] <= 0.4)]
close04= df.loc[(df["Close"]>0.4) & (df["Close"] <= 0.5)]
close05= df.loc[(df["Close"]>0.5) & (df["Close"] <= 0.6)]

closes = [len(close00["Close"]),len(close01["Close"]),len(close02["Close"]),len(close03["Close"]),len(close04["Close"]),len(close05["Close"])]
ranges = ["<=0.1", ">0.1 to 0.2", ">0.2 to 0.3", ">0.3 to 0.4", ">0.4 to 0.5", ">0.5 to 0.6"]
plt.figure(figsize=(12, 6))
plt.bar(ranges,closes)
plt.xlabel("Close Price")
plt.ylabel("amount of days")
plt.grid()
plt.show()

