import os
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows

df = pd.read_csv("data/Sales_January_2019.csv")
print(df.head())
print("done")

#files=[file for file in os.listdir("Data")]
#for file in files:
    #print(file)

files=[file for file in os.listdir("Data")]
all_months_data = pd.DataFrame()
dataframe = pd.DataFrame
print(files)

for file in files:
    dataframe = pd.read_csv("Data/" + file)
    all_months_data = pd.concat([all_months_data, dataframe])

all_months_data.to_csv("all_data.csv", index=False)

