import copy
import matplotlib.pyplot as plt
from data_explorer_screen import *
from window_controller import *
import PySimpleGUI as sg

# This serves as the entry point for the application
# It takes care of procedural creation of objects and providing the intializing fields for these objects
if __name__ == '__main__':

    # Create the layout for the chat section of a data explorer screen
    chat = [[sg.Text("Chat")], [sg.Text("", size=(
        40, 5), text_color="#000000", background_color="#FFFFFF", key="-CHAT-")], [sg.Input("", key="-CHAT-IN-"), sg.Button("Send", key="-SEND-")]]
    
    # Create the layout for the details section of a data explorer screen
    details = [
        [sg.Text("Details")], [sg.Text("Details pertaining to the graph", size=(40, 5), text_color="#000000", background_color="#FFFFFF")]]

    # Extra options such as zooming and navigation
    sideButtons = [[sg.Text("Zoom")], [sg.Button('+', key="-ZOOM-IN-"), sg.Button('-', key="-ZOOM-OUT-")], [sg.Button('Settings', key="-SETTINGS-")],
                   [sg.Text("Navigation")], [sg.Button("<", key="-NAVIGATE-BACK-"), sg.Button(">", key="-NAVIGATE-FORWARD-")]]

    # Combines all the previous layouts and adds the area for the graph to the layout
    # This is the final layout the data explorer screen uses
    layout = [[sg.Text('Title', key="title")],
              [sg.Canvas(size=(600, 400), key="-GRAPH-"), sg.Column(layout=sideButtons)],
              [sg.Column(layout=chat), sg.Column(layout=details)],
              [sg.Button('Exit')]]

    # Creating the settings layout, this could be further split up for readablitiy purposes
    settings = [[sg.Text('Settings', key="title")],
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
                [sg.Push(), sg.Button("Save", key="-SAVE-SETTINGS-"), sg.Button("Cancel", key="-CANCEL-SETTINGS-")]
                ]

    # Create instances of the data explorer screens
    # NOTE: you cannot create multiple windows that are derived from the same instance of an object e.g. sg.Text().
    #       To avoid this each data explorer screen uses a deepcopy of the original layout
    des1 = DataExplorerScreen("DES 1", {"title": "DES 1"}, copy.deepcopy(layout), copy.deepcopy(settings)) 
    des2 = DataExplorerScreen("DES 2 ", {"title": "DES 2"}, copy.deepcopy(layout), copy.deepcopy(settings))
    des3 = DataExplorerScreen("DES 3 ", {"title": "DES 3"}, copy.deepcopy(layout), copy.deepcopy(settings)) 

    # Create the window controller and start it
    # This will handle the reading, event triggering and navigation between windows
    controller = WindowController([des1, des2, des3])
    controller.start()
