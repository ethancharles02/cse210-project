"""
The lightbike module is a parent module to player and ai. It
holds the methods that are the same between them, most important of which,
is the trail. 

It is also in charge of checking collisions between the bike and other objects
"""
from math import sin, cos, radians
from arcade import sprite
from data.actor import Actor
from data.trail import Trail
from data.point import Point
from data import constants

class Lightbike(Actor):
    """
    The Lightbike class is used as a parent class for player and ai
    
    Stereotype:
        Information Holder, Service Provider

    Methods:
        __init__(): Assigns base attributes
        get_trail(): Returns the trail class of type Trail
        set_trail(): Sets the trail class
        update_trail(): Updates the trail, this is used for the actively changing trail right behind the lightbike
        get_name(): Returns the name of the player/ai
        set_name(): Sets the name
        get_movement_speed(): Returns the movement speed of the bike
        set_movement_speed(): Sets the movement speed
        is_dead(): Returns a bool value for if the lightbike is dead
        dead_sprite(): Sets the lightbike to dead, stopping its velocity and returning true on the is_dead method
        check_collision(): Checks for collisions between the lightbike and a list of sprites
    """
    def __init__(self, movement_speed = constants.MOVEMENT_SPEED):
        """
        The class constructor
        """
        super().__init__()
        self._trail = Trail()
        self._name = ""
        self._movement_speed = movement_speed
        self._dead = False

    def get_trail(self):
        """
        gets the Trail
        """
        return self._trail 
        
    def set_trail(self, trail):
        """
        Sets the variable to trail
        """
        self._trail = trail
    
    def update_trail(self):
        """
        Updates the trail, this is used for the actively changing trail right behind the lightbike
        """
        if self.get_trail().get_point_list():
            self.get_trail().update_temp_list([self.get_trail().get_point_list()[-1], self.get_position()])

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
        if self._movement_speed != 0:
            speed_change = movement_speed / self._movement_speed
            self.set_velocity(self.get_velocity().multiply(speed_change))
        else:
            angle = radians(self._sprite.angle)
            self.set_velocity(Point(cos(angle), sin(angle)).multiply(movement_speed))

        self._movement_speed = movement_speed
    
    def is_dead(self):
        """
        Returns a bool value for if the lightbike is dead

        Returns:
            bool: Value for if the lightbike is dead or not
        """
        return self._dead

    def kill(self):
        """
        hide and stop the player temporarily
        """
        self._dead = True
        self.get_sprite().scale = 0
        self.set_velocity(Point(0, 0))

    def check_collision(self, trail_sprite_list):
        """
        Checks for collisions between the lightbike and a list of sprites

        Args:
            trail_sprite_list (dict): Dictionary of sprites to check for collisions with
        """
        for key in trail_sprite_list:
            # if self._dead:
            #     break
            if self._sprite.collides_with_list(trail_sprite_list[key]):
                # self._dead = True
                # self.dead_sprite()
                return True
            # for sprite in trail_sprite_list[key]:
            #     if self._sprite.collides_with_sprite(sprite):
            #         self._dead = True
            #         self.dead_sprite()
            #         break