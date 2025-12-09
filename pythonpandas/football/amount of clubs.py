import pandas as pd
df = pd.read_excel("EPL_20_21.xlsx")
print(df["Club"].unique())
clubs = df["Club"].unique()
print(f"there are {len(clubs)} unique clubs")