import pandas as pd

df = pd.read_csv("cereal.csv")
cal=df["calories"]
cups=df["cups"]
cal_per_cup=cal / cups
print(cal_per_cup)