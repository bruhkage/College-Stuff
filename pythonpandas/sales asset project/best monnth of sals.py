import pandas as pd  # Import pandas for data manipulation
import os            # Import os for operating system interactions
import matplotlib.pyplot as plt  # Import matplotlib for data visualization (plotting)

# Load the CSV file into a DataFrame
df = pd.read_csv("all_data.csv")

# Extract the first two characters (month) from 'Order Date' column and assign it to a new 'Month' column
df["Month"] = df["Order Date"].str[0:2]

print(df.head())  # Display the first 5 rows of the DataFrame to inspect the data

# Filter rows with any missing (NaN) values and create a DataFrame containing only those rows
nan_df = df[df.isna().any(axis=1)]
print(nan_df.head())  # Display rows with NaN values

# Drop rows where all values are missing (NaN)
df = df.dropna(how="all")

print(df.head())  # Display the updated DataFrame after dropping rows with all NaN values

# Remove rows where the 'Order Date' starts with "Or" (likely invalid rows or header data)
df = df[df["Order Date"].str[0:2] != "Or"]

# Convert 'Price Each' and 'Quantity Ordered' columns to numeric values (coercing any errors to NaN)
df["Price Each"] = pd.to_numeric(df["Price Each"])
df["Quantity Ordered"] = pd.to_numeric(df["Quantity Ordered"])

# Convert 'Month' column to an integer type for proper numerical operations
df["Month"] = df["Month"].astype("int32")

# Calculate a new column 'Sales' by multiplying 'Quantity Ordered' and 'Price Each'
df["Sales"] = df["Quantity Ordered"] * df["Price Each"]

# Display the first 20 rows of the updated DataFrame
print(df.head(20).to_string())

# Group data by 'Month' and calculate the sum for each group (aggregating sales data by month)
results = df.groupby("Month").sum()
print(results)  # Display the summarized results by month

# Create a range for months (1 to 12)
months = range(1, 13)
# Plot the total sales for each month as a bar chart
plt.bar(months, results["Sales"])  # Plot bars for 'Sales' by month
plt.xticks(months)  # Set x-axis ticks to show month numbers
plt.ylabel("Sales in USD ($)")  # Label for y-axis
plt.xlabel("Month Number")  # Label for x-axis
plt.show()  # Display the plot

