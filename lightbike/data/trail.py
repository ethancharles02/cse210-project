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

class Trail:
    def __init__(self):
        pass
    def get_point_list(self):
        pass
    def set_point_list(self):
        pass
    def add_new_point(self):
        pass

    def get_sprite_list(self):
        pass
    def set_sprite_list(self):
        pass
    def add_sprite_list(self):
        pass

    def points_to_sprites(self, point_list):
        pass