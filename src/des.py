from settings import Settings
from screen import Screen
from user_manager import UserManager
import time
from datetime import datetime
import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
matplotlib.use('TkAgg')


class DES(Screen):
    def __init__(self, controller, title):
        super().__init__(title)
        self.controller = controller

        # Creates a placeholder line plot
        self.figure = plt.gcf()
        self.figure_agg = None

    def draw_figure(self):

        self.figure = plt.gcf()
        figure_canvas_agg = FigureCanvasTkAgg(
            self.figure, self.window["-GRAPH-"].TKCanvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    # Clears the graph on the window, purely visually
    def delete_figure_agg(self):
        if self.figure_agg:
            self.figure_agg.get_tk_widget().forget()
        plt.close('all')

    def start_update_thread(self):
        if self.window:
            self.window.start_thread(
                lambda: self.update_chat(), ('-THREAD-', '-THREAD ENDED-'))

    def update_chat(self):
        while self.window:
            if self == self.controller.currentDES:
                chats = UserManager.instance.get_chats(self.window.Title)
                chatString = ''.join(list(map(
                    lambda chat: f'{chat["chat"]} - {datetime.fromtimestamp(chat["time_sent"]).strftime("%d/%m/%Y")}\n', chats)))
                self.window["-CHAT-"].update(chatString)
            time.sleep(1)

    # Updates all elements, including graph
    def update_figure(self):
        if self.figure_agg:
            # ** IMPORTANT ** Clean up previous drawing before drawing again
            self.delete_figure_agg()

        if UserManager.current_data_source is not None:
            data = UserManager.current_data_source
            plt.plot(data.datetime, data.temp)
        else:
            plt.plot([])
        self.figure_agg = self.draw_figure()  # draw the figure

    def create_layout(self):
        # Create the layout for the chat section of a data explorer screen
        chat = [[sg.Text("Chat")], [sg.Text("", size=(
            40, 5), text_color="#000000", background_color="#FFFFFF", key="-CHAT-")], [sg.Input("", key="-CHAT-IN-"), sg.Button("Send", key="-SEND-")]]

        # Create the layout for the details section of a data explorer screen
        details = [
            [sg.Text("Details")], [sg.Text("Details pertaining to the graph", size=(40, 5), text_color="#000000", background_color="#FFFFFF")]]

        # Extra options such as zooming and navigation
        sideButtons = [[sg.Text("Zoom")], [sg.Button('+', key="-ZOOM-IN-"), sg.Button('-', key="-ZOOM-OUT-")], [sg.Button('Settings', key="-SETTINGS-")],
                       [sg.Text("Navigation")], [sg.Button("<", key="-NAVIGATE-BACK-"), sg.Button(">", key="-NAVIGATE-FORWARD-")], [sg.Button("Open CSV", key="-OPEN-")]]
        self.controllers.append(self.send_chat)
        self.controllers.append(self.navigate)
        self.controllers.append(self.open_settings)
        self.controllers.append(self.open_csv)

        # Combines all the previous layouts and adds the area for the graph to the layout
        # This is the final layout the data explorer screen uses
        self.layout = [[sg.Text('Title', key="title")],
                       [sg.Canvas(size=(600, 400), key="-GRAPH-"),
                        sg.Column(layout=sideButtons)],
                       [sg.Column(layout=chat), sg.Column(layout=details)],
                       [sg.Button('Exit')]]
    def open_csv(self, event, values):
        if event == '-OPEN-':
            file_name = sg.PopupGetFile('Please select file to open', file_types=(("Comma separated value", "*.csv"),)) 
            if file_name != None :
                UserManager.instance.update_data_source(file_name)
                self.update_figure()

    def send_chat(self, event, values):
        if event == '-SEND-':
            print(UserManager.instance.send_chat(
                values["-CHAT-IN-"], self.window.Title))

    def navigate(self, event, values):
        if event == '-NAVIGATE-FORWARD-':
            self.controller.changeDES(True)
        if event == '-NAVIGATE-BACK-':
            self.controller.changeDES(False)

    def open_settings(self, event, values):
        if event == '-SETTINGS-':
            settings = Settings(f"Settings for {self.title}")
            settings.create_layout()
            settings.render()
            settings.open()
