import math
from arcade import key
from data import constants
from data.action import Action
from data.point import Point

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        pass

    def execute(self, game, cast, key):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        for player in cast["players"]:
            direction = self._get_direction(game, player, key)

            # checks if a direction was returned since it will return None if invalid key
            if direction:
                player_velocity = player.get_velocity()
                # player1_velocity_x = player1_velocity.get_x()
                # player1_velocity_y = player1_velocity.get_y()
                
                direction_angle = direction.get_angle()

                if not ((player_velocity.get_x() != 0 and direction.get_x() != 0) or (player_velocity.get_y() != 0 and direction.get_y() != 0)):
                    player.set_velocity(direction)
                    player.get_sprite().angle = direction_angle
        
    def _get_direction(self, game, player, key):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
            None: If there was an invalid key inputted
        """

        # direction = Point(0, 0)
        if key == 65307:
            game.close()
        
        player_keys = player.get_keys()
        if key in player_keys:
            direction = player_keys[key]
            return direction

    # def set_movement_speed(self, speed):
    #     """
    #     Sets the movement speed to be used for the velocity
    #     """
    #     self._movement_speed = speed
    #     self._update_keys()

    # def get_movement_speed(self):
    #     """
    #     Gets the movement speed

    #     Returns:
    #         Int: The movement speed
    #     """
    #     return self._movement_speed