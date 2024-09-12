from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

script_directory = os.path.dirname(os.path.abspath(__file__))
TASKS_DIRECTORY = 'data'
DATA_PATH = os.path.join(script_directory, TASKS_DIRECTORY)
TASKS_FILE = os.path.join(DATA_PATH, 'tasks.txt')
os.makedirs(DATA_PATH, exist_ok=True)

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            for line in file:
                task_data = line.strip().split("Added at: ")
                task = task_data[0]
                priority_data = task_data[1].split('Priority: ')
                timestamp = priority_data[0]
                priority = int(priority_data[1])
                tasks.append((task, timestamp, priority))
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task, timestamp, priority in tasks:
            file.write(f"{task} Added at: {timestamp} Priority: {priority}\n")

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    priority = request.form['priority']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if priority:
        tasks.append((task, timestamp, int(priority)))
    else:
        tasks.append((task, timestamp, 3))

    save_tasks()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

