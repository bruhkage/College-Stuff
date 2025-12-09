import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dogecoin.csv")
df['Date'] = pd.to_datetime(df['Date'])


plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Volume'], label='Volume', color='blue')
plt.xlabel("Date")
plt.ylabel("Volume")
plt.title("Volume over time")
plt.grid()
plt.show()


