"""
The entry point to run the lightbike game
"""
import arcade

from data.game import Game
from data import constants


def main():
    """ Main method """
    window = Game(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    window.setup()
    background_sound = arcade.load_sound("assets/Sci-Fi-Dramatic-Theme.mp3")
    arcade.play_sound(background_sound)
    arcade.run()

if __name__ == "__main__":
    main()