import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("electronics_purchases.csv",parse_dates=["Purchase_DateTime"])

#print(df.head())
#print(df.describe())


#print(df[df["Quantity"]>2])
print(df[df["Product"].isin(["Smartphone", "Laptop"])])
print(df[df["Location"].isin("New York","Los Angles")])
