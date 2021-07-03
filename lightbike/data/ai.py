# checks in front of it to see if it will collide (using the list of trail points checking between a range maybe of the sprite size)
# also checks if it will collide with boundary
# turns random direction

# if it doesn't detect a collision, have a random tick check that will make it turn

# Ai attributes:
# trail
# dead

# Ai methods:
# check_collision() (have a set range, if collision is too close, don't turn)
# is_dead()
# get_trail()
# set_trail()

import random
from data.actor import Actor
from data.trail import Trail
from data import constants
from data.point import Point

class Ai(Actor):
    def __init__(self, movement_speed = constants.MOVEMENT_SPEED):
        super().__init__()
        self._trail = Trail()
        self._name = ""
        self._movement_speed = movement_speed

    def check_collision(self, trail_sprite_lists):
        aix = self.get_position().get_x()
        aiy = self.get_position().get_y()
        aidx = self.get_velocity().get_x()
        aidy = self.get_velocity().get_y()
        if aix + aidx >= constants.SCREEN_WIDTH and aix + aidx < 0:
            self.turn()
        #elif aix <= 10 and aix > 5:
            #turn
        elif aiy + aidy >= constants.SCREEN_HEIGHT and aiy + aidy < 0:
            self.turn()
        #elif aiy <= 10 and aiy > 5:
            #turn
        self._sprite.center_x += aidx
        self._sprite.center_y += aidy
        for trail_sprite_list in trail_sprite_lists:
            if self._sprite.check_for_collision_with_list(trail_sprite_list):
                self.turn()
                break
        self._sprite.center_x -= aidx
        self._sprite.center_y -= aidy

    def turn(self):
        aidx = self.get_velocity().get_x()
        aidy = self.get_velocity().get_y()
        if aidx == 0:
            self.set_velocity(Point(self._movement_speed * random.choice([-1, 1]), 0))
        if aidy == 0:
            self.set_velocity(0, Point(self._movement_speed * random.choice([-1, 1])))

    def get_trail(self):
        return self._trail 
    
    def set_trail(self, trail):
        self._trail = trail

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

    def dead_sprite(self):
        """
        hide and stop the player temporarily
        """
        self.get_sprite().scale = 0
        self.set_velocity(Point(0, 0))
