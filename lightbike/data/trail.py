# trail class will hold a trail list
# the list will hold Point classes
# Start of game, [Point(0, 0)]
# Player turns a direction at (0, 10), [Point(0, 0), Point(0, 10)]
# Draw trail class would take the trail and draw walls between each point

# Trail attributes:
# point_list
# sprite_list

# Trail methods:
# get_point_list
# set_point_list
# add_new_point

# example: arcade.SpriteList(use_spatial_hash=True, is_static=True)
# arcade.SpriteList().append(arcade.Sprite())

# get_sprite_list
# set_sprite_list
# add_sprite_list (list of sprites not of type SpriteList, most likely from the points_to_sprites method)

# points_to_sprites

from arcade import SpriteList, sprite_list
from arcade import Sprite
from data.point import Point
from data import constants

class Trail:
    def __init__(self):
        self._point_list = []
        self._sprite_list = []
        self._sprite_image = "assets/blue_wall.png"
        self._sprite_width = Sprite(self._sprite_image, constants.SPRITE_SCALING).width
        self._sprite_height = Sprite(self._sprite_image, constants.SPRITE_SCALING).height

    def get_point_list(self):
        return self._point_list

    def set_point_list(self, point_list):
        self._point_list = point_list

    def add_point(self, point):
        self._point_list.append(point)
        if len(self._point_list) > 1:
            self.add_sprite_list(self._points_to_sprites([self._point_list[-2], point]))
    
    def add_point_list(self, point_list):
        for point in point_list:
            self.add_point(point)

    def get_sprite_list(self):
        return self._sprite_list

    def set_sprite_list(self, sprite_list):
        self._sprite_list = sprite_list

    # def add_sprite(self, sprite):
    #     self.sprite_list.append(sprite)

    def add_sprite_list(self, sprite_list):
        self._sprite_list.append(sprite_list)
        # for sprite in sprite_list:
        #     self.add_sprite(sprite)

    def _points_to_sprites(self, point_list):
        # point_list = [Point(0, 300), Point(400, 300)]
        if self._sprite_list:
            if type(self._sprite_list[-1]) == list:
                del self._sprite_list[-1]
                
        point_x = point_list[0].get_x()
        point_y = point_list[0].get_y()
        point_x2 = point_list[1].get_x()
        point_y2 = point_list[1].get_y()

        if point_x == point_x2:
            directionx = False
        if point_y == point_y2:
            directionx = True

        sprite_list = SpriteList()

        if directionx:

            direction = 1
            if point_x2 - point_x > 0:
                direction = 1
            else:
                direction = -1

            num_walls = abs(int(((point_x2 - point_x) * direction) // self._sprite_width))

            for i in range(num_walls):
                sprite_list.append(Sprite(self._sprite_image, constants.SPRITE_SCALING))
                sprite_list[i].center_x = ((i * self._sprite_width) + (self._sprite_width / 2)) * direction + point_list[0].get_x()
                sprite_list[i].center_y = point_list[0].get_y()
            
            if (point_x2 - point_x) % self._sprite_width != 0:
                sprite_list.append(Sprite(self._sprite_image, constants.SPRITE_SCALING))
                sprite_list[-1].width = ((point_x2 - point_x) * direction) % self._sprite_width
                sprite_list[-1].center_x = ((self._sprite_width * num_walls) + (sprite_list[-1].width / 2)) * direction + point_list[0].get_x()
                sprite_list[-1].center_y = point_list[0].get_y()
        else:

            direction = 1
            if point_y2 - point_y > 0:
                direction = 1
            else:
                direction = -1

            num_walls = abs(int(((point_y2 - point_y) * direction) // self._sprite_width))

            for i in range(num_walls):
                sprite_list.append(Sprite(self._sprite_image, constants.SPRITE_SCALING))
                sprite_list[i].angle = 90
                sprite_list[i].center_y = ((i * self._sprite_width) + (self._sprite_width / 2)) * direction + point_list[0].get_y()
                sprite_list[i].center_x = point_list[0].get_x()
            
            if (point_y2 - point_y) % self._sprite_width != 0:
                sprite_list.append(Sprite(self._sprite_image, constants.SPRITE_SCALING))
                sprite_list[-1].angle = 90
                sprite_list[-1].width = ((point_y2 - point_y) * direction) % self._sprite_width
                sprite_list[-1].center_y = ((self._sprite_width * num_walls) + (sprite_list[-1].width / 2)) * direction + point_list[0].get_y()
                sprite_list[-1].center_x = point_list[0].get_x()

        return sprite_list

    def update(self, points_list):
        self.add_sprite_list([self._points_to_sprites(points_list)])
        # else:
        #     for i in range(point_y2 - point_y % sprite.width):