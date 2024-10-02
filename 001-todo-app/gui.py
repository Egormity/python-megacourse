from functions import get_todos, write_todos, add_todo, edit_todo
import PySimpleGUI

window = PySimpleGUI.Window(
    # TITLE
    "My To-Do App",

    # GUI
    layout=[
    [
        PySimpleGUI.Text("Type in a to-do:"),
    ],
    [
        PySimpleGUI.InputText(tooltip="Enter a todo", key="todo"), PySimpleGUI.Button("Add")
    ],
    [
        PySimpleGUI.Listbox(values=get_todos(), key="todos", size=[45, 10], enable_events=True),
        PySimpleGUI.Button("Edit")
    ]
    ],

    # FONT
    font=('Helvetica', 16))

while True:
    event, values = window.read()
    # print(event, values)

    match event:
        case "Add":
            add_todo(values["todo"] + "\n")
            window["todos"].update(values=get_todos())
        
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]
            edit_todo(todo_to_edit, new_todo + "\n")
            window["todos"].update(values=get_todos())

        case "todos":
            window["todo"].update(value=values["todos"][0])
        
        case PySimpleGUI.WIN_CLOSED:
            break