import copy
from data_explorer_screen import *
from window_controller import *
import PySimpleGUI as sg

if __name__ == '__main__':

    data = {"title": "Des 1"}

    chat = [[sg.Text("Chat")], [sg.Text("Chat placeholder", size=(
        40, 5), text_color="#000000", background_color="#FFFFFF", key="-CHAT-")], [sg.Input("", key="-CHAT-IN-"), sg.Button("Send", key="-SEND-")]]

    details = [
        [sg.Text("Details")], [sg.Text("Lorem Ipsum", size=(40, 5), text_color="#000000", background_color="#FFFFFF")]]

    sideButtons = [[sg.Text("Zoom")], [sg.Button('+', key="-ZOOM-IN-"), sg.Button('-', key="-ZOOM-OUT-")], [sg.Button('Settings', key="-SETTINGS-")],
                   [sg.Text("Navigation")], [sg.Button("<", key="-NAVIGATE-BACK-"), sg.Button(">", key="-NAVIGATE-FORWARD-")]]

    layout = [[sg.Text('Title', key="title")],
              [sg.Graph(canvas_size=(600, 400), graph_bottom_left=(0, 0), graph_top_right=(
                  400, 400), key="graph"), sg.Column(layout=sideButtons)],
              [sg.Column(layout=chat), sg.Column(layout=details)],
              [sg.Button('Exit')]]

    des1 = DataExplorerScreen("DES 1", data, copy.deepcopy(layout))
    des2 = DataExplorerScreen("DES 2", data, copy.deepcopy(layout))

    controller = WindowController([des1, des2])
    controller.start()
