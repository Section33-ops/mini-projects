# 10/18/2025

import inventory_item, inventory_manager    # Import the InventoryItem and InventoryManager modules

my_manager = inventory_manager.InventoryManager()   # Create an instance of InventoryManager to manage items


def menu(): # Function that displays the main menu to the user
    print("1. Add item \n2. Display items \n3. Update item \n4. Exit")  # Print menu options
    option = input("Choose an option(1,2,3,4): ")   # Ask the user to select an option

    if option == "1":  # If the user chooses 1
        add_item_option()   # Call the function to add an item
    elif option == "2": # # If the user chooses 2
        display_items_option()  # Call the function to display all items
    elif option == "3": # If the user chooses option 2
        update_item_option()    # Call the function to update an item (currently a placeholder)
    elif option == "4": # If the user chooses option 2
        exit_option()   # Call the function to exit the program

def add_item_option(): # Function to add a new item
    my_manager.add_item()   # Calls the add_item() method from InventoryManager to handle input and storage

def display_items_option(): # Function to display all items in the inventory
    my_manager.display_items()  # Calls rhe dispaly_items() method from InventoryManager to print each item

def update_item_option():   # Function to update an existing item's price or quantity
    print("Feature comming soon")   # Placeholder message until update functionality is implemented

def exit_option():  # Function to exit the program
    exit()  # Terminates the program


while True: # Infinite loop to keep showing the menu until the user chooses to exit
    menu()  # Calls the menu function on each iteration