import PySimpleGUI as sg
class DataExplorerScreen():
    def __init__(self, title, events, data, layout):
        self.title = title
        self.events = events
        self.window = sg.Window(self.title, layout, finalize=True)
        self.data = data
        self.chat_room = None
        self.settings = {}

    def update(self):
        for key, value in self.data.items():
            self.window[key].update(value)
