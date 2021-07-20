"""
The AI module contains the class and functions used to simulate a player with artificial intelligence
so that a player only chosing to play by themselves has an opponent
"""

import random
from data.lightbike import Lightbike
from data import constants
from math import atan2, degrees

class Ai(Lightbike):
    """
    The Ai class is used to create the ai in the lightbike game
    
    Stereotype:
        Information Holder, Service Provider

    Methods:
        __init__(): initializes the parent class, assigns attributes
        check_ai_collisions(): Checks ahead of time between the ai and possible collisions, turning if they are found
        turn(): Turns the ai in a random direction, left or right
        set_velocity(): Sets the velocity of the ai, updating the angle of the sprite as well
    """
    def __init__(self, movement_speed = constants.MOVEMENT_SPEED, turn_cooldown = constants.AI_TURN_COOLDOWN, wall_sprite=constants.PLAYER_WALL_SPRITE):
        """
        initializes the parent class, assigns attributes

        Args:
            movement_speed (float): How fast the ai moves in pixels/second 
            turn_cooldown (float): The amount of time it takes before the ai can turn after turning (not implemented yet)
        """
        super().__init__(movement_speed, wall_sprite)
        self.turn_cooldown = turn_cooldown
        self.cur_turn_cooldown = 0

    def check_ai_collisions(self, trail_sprite_list):
        """
        Checks ahead of time between the ai and possible collisions, turning if they are found

        Args:
            trail_sprite_list (dict): Dictionary of sprites to check for collisions against
        """
        aix = self.get_position()[0]
        aiy = self.get_position()[1]

        aidx = self.get_velocity()[0] * 0.3
        aidy = self.get_velocity()[1] * 0.3


        if aix + aidx >= constants.SCREEN_WIDTH or aix + aidx < 0:
            self.turn()
        elif aiy + aidy >= constants.SCREEN_HEIGHT or aiy + aidy < 0:
            self.turn()
        
        self._sprite.center_x += aidx
        self._sprite.center_y += aidy

        on_collision_course = False
        if self.check_collision(trail_sprite_list):
            on_collision_course = True
        
        self._sprite.center_x -= aidx
        self._sprite.center_y -= aidy

        if on_collision_course:
            self.turn()

    def turn(self):
        """
        Turns the ai in a random direction, left or right
        """
        if self.cur_turn_cooldown <= 0:
            self.get_trail().add_point(self.get_position())
            
            aidx = self.get_velocity()[0]
            aidy = self.get_velocity()[1]

            if aidx == 0:
                self.set_velocity((random.choice([-1, 1]), 0))
            elif aidy == 0:
                self.set_velocity((0, random.choice([-1, 1])))

            self.cur_turn_cooldown = self.turn_cooldown
    
    def set_velocity(self, velocity):
        """
        Overridden from Actor parent class
        Sets the velocity of the ai, updating the angle of the sprite as well

        Args:
            velocity (tuple): The velocity of type tuple, ie. (1, 0)
        """
        self._sprite.angle = degrees(atan2(velocity[1], velocity[0])) % 360
        self._velocity = (velocity[0] * self._movement_speed, velocity[1] * self._movement_speed)
    
    def update_cooldown(self, delta_time):
        """
        Updates the ai turn cooldown. This will countdown until it becomes 0 or less than zero which will then allow the ai to turn
        """
        self.cur_turn_cooldown -= delta_time