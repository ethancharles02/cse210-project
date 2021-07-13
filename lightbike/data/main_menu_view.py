# Main menu will be built here
# https://arcade.academy/examples/view_instructions_and_game_over.html
# It will be an arcade.View
"""
"""

import arcade
from data.button import Button
from data import constants

class MainMenuView(arcade.View):
    """
    """
    def __init__(self, window: arcade.Window):
        """
        """
        super().__init__(window=window)
        self.cur_map = constants.MAP0
        self.num_players = 1
        self.num_ai = 1
        self._cast = {}

    def on_show(self):
        """
        """
        self._cast["buttons"] = []
        self._cast["buttons"].append(Button(text="test", text_color="black", font="arial", selectable=True, selected=False))
        self._cast["buttons"][0].position = (50, 100)
        # set your background image (find that code to do that)
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        """
        # Look at game.py or game_view.py for some of the code to use
        arcade.start_render()
        arcade.draw_text("Menu Screen", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """
        """
        play_button = Button("assets/play_button.png")
        if play_button.coords_in_hitbox(_x, _y):
            play_button.select()
            
        # self.window.show_view(instructions_view)
        # instructions_view = InstructionView()