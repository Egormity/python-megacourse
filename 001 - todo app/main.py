# user_prompt = "Enter your todo: "

# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)

# todos = [todo1, todo2, todo3]
# print(todos)

# a = [1, 2, 3]
# b = ['a', 'b', 'c']

# for num, str in zip(a, b):
#     print(num, str)

# filenames = ["accounts.txt", "details.csv", "invite.docx"]
# filenames = [filename.replace('.', '-hi.') for filename in filenames]
# print (filenames)

todos_path = r"C:\Users\kotla\Desktop\python-megacourse\001 - todo app\todos.txt"

def get_todos():
    with open(todos_path, "r") as file:
        todos = file.readlines()
    return todos


while True:
    user_action = input("Type add (your todo), show, edit (todo number), complete (todo number), or exit: ").strip()
    
    if user_action.startswith("add ") or user_action.startswith("new "):
        todo = user_action[4:]
        with open(todos_path, "a") as file:
            file.writelines(todo + '\n')
        print(f"Todo {todo} successfully added to the list")

    elif user_action.startswith("show"):
        todos = get_todos()

        if (len(todos) == 0):
            print("Your todo list is empty")
            continue
        for index, item in enumerate(todos):
            print(f'{index + 1}: {item.replace('\n', "")}')

    elif user_action.startswith("edit "):
        try:
            todos = get_todos()

            # UPDATE TODOS
            todo_index = int(user_action[5:]) - 1
            todos[todo_index] = input("Enter new todo: ") + '\n'

            # UPDATE FILE
            with open(todos_path, "w") as file:
                file.writelines(todos)

        except (ValueError, IndexError):
            print(f"You entered an invalid todo number {user_action[5:]}")

    elif user_action.startswith("complete "):
        try:
            todos = get_todos()

            # UPDATE TODOS
            todo_index = int(user_action[9:]) - 1
            todo_to_remove = todos[todo_index]
            todos.pop(todo_index)

            # UPDATE FILE
            with open(todos_path, "w") as file:
                file.writelines(todos)
            
            print(f"Todo '{todo_to_remove.replace('\n', '')}' was removed from the list")
            
        except (ValueError, IndexError):
            print(f"You entered an invalid todo number {user_action[5:]}")

    elif user_action.startswith("exit"):
        break

    else:
        print("Unknown command")

print("Bye!")