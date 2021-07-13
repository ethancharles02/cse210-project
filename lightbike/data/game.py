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
# import os
from random import randint
from data import constants
from data.control_actors_action import ControlActorsAction
from data.draw_actors_action import DrawActorsAction
from data.handle_collisions_action import HandleCollisionsAction
from data.move_actors_action import MoveActorsAction
from data.output_service import OutputService
from data.player import Player
from data.ai import Ai
from data.map import Map
from data.button import Button


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
        
        # player2_keys = {
        #     arcade.key.LEFT: (-1, 0),
        #     arcade.key.RIGHT: (1, 0),
        #     arcade.key.UP: (0, 1),
        #     arcade.key.DOWN: (0, -1)
        # }

        self._cast["players"] = []
        for i in range(constants.NUM_PLAYERS):
            # if i == 1:
            #     self._cast["players"].append(Player(keys=player2_keys))
            # else:
            self._cast["players"].append(Player(wall_sprite=constants.PLAYER_WALL_SPRITE))
            self._cast["players"][i].set_sprite(arcade.Sprite(constants.PLAYER_SPRITE, constants.SPRITE_SCALING))
            # self._cast["players"][i].set_name("player")
            # self._cast["players"][0].set_position(Point(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT * 0.25))
            self._cast["players"][i].set_velocity((0, 1 * self._cast["players"][i].get_movement_speed()))

            # Hitbox adjustment to half of the players sprite
            orig_width = self._cast["players"][i].get_sprite().width * constants.SPRITE_SCALING**-1
            hitbox = self._cast["players"][i].get_sprite().get_hit_box()
            # print(hitbox)
            self._cast["players"][i].get_sprite().set_hit_box(tuple(map(lambda x: (x[0] + 2 + orig_width / 2, x[1]) if x[0] < 0 else (x[0], x[1]), hitbox)))

        # self._cast["players"].append(Player(keys=player2_keys))
        
        screen_dx = constants.SCREEN_WIDTH / (len(self._cast["players"]) + 1)
        i = 0
        for player in self._cast["players"]:
            player.set_position((screen_dx * (i + 1), constants.SCREEN_HEIGHT * 0.05))
            player.get_trail().add_point(player.get_position())
            i += 1

        self._cast["ai"] = []

        for i in range(constants.NUM_AI):
            self._cast["ai"].append(Ai(wall_sprite=constants.AI_WALL_SPRITE))
            self._cast["ai"][i].set_sprite(arcade.Sprite(constants.AI_SPRITE, constants.SPRITE_SCALING))
            # self._cast["ai"][i].set_position((constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT * 0.75))
            self._cast["ai"][i].set_velocity((0, -1))
            # self._cast["ai"][i].get_trail().add_point(self._cast["ai"][i].get_position())

            # Hitbox adjustment
            orig_width = self._cast["ai"][i].get_sprite().width * constants.SPRITE_SCALING**-1
            hitbox = self._cast["ai"][i].get_sprite().get_hit_box()
            self._cast["ai"][i].get_sprite().set_hit_box(tuple(map(lambda x: (x[0] + 2 + orig_width / 2, x[1]) if x[0] < 0 else (x[0], x[1]), hitbox)))
        
        screen_dx = constants.SCREEN_WIDTH / (len(self._cast["ai"]) + 1)
        i = 0
        for ai in self._cast["ai"]:
            ai.set_position((screen_dx * (i + 1), constants.SCREEN_HEIGHT * 0.95))
            ai.get_trail().add_point(ai.get_position())
            i += 1

        self._cast["map"] = []
        self._cast["map"].append(Map(constants.MAP3))

        constants.SOUND_BACKGROUND.play(volume=0.2, loop=True)
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

        for ai in self._cast["ai"]:
            if not ai.is_dead():
                ai.update_cooldown(delta_time)
                if randint(1, 100) == 1:
                    ai.turn()
                    
        self._handle_collisions_action.execute(self._cast)

        # self._time_elapsed = delta_time ** -1
        self._time_elapsed += delta_time