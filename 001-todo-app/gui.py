from functions import get_todos, add_todo, edit_todo, complete_todo
import PySimpleGUI
import time

PySimpleGUI.theme("Black")

window = PySimpleGUI.Window(
    # TITLE
    "My To-Do App",

    # GUI
    layout=[
    [
        PySimpleGUI.Text(time.strftime("%b %d, %Y %H:%M:%S"), key="clock")
    ],
    [
        PySimpleGUI.Text("Type in a to-do:"),
    ],
    [
        PySimpleGUI.InputText(tooltip="Enter a todo", key="todo"), PySimpleGUI.Button("Add")
    ],
    [
        PySimpleGUI.Listbox(values=get_todos(), key="todos", size=[45, 10], enable_events=True),
        PySimpleGUI.Button("Edit"),
        PySimpleGUI.Button("Complete")
    ],
    [
        PySimpleGUI.Button("Exit")
    ]

    ],

    # FONT
    font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=1000)

    match event:
        case "Add":
            add_todo(values["todo"] + "\n")
            window["todos"].update(values=get_todos())
            window["todo"].update(value="")
        
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                edit_todo(todo_to_edit, new_todo + "\n")
                window["todos"].update(values=get_todos())
            except IndexError:
                PySimpleGUI.popup("Please select a todo first", font=("Helvetica", 16))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                complete_todo(todo_to_complete)
                window["todos"].update(values=get_todos())
                window["todo"].update(value="")
            except IndexError:
                PySimpleGUI.popup("Please select a todo first", font=("Helvetica", 16))

        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0])
        
        case PySimpleGUI.WIN_CLOSED:
            break

    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))