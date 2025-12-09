import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("EPL_20_21.xlsx")

gtotal = df["Goals"].sum()
ptotal = df["Penalty_Attempted"].sum()
pgtotal = df["Penalty_Goals"].sum()

print(f"The total amount of goals is {gtotal}")
print(f"The total amount of penaltys attempted is {ptotal}")
print(f"The total amount of penalty goals is {pgtotal}")

plt.figure(figsize=(13,6))
MissedP = ptotal - pgtotal
data=[pgtotal,MissedP]
labels=["Penalty Goals","Missed Penalty"]
plt.pie(data,labels=labels, autopct= "%.0f%%")
plt.show()