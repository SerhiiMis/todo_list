import os
from datetime import datetime

# Define the directory and file paths for storing tasks
script_directory = os.path.dirname(os.path.abspath(__file__))
TASKS_DIRECTORY = "data"
DATA_PATH = os.path.join(script_directory, TASKS_DIRECTORY)
TASKS_FILE = os.path.join(DATA_PATH, "tasks.txt")

# Function to load tasks from the file 
def load_tasks():
    tasks =[]
    try:
        with open(TASKS_FILE, 'r') as file:
            for line in file:
                # Split each line to extract task, timestamp, and priority
                task_data = line.strip().split("Added at: ")
                task = task_data[0]
                priority_data = task_data[1].split(") (Priority: ")
                timestamp = priority_data[0]
                priority = int(priority_data[1])
                tasks.append((task, timestamp, priority))
    except FileNotFoundError:
        print(f"File '{TASKS_FILE}' not found. Creating an empty list.")
    return tasks

# Function to save tasks to the file   
def save_tasks(tasks):
    try:
        os.makedirs(DATA_PATH, exist_ok=True)
        
        with open(TASKS_FILE, 'w') as file:
            for task, timestamp, priority in tasks:
                file.write(f"{task} (Added at: {timestamp}) (Priority: {priority}\n")
    except Exception as e:
        print(f"An error occurred while saving tasks: {e}")

# Function to display tasks
def display_tasks(tasks):
    if tasks:
        print("Your ToDo list:")
        for index, (task, timestamp, priority) in enumerate(tasks, start=1):
            # Print each task with its details
            print(f"{index}. {task} (Added at: {timestamp}) (Priority: {priority})\n")
    else:
        print("Your ToDo list is empty!")

# Function to add a new task
def add_task(tasks, task, priority=1):
    if task.strip():  
        timestamp = datetime.now().strftime("%d-%m-%Y") 
        # Add the task along with timestamp and priority to the list
        tasks.append((task, timestamp, priority))
        # Save the updated tasks list
        save_tasks(tasks)
        print(f"Task {task} added to your ToDo list.")
    else:
        print("Task description cannot be empty!")

# Function to remove a task
def remove_task(tasks, index):
    if index >= 1 and index <= len(tasks):
        # Removed the task at the specified index
        removed_task = tasks.pop(index - 1)
        # Save the updated tasks list
        save_tasks(tasks)
        print(f"Your task {removed_task} removed from your ToDo list.")
    else:
        print("Invalid task index!")

# Main function to run the ToDo list application
def main():
    # Load tasks from the file
    tasks = load_tasks()
    
    # Main loop for user interaction
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
            priority = int(input("Enter priority lewel (1 for lowest, 10 for highest)"))
            add_task(tasks, task, priority)
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

# Entry point of the script
if __name__ == "__main__":
    main()