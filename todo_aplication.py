import os
from datetime import datetime

script_directory = os.path.dirname(os.path.abspath(__file__))
TASKS_DIRECTORY = "data"
DATA_PATH = os.path.join(script_directory, TASKS_DIRECTORY)
TASKS_FILE = os.path.join(DATA_PATH, "tasks.txt")

def load_tasks():
    tasks =[]
    try:
        with open(TASKS_FILE, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"File '{TASKS_FILE}' not found. Creating an empty list.")
        return []
    
def save_tasks(tasks):
    try:
        os.makedirs(DATA_PATH, exist_ok=True)
        
        with open(TASKS_FILE, 'w') as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        print(f"An error occurred while saving tasks: {e}")

def display_tasks(tasks):
    if tasks:
        print("Your ToDo list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your ToDo list is empty!")

def add_task(tasks, task):
    if task.strip():   
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task {task} added to your ToDo list.")
    else:
        print("Task description cannot be empty!")

def remove_task(tasks, index):
    if index >= 1 and index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Your task {removed_task} removed from your ToDo list.")
    else:
        print("Invalid task index!")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Display ToDo list.")
        print("2. Add task.")
        print("3. Remove task.")
        print("4. Exit.")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            task = input("Enter your task: ")
            add_task(tasks, task)
        elif choice == '3':
            try:
                index = int(input("Enter task index to remove:"))
                remove_task(tasks, index)
            except ValueError:
                print("Invalid input! Plaese enter a valid task index.")
        elif choice == '4':
            print("Exiting ToDo list aplication. Good bye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()