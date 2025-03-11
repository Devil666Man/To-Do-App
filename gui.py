import functions
import FreeSimpleGUI as gui

# This is the Add Feature

label = gui.Text("Type in a To-Do")
input_box = gui.InputText(tooltip="Enter To-Do", key="todo")
add_button = gui.Button("Add")

# This is the Edit Feature

list_box = gui.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=[45,10])
edit_button = gui.Button("Edit")

window = gui.Window("My To-Do App",
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    font=("Helvetica", 12))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "todos":
            window["todo"].update(value=values["todos"][0])
        case gui.WINDOW_CLOSED:
            break

window.close()

