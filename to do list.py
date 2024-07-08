todo_list = []
while True:
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter task to add: ")
        todo_list.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully!")

    elif choice == '2':
        if not todo_list:
            print("No tasks in the list.")
        else:
            print("\n===== Tasks in To-Do List =====")
            for index, task in enumerate(todo_list, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{index}. {task['task']} - {status}")

    elif choice == '3':
        task_number = int(input("Enter task number to mark as completed: "))
        if task_number <= len(todo_list) and task_number > 0:
            todo_list[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    elif choice == '4':
        task_number = int(input("Enter task number to delete: "))
        if task_number <= len(todo_list) and task_number > 0:
            del todo_list[task_number - 1]
            print(f"Task {task_number} deleted.")
        else:
            print("Invalid task number.")

    elif choice == '5':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")