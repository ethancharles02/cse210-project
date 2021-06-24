# Remove guess and methods related to it
# Week 2: trail class

from data.actor import Actor

class Player(Actor):
    """
    The Player class generates a code
    
    Stereotype:
        Information Holder

    Methods:
        __init__(): generates the name and guess variables
        get_name(): returns the name
        set_name(name): sets the name

        get_guess(): returns the guess
        set_guess(guess): sets the guess
    """
    
    def __init__(self):
        """
        Class constructor, initializes private attributes for name and guess
        """
        super().__init__()
        self.__name = ""
    
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