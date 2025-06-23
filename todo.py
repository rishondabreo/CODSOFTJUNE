# todo.py

tasks = []

def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task name: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else " Not Done"
        print(f"{i}. {task['task']} [{status}]")

def mark_task_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            print(f"Deleted: {deleted['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_task_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting... Have a productive day!")
        break
    else:
        print("Invalid choice. Please choose a number from 1 to 5.")
