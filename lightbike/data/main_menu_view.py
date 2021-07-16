# Main menu will be built here
# https://arcade.academy/examples/view_instructions_and_game_over.html
# It will be an arcade.View
"""
"""

import arcade
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
        self.cur_map = constants.MAP0
        self.view_screen = arcade.load_texture('assets/main_menu.png')
        self.num_players = 1
        self.num_ai = 1
        self._cast = {}
        self.window = window

    def on_show(self):
        """
        """
        self.play_button = Button("assets/play_button.png")
        self._cast["buttons"] = []
        self._cast["buttons"].append(Button(text="test", text_color="black", font="arial", selectable=True, selected=False))
        self._cast["buttons"][0].position = (50, 100)
        
        # set your background image (find that code to do that)
        #arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        """
        # Look at game.py or game_view.py for some of the code to use
        arcade.start_render()
        self.view_screen.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        
        # arcade.draw_text("Menu Screen", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2,
        #                  arcade.color.BLACK, font_size=50, anchor_x="center")
        # arcade.draw_text("Click to advance", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-75,
        #                  arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """
        """
        if self.play_button.coords_in_hitbox(_x, _y):
            self.play_button.select()
            game_view = GameView(self.window)
            self.window.show_view(game_view)

        if self.num_player_button1.coords_in_hitbox(_x, _y):
            self.num_player_button2.unselect()
            self.num_player_button3.unselect()
            self.num_player_button4.unselect()
            self.num_player_button1.select()
            self.num_players = 1
        elif self.num_player_button2.coords_in_hitbox(_x, _y):
            self.num_player_button1.unselect()
            self.num_player_button3.unselect()
            self.num_player_button4.unselect()
            self.num_player_button2.select()
            self.num_players = 2
        elif self.num_player_button3.coords_in_hitbox(_x, _y):
            self.num_player_button1.unselect()
            self.num_player_button2.unselect()
            self.num_player_button4.unselect()
            self.num_player_button3.select()
            self.num_players = 3
        elif self.num_player_button4.coords_in_hitbox(_x, _y):
            self.num_player_button1.unselect()
            self.num_player_button2.unselect()
            self.num_player_button3.unselect()
            self.num_player_button4.select()
            self.num_players = 4

        if self.num_ai_button0.coords_in_hitbox(_x, _y):
            self.num_ai_button1.unselect()
            self.num_ai_button2.unselect()
            self.num_ai_button3.unselect()
            self.num_ai_button4.unselect()
            self.num_ai_button0.select()
            self.num_ai = 0
        elif self.num_ai_button1.coords_in_hitbox(_x, _y):
            self.num_ai_button0.unselect()
            self.num_ai_button2.unselect()
            self.num_ai_button3.unselect()
            self.num_ai_button4.unselect()
            self.num_ai_button1.select()
            self.num_ai = 1
        elif self.num_ai_button2.coords_in_hitbox(_x, _y):
            self.num_ai_button0.unselect()
            self.num_ai_button1.unselect()
            self.num_ai_button3.unselect()
            self.num_ai_button4.unselect()
            self.num_ai_button2.select()
            self.num_ai = 2
        elif self.num_ai_button3.coords_in_hitbox(_x, _y):
            self.num_ai_button0.unselect()
            self.num_ai_button1.unselect()
            self.num_ai_button2.unselect()
            self.num_ai_button4.unselect()
            self.num_ai_button3.select()
            self.num_ai = 3
        elif self.num_ai_button4.coords_in_hitbox(_x, _y):
            self.num_ai_button0.unselect()
            self.num_ai_button1.unselect()
            self.num_ai_button2.unselect()
            self.num_ai_button3.unselect()
            self.num_ai_button4.select()
            self.num_ai = 4 

        if self.map_button0.coords_in_hitbox(_x, _y):
            self.num_ai_button1.unselect()
            self.num_ai_button2.unselect()
            self.num_ai_button3.unselect()
            self.cur_map = constants.MAP0
        elif self.map_button1.coords_in_hitbox(_x, _y):
            self.num_ai_button0.unselect()
            self.num_ai_button2.unselect()
            self.num_ai_button3.unselect()
            self.cur_map = constants.MAP1
        elif self.map_button2.coords_in_hitbox(_x, _y):
            self.num_ai_button0.unselect()
            self.num_ai_button1.unselect()
            self.num_ai_button3.unselect()
            self.cur_map = constants.MAP2
        elif self.map_button3.coords_in_hitbox(_x, _y):
            self.num_ai_button0.unselect()
            self.num_ai_button1.unselect()
            self.num_ai_button2.unselect()
            self.cur_map = constants.MAP3     
            
        # self.window.show_view(instructions_view)
        # instructions_view = InstructionView()