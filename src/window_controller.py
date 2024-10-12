import PySimpleGUI as sg


class WindowController():
    def __init__(self, screens):
        self.screens = screens
        self.currentWindow = self.screens[0]
        self.location = self.currentWindow.window.current_location(True, True)

    def start(self):
        while True:
            self.update_all_screens()

            window, event, values = sg.read_all_windows()

            if window == sg.WIN_CLOSED:
                break
            if event == sg.WIN_CLOSED or event == 'Exit':
                break

            if window:
                curScreen = self.getScreen(window.Title)

                result = curScreen.events[event]()
                if callable(result):
                    result(self)

    def getScreen(self, title):
        return list(filter(lambda screen: screen.title == title, self.screens))[0]

    def update_all_screens(self):

        for screen in self.screens:
            screen.update()
            if screen == self.currentWindow:
                screen.window.UnHide()
            else:
                screen.window.Hide()
        self.currentWindow.window.move(self.location[0], self.location[1])
        print(str(self.currentWindow.window.current_location(True, True)) + " Screen Updated")
        print(str(self.location) + " Screen Updated")


    def changeWindow(self, forward):
        curIndex = self.screens.index(
            self.currentWindow) + (1 if forward else -1)

        curIndex = 0 if curIndex > len(self.screens)-1 else curIndex
        curIndex = len(self.screens)-1 if curIndex < 0 else curIndex
        
        self.location = self.currentWindow.window.current_location(True, True)
        print(str(self.location) + " Window Changed")

        self.currentWindow = self.screens[curIndex]

        self.update_all_screens()
