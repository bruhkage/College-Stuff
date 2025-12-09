import pandas as pd  # For data manipulation and analysis
import matplotlib.pyplot as plt  # For creating visualizations
from itertools import combinations  # For generating combinations of items
from collections import Counter  # For counting frequency of elements

count = Counter()  # Initialize a Counter object to count combinations of products

def get_state(address):  # Function to extract the state from a given address
    return address.split(",")[2].split(" ")[1]  # Extract the state (2nd part after splitting by space)

df = pd.read_csv("Original_all_data.csv")  # Load the dataset into a pandas DataFrame

df["City"] = df["Purchase Address"].apply(lambda x: x.split(",")[1] + "(" + get_state(x) + ")")
# Create a new "City" column by extracting city and state from "Purchase Address"

results = df.groupby("City").sum()  # Group the data by city and calculate sum of numeric columns

cities = [city for city, df in df.groupby("City")]  # Extract unique city names for visualization

# # Create a bar chart of total sales per city
# plt.bar(cities, results["Sales"], color="skyblue")  # Bar chart with sky-blue bars
# plt.xlabel('Cities')  # Label for the x-axis
# plt.ylabel('Total sales')  # Label for the y-axis
# plt.title('Total sales of Cities')  # Title of the chart
# plt.xticks(rotation=45, ha='right')  # Rotate city names for better readability
# plt.tight_layout()  # Adjust layout to avoid overlap
# plt.show()  # Display the chart

df["Order Date"] = pd.to_datetime(df["Order Date"])  # Convert "Order Date" column to datetime format

df["Hour"] = df["Order Date"].dt.hour  # Extract the hour from "Order Date" into a new column
df["Minute"] = df["Order Date"].dt.minute  # Extract the minute from "Order Date" into a new column

# # Create a line chart of number of orders by hour
# hours = [hour for hour, df in df.groupby("Hour")]  # Extract unique hours for visualization
# plt.plot(hours, df.groupby("Hour").count())  # Plot number of orders for each hour
# plt.xticks(hours)  # Set x-axis ticks to show each hour
# plt.xlabel("Hour")  # Label for the x-axis
# plt.ylabel("Number of Orders")  # Label for the y-axis
# plt.grid()  # Add grid lines for better readability
# plt.show()  # Display the chart

# # Find duplicate rows based on "Order ID" for grouping products in the same order
# duplicate_rows = df[df["Order ID"].duplicated(keep=False)]  # Select duplicate rows

# duplicate_rows["Grouped"] = duplicate_rows.groupby("Order ID")["Product"].transform(lambda x: ",".join(x))
# Combine product names for the same "Order ID" into a single string

# duplicate_rows = duplicate_rows[["Order ID", "Grouped"]].drop_duplicates()  # Remove duplicate rows

# # Count product pairs frequently bought together
# for row in duplicate_rows["Grouped"]:
#     row_list = row.split(",")  # Split grouped products into a list
#     count.update(Counter(combinations(row_list, 2)))  # Count combinations of two products

# # Display the 10 most common product pairs
# for key, value in count.most_common(10):
#     print(key, value)

product_group = df.groupby("Product")  # Group data by "Product"
quantity_ordered = product_group.sum()["Quantity Ordered"]  # Calculate total quantity ordered for each product

products = [product for product, df in product_group]  # Extract unique product names for visualization

plt.bar(products, quantity_ordered)  # Create a bar chart for quantity ordered per product
plt.ylabel("# Ordered")  # Label for the y-axis
plt.xticks(products, rotation=45, size=8)  # Rotate product names and set font size for readability
plt.show()  # Display the chart
