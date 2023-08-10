from behave import given, when, then
from util import ToDoListManager, Task

# Creamos una variable global para mantener el estado de la lista de tareas
todo_manager = None



@given(u'the to-do list is empty')
def step_given_empty_todo_list(context):
    global todo_manager
    todo_manager = ToDoListManager()

@when(u'the user adds a task "{task_info}"')
def step_when_add_task(context, task_info):
    task_id, title, description, due_date, completed = task_info.split("|")
    todo_manager.add_task(title, description, due_date)
    context.last_added_task_id = int(task_id)

@then(u'the to-do list should contain "{task_info}"')
def step_then_check_todo_list(context, task_info):
    task_id, title, description, due_date, completed = task_info.split("|")
    task_id = int(task_id)

    task_found = False
    for task in todo_manager.tasks:
        if task.task_id == task_id:
            assert task.title == title
            assert task.description == description
            assert task.due_date == due_date
            assert task.completed == (completed == "True")
            task_found = True
            break

    assert task_found, f"Task with ID {task_id} not found in the to-do list."

# Elimina las definiciones duplicadas de estos pasos

@when(u'the user marks task "{task_title}" as completed')
def step_when_mark_task_completed(context, task_title):
    for task in todo_manager.tasks:
        if task.title == task_title:
            task.completed = True
            return
    raise ValueError(f"Task '{task_title}' not found.")

@when(u'the user saves the tasks list into tasks.txt')
def step_when_save_tasks(context):
    todo_manager.save_all_tasks()

@then(u'tasks.txt file should show "{task_info}"')
def step_then_check_tasks_file(context, task_info):
    with open("tasks.txt", "r") as file:
        content = file.read()
        assert task_info in content, f"Expected task info not found in file content:\nExpected: {task_info}\nActual: {content}"

@when(u'the user clears the to-do list')
def step_when_clear_todo_list(context):
    todo_manager.clear_all_tasks()

@then(u'the to-do list should be empty')
def step_then_check_empty_todo_list(context):
    assert len(todo_manager.tasks) == 0, "The to-do list is not empty."

@given(u'the to-do list contains tasks')
def step_impl(context):
    pass  # No need to implement this step as it's already implemented

@when(u'the user lists all tasks')
def step_impl(context):
    todo_manager.list_tasks()
    context.list_output = context.stdout_capture.getvalue().strip().split("\n")
    # Imprimir el contenido de context.list_output para depurar
    expected_task_info = {
        "ID": "1",
        "Title": "Acceptance Testing Workshop",
        "Description": "Complete the workshop, the description is in AV",
        "Due Date": "TODAY",
        "Completed": "Not Completed"
    }
    actual_task_info = {}
    for element in context.list_output[0].split("|"):
        key, value = element.split(":")
        actual_task_info[key.strip()] = value.strip()


    # Impresión caracter a caracter para depurar
    for key in expected_task_info:
        print(f"Key: {key}")
        print(f"Expected: {expected_task_info[key]}")
        print(f"Actual  : {actual_task_info[key]}")
        print("----------------------")
    
    assert actual_task_info == expected_task_info, f"Task info mismatch.\nExpected: {expected_task_info}\nActual: {actual_task_info}"

    assert actual_task_info == expected_task_info, f"Task info mismatch.\nExpected: {expected_task_info}\nActual: {actual_task_info}"
    # print("DANANSDNSDANDSDNAA")
    # for line in context.list_output:
    #     print(line)
        
@then(u'the output should contain')
def step_impl(context):
    expected_output = context.text
    actual_output = "\n".join(context.list_output)
    assert expected_output in actual_output, f"Expected output:\n{expected_output}\nActual output:\n{actual_output}"

@then(u'the to-do list should show task "{task_title}" as completed')
def step_impl(context, task_title):
    for task in todo_manager.tasks:
        if task.title == task_title:
            assert task.completed is True
            return
    raise AssertionError(f"Task '{task_title}' is not marked as completed.")

@then(u'command line should show "All tasks saved."')
def step_impl(context):
    assert context.stdout_capture.getvalue().strip() == "All tasks saved.", "Expected output not found"

