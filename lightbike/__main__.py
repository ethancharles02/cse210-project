"""
The entry point to run the lightbike game
"""
import arcade
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

# from data.game import Game
from data import constants
from data.game_view import GameView
# from data.main_menu_view import MainMenuView

def main():
    """ Main method """
    # window = Game(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    # window.setup()
    game_view = GameView(window)
    window.show_view(game_view)
    arcade.run()

if __name__ == "__main__":
    main()