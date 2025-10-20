# 10/18/2025

import inventory_item, inventory_manager

my_manager = inventory_manager.InventoryManager()


def menu():
    print("1. Add item \n2. Display items \n3. Update item \n4. Exit")
    option = input("Choose an option(1,2,3,4): ")

    if option == "1":
        add_item_option()
    elif option == "2":
        display_items_option()
    elif option == "3":
        update_item_option()
    elif option == "4":
        exit_option()

def add_item_option():
    my_manager.add_item()

def display_items_option():
    my_manager.display_items()

def update_item_option():
    print("What do you want to update? \n1. Update price\n 2. Update quantity")
    update_option = input("Choose 1 or 2")
    if update_option == "1":
        my_manager.update_price
    elif update_option == "2":
        my_manager.update_quantity
    else:
        print("Invalid option")

def exit_option():
    exit()


while True:
    menu()