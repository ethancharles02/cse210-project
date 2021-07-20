"""
The entry point to run the lightbike game
"""

import arcade
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

from data import constants
from data.main_menu_view import MainMenuView

def main():
    """ Main method """
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    main_menu_view = MainMenuView(window)
    window.show_view(main_menu_view)
    arcade.run()

if __name__ == "__main__":
    main()