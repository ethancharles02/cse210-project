# Add w and s key for the points
# Change asciimatics module to arcade

import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for up, dn, lt, rt.
    """

    def __init__(self, screen):
        """The class constructor."""
        self._screen = screen
        self._keys = {}
        self._keys[97] = Point(-1, 0) # a
        self._keys[100] = Point(1, 0) # d
        
    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        # if key == arcade.key.UP:
        #     self.player_sprite.change_y = MOVEMENT_SPEED
        # elif key == arcade.key.DOWN:
        #     self.player_sprite.change_y = -MOVEMENT_SPEED
        # elif key == arcade.key.LEFT:
        #     self.player_sprite.change_x = -MOVEMENT_SPEED
        # elif key == arcade.key.RIGHT:
        #     self.player_sprite.change_x = MOVEMENT_SPEED
        direction = Point(0, 0)
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == 27 or event.key_code == -1:
                sys.exit()
            direction = self._keys.get(event.key_code, Point(0, 0))
        return direction