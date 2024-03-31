tasks = []

def load_tasks():
    try:
        with open("tasks.txt", 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("File 'tasks.txt' not found. Creating an empty list.")
        return []
    
def save_tasks():
    try:
        with open("tasks.txt", 'w') as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        print(f"An error occurred while saving tasks: {e}")



tasks = load_tasks()

def display_tasks():
    if tasks:
        print("Your ToDo list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your ToDo list is empty!")

def add_task(task):
    if task.strip():   
        tasks.append(task)
        save_tasks()
        print(f"Task {task} added to your ToDo list.")
    else:
        print("Task description cannot be empty!")

def remove_task(index):
    if index >= 1 and index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks()
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
        try:
            index = int(input("Enter task index to remove:"))
            remove_task(index)
        except ValueError:
            print("Invalid input! Plaese enter a valid task index.")
    elif choice == '4':
        print("Exiting ToDo list aplication. Good bye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")

