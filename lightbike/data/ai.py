"""
"""
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
# from data.actor import Actor
from data.lightbike import Lightbike
# from data.trail import Trail
from data import constants
from data.point import Point

class Ai(Lightbike):
    """
    """
    def __init__(self, movement_speed = constants.MOVEMENT_SPEED, turn_cooldown = constants.AI_TURN_COOLDOWN):
        super().__init__(movement_speed)
        # self._trail = Trail()
        # self._name = ""
        # self._movement_speed = movement_speed
        self._turn_cooldown = turn_cooldown
        # self._dead = False

    def check_ai_collisions(self, trail_sprite_list):
        aix = self.get_position().get_x()
        aiy = self.get_position().get_y()

        aidx = self.get_velocity().get_x() * 0.3
        aidy = self.get_velocity().get_y() * 0.3


        if aix + aidx >= constants.SCREEN_WIDTH or aix + aidx < 0:
            self.turn()
        elif aiy + aidy >= constants.SCREEN_HEIGHT or aiy + aidy < 0:
            self.turn()

        # collision = False
        # for sprite in trail_sprite_list:
        #     if self._sprite.collides_with_sprite(sprite):
        #         collision = True
        #         self._dead = True
        #         self.dead_sprite()
        #         break
        
        self._sprite.center_x += aidx
        self._sprite.center_y += aidy

        on_collision_course = False
        for key in trail_sprite_list:
            if on_collision_course:
                break
            for sprite in trail_sprite_list[key]:
            # print(self._sprite.collides_with_list(trail_sprite_list))
                if self._sprite.collides_with_sprite(sprite):
                    on_collision_course = True
                    # self._sprite.center_x -= aidx
                    # self._sprite.center_y -= aidy
                    # self.turn()
                    break
        
        self._sprite.center_x -= aidx
        self._sprite.center_y -= aidy

        if on_collision_course:
            self.turn()

    def turn(self):
        self.get_trail().add_point(self.get_position())
        
        aidx = self.get_velocity().get_x()
        aidy = self.get_velocity().get_y()
        # print(aidx, aidy)
        if aidx == 0:
            self.set_velocity(Point(random.choice([-1, 1]), 0))
        if aidy == 0:
            self.set_velocity(Point(0, random.choice([-1, 1])))
        

    # def get_trail(self):
    #     return self._trail 
    
    # def set_trail(self, trail):
    #     self._trail = trail

    # def get_name(self):
    #     """
    #     Returns the player's name
    #     """
    #     return self._name
    
    # def set_name(self, name):
    #     """
    #     Sets the players name as a string

    #     Parameters:
    #     name(str): The name to be set to the private attribute
    #     """
    #     self._name = str(name)
    
    # def get_movement_speed(self):
    #     """
    #     Gets the movement speed

    #     Returns:
    #         Int: The movement speed
    #     """
    #     return self._movement_speed

    # def set_movement_speed(self, movement_speed):
    #     """
    #     Sets the movement speed to be used for the velocity
    #     """
    #     self._movement_speed = movement_speed
        # self.set_velocity(self)
        # self._update_keys()

    # def dead_sprite(self):
    #     """
    #     hide and stop the player temporarily
    #     """
    #     self.get_sprite().scale = 0
    #     self.set_velocity(Point(0, 0))
    
    def set_velocity(self, velocity):
        self._sprite.angle = velocity.get_angle()
        self._velocity = velocity.multiply(self._movement_speed)
    
    # def update_trail(self):
    #     if self.get_trail().get_point_list():
    #         self.get_trail().update_temp_list([self.get_trail().get_point_list()[-1], self.get_position()])
    
    # def is_dead(self):
    #     return self._dead