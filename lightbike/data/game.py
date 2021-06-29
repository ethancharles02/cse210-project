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
    """
    The game is in charge of bringing everything together and putting it into the arcade window

    Stereotype: 
        Service Provider

    Attributes:
        _cast (dictionary): Holds all the objects that will be displayed on the screen
        _output_service (OutputService): In charge of displaying objects
        _draw_actors_action (DrawActorsAction): Draws actors
        _input_service (InputService): Takes inputs from the player
        _control_actors_action (ControlActorsAction): Controls the player's character based on their inputs
        _move_actors_action (MoveActorsAction): Moves each object based on their velocity
        _handle_collisions_action (HandleCollisionsAction): Handles collisions between objects
    """

    def __init__(self, width, height, title):
        """
        The class constructor
        """
        super().__init__(width, height, title)


        self._cast = {}
        self._output_service = OutputService()
        self._draw_actors_action = DrawActorsAction(self._output_service)

        self._input_service = InputService()
        self._control_actors_action = ControlActorsAction(self._input_service)

        self._move_actors_action = MoveActorsAction()

        self._handle_collisions_action = HandleCollisionsAction()

    def setup(self):
        """
        Set up the game and initialize the variables.
        """
        
        self._cast["players"] = []
        self._cast["players"].append(Player())

        
        self._cast["players"][0].set_sprite(arcade.Sprite("assets/blue_player_resized.png", constants.SPRITE_SCALING))
        self._cast["players"][0].set_position(Point(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2))
        
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """
        
        arcade.start_render()

        self._draw_actors_action.execute(self._cast)

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed
        """

        self._control_actors_action.execute(self, self._cast, key)

    def on_update(self, delta_time):
        """
        Movement and game logic
        """

        self._move_actors_action.execute(self._cast, delta_time)
        self._handle_collisions_action.execute(self, self._cast)