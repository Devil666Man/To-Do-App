import functions
import time

show_time = time.strftime("%b %d, %Y, %H:%M:%S")
print("It is", show_time)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()  # This line removes all spaces when user provides an input
    user_action = user_action.lower()  # This line defines that any input provided will be converted to lower case

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo + '\n')  # User provided input will be stored in the list one after another

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]
        # This is for removing the extra break lines using list comprehension

        for index, item in enumerate(todos):  # For showing the number of eachtodo item
            item = item.capitalize()  # Makes thetodo lists capital
            item = item.strip('\n')
            row = f"{index + 1}- {item}"  # For optimizing the output
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1  # -1 because list indexing starts from 0

            todos = functions.get_todos()

            new_todo = input("Please enter your new to-do: ")
            todos[number] = new_todo + '\n'  # To assign newtodo item to the assigned number of the list

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid, please enter the right command.")
            continue

    elif user_action.startswith('complete'):
        try:
            completed_todo = int(user_action[9:])

            todos = functions.get_todos()

            index = completed_todo - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number. Please try again")
            continue

    elif user_action.startswith('exit'):
        break  # Program finished

    else:
        print("Invalid command")  # if anything else is entered.

print("Till next time, Peace!")
