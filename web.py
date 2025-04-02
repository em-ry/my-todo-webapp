import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    if new_todo not in todos:
        todos.append(new_todo)
        functions.write_todos(todos)
        # Clear the input box after hitting enter
        st.session_state["new_todo"] = ""
    else:
        st.warning("No duplicate todo items!!")


st.title("Quick Online Todo App")
st.subheader("A minimalist todo app")

# remove completed todos
for index, todo in enumerate(todos):
    # assign unique keys so it reflects in session state.
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

# the on_change attribute is a callback function(takes a custom function)
st.text_input(label="Type your todo", label_visibility="hidden",
              placeholder="Add a todo...", on_change=add_todo,
              key="new_todo", value="")
