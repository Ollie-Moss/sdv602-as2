import PySimpleGUI as sg


class DataExplorerScreen():
    def __init__(self, title, data, layout):
        self.title = title
        self.events = {"-ZOOM-IN-": lambda: self.zoom(True),
                       "-ZOOM-OUT-": lambda: self.zoom(False),
                       "-NAVIGATE-FORWARD-": lambda: self.navigate(True),
                       "-NAVIGATE-BACK-": lambda: self.navigate(False),
                       "-SEND-": self.send,
                       "-SETTINGS-": self.settings}
        self.window = sg.Window(self.title, layout, finalize=True)
        self.data = data
        self.chat_room = None
        self.settings = {}


    def update(self):
        graph = self.window.Element("graph")
        graph.DrawRectangle((1, 1), (399, 399), line_color="red")
        for key, value in self.data.items():
            self.window[key].update(value)

    def settings(self):

        pass

    def zoom(self, foward):
        pass

    def navigate(self, forward):
        return lambda winMan: winMan.changeWindow(forward)

    def send(self):
        currentChat = self.window["-CHAT-"].get()
        self.window["-CHAT-"].update(currentChat +
                                     "\n" + self.window["-CHAT-IN-"].get())
