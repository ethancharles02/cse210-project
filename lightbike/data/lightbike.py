from math import sin, cos, radians
from arcade import sprite
from data.actor import Actor
from data.trail import Trail
from data.point import Point
from data import constants

class Lightbike(Actor):
    def __init__(self, movement_speed = constants.MOVEMENT_SPEED):
        super().__init__()
        self._trail = Trail()
        # self._trail = Trail()
        self._name = ""
        # self._name = ""
        self._movement_speed = movement_speed
        # self._movement_speed = movement_speed
        self._dead = False
        
        # self._dead = False

        # self._turn_cooldown = turn_cooldown
        # self._orig_keys = keys.copy()
        # self._keys = keys
        # self._update_keys()

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
        return self._dead

    def dead_sprite(self):
        """
        hide and stop the player temporarily
        """
        self.get_sprite().scale = 0
        self.set_velocity(Point(0, 0))

    def check_collision(self, trail_sprite_list):
        hitbox = self._sprite.get_hit_box()
        # print(self._sprite.width)
        # print((hitbox[0], *hitbox[1:]))

        # self._sprite.set_hit_box()
        # self._sprite.set_hit_box()
        # orig_position = self.get_position()

        # x = self.get_position().get_x()
        # y = self.get_position().get_y()
        # dx = self.get_velocity().get_x()
        # dy = self.get_velocity().get_y()

        # # Moves the hitbox of the bike up to the front half
        # if dx > 0:
        #     self.set_position(Point(x + self._sprite.width / 2, y))
        # elif dx < 0:
        #     self.set_position()
        # elif dy > 0:
        #     self.set_position()
        # else:
        #     self.set_position()

        for key in trail_sprite_list:
            if self._dead:
                break
            for sprite in trail_sprite_list[key]:
                if self._sprite.collides_with_sprite(sprite):
                    self._dead = True
                    self.dead_sprite()
                    break