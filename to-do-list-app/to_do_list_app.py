# 09/21/2025
import os

tasks = []

print("Welcome!")
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    menu = input("To-do List Menu: \n1. Add task \n2. Remove task \n3. View tasks \n4. Quit \nChoose: ")

    if menu == "1":
        add_task = input("Add task: ")
        tasks.append(add_task)
        

    elif menu == "2":
        remove_task = input("Remove task: ")
        if remove_task in tasks:
            tasks.remove(remove_task)
            print(f"Removed: {remove_task}")
        else:
            print("Task not found!")
        
    elif menu == "3":
        if tasks:
            print("Your tasks: ")
            for task in tasks:
                print(f"- {task}")
        else:
            print("No tasks yet!")
        
    elif menu == "4":
        print("Goodbye!")
        break
        
    
    else:
        print("Invalid option!")
    
    input("\nPress Enter to continue...")