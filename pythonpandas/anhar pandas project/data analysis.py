import pandas as pd
import matplotlib.pyplot as plt
import time

df = pd.read_csv("../data.csv")
program_running = True
product_name = df["Produce"].values.tolist()
dates = df.columns.tolist()
dates.remove("Produce")

def display_options():
    print("Choose an option from below:  ")
    print("[1] -- See the whole data set")
    print("[2] -- Sort item names in ascending order")
    print("[3] -- Sort item names in Descending order")
    print("[4] -- Show all available products")
    print("[5] -- Show all available dates")
    print("[6] -- Search date range for all items")
    print("[7] -- Search item name, start date and end date")
    print("[8] -- Show total sales per item in a chart")
    print("[9] -- Show average sales per item in a chart")
    print("[10] -- Show chart for entire dataset ")
    print("[11] -- Exit the program")

def show_full_dataset():
    print(df.to_string())

def sort_dataset(switch):
    sortedDF=df.sort_values("Produce", ascending=switch)
    sortedDF= sortedDF.reset_index(drop=True)
    print(sortedDF.to_string())
def show_average():
    df2 = df.copy()
    df2["Average Sales"] = df2.iloc[:, 1:].mean(axis=1)
    df2["Average Sales"] = df2["Average Sales"].round().astype("int")
    df2 = df2[["Produce", "Average Sales"]]
    print(df2.to_string())

def show_total():
    df2 = df.copy()
    df2["Total Sales"] = df2.iloc[:, 1:].sum(axis=1)
    df2 = df2[["Produce", "Total Sales"]]
    print(df2.to_string())

def product_name_dates(name, start, date):


def make_charts_with_transpose():
    pass

def make_charts():
    pass

def capture_user_input(on_item, from_start, to_end):
    while on_item or from_start or to_end:
        item_name = ""
        if on_item:
            item_name = input("Enter the item name: ")
            item_name = item_name.title()
            if item_name in product_name:
                print("Item " + item_name + " is found")
                on_item = False
                from_start = True
            else:
                print(f"{item_name} is not found. Try again.")
                from_start = False
                to_end = False

            if from_start:
                start_date = input("Enter the start date(dd/mm/yyyy): ")

                if start_date in dates:
                    print(f"{start_date} is valid")
                    start_index = dates.index(start_date)
                    from_start = False
                    to_end = True
                else:
                    print(f"{start_date} is not valid. Try again")
                    from_start = True
                    to_end=False

            if to_end:
                end_date = input("Enter the end date(dd/mm/yyyy): ")
                if end_date in dates:
                    print(f"{end_date} is valid")
                    end_index = dates.index(end_date)
                    if start_index >= end_index:
                        print("End date cannot be the same date as or earlier than start date")
                        print("Enter start and end date again")
                        from_start=True
                        to_end=False
                    else:
                        to_end=False
                        product_name_dates(item_name,start_date,end_date)
                else:
                    print("End date is not valid")
                    to_end=True

while program_running:
    time.sleep(1)
    print("\n \n")
    display_options()
    user_input= input("Enter a selection: ")
    if user_input == "1":#prints the full data set
        print("the full data set is displayed below: ")
        show_full_dataset()

    elif user_input == "2":#prints the product name in ascending order
        print("Product names in ascending order: ")
        sort_dataset(True)

    elif user_input == "3":#prints the product name in descending order
         print("Product names in descending order")
         sort_dataset(False)

    elif user_input == "4":#prints all product names
        print("All available products")
        print(product_name)

    elif user_input == "5":#prints all available dates
        print("All available dates are: ")
        print(dates)

    elif user_input == "6":#allows the user to input a range of dates
        print("Enter a range of dates to search")
        capture_user_input(False, True,True)

    elif user_input == "7":#allows the user to search using item details
        print("Enter item name, start date and end date to search")
        capture_user_input(True,True,True)

    elif user_input == "8":#shows the total sales per item
        print("Showing the total sales per item")
        show_total()
    elif user_input == "9":#shows average sales per item
        print("Showing average sales per item")
        show_average()

    elif user_input == "10":#shows the chart for the data set
        print("Showing the chart for the data set")

    elif user_input == "11":#exits the program
        print("Goodbye and have a good day")
        break
