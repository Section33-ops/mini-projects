# 09/21/2025
tasks = []

print("Welcome!")
while True:
    menu = input("To-do List Menu: \n1. Add task \n2. Remove task \n3. View tasks \n4. Quit \nChoose: ")

    if menu == "1":
        add_task = input("Add task: ")
        tasks.append(add_task)
        pass

    elif menu == "2":
        remove_task = input("Remove task: ")
        tasks.remove(remove_task)
        pass
    elif menu == "3":
        for task in tasks:
            print(f"- {task}")
        pass
    elif menu == "4":
        quit()
        pass
    
    else:
        print("Invalid option!")