import PySimpleGUI as sg


class WindowController():
    def __init__(self, screens):
        self.screens = {screens[i].title: screens[i]
                        for i in range(0, len(screens))}

    def start(self):
        while True:
            self.update_all_screens()

            window, event, values = sg.read_all_windows()
            if window:
                print(self.screens[window.Title])

            if event == sg.WIN_CLOSED or event == 'Exit':
                window.close()
                break

    def update_all_screens(self):
        for screen in self.screens.values():
            screen.update()
