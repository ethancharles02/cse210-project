"""
The trail module holds the information for trails (points and sprites).
It also provides methods for converting points into sprites.
"""
from arcade import SpriteList
from arcade import Sprite
from data import constants

class Trail:
    """
    The Trail class is used to create the trails in the lightbike game
    
    Stereotype:
        Information Holder, Service Provider

    Methods:
        __init__(): Assigns base attributes
        get_point_list(): Returns the point list
        set_point_list(): Sets the point list
        add_point(): Adds a point to the point list but also updates the sprite list based on this new point
        add_point_list(): Adds points from an iterable object using the add_point method for each one
        get_sprite_list(): Returns the sprite list
        set_sprite_list(): Sets the sprite list
        add_sprite(): Adds a sprite to the sprite list
        _points_to_sprites(): Converts two points into the corresponding trail sprite between those points
        update_temp_list(): Updates the sprite list similar to add point but uses a temporary trail 
            that will be reset on the next update of the trail (this is to create the trails that are actively being created by the lightbike)
    """
    def __init__(self):
        """The class constructor
        """
        self._point_list = []
        self._sprite_list = SpriteList(use_spatial_hash=True, is_static=True)
        self._sprite_image = "assets/blue_wall.png"
        self._sprite_width = Sprite(self._sprite_image, constants.SPRITE_SCALING).width
        self._sprite_height = Sprite(self._sprite_image, constants.SPRITE_SCALING).height
        self._temp_list = False

    def get_point_list(self):
        """
        Returns the point list

        Returns:
            list: List of points of type tuple
        """
        return self._point_list

    def set_point_list(self, point_list):
        """
        Sets the point list

        Args:
            point_list (list): List of points of type tuple
        """
        self._point_list = point_list

    def add_point(self, point):
        """
        Adds a point to the point list but also updates the sprite list based on this new point

        Args:
            point (tuple): The Point to add.
        """
        self._point_list.append(point)
        if len(self._point_list) > 1:
            self.add_sprite(self._points_to_sprites([self._point_list[-2], point]))
    
    def add_point_list(self, point_list):
        """
        Adds points from an iterable object using the add_point method for each one

        Args:
            point_list (list): List of points of type tuple
        """
        for point in point_list:
            self.add_point(point)

    def get_sprite_list(self):
        """
        Returns the sprite list

        Returns:
            SpriteList: A list of sprites of type Sprite from the arcade module
        """
        return self._sprite_list

    def set_sprite_list(self, sprite_list):
        """
        Sets the sprite list

        Args:
            sprite_list (SpriteList): A list of sprites of type Sprite from the arcade module
        """
        self._sprite_list = sprite_list

    def add_sprite(self, sprite):
        """
        Adds a sprite to the sprite list

        Args:
            sprite (Sprite): The Sprite to add
        """
        self._sprite_list.append(sprite)

    def _points_to_sprites(self, point_list):
        """
        Converts two points into the corresponding trail sprite between those points

        Args:
            point_list (list): The list of points to convert (restricted to two points)
        """
        if self._temp_list:
            self._sprite_list.pop()
            self._temp_list = False

        point_x = point_list[0][0]
        point_y = point_list[0][1]
        point_x2 = point_list[1][0]
        point_y2 = point_list[1][1]

        is_directionx = True
        if point_x == point_x2:
            is_directionx = False
        if point_y == point_y2:
            is_directionx = True

        sprite_list = Sprite(self._sprite_image, constants.SPRITE_SCALING)

        if is_directionx:
            sprite_list.width = abs(point_x2 - point_x)
            sprite_list.center_x = (point_x2 - point_x) / 2 + point_x
            sprite_list.center_y = point_y

        else:
            sprite_list.angle = 90
            sprite_list.width = abs(point_y2 - point_y)
            sprite_list.center_y = (point_y2 - point_y) / 2 + point_y
            sprite_list.center_x = point_x

        return sprite_list

    def update_temp_list(self, points_list):
        """
        Updates the sprite list similar to add point but uses a temporary trail 
            that will be reset on the next update of the trail (this is to create the trails that are actively being created by the lightbike)

        Args:
            points_list (list): List of points of type tuple
        """
        self.add_sprite(self._points_to_sprites(points_list))
        self._temp_list = True