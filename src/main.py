from data_explorer_screen import *
from window_controller import *
import PySimpleGUI as sg

if __name__ == '__main__':
    events = {}
    data = {"title": "Des 1"}
    layout = [[sg.Text('Window 2', key="title")],
              [sg.Text('Enter something to output to Window 1')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text(size=(25,1), key='-OUTPUT-')],
              [sg.Button('Exit')]]
    des1 = DataExplorerScreen("DES 1", events, data, layout)
    controller = WindowController([des1])
    controller.start()
