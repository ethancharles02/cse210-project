# Week 2: add trail class

# Player attributes
# _trail
# dead
# movement_speed

# Player methods:
# is_dead()
# set_trail()
# get_trail()
# get_movement_speed()
# set_movement_speed()

from typing import KeysView
from arcade import key
from data.actor import Actor
from data.trail import Trail
from data import constants

class Player(Actor):
    """
    The Player class is used to create the players in the lightbike game
    
    Stereotype:
        Information Holder

    Methods:
        __init__(): generates the name and initializes the parent class
        get_name(): returns the name
        set_name(name): sets the name
    """
    
    def __init__(
        self, 
        movement_speed = constants.MOVEMENT_SPEED,
        keys = constants.DEFAULT_KEYS, 
        ):
        """
        Class constructor, initializes private attributes for name and guess
        """
        super().__init__()
        self._name = ""
        self._trail = Trail()
        self._movement_speed = movement_speed
        self._orig_keys = keys.copy()
        self._keys = keys
        self._update_keys()
    
    def get_name(self):
        """
        Returns the player's name
        """
        return self._name
    
    def set_name(self, name):
        """
        Sets the players name as a string

        Parameters:
        name(str): The name to be set to the private attribute
        """
        self._name = str(name)
    
    def get_movement_speed(self):
        """
        Gets the movement speed

        Returns:
            Int: The movement speed
        """
        return self._movement_speed

    def set_movement_speed(self, movement_speed):
        """
        Sets the movement speed to be used for the velocity
        """
        self._movement_speed = movement_speed
        self._update_keys()

    def get_keys(self):
        """
        Gets the keys dictionary, it follows the format {arcade.key: Point()}

        Returns:
            Dict: The keys dictionary
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
            self._keys[key] = self._orig_keys[key].multiply(self._movement_speed)