"""
The entry point to run the lightbike game
"""
import arcade
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

from data.game import Game
from data import constants


def main():
    """ Main method """
    window = Game(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()