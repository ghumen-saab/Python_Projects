from todo import(
    add_task,
    view_tasks,
    complete_task,
    delete_task
)
def show_menu():
    print("\n==============================")
    print("Welcome to the Python Todo App!")
    print("==============================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        title = input("Enter the task title: ")
        if title.strip():
            add_task(title)
        else:
            print("Task title cannot be empty. Please try again.")

    elif choice == '2':
        view_tasks()

    elif choice == '3':
        try:
            task_id = int(input("Enter the task ID to mark as completed: "))
            complete_task(task_id)
        except ValueError:
            print("Invalid input. Please enter a valid task ID.")

    elif choice == '4':
        try:
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(task_id)
        except ValueError:
            print("Invalid input. Please enter a valid task ID.")

    elif choice == '5':
        print("Goodbye!")     
        break
    
    else:
        print("Invalid choice. Please try again.")   