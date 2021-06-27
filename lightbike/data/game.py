# from time import *
# import math

# def updateTime():
#     global old_time
#     old_time = time()

# def displayTime():
#     global old_time
#     print(time() - old_time)

# updateTime()
# displayTime()

import arcade
from data import constants
from data.point import Point
from data.control_actors_action import ControlActorsAction
from data.draw_actors_action import DrawActorsAction
from data.handle_collisions_action import HandleCollisionsAction
from data.move_actors_action import MoveActorsAction
from data.input_service import InputService
from data.output_service import OutputService
from data.player import Player


class Game(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)


        self.cast = {}
        self.output_service = OutputService()
        self.draw_actors_action = DrawActorsAction(self.output_service)

        self.input_service = InputService()
        self.control_actors_action = ControlActorsAction(self.input_service)

        self.move_actors_action = MoveActorsAction()

        self.handle_collisions_action = HandleCollisionsAction()

    def setup(self):
        """ Set up the game and initialize the variables. """
        
        self.cast["players"] = []
        self.cast["players"].append(Player())

        
        self.cast["players"][0].set_sprite(arcade.Sprite("assets/blue_player_resized.png", constants.SPRITE_SCALING))
        self.cast["players"][0].set_position(Point(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2))
        
        arcade.set_background_color(arcade.color.BLACK)
        
        

    def on_draw(self):
        """
        Render the screen.
        """
        
        arcade.start_render()

        self.draw_actors_action.execute(self.cast)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        self.control_actors_action.execute(self, self.cast, key)

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.move_actors_action.execute(self.cast, delta_time)
        self.handle_collisions_action.execute(self, self.cast)