# Week 2: add trail class
# Methods to add:
#   set_trail()
#   get_trail()

from data.actor import Actor
from data.trail import Trail

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
    
    def __init__(self):
        """
        Class constructor, initializes private attributes for name and guess
        """
        super().__init__()
        self.__name = ""
        self._trail = Trail()
    
    def get_name(self):
        """
        Returns the player's name
        """
        return self.__name
    
    def set_name(self, name):
        """
        Sets the players name as a string

        Parameters:
        name(str): The name to be set to the private attribute
        """
        self.__name = str(name)