FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Reads the to-do text file and returns the to-do list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_list, filepath=FILEPATH):
    """ Writes the to-do item list in the to-do text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_list)


if __name__ == "__main__":
    print(get_todos())
    