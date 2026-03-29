# Task Manager using Lists

tasks = []

def add_task():
    task_name = input("Enter task: ")
    priority = input("Enter priority (High/Medium/Low): ")
    tasks.append({"task": task_name, "priority": priority, "done": False})
    print("Task added!\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return
    
    print("\nTask List:")
    for i, t in enumerate(tasks):
        status = "✔ Done" if t["done"] else "❌ Pending"
        print(f"{i+1}. {t['task']} | Priority: {t['priority']} | {status}")
    print()

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter task number to remove: ")) - 1
        removed = tasks.pop(index)
        print(f"Removed: {removed['task']}\n")
    except:
        print("Invalid input!\n")

def mark_done():
    view_tasks()
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        tasks[index]["done"] = True
        print("Task marked as completed!\n")
    except:
        print("Invalid input!\n")

# Menu
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        mark_done()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice!\n")