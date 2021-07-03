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

from arcade import SpriteList
from data.point import Point

class Trail:
    def __init__(self):
        self.point_list = []
        self.sprite_list = SpriteList

    def get_point_list(self):
        return self.point_list

    def set_point_list(self, point_list):
        self.point_list = point_list

    def add_point(self, point):
        self.point_list.append(point)
    
    def add_point_list(self, point_list):
        for point in point_list:
            self.add_point(point)


    def get_sprite_list(self):
        return self.sprite_list

    def set_sprite_list(self, sprite_list):
        self.sprite_list = sprite_list

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_sprite_list(self, sprite_list):
        for sprite in sprite_list:
            self.add_sprite(sprite)

    def points_to_sprites(self, point_list):
        pass