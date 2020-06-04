import os
import getpass
import PySimpleGUI as sg
from insta import *
user = getpass.getuser()
os.chdir("/Users/" + user + "/Desktop")

sg.theme('Black')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('What persons photos do you want to download? Please enter the username.')],
            [sg.InputText()],
            [sg.Button('Get the pics')] ]


# Create the Window
window = sg.Window('InstaDownloader', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    print('You entered ', values[0])
    person = values[0]
    if len(person) > 2:
        path(person)
        GetData(person)
    else:
        print("string not long enough")
window.close()

