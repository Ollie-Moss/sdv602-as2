import PySimpleGUI as sg

"""
Responsible for managing multiple data explorer screen objects and the 
passing of events between them.
"""
class WindowController():
    def __init__(self, screens):
        self.screens = screens
        self.currentWindow = self.screens[0]
        self.location = self.currentWindow.window.current_location(True, True)
    
    # Reads the windows and passes the event read to the correct DES object for handling
    # Handles closing states
    def start(self):
        while True:
            self.update_all_screens()

            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED and window.metadata == "Settings":
                event = "-CANCEL-SETTINGS-"

            if window == sg.WIN_CLOSED and not window.metadata == "Settings":
                break
            if event == sg.WIN_CLOSED or event == 'Exit':
                break

            # This is where the event is passed to the DES Object and if a
            # function is returned from handler it is called
            if window:
                curScreen = self.getScreen(window.Title)
                result = curScreen.events[event]()
                if callable(result):
                    result(self)
    
    # Gets a DES from the self.screens list using the DES title
    # The DES.title is equal to DES.window.title
    # NOTE: DES.title could be removed as DES.window.title is more clear
    def getScreen(self, title):
        return list(filter(lambda screen: screen.title == title, self.screens))[0]

    # Updates all data on each DES
    # Hides and shows each DES based on which one is the current window
    # NOTE: Window should stay in the same place when navigating, but doesn't
    def update_all_screens(self):
        for screen in self.screens:
            screen.update()
            if screen == self.currentWindow:
                screen.window.UnHide()
            else:
                screen.window.Hide()
        self.currentWindow.window.move(self.location[0], self.location[1])

    # Changes window in the direction provided
    # Handles looping
    # NOTE: Should handle the location issue addressed in update_all_screens()
    #       But does not
    def changeWindow(self, forward):
        curIndex = self.screens.index(
            self.currentWindow) + (1 if forward else -1)

        curIndex = 0 if curIndex > len(self.screens)-1 else curIndex
        curIndex = len(self.screens)-1 if curIndex < 0 else curIndex
        
        self.location = self.currentWindow.window.current_location(True, True)

        self.currentWindow = self.screens[curIndex]

        self.update_all_screens()
