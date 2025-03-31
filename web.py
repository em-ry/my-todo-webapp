import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("A minimalist todo app")

# remove completed todos
for index, todo in enumerate(todos):
    # assign unique keys so as to reflect in session state.
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

for todo in todos:
    st.checkbox(todo)

# the on_change attribute is like a callback function(takes a custom function)
st.text_input(label="Type your todo", label_visibility="hidden",
              placeholder="Add a todo...", on_change=add_todo,
              key="new_todo")
