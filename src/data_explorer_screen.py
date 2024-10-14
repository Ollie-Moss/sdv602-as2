from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

"""
Data Explorer Screen (DES): 
Handles all events and window management for a given DES.
Features:
- Modifiable graph
- Settings menu for graph
- Chat system
"""


class DataExplorerScreen():
    def __init__(self, title, data, layout, settings):
        self.title = title
        self.events = {"-ZOOM-IN-": lambda: self.zoom(True),
                       "-ZOOM-OUT-": lambda: self.zoom(False),
                       "-NAVIGATE-FORWARD-": lambda: self.navigate(True),
                       "-NAVIGATE-BACK-": lambda: self.navigate(False),
                       "-SEND-": self.send,
                       "-SETTINGS-": self.openSettings,
                       "-CANCEL-SETTINGS-": self.cancelSettings,
                       "-SAVE-SETTINGS-": self.saveSettings
                       }
        self.window = sg.Window(self.title, layout, finalize=True)
        self.chat_room = None
        self.settings = {}
        self.data = data

        # Creates a placeholder line plot
        plt.plot([-1, -4.5, 16, 23])
        self.figure = plt.gcf()
        self.figure_agg = None

        # Ensures the title of the settings window is the same as the main window
        # so events are passed to this object
        self.settingsWindow = sg.Window(self.title, settings, finalize=True)
        self.settingsWindow.Hide()
        self.settingsWindow.metadata = "Settings"

    # Responsible for rendering the self.figure graph
    # Honestly I haven't had a good enough look to full understand
    def draw_figure(self):
        figure_canvas_agg = FigureCanvasTkAgg(
            self.figure, self.window["-GRAPH-"].TKCanvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    # Clears the graph on the window, purely visually
    def delete_figure_agg(self, figure_agg):
        figure_agg.get_tk_widget().forget()
        plt.close('all')

    # Updates all elements, including graph
    def update(self):
        if self.figure_agg:
            # ** IMPORTANT ** Clean up previous drawing before drawing again
            self.delete_figure_agg(self.figure_agg)
        self.figure_agg = self.draw_figure()  # draw the figure

        for key, value in self.data.items():
            self.window[key].update(value)

    def openSettings(self):
        self.settingsWindow.UnHide()
        pass

    def saveSettings(self):
        self.settingsWindow.Hide()
        pass

    def cancelSettings(self):
        self.settingsWindow.Hide()
        pass

    # Changes the zoom level of the graph based on the direction specified
    # NOTE: To be implemented when matplotlib is fully intergrated
    def zoom(self, foward):
        pass

    # Sends the navigate direction back to window controller for handling
    def navigate(self, forward):
        return lambda winMan: winMan.changeWindow(forward)

    # Basic implementation just creates a newline with the provided input
    def send(self):
        currentChat = self.window["-CHAT-"].get()
        self.window["-CHAT-"].update(currentChat +
                                     self.window["-CHAT-IN-"].get() + "\n")
