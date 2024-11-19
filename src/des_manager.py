from des import DES 
import PySimpleGUI as sg

"""
Responsible for managing multiple data explorer screen objects and the 
passing of events between them.
"""


class DESManager():
    def __init__(self, multiWindow = False):
        self.DESs = []
        self.currentDES = None
        self.multiWindow = multiWindow

    def setup_DESs(self):
        self.DESs.append(DES(self, "DES 1"))
        self.DESs.append(DES(self, "DES 2"))
        self.DESs.append(DES(self, "DES 3"))
        self.currentDES = self.DESs[0]

        for des in self.DESs:
            des.create_layout()
            des.render()

    # Reads the windows and passes the event read to the correct DES object for handling
    # Handles closing states
    def start(self):
        if self.multiWindow:
            for des in self.DESs:
                des.show()
                des.finalize()
                des.update_figure()
                des.start_update_thread()
        else:
            self.currentDES.show()
            self.currentDES.finalize()
            self.currentDES.update_figure()
            self.currentDES.start_update_thread()
        while True:
            if self.multiWindow:
                for des in self.DESs:
                    des.finalize()
                    des.start_update_thread()
                window, event, values = sg.read_all_windows()
                self.currentDES = list(filter(lambda des: des.window.Title == window.Title, self.DESs))[0]
            else:
                event, values = self.currentDES.window.read()

            if event == sg.WIN_CLOSED or event == 'Exit':
                break

            self.currentDES.accept_input(event, values)
            self.currentDES.window.TKroot.update()

    def changeDES(self, forward):
        curIndex = self.DESs.index(
            self.currentDES) + (1 if forward else -1)

        curIndex = 0 if curIndex > len(self.DESs)-1 else curIndex
        curIndex = len(self.DESs)-1 if curIndex < 0 else curIndex

        self.currentDES = self.DESs[curIndex]

        for des in self.DESs:
            if des != self.currentDES:
                des.hide()
            else:
                des.show()
                des.finalize()
                des.update_figure()


if __name__ == '__main__':
    winMan = DESManager()
    winMan.setup_DESs()
    winMan.start()
