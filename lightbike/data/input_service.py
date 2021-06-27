# Add w and s key for the points
# Change asciimatics module to arcade

import sys
from arcade import keys
from data.point import Point
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _keys (list): Points for up, dn, lt, rt.
    """

    def __init__(self):
        """The class constructor."""
        self._keys = {}
        self._keys[keys.A] = Point(-1, 0) # a
        self._keys[keys.D] = Point(1, 0) # d
        self._keys[keys.W] = Point(0, -1) # w
        self._keys[keys.S] = Point(0, 1) # s
        
    def get_direction(self, key):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        direction = Point(0, 0)
        if key == 65307:
            sys.exit()
        direction = self._keys.get(key, Point(0, 0))
        return direction

    
