import pandas as pd

df=pd.read_csv("new_roller_coaster.csv")
df.query("Speed_mph == Speed_mph.max()")
print(df.query("Speed_mph == Speed_mph.max()").to_string())
print("\n")
print(df.query("Height_ft == Height_ft.min()").to_string())
print("\n")
print(df.query("Speed_mph == Speed_mph.min()").to_string())
print("\n")
print(df.query('Type_Main == "Wood"').to_string())
print("\n")
print(df.query('Type_Main == "Steel"').to_string())
print("\n")
print(df.query('Type_Main == "Steel"').max().to_string())

