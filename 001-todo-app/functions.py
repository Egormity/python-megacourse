
import os

# TODOS_PATH = r"C:\Users\kotla\Desktop\python-megacourse\001-todo-app\todos.txt"
TODOS_PATH = r"todos.txt"

if (not os.path.exists("todos.txt")):
    with open(TODOS_PATH, "w") as file: 
        pass

def get_todos():
    """Read a text file and return the list of to-do items"""
    with open(TODOS_PATH, "r") as file:
        todos = file.readlines()
    return todos

def add_todo(todo):
    """Write the to-do item to the text file"""
    with open(TODOS_PATH, "a") as file:
        file.writelines(todo)

def write_todos(todos):
    """Write the to-do items list to the text file"""
    with open(TODOS_PATH, "w") as file:
        file.writelines(todos)

def edit_todo(todo_to_edit, new_todo):
    """Edit the to-do item"""
    todos = get_todos()
    old_todo_index = todos.index(todo_to_edit)
    todos[old_todo_index] = new_todo 
    write_todos(todos)

def complete_todo(todo_to_complete):
    """Complete and remove the to-do item"""
    todos = get_todos()
    todos.remove(todo_to_complete)
    write_todos(todos)

if __name__ == "__main__":
    print('HELLO FROM THE FUNCTIONS!')