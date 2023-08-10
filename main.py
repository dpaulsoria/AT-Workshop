from util import ToDoListManager, Task

def main():
    todo_manager = ToDoListManager()

    while True:
        print("\n===== To-Do List Manager =====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Clear All Tasks")
        print("5. Save All Tasks")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            todo_manager.add_task(title, description, due_date)
        elif choice == "2":
            todo_manager.list_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as completed: "))
            todo_manager.mark_as_completed(task_id)
        elif choice == "4":
            todo_manager.clear_all_tasks()
        elif choice == "5":
            todo_manager.save_all_tasks()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
