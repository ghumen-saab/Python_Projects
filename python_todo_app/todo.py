import json 
from pathlib import Path



Tasks_FILE = Path("tasks.json")


def load_tasks():
    """Load tasks from the JSON file."""
    if not Tasks_FILE.exists():
        return []

    with open(Tasks_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(Tasks_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(title):
    """Add a new task to the list."""
    tasks = load_tasks()

    new_id = max(task["id"] for task in tasks) + 1 if tasks else 1

    new_task = {
        "id": new_id,
        "title": title,
        "completed": False
    }

    tasks.append(new_task)

    save_tasks(tasks)

    print(f"Task '{title}' added successfully.")

def view_tasks():
    """View all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("\n========== YOUR TODOS ==========")

    for task in tasks:
        status = "✓" if task["completed"] else "Pending"
        print(
            f"{task["id"]}.[{status}] {task["title"]}"
        )


def complete_task(task_id):
    """Mark a task as completed."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"Task '{task['title']}' marked as completed.")
            return

    print(f"Task with ID {task_id} not found.")



def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task '{task['title']}' deleted successfully.")
            return

    print(f"Task with ID {task_id} not found.")            