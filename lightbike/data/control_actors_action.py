"""
The control actions action contains the class and functions that get the direction of 
the actor and also will close the game if the escape key is pressed
"""
# from arcade import key as arcade_key
from data.action import Action
from data import constants

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    """

    def __init__(self):
        """The class constructor.
        """
        pass

    def execute(self, game, cast, key, main_menu):
        """Executes the action using the given actors.

        Args:
            game (arcade.Window): The game (only used to close if the escape key is pressed)
            cast (dict): The game actors {key: tag, value: list}.
            key (arcade.key): The current key that has been pressed
        """

        for player in cast["players"]:
            direction = self._get_direction(game, player, key, main_menu)
            if not player.is_dead():

                if direction:
                    player_velocity = player.get_velocity()

                    if not ((player_velocity[0] != 0 and direction[0] != 0) or (player_velocity[1] != 0 and direction[1] != 0)):
                        player.set_velocity(direction)
                        player.get_trail().add_point(player.get_position())
        
    def _get_direction(self, game, player, key, main_menu):
        """Gets the selected direction for the given player.

        Returns:
            tuple: The selected direction.
            None: If there was an invalid key inputted
        """

        if key == constants.ESCAPE_KEY:
            # game.window.close()
            constants.SOUND_BACKGROUND.stop(game.background_music)
            game.window.show_view(main_menu)
        
        player_keys = player.get_keys()
        if key in player_keys:
            direction = player_keys[key]
            return direction