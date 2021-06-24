# Remove text and tag and methods related to them
# Add sprite property, getter and setter for sprite
# sprite setter should take a string and open
# self.player = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING)

from game import constants
from game.point import Point

class Actor:
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _tag (string): The actor's tag.
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
    """

    def __init__(self):
        """The class constructor."""
        self._tag = ""
        self._text = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the actor's textual representation.
        
        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity

    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            position (Point): The given position.
        """
        # self.cast["players"][0].sprite.center_x = constants.SCREEN_WIDTH / 2
        # self.cast["players"][0].sprite.center_y = constants.SCREEN_HEIGHT / 2
        self._position = position
    
    def set_text(self, text):
        """Updates the actor's text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            position (Point): The given velocity.
        """
        self._velocity = velocity
    
    def set_tag(self, tag):
        """
        Updates the actor's tag to the given one

        Args:
            tag (str): The given tag
        """
        self._tag = tag

    def get_tag(self):
        """
        Gets the actor's tag

        Returns:
            tag (str): Actor's tag
        """
        return self._tag