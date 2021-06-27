from arcade import key
from data.point import Point
from data import constants

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _keys (list): Points for up, dn, lt, rt.
    """

    def __init__(self):
        """The class constructor."""
        self._movement_speed = constants.MOVEMENT_SPEED
        self._keys = {}
        self._update_keys()
        
    def get_direction(self, game, key):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """

        direction = Point(0, 0)
        if key == 65307:
            game.close()
        direction = self._keys.get(key, Point(0, 0))
        return direction

    def set_movement_speed(self, speed):
        self._movement_speed = speed
        self._update_keys()

    def get_movement_speed(self):
        return self._movement_speed

    def _update_keys(self):
        self._keys[key.A] = Point(-self._movement_speed, 0) # a
        self._keys[key.D] = Point(self._movement_speed, 0) # d
        self._keys[key.W] = Point(0, self._movement_speed) # w
        self._keys[key.S] = Point(0, -self._movement_speed) # s