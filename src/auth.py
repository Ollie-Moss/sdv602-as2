from screen import Screen
import PySimpleGUI as sg


class Login(Screen):
    def __init__(self, title):
        super().__init__(title)

    def create_layout(self):
        self.layout = [[sg.Text('User Name:'), sg.InputText('', key='User', size=(10, 30))],
                       [sg.Text('Password : '), sg.InputText(
                           '', key='Password', password_char='*', size=(10, 30))],
                       [sg.Button(button_text="Login", size=(10, 2)), sg.Button(
                           button_text="Register", size=(10, 2)), sg.Exit(size=(5, 2))]
                       ]


class Register(Screen):
    def __init__(self, title):
        super().__init__(title)

    def create_layout(self):
        self.layout = [[sg.Text('User Name:'), sg.InputText('', key='User', size=(10, 30))],
                       [sg.Text('Password : '), sg.InputText(
                           '', key='Password', password_char='*', size=(10, 30))],
                       [sg.Button(button_text="Register", size=(10, 2)), sg.Exit(size=(5, 2))]]

