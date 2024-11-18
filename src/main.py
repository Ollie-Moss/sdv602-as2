from des_manager import DESManager
from auth import Login, Register
from settings import Settings
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--multi', action='store_true', help="Enabled multi-window mode for the application")

    args = parser.parse_args()

    winMan = DESManager(args.multi)
    winMan.setup_DESs()
    winMan.start()

