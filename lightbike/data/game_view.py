"""
The GameView module combines all of the modules to create the 
frame of the game, deciding where everything goes. It comes 
from arcade.View and overrides methods to draw the game, update it, etc.
"""

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


class GameView(arcade.View):
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

    def __init__(self, window: arcade.Window, main_menu, num_players = constants.NUM_PLAYERS, num_ai = constants.NUM_AI, map = constants.DEFAULT_MAP):
        """
        The class constructor
        """
        super().__init__(window=window)

        self._main_menu = main_menu

        self._cast = {}
        self._output_service = OutputService()
        self._draw_actors_action = DrawActorsAction(self._output_service)

        self._control_actors_action = ControlActorsAction()

        self._move_actors_action = MoveActorsAction()

        self._handle_collisions_action = HandleCollisionsAction()
        self._time_elapsed = 0

        self._explosions_list = None #Explosions

        self._num_players = num_players
        self._num_ai = num_ai
        self._map = map

        self.game_over = False

    def on_show(self):
        """
        Set up the game and initialize the variables.
        """

        self._cast["players"] = []
        for i in range(self._num_players):
            self._cast["players"].append(Player(wall_sprite=constants.PLAYER_WALL_SPRITE, keys=constants.DEFAULT_KEYS[i]))
            self._cast["players"][i].set_sprite(arcade.Sprite(constants.PLAYER_SPRITE, constants.SPRITE_SCALING))
            self._cast["players"][i].set_velocity((0, 1 * self._cast["players"][i].get_movement_speed()))

            # Hitbox adjustment to half of the players sprite
            orig_width = self._cast["players"][i].get_sprite().width * constants.SPRITE_SCALING**-1
            hitbox = self._cast["players"][i].get_sprite().get_hit_box()
            self._cast["players"][i].get_sprite().set_hit_box(tuple(map(lambda x: (x[0] + 2 + orig_width / 2, x[1] / 3) if x[0] < 0 else (x[0], x[1] / 3), hitbox)))
        
        screen_dx = constants.SCREEN_WIDTH / (len(self._cast["players"]) + 1)
        i = 0
        for player in self._cast["players"]:
            player.set_position((screen_dx * (i + 1), constants.SCREEN_HEIGHT * 0.05))
            player.get_trail().add_point(player.get_position())
            i += 1

        self._cast["ai"] = []

        for i in range(self._num_ai):
            self._cast["ai"].append(Ai(wall_sprite=constants.AI_WALL_SPRITE))
            self._cast["ai"][i].set_sprite(arcade.Sprite(constants.AI_SPRITE, constants.SPRITE_SCALING))
            self._cast["ai"][i].set_velocity((0, -1))

            # Hitbox adjustment
            orig_width = self._cast["ai"][i].get_sprite().width * constants.SPRITE_SCALING**-1
            hitbox = self._cast["ai"][i].get_sprite().get_hit_box()
            self._cast["ai"][i].get_sprite().set_hit_box(tuple(map(lambda x: (x[0] + 2 + orig_width / 2, x[1] / 3) if x[0] < 0 else (x[0], x[1] / 3), hitbox)))
        
        screen_dx = constants.SCREEN_WIDTH / (len(self._cast["ai"]) + 1)
        i = 0
        for ai in self._cast["ai"]:
            ai.set_position((screen_dx * (i + 1), constants.SCREEN_HEIGHT * 0.95))
            ai.get_trail().add_point(ai.get_position())
            i += 1
        
        self._explosions_list = arcade.SpriteList()

        self._cast["map"] = []
        self._cast["map"].append(Map(self._map))

        self.background_music = constants.SOUND_BACKGROUND.play(volume=0.1, loop=True)

        arcade.set_background_color(constants.BACKGROUND_COLOR)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        self._draw_actors_action.execute(self._cast)
        
        self._explosions_list.draw()
        arcade.draw_text(f"Time: {self._time_elapsed:.2f}", 0, constants.SCREEN_HEIGHT, arcade.color.WHITE, anchor_x="left", anchor_y="top")

        if self.game_over:
            arcade.draw_text("Game Over!", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 25,
                arcade.color.WHITE, font_size=50, anchor_x="center")
            arcade.draw_text(f"Time: {self._time_elapsed:.2f}", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 25,
                arcade.color.GRAY, font_size=25, anchor_x="center")
            arcade.draw_text("Click: Restart", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 50,
                arcade.color.WHITE, font_size=15, anchor_x="center")
            arcade.draw_text("ESC: Return to Menu", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 65,
                arcade.color.WHITE, font_size=15, anchor_x="center")

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed
        """

        self._control_actors_action.execute(self, self._cast, key, self._main_menu)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """
        Called whenever a mouse key is pressed
        """
        if self.game_over:
            self.window.show_view(GameView(self._main_menu.window, self._main_menu, self._main_menu.num_players, self._main_menu.num_ai, self._main_menu.cur_map))

    def on_update(self, delta_time):
        """
        Movement and game logic
        """

        if not self.game_over:
            self._move_actors_action.execute(self._cast, delta_time)

            for ai in self._cast["ai"]:
                if not ai.is_dead():
                    ai.update_cooldown(delta_time)
                    if randint(1, 400) == 1:
                        ai.turn()
            
            self.game_over = True

            for player in self._cast["players"]:
                if not player.is_dead():
                    self.game_over = False
            
            for ai in self._cast["ai"]:
                if not ai.is_dead():
                    self.game_over = False
            
            if self.game_over:
                constants.SOUND_BACKGROUND.stop(self.background_music)

            self._handle_collisions_action.execute(self._cast, self._explosions_list)

            # self._time_elapsed = delta_time ** -1
            self._time_elapsed += delta_time
        self._explosions_list.update()