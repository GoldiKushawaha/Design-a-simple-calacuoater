# Simple Command-Line To-Do List Application

todo_list = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def view_list():
    if not todo_list:
        print("\nYour To-Do list is empty!")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            status = "✔" if task['completed'] else "❌"
            print(f"{idx}. {task['task']} [{status}]")

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

def remove_task():
    view_list()
    try:
        task_num = int(input("Enter task number to remove: "))
        removed_task = todo_list.pop(task_num - 1)
        print(f"Task '{removed_task['task']}' removed successfully!")
    except (IndexError, ValueError):
        print("Invalid task number!")

def mark_completed():
    view_list()
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        todo_list[task_num - 1]['completed'] = True
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number!")

# Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        view_list()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        mark_completed()
    elif choice == '5':
        print("Exiting To-Do List Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        
        
        
  