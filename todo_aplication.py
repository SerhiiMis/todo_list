import os
from datetime import datetime
import tkinter as tk 
from tkinter import messagebox 
 
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
        tasks_text = "Your ToDo list:"
        for index, (task, timestamp, priority) in enumerate(tasks, start=1):
            # Print each task with its details
            tasks_text += f"{index}. {task} (Added at: {timestamp}) (Priority: {priority})\n"
        messagebox.showinfo("Tasks", tasks_text)
    else:
        messagebox.showinfo("Tasks", "Your ToDo list is empty!")

# Function to add a new task
def add_task(tasks, task, priority=1):
    if task.strip():  
        timestamp = datetime.now().strftime("%d-%m-%Y") 
        # Add the task along with timestamp and priority to the list
        tasks.append((task, timestamp, priority))
        # Save the updated tasks list
        save_tasks(tasks)
        messagebox.showinfo('Info', f"Task {task} added to your ToDo list.")
    else:
        messagebox.showerror('Error', "Task description cannot be empty!")

# Function to remove a task
def remove_task(tasks, index):
    if index >= 1 and index <= len(tasks):
        # Removed the task at the specified index
        removed_task = tasks.pop(index - 1)
        # Save the updated tasks list
        save_tasks(tasks)
        messagebox.showinfo('Info', f"Your task {removed_task} removed from your ToDo list.")
    else:
        messagebox.showerror('Error', "Invalid task index!")

# Function to exit the aplication
def exit_application(root):
    root.quit()

# Main function to run the ToDo list application
def main():
    # Load tasks from the file
    tasks = load_tasks()
    
    # Main GUI window
    root = tk.Tk()
    root.title("ToDo List")

    # Function for buttons
    def add_button_click():
        task = task_entry.get()
        priority = int(priority_entry.get())
        add_task(tasks, task, priority)
        task_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)

    def remove_button_click():
        index = int(index_entry.get())
        remove_task(tasks, index)
        index_entry.delete(0, tk.END)

    def display_button_click():
        display_tasks(tasks)

    # Widgets
    task_label = tk.Label(root, text="Task:")
    task_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

    task_entry = tk.Entry(root, width=50)
    task_entry.grid(row=0, column=1, padx=5, pady=5)

    priority_label = tk.Label(root, text="Priority (1-10):")
    priority_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    priority_entry = tk.Entry(root, width=5)
    priority_entry.grid(row=1, column=1, padx=5, pady=5)

    add_button = tk.Button(root, text="Add Task", command=add_button_click)
    add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    index_label = tk.Label(root, text="Index to Remove:")
    index_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    index_entry = tk.Entry(root, width=5)
    index_entry.grid(row=3, column=1, padx=5, pady=5)

    remove_button = tk.Button(root, text="Remove Task", command=remove_button_click)
    remove_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    display_button = tk.Button(root, text="Display Tasks", command=display_button_click)
    display_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    exit_button = tk.Button(root, text="Exit", command=lambda: exit_application(root))
    exit_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky='we')
    
    # Run the main loop
    root.mainloop()

    
# Entry point of the script
if __name__ == "__main__":
    main()