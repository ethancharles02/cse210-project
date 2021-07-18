"""
The main menu view module holds the GUI for the games main menu.
It uses the button module to be able to create bottons for the player to customize the game mode.
"""

import arcade
from random import random
from data.button import Button
from data import constants
from data.game_view import GameView

class MainMenuView(arcade.View):
    """
    The Main Menu View is used to create and display the buttons and background of the main menu in the game.

    Stereotype:
        Service Provider

    Methods:
        __init__(): Assigns attributes
        on_show(): This runs every time that the View is shown. It is used for placing objects on the screen. Overridden from arcade.View
        on_draw(): Draws the objects on the screen. Overridden from arcade.View
        on_key_press(): Whenever a key is pressed, this is run. It checks for the key to exit the game. Overridden from arcade.View
        on_mouse_press(): Runs when a mouse button is pressed, used for clicking buttons. Overridden from arcade.View
    """
    def __init__(self, window: arcade.Window):
        """
        The class constructor
        """
        super().__init__(window=window)
        self.view_screen = arcade.load_texture(constants.MAIN_MENU)

        self.num_players = constants.NUM_PLAYERS
        self.num_ai = constants.NUM_AI
        self.cur_map = constants.DEFAULT_MAP

        self.window = window

    def on_show(self):
        """
        Designs the buttons for the main menu
        """
        # Screen width is 800
        # Screen height is 600
        self.play_button = Button(text="PLAY", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=False)
        self.play_button.position = (400, 450)
        
        self.num_players_buttons = arcade.SpriteList(use_spatial_hash=True, is_static=True)
        self.num_players_buttons.append(Button(text="1 PLAYER", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True if self.num_players == 1 else False, selected_color=(12, 255, 255)))
        self.num_players_buttons[0].position = (300, 385)
        self.num_players_buttons.append(Button(text="2 PLAYER", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True if self.num_players == 2 else False, selected_color=(12, 255, 255)))
        self.num_players_buttons[1].position = (500, 385)
        self.num_players_buttons.append(Button(text="3 PLAYER", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True if self.num_players == 3 else False, selected_color=(12, 255, 255)))
        self.num_players_buttons[2].position = (300, 310)
        self.num_players_buttons.append(Button(text="4 PLAYER", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True if self.num_players == 4 else False, selected_color=(12, 255, 255)))
        self.num_players_buttons[3].position = (500, 310)

        self.num_ai_buttons = arcade.SpriteList(use_spatial_hash=True, is_static=True)
        self.num_ai_buttons.append(Button(text="0 AI", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True if self.num_ai == 0 else False, selected_color=(12, 255, 255)))
        self.num_ai_buttons[0].position = (150, 235)
        self.num_ai_buttons.append(Button(text="1 AI", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True if self.num_ai == 1 else False, selected_color=(12, 255, 255)))
        self.num_ai_buttons[1].position = (275, 235)
        self.num_ai_buttons.append(Button(text="2 AI", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True if self.num_ai == 2 else False, selected_color=(12, 255, 255)))
        self.num_ai_buttons[2].position = (400, 235)
        self.num_ai_buttons.append(Button(text="3 AI", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True if self.num_ai == 3 else False, selected_color=(12, 255, 255)))
        self.num_ai_buttons[3].position = (525, 235)
        self.num_ai_buttons.append(Button(text="4 AI", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True if self.num_ai == 4 else False, selected_color=(12, 255, 255)))
        self.num_ai_buttons[4].position = (650, 235)

        self.map_buttons = arcade.SpriteList(use_spatial_hash=True, is_static=True)
        self.map_buttons.append(Button(text="Map 1", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True if self.cur_map == constants.MAP0 else False, selected_color=(12, 255, 255)))
        self.map_buttons[0].position = (175, 160)
        self.map_buttons.append(Button(text="Map 2", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True if self.cur_map == constants.MAP1 else False, selected_color=(12, 255, 255)))
        self.map_buttons[1].position = (325, 160)
        self.map_buttons.append(Button(text="Map 3", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True if self.cur_map == constants.MAP2 else False, selected_color=(12, 255, 255)))
        self.map_buttons[2].position = (475, 160)
        self.map_buttons.append(Button(text="Map 4", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True if self.cur_map == constants.MAP3 else False, selected_color=(12, 255, 255)))
        self.map_buttons[3].position = (625, 160)

    def on_draw(self):
        """
        Displays the buttons on the main menu
        """
        arcade.start_render()

        self.view_screen.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.play_button.draw()
        self.num_players_buttons.draw()
        self.num_ai_buttons.draw()
        self.map_buttons.draw()

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed

        Args:
            key: Library used in the constant module
        """
        if key == constants.ESCAPE_KEY:
            self.window.close()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """
        Determine the active conditions on the constants of the game when a botton is selected
        
        Args:
            _x: x axis position of the mouse press
            _y: y axis position of the mouse press
            _button: Conditions created from button press
        """
        if self.play_button.coords_in_hitbox(_x, _y):
            game_view = GameView(self.window, self, self.num_players, self.num_ai, self.cur_map)
            self.window.show_view(game_view)

        if self.num_players_buttons[0].coords_in_hitbox(_x, _y):
            for button in self.num_players_buttons:
                button.unselect()
            self.num_players_buttons[0].select()
            self.num_players = 1
        elif self.num_players_buttons[1].coords_in_hitbox(_x, _y):
            for button in self.num_players_buttons:
                button.unselect()
            self.num_players_buttons[1].select()
            self.num_players = 2
        elif self.num_players_buttons[2].coords_in_hitbox(_x, _y):
            for button in self.num_players_buttons:
                button.unselect()
            self.num_players_buttons[2].select()
            self.num_players = 3
        elif self.num_players_buttons[3].coords_in_hitbox(_x, _y):
            for button in self.num_players_buttons:
                button.unselect()
            self.num_players_buttons[3].select()
            self.num_players = 4

        if self.num_ai_buttons[0].coords_in_hitbox(_x, _y):
            for button in self.num_ai_buttons:
                button.unselect()
            self.num_ai_buttons[0].select()
            self.num_ai = 0
        elif self.num_ai_buttons[1].coords_in_hitbox(_x, _y):
            for button in self.num_ai_buttons:
                button.unselect()
            self.num_ai_buttons[1].select()
            self.num_ai = 1
        elif self.num_ai_buttons[2].coords_in_hitbox(_x, _y):
            for button in self.num_ai_buttons:
                button.unselect()
            self.num_ai_buttons[2].select()
            self.num_ai = 2
        elif self.num_ai_buttons[3].coords_in_hitbox(_x, _y):
            for button in self.num_ai_buttons:
                button.unselect()
            self.num_ai_buttons[3].select()
            self.num_ai = 3
        elif self.num_ai_buttons[4].coords_in_hitbox(_x, _y):
            for button in self.num_ai_buttons:
                button.unselect()
            self.num_ai_buttons[4].select()
            self.num_ai = 4
        
        if self.map_buttons[0].coords_in_hitbox(_x, _y):
            for button in self.map_buttons:
                button.unselect()
            self.map_buttons[0].select()
            self.cur_map = constants.MAP0
        elif self.map_buttons[1].coords_in_hitbox(_x, _y):
            for button in self.map_buttons:
                button.unselect()
            self.map_buttons[1].select()
            self.cur_map = constants.MAP1
        elif self.map_buttons[2].coords_in_hitbox(_x, _y):
            for button in self.map_buttons:
                button.unselect()
            self.map_buttons[2].select()
            self.cur_map = constants.MAP2
        elif self.map_buttons[3].coords_in_hitbox(_x, _y):
            for button in self.map_buttons:
                button.unselect()
            self.map_buttons[3].select()
            self.cur_map = constants.MAP3