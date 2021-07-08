"""
The AI module contains the class and functions used to simulate a player with artificial intelligence
so that a player only chosing to play by themselves has an opponent
"""

import random
# from data.actor import Actor
from data.lightbike import Lightbike
# from data.trail import Trail
from data import constants
from data.point import Point

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
    def __init__(self, movement_speed = constants.MOVEMENT_SPEED, turn_cooldown = constants.AI_TURN_COOLDOWN):
        """
        initializes the parent class, assigns attributes

        Args:
            movement_speed (float): How fast the ai moves in pixels/second 
            turn_cooldown (float): The amount of time it takes before the ai can turn after turning (not implemented yet)
        """
        super().__init__(movement_speed)
        self._turn_cooldown = turn_cooldown

    def check_ai_collisions(self, trail_sprite_list):
        """
        Checks ahead of time between the ai and possible collisions, turning if they are found

        Args:
            trail_sprite_list (dict): Dictionary of sprites to check for collisions against
        """
        aix = self.get_position().get_x()
        aiy = self.get_position().get_y()

        aidx = self.get_velocity().get_x() * 0.3
        aidy = self.get_velocity().get_y() * 0.3


        if aix + aidx >= constants.SCREEN_WIDTH or aix + aidx < 0:
            self.turn()
        elif aiy + aidy >= constants.SCREEN_HEIGHT or aiy + aidy < 0:
            self.turn()
        
        self._sprite.center_x += aidx
        self._sprite.center_y += aidy

        on_collision_course = False
        if self.check_collision(trail_sprite_list):
            on_collision_course = True
        # for key in trail_sprite_list:
        #     if on_collision_course:
        #         break
        #     for sprite in trail_sprite_list[key]:
        #         if self._sprite.collides_with_sprite(sprite):
        #             on_collision_course = True
        #             break
        
        self._sprite.center_x -= aidx
        self._sprite.center_y -= aidy

        if on_collision_course:
            self.turn()

    def turn(self):
        """
        Turns the ai in a random direction, left or right
        """
        self.get_trail().add_point(self.get_position())
        
        aidx = self.get_velocity().get_x()
        aidy = self.get_velocity().get_y()

        if aidx == 0:
            self.set_velocity(Point(random.choice([-1, 1]), 0))
        if aidy == 0:
            self.set_velocity(Point(0, random.choice([-1, 1])))
    
    def set_velocity(self, velocity):
        """
        Overridden from Actor parent class
        Sets the velocity of the ai, updating the angle of the sprite as well

        Args:
            velocity (Point): The velocity of type Point
        """
        self._sprite.angle = velocity.get_angle()
        self._velocity = velocity.multiply(self._movement_speed)