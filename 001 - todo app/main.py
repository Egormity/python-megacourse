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

filenames = ["accounts.txt", "details.csv", "invite.docx"]
filenames = [filename.replace('.', '-hi.') for filename in filenames]
print (filenames)

todos_path = r"C:\Users\kotla\Desktop\python-megacourse\001 - todo app\todos.txt"

while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter your todo: ") + "\n"

            file = open(todos_path, "a")
            file.writelines(todo)
            file.close()
        case "show":
            file = open(todos_path, "r")
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip("\n") for item in todos]

            if (len(todos) == 0):
                print("Your todo list is empty")
                continue
            for index, item in enumerate(todos):
                print(f'{index + 1}: {item.replace('\n', "")}')

        case "edit":
            todo_index = int(input("Enter todo number to edit: ")) - 1
            todos[todo_index] = input("Enter new todo: ")
        case "complete":
            todo_index = int(input("Enter todo number to complete: ")) - 1
            todos.pop(todo_index)
        case "exit":
            break
        # case whatever: = case _:
        case _:
            print("Unknown command")