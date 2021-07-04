"""
The game module combines all of the modules to create the 
frame of the game, deciding where everything goes. It comes 
from arcade.Window and overrides methods to draw the game, update it, etc.
"""
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
import os
from random import randint
from data import constants
from data.point import Point
from data.control_actors_action import ControlActorsAction
from data.draw_actors_action import DrawActorsAction
from data.handle_collisions_action import HandleCollisionsAction
from data.move_actors_action import MoveActorsAction
from data.output_service import OutputService
from data.player import Player
from data.ai import Ai


class Game(arcade.Window):
    """
    The game is in charge of bringing everything together and putting it into the arcade window

    Stereotype: 
        Service Provider

    Attributes:
        _cast (dictionary): Holds all the objects that will be displayed on the screen
        _output_service (OutputService): In charge of displaying objects
        _draw_actors_action (DrawActorsAction): Draws actors
        _control_actors_action (ControlActorsAction): Controls the player's character based on their inputs
        _move_actors_action (MoveActorsAction): Moves each object based on their velocity
        _handle_collisions_action (HandleCollisionsAction): Handles collisions between objects
        _time_elapsed (float): Value for how much time has passed since the start of the program in seconds
    """

    def __init__(self, width, height, title):
        """
        The class constructor
        """
        super().__init__(width, height, title)

        self._cast = {}
        self._output_service = OutputService()
        self._draw_actors_action = DrawActorsAction(self._output_service)

        self._control_actors_action = ControlActorsAction()

        self._move_actors_action = MoveActorsAction()

        self._handle_collisions_action = HandleCollisionsAction()
        self._time_elapsed = 0

    def setup(self):
        """
        Set up the game and initialize the variables.
        """
        
        self._cast["players"] = []
        self._cast["players"].append(Player())
        self._cast["players"][0].set_sprite(arcade.Sprite("assets/blue_player.png", constants.SPRITE_SCALING))
        self._cast["players"][0].set_position(Point(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT * 0.25))
        self._cast["players"][0].set_velocity(Point(1 * self._cast["players"][0].get_movement_speed(), 0))
        self._cast["players"][0].get_trail().add_point(self._cast["players"][0].get_position())

        # Hitbox adjustment to half of the players sprite
        orig_width = self._cast["players"][0].get_sprite().width * constants.SPRITE_SCALING**-1
        hitbox = self._cast["players"][0].get_sprite().get_hit_box()
        self._cast["players"][0].get_sprite().set_hit_box(tuple(map(lambda x: (x[0] + 5 + orig_width / 2, x[1]) if x[0] < 0 else (x[0], x[1]), hitbox)))

        # player2_keys = {
        #     arcade.key.LEFT: Point(-1, 0),
        #     arcade.key.RIGHT: Point(1, 0),
        #     arcade.key.UP: Point(0, 1),
        #     arcade.key.DOWN: Point(0, -1)
        # }
        # self._cast["players"].append(Player(keys=player2_keys))
        
        self._cast["ai"] = []

        for i in range(1):
            self._cast["ai"].append(Ai())
            self._cast["ai"][i].set_sprite(arcade.Sprite("assets/blue_player.png", constants.SPRITE_SCALING))
            self._cast["ai"][i].set_position(Point(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT * 0.75))
            self._cast["ai"][i].set_velocity(Point(1, 0))
            self._cast["ai"][i].get_trail().add_point(self._cast["ai"][i].get_position())

            # Hitbox adjustment
            orig_width = self._cast["ai"][i].get_sprite().width * constants.SPRITE_SCALING**-1
            hitbox = self._cast["ai"][i].get_sprite().get_hit_box()
            self._cast["ai"][i].get_sprite().set_hit_box(tuple(map(lambda x: (x[0] + 5 + orig_width / 2, x[1]) if x[0] < 0 else (x[0], x[1]), hitbox)))
        
        arcade.set_background_color(constants.BACKGROUND_COLOR)

    def on_draw(self):
        """
        Render the screen.
        """
        
        arcade.start_render()

        self._draw_actors_action.execute(self._cast)
        arcade.draw_text(f"Time: {self._time_elapsed:.2f}", 0, constants.SCREEN_HEIGHT, arcade.color.WHITE, anchor_x="left", anchor_y="top")

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

        for ai in self._cast["ai"]:
            if not ai.is_dead():
                if randint(1, 100) == 1:
                    ai.turn()

        self._time_elapsed += delta_time