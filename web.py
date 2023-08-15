import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    new_todos = st.session_state["new_todo"] + "\n"
    todos.append(new_todos)
    functions.write_todos(todos)


st.title("My todo App")
st.subheader("This is my todo app")
st.write("This app is suppose to help increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Enter a new todo...",
              on_change=add_todo, key='new_todo')
