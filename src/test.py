import copy
import PySimpleGUI as sg

data = {"title": "Des 1"}

chat = [[sg.Text("Chat")], [sg.Text("Chat placeholder", size=(
    40, 5), text_color="#000000", background_color="#FFFFFF", key="-CHAT-")], [sg.Input("", key="-CHAT-IN-"), sg.Button("Send", key="-SEND-")]]

details = [
    [sg.Text("Details")], [sg.Text("Lorem Ipsum", size=(40, 5), text_color="#000000", background_color="#FFFFFF")]]

sideButtons = [[sg.Text("Zoom")], [sg.Button('+', key="-ZOOM-IN-"), sg.Button('-', key="-ZOOM-OUT-")], [sg.Button('Settings', key="-SETTINGS-")],
               [sg.Text("Navigation")], [sg.Button("<", key="-NAVIGATE-BACK-"), sg.Button(">", key="-NAVIGATE-FORWARD-")]]

layout = [[sg.Text('Title', key="title")],
          [sg.Graph(canvas_size=(600, 400), graph_bottom_left=(0, 0), graph_top_right=(
              400, 400), key="graph"), sg.Column(layout=sideButtons)],
          [sg.Column(layout=chat), sg.Column(layout=details)],
          [sg.Button('Exit')]]

window1 = sg.Window(
    title="window1", margins=(0, 0), element_padding=(0, 0), layout=copy.deepcopy(layout), finalize=True)
window2 = sg.Window(
    title="window2", margins=(0,0), element_padding=(0, 0), layout=copy.deepcopy(layout), finalize=True)

while True:
    window, event, values = sg.read_all_windows()

    if event == "-ZOOM-OUT-":
        win1_x, win1_y = window1.current_location()
        window2.move(win1_x, win1_y)

    if event == "-ZOOM-IN-":
        win1_x, win1_y = window1.CurrentLocation()
        win2_x, win2_y = window2.CurrentLocation()
        print("win1 pos:", win1_x, win1_y)
        print("win2 pos:", win2_x, win2_y)

    if window == sg.WIN_CLOSED:
        break
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
