"""
The draw actors action module contains the class and function to draw the actors on the screen.
"""
from data.action import Action

class DrawActorsAction(Action):
    """
    DrawActorsAction draws actors onto the screen from a given cast using the execute method

    Stereotype:
        Service Provider

    Attributes:
        _output_service (OutputService): The output_service object
    
    Methods:
    execute(cast): takes a cast dictionary and draws each of the objects inside it
    """
    def __init__(self, output_service):
        """
        Class constructor

        Args:
        self (DrawActorsAction): An instance of DrawActorsAction
        output_service (OutputService): An instance of OutputService
        """
        self._output_service = output_service

    def execute(self, cast):
        """
        The execute method takes a cast dictionary and draws each of the objects inside it

        Args:
        self (DrawActorsAction): An instance of DrawActorsAction
        cast (dict): The dictionary of actors and tags assigned to those actors
        """
        for group in cast:
            self._output_service.draw_actors(cast[group], group)