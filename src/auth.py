from screen import Screen
import PySimpleGUI as sg
from user_manager import UserManager
from des_manager import DESManager


class Login(Screen):
    def __init__(self, title):
        super().__init__(title)

    def create_layout(self):
        self.controllers.append(self.login)
        self.controllers.append(self.register_button)
        self.layout = [[sg.Text('User Name:'), sg.InputText('', key='User', size=(10, 30))],
                       [sg.Text('Password : '), sg.InputText(
                           '', key='Password', password_char='*', size=(10, 30))],
                       [sg.Button(button_text="Login", key="-LOGIN-", size=(10, 2)), sg.Button(
                           button_text="Register", key="-REGISTER-", size=(10, 2)), sg.Exit(size=(5, 2))]
                       ]

    def login(self, event, values):
        if event == "-LOGIN-":
            UserManager.instance.login(values["User"], values["Password"])
            if UserManager.current_user:
                self.close()
                winMan = DESManager(UserManager.multi)
                winMan.setup_DESs()
                winMan.start()


    def register_button(self, event, values):
        if event == "-REGISTER-":
            register = Register("Register")
            register.create_layout()
            register.render()
            register.open()


class Register(Screen):
    def __init__(self, title):
        super().__init__(title)

    def create_layout(self):
        self.controllers.append(self.signup)
        self.layout = [[sg.Text('User Name:'), sg.InputText('', key='User', size=(10, 30))],
                       [sg.Text('Password : '), sg.InputText(
                           '', key='Password', password_char='*', size=(10, 30))],
                       [sg.Button(button_text="Register", key="-SIGNUP-", size=(10, 2)), sg.Exit(size=(5, 2))]]

    def signup(self, event, values):
        if event == "-SIGNUP-":
            UserManager.instance.signup(values["User"], values["Password"])

