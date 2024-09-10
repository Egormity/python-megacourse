# user_prompt = "Enter your todo: "

# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)

# todos = [todo1, todo2, todo3]
# print(todos)

todos = []
while True:
    user_action = input("Type add, show, or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter your todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "exit":
            break
        # case whatever:
        case _:
            print("Unknown command")