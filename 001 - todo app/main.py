# user_prompt = "Enter your todo: "

# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)

# todos = [todo1, todo2, todo3]
# print(todos)

a = [1, 2, 3]
b = ['a', 'b', 'c']

for num, str in zip(a, b):
    print(num, str)

todosPath = r"C:\Users\kotla\Desktop\python-megacourse\001 - todo app\todos.txt"

while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter your todo: ") + "\n"

            file = open(todosPath, "a")
            file.writelines(todo)
            file.close()
        case "show":
            file = open(todosPath, "r")
            todos = file.readlines()
            file.close()

            if (len(todos) == 0):
                print("Your todo list is empty")
                continue
            for index, item in enumerate(todos):
                print(f'{index + 1}: {item}')

        case "edit":
            todoIndex = int(input("Enter todo number to edit: ")) - 1
            todos[todoIndex] = input("Enter new todo: ")
        case "complete":
            todoIndex = int(input("Enter todo number to complete: ")) - 1
            todos.pop(todoIndex)
        case "exit":
            break
        # case whatever: = case _:
        case _:
            print("Unknown command")