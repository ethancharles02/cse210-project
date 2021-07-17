"""
"""

import arcade
from random import random
from data.button import Button
from data import constants
from data.game_view import GameView

class MainMenuView(arcade.View):
    """
    """
    def __init__(self, window: arcade.Window):
        """
        """
        super().__init__(window=window)
        self.view_screen = arcade.load_texture(constants.MAIN_MENU)

        self.num_players = constants.NUM_PLAYERS
        self.num_ai = constants.NUM_AI
        self.cur_map = constants.DEFAULT_MAP

        self.window = window

    def on_show(self):
        """
        """
        # Screen width is 800
        # Screen height is 600
        self.play_button = Button(text="PLAY", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=False)
        self.play_button.position = (400, 450)
        
        self.num_players_buttons = arcade.SpriteList(use_spatial_hash=True, is_static=True)
        self.num_players_buttons.append(Button(text="1 PLAYER", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True, selected_color=(12, 255, 255)))
        self.num_players_buttons[0].position = (300, 385)
        self.num_players_buttons.append(Button(text="2 PLAYER", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=False, selected_color=(12, 255, 255)))
        self.num_players_buttons[1].position = (500, 385)
        self.num_players_buttons.append(Button(text="3 PLAYER", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=False, selected_color=(12, 255, 255)))
        self.num_players_buttons[2].position = (300, 310)
        self.num_players_buttons.append(Button(text="4 PLAYER", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=False, selected_color=(12, 255, 255)))
        self.num_players_buttons[3].position = (500, 310)

        self.num_ai_buttons = arcade.SpriteList(use_spatial_hash=True, is_static=True)
        self.num_ai_buttons.append(Button(text="0 AI", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=False, selected_color=(12, 255, 255)))
        self.num_ai_buttons[0].position = (150, 235)
        self.num_ai_buttons.append(Button(text="1 AI", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=False, selected_color=(12, 255, 255)))
        self.num_ai_buttons[1].position = (275, 235)
        self.num_ai_buttons.append(Button(text="2 AI", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=False, selected_color=(12, 255, 255)))
        self.num_ai_buttons[2].position = (400, 235)
        self.num_ai_buttons.append(Button(text="3 AI", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=False, selected_color=(12, 255, 255)))
        self.num_ai_buttons[3].position = (525, 235)
        self.num_ai_buttons.append(Button(text="4 AI", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True, selected_color=(12, 255, 255)))
        self.num_ai_buttons[4].position = (650, 235)

        self.map_buttons = arcade.SpriteList(use_spatial_hash=True, is_static=True)
        self.map_buttons.append(Button(text="Map 1", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True, selected_color=(12, 255, 255)))
        self.map_buttons[0].position = (175, 160)
        self.map_buttons.append(Button(text="Map 2", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=False, selected_color=(12, 255, 255)))
        self.map_buttons[1].position = (325, 160)
        self.map_buttons.append(Button(text="Map 3", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=False, selected_color=(12, 255, 255)))
        self.map_buttons[2].position = (475, 160)
        self.map_buttons.append(Button(text="Map 4", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=False, selected_color=(12, 255, 255)))
        self.map_buttons[3].position = (625, 160)
        
        # self.num_players_buttons.append(Button(text="2 PLAYER", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=10, selectable=True, selected=False, selected_color=(12, 255, 255)))
        
        # self.num_players_buttons.append(Button(text="3 PLAYER", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=10, selectable=True, selected=False, selected_color=(12, 255, 255)))
        
        # self.num_players_buttons.append(Button(text="4 PLAYER", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=10, selectable=True, selected=False, selected_color=(12, 255, 255)))
        # self._cast["buttons"] = []
        # self._cast["buttons"].append(Button(text="test", text_color="black", font="arial", selectable=True, selected=False))
        # self._cast["buttons"][0].position = (50, 100)
        
        # set your background image (find that code to do that)
        #arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        """
        # Look at game.py or game_view.py for some of the code to use
        arcade.start_render()

        self.view_screen.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.play_button.draw()
        self.num_players_buttons.draw()
        self.num_ai_buttons.draw()
        self.map_buttons.draw()
        
        # arcade.draw_text("Menu Screen", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2,
        #                  arcade.color.BLACK, font_size=50, anchor_x="center")
        # arcade.draw_text("Click to advance", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-75,
        #                  arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed
        """
        if key == constants.ESCAPE_KEY:
            self.window.close()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """
        """
        if self.play_button.coords_in_hitbox(_x, _y):
            # self.play_button.select()
            game_view = GameView(self.window, self, self.num_players, self.num_ai, self.cur_map)
            self.window.show_view(game_view)

        if self.num_players_buttons[0].coords_in_hitbox(_x, _y):
            for button in self.num_players_buttons:
                button.unselect()
            self.num_players_buttons[0].select()
            # self.num_players_buttons[0].texture.name = str(random())
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
        # self.window.show_view(instructions_view)
        # instructions_view = InstructionView()