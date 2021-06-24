# get direction from input service, turn player within the cast variable based on the direction
# restrict direction from moving directly back the way the player is moving (ie. velocity (1, 0) can't suddenly become velocity(-1, 0))

from game import constants
from game.action import Action
from game.point import Point

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
        paddle = cast["paddle"][0] # there's only one in the cast
        # Checks if the paddle is at either edge of the screen and if the current direction would put it off the screen, if it does, it will set its velocity to 0
        if (paddle.get_position().get_x() == 1 and direction.get_x() == -1) or (paddle.get_position().get_x() == constants.MAX_X - len(paddle.get_text()) - 1 and direction.get_x() == 1):
            paddle.set_velocity(Point(0, 0))
        else:
            paddle.set_velocity(direction)
            paddle.set_position(paddle.get_position().add(paddle.get_velocity()))