# user_prompt = "Enter your todo: "

# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)

# todos = [todo1, todo2, todo3]
# print(todos)

todos = []
while True:
    user_action = input("Type add, show, edit, or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter your todo: ")
            todos.append(todo)
        case "show":
            if (len(todos) == 0):
                print("Your todo list is empty")
                continue
            for item in todos:
                print(f'{todos.index(item) + 1}: {item}')
        case "edit":
            todoIndex = int(input("Enter todo number: ")) - 1
            todos[todoIndex] = input("Enter new todo: ")
        case "exit":
            break
        # case whatever:
        case _:
            print("Unknown command")

            