"""
The Map class holds the information for map design, allowing the creator to easily create basic maps.
"""

from data.actor import Actor
from data import constants
from arcade import SpriteList, Sprite

class Map(Actor):
    """
    The Map class holds information for the map of wall sprites

    Stereotype:
        Information Holder

    Methods: 
        __init__(): initializes the parent class, assigns attributes
        set_map(): Sets the map
        get_map(): Gets the map
        set_mapx(): Sets the map width
        get_mapx(): Gets the map width
        set_mapy(): Sets the map height
        get_mapy(): Gets the map height
        _return_sprite_map(): Creates a SpriteList of walls from the _map attribute
    """
    def __init__(self, map : list = constants.MAP1, mapx : int = constants.MAPX, mapy : int = constants.MAPY):
        """
        The class constructor

        Args:
            map (list): The map list which holds specifications for each wall with the format: [(x, y), filepath, angle]
            mapx (int): The grid width of the map
            mapy (int): The grid height of the map
        """
        super().__init__()
        self._map = map
        self._mapx = mapx
        self._mapy = mapy
        self.set_sprite(self._return_sprite_map())
    
    def set_map(self, map):
        """
        Sets the map

        Args:
            map (list): The map list which holds specifications for each wall with the format: [(x, y), filepath, angle]
        """
        self._map = map
        self.set_sprite(self._return_sprite_map())
        
    def get_map(self):
        """
        Gets the map

        Returns:
            list: The map list which holds specifications for each wall with the format: [(x, y), filepath, angle]
        """
        return self._map
    
    def set_mapx(self, mapx):
        """
        Sets the map width

        Args:
            mapx (int): The map width
        """
        self._mapx = mapx
        self.set_sprite(self._return_sprite_map())
        
    def get_mapx(self):
        """
        Gets the map width

        Returns:
            int: Map width
        """
        return self._map

    def set_mapy(self, mapy):
        """
        Sets the map height

        Args:
            mapy (int): The map height
        """
        self._mapy = mapy
        self.set_sprite(self._return_sprite_map())
        
    def get_mapy(self):
        """
        Gets the map height

        Returns:
            list: The map list which holds specifications for each wall with the format: [(x, y), filepath, angle]
        """
        return self._map

    def _return_sprite_map(self):
        """
        Creates a SpriteList of walls from the _map attribute

        Returns:
            SpriteList: List of wall sprites
        """
        sprite_list = SpriteList(use_spatial_hash=True, is_static=True)

        dx = constants.SCREEN_WIDTH / self._mapx
        dy = constants.SCREEN_HEIGHT / self._mapy

        for wall in self._map:
            sprite = Sprite(wall[1]) if len(wall) > 1 else Sprite(constants.DEFAULT_WALL)
            sprite.angle = wall[2] if len(wall) > 2 else 0

            sprite.width = dx
            sprite.height = dy

            sprite.position = ((wall[0][0] * dx) + (dx / 2), (wall[0][1] * dy) + (dy / 2))

            sprite_list.append(sprite)
        
        return sprite_list