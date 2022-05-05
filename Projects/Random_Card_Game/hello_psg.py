# hello_psg.py

import PySimpleGUI as sg

sg.theme('DarkGrey4')

layout = [[sg.Text("Hello")], [sg.Button("Image"), sg.InputText("Pick a card: ")], [sg.Button("Exit")]]

# layout.append([sg.Button("Hi")]) # add a new button to the layout (GUI)

# Create the window
window = sg.Window("Card Game", layout, resizable=True)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Image":
        layout.append([sg.Button("*IMAGE*")])
        window.refresh()

window.close()