import pandas as pd
df=pd.read_csv("Dogecoin.csv")
average = df["Volume"].mean()
average=format(average, ',')
print(average)