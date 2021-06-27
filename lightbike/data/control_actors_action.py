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

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction()
        player1 = cast["players"][0]

        player1_velocity = player1.get_velocity()
        # player1_velocity_x = player1_velocity.get_x()
        # player1_velocity_y = player1_velocity.get_y()
        
        if not (player1_velocity.reverse().equals(direction) or player1_velocity.equals(direction)):
            player1.set_velocity(direction)