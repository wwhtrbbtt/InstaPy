import os
import getpass
import PySimpleGUI as sg
from defs import *

user = getpass.getuser()


sg.theme('Black')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.InputCombo(('Instagram - Profile (enter name)', 'Youtube video (enter url, several plattforms supported)'), 'Please select one option', size=(45, 50))],
            [sg.InputText('Where to store the data?'), sg.FolderBrowse()],
            [sg.InputText()],
            [sg.Button('Get the media')] ]


# Create the Window
window = sg.Window('PyLoader', layout)
# Event Loop to process "events" and get the "values" of the inputs



while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        print("quit")
        break
    controller(values)
window.close()

