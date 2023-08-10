class Task:
    def __init__(self, task_id, title, description, due_date, completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

class ToDoListManager:
    def __init__(self):
        self.tasks = []
        self.current_id = 1

    def add_task(self, title, description, due_date):
        new_task = Task(self.current_id, title, description, due_date)
        self.tasks.append(new_task)
        self.current_id += 1
        print("Task added successfully.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return

        for task in self.tasks:
            status = "Completed" if task.completed else "Not Completed"
            print(f"ID: {task.task_id}| Title: {task.title}| Description: {task.description}| Due Date: {task.due_date}| Completed: {status}")

    def mark_as_completed(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                print("Task marked as completed.")
                return
        print("Task not found.")

    def clear_all_tasks(self):
        self.tasks = []
        self.save_all_tasks()
        print("All tasks cleared.")

    def save_all_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(f"{task.task_id}|{task.title}|{task.description}|{task.due_date}|{task.completed}\n")
        print("All tasks saved.")
        
    def load_tasks_from_file(self):
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    task_info = line.strip().split("|")
                    task_id, title, description, due_date, completed = task_info
                    task = Task(int(task_id), title, description, due_date, completed == "True")
                    self.tasks.append(task)
        except FileNotFoundError:
            pass  # Si el archivo no existe, simplemente continuamos sin cargar tareas