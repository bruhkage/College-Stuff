import pandas as pd
import datetime
import matplotlib.pyplot as plt
df = pd.read_csv("Task4a_data.csv")

def profit_loss_menu():

    flag = True
    
    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show profit/loss for specific products")
        print("2. Show profit/loss for all products")
        print("###############################################")

        profit_loss_choice = input("Please enter the number of your choice (1-2): ")

        try:
            int(profit_loss_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(profit_loss_choice) < 1 or int(profit_loss_choice) > 2:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                return int(profit_loss_choice) 




def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a product form the list:")
        print("Please enter the number of the product (1-16)")
        print("1.  Potatoes")
        print("2.  Carrots")
        print("3.  Peas")
        print("4.  Lettuce")
        print("5.  Onions")
        print("6.  Apples")
        print("7.  Oranges")
        print("8.  Pears")
        print("9.  Lemons")
        print("10. Limes")
        print("11. Melons")
        print("12. Cabbages")
        print("13. Asparagus")
        print("14. Broccoli")
        print("15. Cauliflower")
        print("16. Celery")
        print("######################################################")

        product_list = ["Potatoes", "Carrots", "Peas", "Lettuce", "Onions", 
"Apples", "Oranges", "Pears", "Lemons", "Limes","Melons", "Cabbages", 
"Asparagus", "Broccoli", "Cauliflower", "Celery"]

        product_choice = input("Please enter the number of your choice (1-16): ")

        try:
            int(product_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(product_choice) < 1 or int(product_choice) > 16:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                product_name = product_list[int(product_choice)-1]
                return product_name



def get_start_date():
    optioninput =int(input("Choose an Option \n(1)Show amount of products sold by supplier \n(2) Show total amount of sales over a range of time \n(3) Show top 10 most sold products \n(4)Profit made per supplier \n"))

    if optioninput == 2:
        flag = True

    if optioninput== 1:
        products_sold_suppliers()
        exit()

    if optioninput ==3:
        top_ten_products()
        exit()
    if optioninput ==4:
        profit_made()
        exit()
    while flag:
        start_date = input('Plese enter start date for your time range (DD/MM/YYYY')

        try:
           pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            return pd.to_datetime(start_date, dayfirst=True)


def top_ten_products():
    products=df["Product"].value_counts()
    print(products.nlargest(10).to_string())


def products_sold_suppliers():
    FarmDirect = df.loc[df["Supplier"] == "Farm Direct"]
    FarmDirect = FarmDirect["Product"].value_counts()

    NaturalBest = df.loc[df["Supplier"] == "Natural Best"]
    NaturalBest = NaturalBest["Product"].value_counts()

    NatureFood = df.loc[df["Supplier"] == "Nature Food"]
    NatureFood = NatureFood["Product"].value_counts()

    GrocersInt = df.loc[df["Supplier"] == "Grocers Int."]
    GrocersInt = GrocersInt["Product"].value_counts()

    CleanLiving = df.loc[df["Supplier"] == "Clean Living"]
    CleanLiving = CleanLiving["Product"].value_counts()

    optioninput = int(input("Choose an Option \n(1) Farm Direct \n(2)Natural Best \n(3)Nature Food \n(4) Grocers Int. \n(5)Clean Living \n(6)Graph totaling products sold by suppliers \n"))

    if optioninput ==1:
        print(FarmDirect.to_string())
    elif optioninput ==2:
        print(NaturalBest.to_string())
    elif optioninput ==3:
        print(NatureFood.to_string())
    elif optioninput ==4:
        print(GrocersInt.to_string())
    elif optioninput == 5:
        print("\n",CleanLiving.to_string())
    elif optioninput == 6:
        products_sold =[FarmDirect.sum(),NaturalBest.sum(),NatureFood.sum(),GrocersInt.sum(),CleanLiving.sum()]
        Suppliers = ["Farm Direct","Natural Best","Nature Food","Grocers Int.","Clean Living"]
        plt.figure(figsize=(12, 6))
        plt.bar(Suppliers, products_sold)
        plt.xlabel("Supplier")
        plt.ylabel("Products Sold")
        plt.grid()
        plt.show()


def profit_made():
    optioninput = int(input("Choose an Option \n(1) Farm Direct \n(2)Natural Best \n(3)Nature Food \n(4) Grocers Int. \n(5)Clean Living \n"))
    if optioninput ==1:
        FarmDirect = df.loc[df["Supplier"] == "Farm Direct"]
        amountMade = FarmDirect["Selling Price"].sum()
        amountSpent = FarmDirect["Purchase Price"].sum()
        profit = amountMade - amountSpent
        print(f"You made a profit of £{profit:,.2f}")

    elif optioninput == 2:
        NaturalBest = df.loc[df["Supplier"] == "Natural Best"]
        amountMade = NaturalBest["Selling Price"].sum()
        amountSpent = NaturalBest["Purchase Price"].sum()
        profit = amountMade - amountSpent
        print(f"You made a profit of £{profit:,.2f}")

    elif optioninput == 3:
        NatureFood = df.loc[df["Supplier"] == "Nature Food"]
        amountMade = NatureFood["Selling Price"].sum()
        amountSpent =  NatureFood["Purchase Price"].sum()
        profit = amountMade - amountSpent
        print(f"You made a profit of £{profit:,.2f}")

    elif optioninput == 4:
        GrocersInt = df.loc[df["Supplier"] == "Grocers Int."]
        amountMade = GrocersInt["Selling Price"].sum()
        amountSpent = GrocersInt["Purchase Price"].sum()
        profit = amountMade - amountSpent
        print(f"You made a profit of £{profit:,.2f}")

    elif optioninput == 5:
        CleanLiving = df.loc[df["Supplier"] == "Clean Living"]
        amountMade = CleanLiving["Selling Price"].sum()
        amountSpent =CleanLiving["Purchase Price"].sum()
        profit = amountMade - amountSpent
        print(f"You made a profit of £{profit:,.2f}")
    elif optioninput ==6:
        FarmDirect = df.loc[df["Supplier"] == "Farm Direct"]
        Farm_amountMade =  FarmDirect["Selling Price"].sum()
        Farm_amountSpent =  FarmDirect["Purchase Price"].sum()

        NaturalBest = df.loc[df["Supplier"] == "Natural Best"]
        Natural_amountMade = NaturalBest ["Selling Price"].sum()
        Natural_amountSpent = NaturalBest ["Purchase Price"].sum()

        NatureFood = df.loc[df["Supplier"] == "Nature Food"]
        Nature_amountMade = NatureFood["Selling Price"].sum()
        Nature_amountSpent = NatureFood["Purchase Price"].sum()

        GrocersInt = df.loc[df["Supplier"] == "Grocers Int."]
        Grocers_amountMade =  GrocersInt["Selling Price"].sum()
        Grocers_amountSpent = GrocersInt["Purchase Price"].sum()

        CleanLiving = df.loc[df["Supplier"] == "Clean Living"]
        Clean_amountMade = CleanLiving["Selling Price"].sum()
        Clean_amountSpent = CleanLiving["Purchase Price"].sum()

def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Plese enter end date for your time range (DD/MM/YYYY')

        try:
           pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            return pd.to_datetime(end_date, dayfirst=True)

def get_date_range_all():
    df1 = pd.read_csv("Task4a_data.csv") 

    df1["Date"] = pd.to_datetime(df1["Date"], dayfirst=True)

    results = df1.loc[(df1["Date"] >= start_date) & (df1["Date"] <= end_date), df1.columns != "Supplier"].copy()
    
    results["Cost Subtotal"] = results["KGs Purchased"] * results["Purchase Price"]
    results["Sales subtotal"] = results["KGs Sold"] * results["Selling Price"]
    results["Profit subtotal"] = results["Sales subtotal"] - results["Cost Subtotal"]
    
    total = round(results["Profit subtotal"].sum(),2)
    results_print = results.to_string(index=False)
    
    print(results_print)
    print("The overall profit/loss for the selected time frame was £{}".format(total))



def get_date_range_product():
    product_name = get_product_choice()
    df2 = pd.read_csv("Task4a_data.csv") 


    df2["Date"] = pd.to_datetime(df2["Date"], dayfirst=True)
   
    product_results = df2.loc[(df2["Date"] >= start_date) & (df2["Date"] <= end_date) & (df2["Product"] == product_name)].copy()

    product_results["Cost Subtotal"] = product_results["KGs Purchased"] * product_results["Purchase Price"]
    product_results["Sales subtotal"] = product_results["KGs Sold"] * product_results["Selling Price"]
    product_results["Profit subtotal"] = product_results["Sales subtotal"] - product_results["Cost Subtotal"]
    
    total = round(product_results["Profit subtotal"].sum(),2)
    results_print = product_results.to_string(index=False)
    
    print(results_print)
    print("The profit/loss for the {} for selected time frame was £{}".format(product_name, total))


def process_menu_choice():

    if profit_choice == 1:
        get_date_range_product()
    else:
        get_date_range_all()

start_date = get_start_date()
end_date = get_end_date()
profit_choice = profit_loss_menu()
process_menu_choice()

