TODOS_PATH = r"C:\Users\kotla\Desktop\python-megacourse\001 - todo app\todos.txt"

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

if __name__ == "__main__":
    print('HELLO FROM THE FUNCTIONS!')