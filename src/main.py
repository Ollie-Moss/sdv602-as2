from des_manager import DESManager
from auth import Login, Register
from settings import Settings
from user_manager import UserManager
import argparse


if __name__ == '__main__':
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

