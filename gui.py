import functions
import FreeSimpleGUI as gui

label = gui.Text("Type in a To-Do")
input_box = gui.InputText(tooltip="Enter To-Do")
add_button = gui.Button("Add")

window = gui.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()

