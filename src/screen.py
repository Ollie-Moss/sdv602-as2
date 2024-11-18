import PySimpleGUI as sg


class Screen:
    def __init__(self, title):
        # Controllers
        self.controllers = []

        # PySimpleGUI Window
        self.title = title
        self.layout = []
        self.window = None

        # Window Properties
        self.hidden = True
        self.finalized = False

    def render(self):
        if self.layout != []:
            self.window = sg.Window(self.title, self.layout)

    def finalize(self):
        self.window.finalize()
        self.finalized = True

    def show(self):
        self.hidden = False
        if self.finalized:
            self.window.UnHide()

    def hide(self):
        self.hidden = True
        if self.finalized:
            self.window.Hide()

    def close(self):
        self.window.close()

    # Provides a dialog style popup
    # Blocks event loop, no other windows can be interacted with
    def open(self):
        keep_going = True
        while keep_going:
            event, values = self.window.read()
            keep_going = self.accept_input(event, values)

            if event == sg.WIN_CLOSED or event == 'Exit':
                keep_going = False
            if keep_going is None:
                keep_going = True
        self.close()

    def accept_input(self, event, values):
        if self.hidden == False:
            if self.finalized == False:
                self.finalize()

            print(f"EVENT RECIEVED: {self.window.Title}")
            # Do thing
            for controller in self.controllers:
                keep_going = controller(event)
                if keep_going != None:
                    return keep_going


if __name__ == "__main__":
    screenTest = Screen(layout)
    screenTest.render()

    screenTest.show()
    screenTest.accept_input()

    screenTest2 = Screen([[sg.Button("hi")]])
    screenTest2.render()

    screenTest2.show()
    screenTest2.accept_input()
