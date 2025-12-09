import pandas as pd
df = pd.read_excel("EPL_20_21.xlsx")
print("The club with the most players is:")
print(df["Club"].value_counts().nlargest(1).to_string())
print("\n")
print("The club with the least players is:")
print(df["Club"].value_counts().nsmallest(1).to_string())

