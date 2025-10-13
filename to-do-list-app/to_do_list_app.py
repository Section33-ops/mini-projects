# 09/21/2025
import os
import csv

tasks = []

def save_tasks(task):   # Function to save tasks to tasks.csv
    with open("tasks.csv", "a", newline="")as tasks_file:   # Open file for appending
        writer = csv.writer(tasks_file)
        writer.writerow([task])
    pass

def load_tasks():
    # Load tasks from tasks.csv only when the program starts or when the user requests to view tasks.
    if os.path.exists("tasks.csv"):  # Check if the file exists first
        with open("tasks.csv", "r", newline="") as tasks_file:
            reader = csv.reader(tasks_file)
            return [row[0] for row in reader]  # Return tasks as a list of strings
    return []  # Return empty list if no tasks exist yet

def delete_tasks(delete_task):
    if delete_task in tasks:
        tasks.remove(delete_task)
        print(f"Removed: {delete_task}")
        save_tasks(tasks)
    else:
        print("Task not found!")

print("Welcome!")

tasks = load_tasks()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    menu = input("To-do List Menu: \n1. Add task \n2. Remove task \n3. View tasks \n4. Quit \nChoose: ")

    if menu == "1":
        add_task = input("Add task: ")
        tasks.append(add_task)
        save_tasks(add_task)
        
    elif menu == "2":
        remove_task = input("Remove task: ")
        delete_tasks(remove_task)
        
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