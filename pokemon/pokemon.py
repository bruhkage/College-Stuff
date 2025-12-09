import pandas as pd
import re
df=pd.read_csv("Modified_pokemon_data.csv")
#print(df.columns)
#print(df["Name"])
#print(df[["Name","Type 1","HP"]])
#print(df[["Name","Type 1","HP"]][0:5])
#print(df.iloc[164])
#for index, row in df.iterrows():
    #print(index, row["Name"])

#print(df.loc[df["Type 1"]== "Fire"])
#print(df.sort_values("Name"))
#df["Total"] = df["HP"] + df["Attack"] + df["Defense"] + df["Sp. Atk"] + df["Sp. Def"] + df["Speed"]
#df = df.drop(columns=["Total"])
#df["Total"] = df.iloc[:,4:11].sum(axis=1)
#cols = list(df.columns)
#df=df[cols[0:4] + [cols[-1]] + cols[4:12]]

#print(df.head(5).tostring())
#print(df.loc[(df["Type 1"]=="Grass") & (df["Type 2"] == "Poison")].to_string())
#print(df.loc[(df["Legendary"]==True)].to_string())
#print(df.loc[(df["Total"]>=600)].to_string())
#new_data = df.loc[df["Type 1"].str.contains("fire|grass", flags= re.I, regex=True)]
#new_data = df.loc[df["Name"].str.contains("^pi[a-z]*", flags= re.I, regex=True)]
df.loc[df["Type 1"]=="Fire", "Type 1"] = "Fuego"
df.loc[df["Type 1"]=="Fuego", "Legendary"] = True
#df=["Mega"]
#df["Mega"] = df.iloc[:,4:11].sum(axis=1)
#df.loc[df["Name"].str.contains("Mega"), "Mega"] = True
#print(df.groupby(["Type 1"]).mean().sort_values("Defense", ascending=False).to_string())

df["Count"]=1
