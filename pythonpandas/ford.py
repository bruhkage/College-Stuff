import pandas as pd
import re
import matplotlib as plt
import matplotlib.pyplot as plt
df=pd.read_csv("ford.csv")
#most popular
#most_popular=df["model"].value_counts()
#print(most_popular[ :1].to_string())
#print(df["model"].value_counts().head(1).to_string())

#total cost
#print("£",df["price"].sum())

#finding most popular by year
#year=int(input("Enter a year: "))
#nd=df.loc[df["year"] == year]
#most_popular=nd["model"].value_counts()
#print(most_popular[ :1].to_string())

#finding mileage per pound

#price=df["price"]
#mileage = df["mileage"]
#mpp=mileage/price
#print(mpp.to_string())
df["MPP"]=df["mileage"] / df["price"]
#print(df.sort_values("MPP", ascending=False))

#search for average mpp by model
#model=input("Enter the model name ")
#model = " " + model
#selected_model = df.loc[df["model"].str.contains(model)]
#total=selected_model["MPP"].mean(axis=0)
#print(f"The average mileage per pound of this model is {total}")

#total cost for model
#model=input("Enter the model name ")
#model = " " + model
#selected_model = df.loc[df["model"].str.contains(model)]
#total=selected_model["price"].sum(axis=0)
#print(model, total)



average_prices = df.groupby('model')['price'].mean().reset_index()

# Plotting
plt.figure(figsize=(10, 6))  # Set the figure size

# Create a bar chart
plt.bar(average_prices['model'], average_prices['price'], color='skyblue')

# Add labels and title
plt.xlabel('Car Model')
plt.ylabel('Average Sell Price')
plt.title('Average Sell Price of Each Car Model')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()
