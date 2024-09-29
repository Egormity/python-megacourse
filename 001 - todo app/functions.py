todos_path = r"C:\Users\kotla\Desktop\python-megacourse\001 - todo app\todos.txt"

def get_todos():
    """Read a text file and return the list of to-do items"""
    with open(todos_path, "r") as file:
        todos = file.readlines()
    return todos

def add_todo(todo):
    """Write the to-do item to the text file"""
    with open(todos_path, "a") as file:
        file.writelines(todo)

def write_todos(todos):
    """Write the to-do items list to the text file"""
    with open(todos_path, "w") as file:
        file.writelines(todos)

if __name__ == "__main__":
    print('HELLO FROM THE FUNCTIONS!')