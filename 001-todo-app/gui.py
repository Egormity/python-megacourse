from functions import get_todos, write_todos, add_todo
import PySimpleGUI

window = PySimpleGUI.Window("My To-Do App", layout=[
    [PySimpleGUI.Text("Type in a to-do:")],
    [PySimpleGUI.InputText(tooltip="Enter a todo"), PySimpleGUI.Button("Add")],
])

window.read()