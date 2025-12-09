import pandas as pd

df = pd.read_excel("EPL_20_21.xlsx")
print("The country with the most players is:")
print(df["Nationality"].value_counts().nlargest(1).to_string())