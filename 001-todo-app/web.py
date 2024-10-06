import streamlit

from functions import get_todos, add_todo, write_todos

def add_new_todo():
    todo = streamlit.session_state["new_todo"]
    add_todo(todo + "\n")

streamlit.title("My todo app")
streamlit.header("Hello world")
streamlit.write("This app is supposed to increase your <b>productivity</b>", unsafe_allow_html=True)

todos = get_todos()

for index, todo in enumerate(todos):
    checkbox = streamlit.checkbox(label=todo, key=f"{todo}-{index}")
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del streamlit.session_state[f"{todo}-{index}"]
        streamlit.rerun()

streamlit.text_input(label="Enter a todo", placeholder="Type new todo here", key="new_todo", on_change=add_new_todo)

# streamlit.session_state