
from screen import Screen
import PySimpleGUI as sg


class Settings(Screen):
    def __init__(self, title):
        super().__init__(title)

    def create_layout(self):
        # Creating the settings layout, this could be further split up for readablitiy purposes
        self.layout = [[sg.Text('Settings', key="title")],
                    [sg.Text('Date Range'), sg.Input(
                        "", size=(10, 1), key="-DATE-START-"), sg.Text("-"), sg.Input("", size=(10, 1), key="-DATE-END-")],
                    [sg.Text('Location'), sg.Input("", size=(20, 1), key="-LOCATION-")],
                    [sg.Text('Graph Style'), sg.Combo(
                        ["Line Plot"], key="-GRAPH-STYLE-")],
                    [sg.Text('Data Source'), sg.Combo(
                        ["Data Source 1"], key="-DATA-SOURCE-")],
                    [sg.vtop(sg.Text('Data Toggle')), sg.Column(layout=[[sg.Checkbox("Precipitation")],
                                                        [sg.Checkbox("Temperature")],
                                                        [sg.Checkbox("Feels like temperature")],
                                                        [sg.Checkbox("Humidity")],
                                                        [sg.Checkbox("Minimum")],
                                                        [sg.Checkbox("Average")],
                                                        [sg.Checkbox("Maximum")] 
                                                        ]) ],
                    [sg.Push(), sg.Button("Save", key="-SAVE-SETTINGS-"), sg.Button("Cancel", key="Exit")]
                    ]
        
    def save(self, event, values):
        pass
