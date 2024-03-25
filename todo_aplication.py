tasks = []

def display_tasks():
    if tasks:
        print("Your ToDo list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your ToDo list is empty!")

def add_task(task):
    tasks.append(task)
    print(f"Task {task} added to your ToDo list.")

def remove_task(index):
    if index >= 1 and index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Your task {removed_task} removed from your ToDo list.")
    else:
        print("Invalid task index!")

while True:
    print("\nWhat would you like to do?")
    print("1. Display ToDo list.")
    print("2. Add task.")
    print("3. Remove task.")
    print("4. Exit.")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        task = input("Enter your task: ")
        add_task(task)
    elif choice == '3':
        index = int(input("Enter task index to remove:"))
        remove_task(index)
    elif choice == '4':
        print("Exiting ToDo list aplication. Good bye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
