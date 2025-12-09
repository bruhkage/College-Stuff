import pandas as pd
df = pd.read_excel("EPL_20_21.xlsx")
middle_field = df.loc[df["Position"] == "MF"]
print(middle_field)
AstonVilla = df.loc[df["Club"] == "Aston Villa"]
print(AstonVilla)