# As we are using text file to keep the data added from user, we do not need todos=[] anymore here.
# Let's introduce custom functions to avoid repetitive code.

# Function get_todos() to retrieve data from the text.file
def get_todos(filepath="todos.txt"):   #We are defining default argument that can avoid using the same arg repeatly.
    #One good practice is to insert information about the function right below its declaration.
    #   This info will be helpful to construct what we call docstring (a documentation about the program)
    #   To do that, just include some texts under triple quotes.

    """ This function reads a text file and return the list of to-do items. To exhibit the documentation, we can type: print(help(get_todos)). """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos
def write_todos(todos_arg, filepath="todos.txt"):  # When we use default and non-default parameter, it's better to start with non-default as primary argument. them the default parameter
    """ Write the to-do items in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# There are some conditionals or methods that we can only execute when we call the file that contains them. See below:
if __name__ == "__main__":
    print("Hello")
    print(get_todos())

# In this case above, even we import this file (functions.py) this conditional will not be executed. Only we execute functions.py directly.
