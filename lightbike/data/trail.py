"""
The trail module holds the information for trails (points and sprites).
It also provides methods for converting points into sprites.
"""
# from arcade import SpriteList, sprite_list
from arcade import Sprite
# from data.point import Point
from data import constants

class Trail:
    def __init__(self):
        self._point_list = []
        self._sprite_list = []
        self._sprite_image = "assets/blue_wall.png"
        self._sprite_width = Sprite(self._sprite_image, constants.SPRITE_SCALING).width
        self._sprite_height = Sprite(self._sprite_image, constants.SPRITE_SCALING).height
        self._temp_list = False

    def get_point_list(self):
        return self._point_list

    def set_point_list(self, point_list):
        self._point_list = point_list

    def add_point(self, point):
        self._point_list.append(point)
        if len(self._point_list) > 1:
            self.add_sprite(self._points_to_sprites([self._point_list[-2], point]))
    
    def add_point_list(self, point_list):
        for point in point_list:
            self.add_point(point)

    def get_sprite_list(self):
        return self._sprite_list

    def set_sprite_list(self, sprite_list):
        self._sprite_list = sprite_list

    def add_sprite(self, sprite):
        self._sprite_list.append(sprite)

    def _points_to_sprites(self, point_list):
        if self._temp_list:
            del self._sprite_list[-1]
            self._temp_list = False

        point_x = point_list[0].get_x()
        point_y = point_list[0].get_y()
        point_x2 = point_list[1].get_x()
        point_y2 = point_list[1].get_y()

        is_directionx = True
        if point_x == point_x2:
            is_directionx = False
        if point_y == point_y2:
            is_directionx = True

        sprite_list = Sprite(self._sprite_image, constants.SPRITE_SCALING)

        if is_directionx:
            sprite_list.width = (point_x2 - point_x)
            sprite_list.center_x = (point_x2 - point_x) / 2 + point_x
            sprite_list.center_y = point_list[0].get_y()

        else:
            sprite_list.angle = 90
            sprite_list.width = (point_y2 - point_y)
            sprite_list.center_y = (point_y2 - point_y) / 2 + point_y
            sprite_list.center_x = point_list[0].get_x()

        return sprite_list

    def update_temp_list(self, points_list):
        self.add_sprite(self._points_to_sprites(points_list))
        self._temp_list = True