import streamlit as st
import functions

todos = functions.get_todos()

# Creating a function to retrieve the value from input text field, and add to todos.txt (list)
def add_todo():
    todoToAdd = st.session_state['new_todo'] + "\n"
    #print(todoToAdd)
    todos.append(todoToAdd)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

# Reading data from todos.txt and creating automatically checkbox list
# Implementing here remove item from todos, using a key to each checkbox created.
# If the checkbox was clicked (true), we can remove the item from the list.
# for this we will use enumerate to get the index item.
# After removed, we need to re-write todos list to update it.

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # Let's also delete the session and rerun the code. It's needed for checkboxes.
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a new todo on the list:", placeholder="Add new todo...", on_change=add_todo, key="new_todo")

# If we want to see what is happening with st.session_state during the app is running
# Just use this command somewhere in this file
# st.session_state