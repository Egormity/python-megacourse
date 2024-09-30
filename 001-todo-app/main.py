from functions import get_todos, write_todos, add_todo
import time

print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
while True:
    # GET USER ACTION
    user_action = input("Type add (your todo), show, edit (todo number), complete (todo number), or exit: ").strip()
    
    # HANDLE ADD COMMAND
    if user_action.startswith("add ") or user_action.startswith("new "):
        # GET TODO FROM USER
        todo = user_action[4:]

        # APPEND TODO TO TODOS
        add_todo(todo + '\n')

        # PRINT ADDED TODO
        print(f"Todo {todo} successfully added to the list")

    # HANDLE SHOW COMMAND
    elif user_action.startswith("show"):
         # GET TODOS
        todos = get_todos()

        # PRINT NO TODOS
        if (len(todos) == 0):
            print("Your todo list is empty")
            continue

        # PRINT TODOS
        for index, item in enumerate(todos):
            print(f'{index + 1}: {item.replace('\n', "")}')

    # HANDLE EDIT COMMAND
    elif user_action.startswith("edit "):
        try:
            # GET TODOS
            todos = get_todos() 

            # INDEX OF TODO TO REPLACE
            todo_index = int(user_action[5:]) - 1

            # REPLACE TODO
            todos[todo_index] = input("Enter new todo: ") + '\n'

            # UPDATE TODOS
            write_todos(todos)

        # HANDLE ERRORS
        except (ValueError, IndexError):
            print(f"You entered an invalid todo number {user_action[5:]}")

    # HANDLE COMPLETE COMMAND
    elif user_action.startswith("complete "):
        try:
            # GET TODOS
            todos = get_todos() 

            # UPDATE TODOS
            todo_index = int(user_action[9:]) - 1
            todo_to_remove = todos[todo_index]
            todos.pop(todo_index)

            # UPDATE TODOS
            write_todos(todos)
            
            # PRINT REMOVED TODO
            print(f"Todo '{todo_to_remove.replace('\n', '')}' was removed from the list")
            
        # HANDLE ERRORS
        except (ValueError, IndexError):
            print(f"You entered an invalid todo number {user_action[5:]}")

    # HANDLE EXIT COMMAND
    elif user_action.startswith("exit"):
        break

    # HANDLE UNKNOWN COMMANDS
    else:
        print("Unknown command")

# BUE!
print("Bye!")