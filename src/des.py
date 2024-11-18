import PySimpleGUI as sg
from screen import Screen
from settings import Settings


class DES(Screen):
    def __init__(self, controller, title):
        super().__init__(title)
        self.controller = controller

    def create_layout(self):
        # Create the layout for the chat section of a data explorer screen
        chat = [[sg.Text("Chat")], [sg.Text("", size=(
            40, 5), text_color="#000000", background_color="#FFFFFF", key="-CHAT-")], [sg.Input("", key="-CHAT-IN-"), sg.Button("Send", key="-SEND-")]]

        # Create the layout for the details section of a data explorer screen
        details = [
            [sg.Text("Details")], [sg.Text("Details pertaining to the graph", size=(40, 5), text_color="#000000", background_color="#FFFFFF")]]

        # Extra options such as zooming and navigation
        sideButtons = [[sg.Text("Zoom")], [sg.Button('+', key="-ZOOM-IN-"), sg.Button('-', key="-ZOOM-OUT-")], [sg.Button('Settings', key="-SETTINGS-")],
                       [sg.Text("Navigation")], [sg.Button("<", key="-NAVIGATE-BACK-"), sg.Button(">", key="-NAVIGATE-FORWARD-")]]
        self.controllers.append(self.navigate)
        self.controllers.append(self.open_settings)

        # Combines all the previous layouts and adds the area for the graph to the layout
        # This is the final layout the data explorer screen uses
        self.layout = [[sg.Text('Title', key="title")],
                       [sg.Canvas(size=(600, 400), key="-GRAPH-"),
                        sg.Column(layout=sideButtons)],
                       [sg.Column(layout=chat), sg.Column(layout=details)],
                       [sg.Button('Exit')]]

    def navigate(self, event):
        if event == '-NAVIGATE-FORWARD-':
            self.controller.changeDES(True)
        if event == '-NAVIGATE-BACK-':
            self.controller.changeDES(False)

    def open_settings(self, event):
        if event == '-SETTINGS-':
            settings = Settings(f"Settings for {self.title}")
            settings.create_layout()
            settings.render()
            settings.open()
