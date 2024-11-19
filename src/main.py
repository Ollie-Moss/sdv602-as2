from des_manager import DESManager
from auth import Login, Register
from settings import Settings
from user_manager import UserManager
import argparse
import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
matplotlib.use('TkAgg')


if __name__ == '__main__':
    sg.set_options(dpi_awareness=True, scaling=plt.gcf().dpi/72)
    # Creates instance of user manager
    UserManager()
    parser = argparse.ArgumentParser()

    parser.add_argument('--multi', action='store_true', help="Enabled multi-window mode for the application")

    args = parser.parse_args()

    UserManager.multi = args.multi

    login = Login("Login")
    login.create_layout()
    login.render()
    login.open()

