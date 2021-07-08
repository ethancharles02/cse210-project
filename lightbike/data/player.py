"""
The player modules contains the Player class that creates the players in the game and functions 
that help set the movement speed and sets the key dicitonary
"""
# from arcade import key
# from data.actor import Actor
from data.lightbike import Lightbike
# from data.trail import Trail
from data import constants

class Player(Lightbike):
    """
    The Player class is used to create the players in the lightbike game
    
    Stereotype:
        Information Holder, Service Provider

    Methods:
        __init__(): initializes the parent class, assigns attributes
        set_movement_speed(): Overriden method from the Lightbike class, it runs the _update_keys method in addition
        get_keys(): Returns the keys dictionary
        set_keys(): Sets the keys dictionary
        _update_keys(): Updates the keys dictionary with new velocities based on the movement speed
    """
    
    def __init__(
        self, 
        movement_speed = constants.MOVEMENT_SPEED,
        keys = constants.DEFAULT_KEYS, 
        ):
        """
        Class constructor, initializes private attributes
        """
        super().__init__(movement_speed)
        self._orig_keys = keys
        self._keys = keys.copy()
        self._update_keys()

    def set_movement_speed(self, movement_speed):
        """
        Sets the movement speed to be used for the velocity
        Updates the keys
        """
        super().set_movement_speed(movement_speed)
        self._update_keys()

    def get_keys(self):
        """
        Gets the keys dictionary, it follows the format {arcade.key: Point()}

        Returns:
            dict: The keys dictionary
        """
        return self._keys

    def set_keys(self, keys):
        """
        Sets the keys dictionary, it follows the format {arcade.key: Point()}
        """
        self._keys = keys
        self._orig_keys = keys.copy()
        self._update_keys()

    def _update_keys(self):
        """
        Updates the corresponding velocities within each key point for the movement speed
        """
        for key in self._keys:
            self._keys[key] = (self._orig_keys[key][0] * self._movement_speed, self._orig_keys[key][1] * self._movement_speed)