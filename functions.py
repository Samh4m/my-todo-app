FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as files_local:  # context manager better optimization
        todos_local = files_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do items list in the text file."""
    with open(filepath, 'w') as files:  # context manager
        files.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos())
     