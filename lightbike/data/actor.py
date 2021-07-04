"""
The actor module contains the Actor class which help display the sprite and help it move
"""

# from data import constants
from data.point import Point
# from arcade import Sprite

class Actor:
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _sprite (Sprite): The sprite that the actor holds
        _velocity (Point): The actor's speed and direction.
    """

    def __init__(self):
        """The class constructor."""
        self._sprite = None
        self._velocity = Point(0, 0)

    def get_sprite(self):
        """Gets the sprites.

        Returns:
            Sprite: The Sprite itself.
        """
        return self._sprite

    def set_sprite(self, sprite) :
        """Updates the sprite.
        """
        self._sprite = sprite

    def get_position(self):
        """Gets the sprites position.
        
        Returns:
            Position: The sprites position.
        """
        return Point(self._sprite.center_x, self._sprite.center_y)

    def set_position(self, position: Point):
        """
        Sets the position of the sprite
        """
        self._sprite.center_x = position.get_x()
        self._sprite.center_y = position.get_y()

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity
