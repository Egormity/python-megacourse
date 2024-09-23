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

while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter your todo: ") + "\n"
            with open(todos_path, "a") as file:
                file.writelines(todo)
        case "show":
            with open(todos_path, "r") as file:
                todos = file.readlines()

            if (len(todos) == 0):
                print("Your todo list is empty")
                continue
            for index, item in enumerate(todos):
                print(f'{index + 1}: {item.replace('\n', "")}')

        case "edit":
            # GET TODOS
            with open(todos_path, "r") as file:
                todos = file.readlines()

            # UPDATE TODOS
            todo_index = int(input("Enter todo number to edit: ")) - 1
            todos[todo_index] = input("Enter new todo: ") + '\n'

            # UPDATE FILE
            with open(todos_path, "w") as file:
                file.writelines(todos)
        case "complete":
            # GET TODOS
            with open(todos_path, "r") as file:
                todos = file.readlines()

            # UPDATE TODOS
            todo_index = int(input("Enter todo number to complete: ")) - 1
            todo_to_remove = todos[todo_index]
            todos.pop(todo_index)

            # UPDATE FILE
            with open(todos_path, "w") as file:
                file.writelines(todos)
            
            print(f"Todo '{todo_to_remove.replace('\n', '')}' was removed from the list")
        case "exit":
            break
        # case whatever: = case _:
        case _:
            print("Unknown command")