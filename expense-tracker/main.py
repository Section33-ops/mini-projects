# 10/27/2025

expenses = []

def add_expense_option():
    item = input("What did you buy? ")
    item_price = float(input("How much did it cost? "))
    item_quantity = int(input("How many did you buy? "))
    total_cost = round(item_price * item_quantity,)
    item_expense = (item, item_price, item_quantity, total_cost)
    expenses.append(item_expense)

def view_expenses_option():
    for expense in expenses:
        print(f"Item: {expense[0]}, Price: {expense[1]}, Quantity: {expense[2]}, Total cost: {expense[3]}")

def view_total_option():
    pass

def menu():
    print("Welcome to the Expense Tracker! \n1. Add expense \n2. View expenses \n3. View total \n4. Exit")
    option = input("Choose an option: ")

    if option == "1":
        add_expense_option()
    elif option == "2":
        view_expenses_option()
    elif option == "3":
        pass
    elif option == "4":
        exit()
    else:
        print("You must enter a number for the option")

while True:
    menu()
    