"""
The map class will be used to hold map designs for the game
"""
# Add a function that takes grid coordinates to add walls to the map, we may need to specify the size of the grid as well (ie. 20 x 15)
from data.actor import Actor
from data import constants
from arcade import SpriteList, Sprite

class Map(Actor):
    def __init__(self, map = constants.MAP1):
        super().__init__()
        self._map = map
        self.set_sprite(self._return_sprite_map())
    
    def set_map(self, map):
        self._map = map
        self.set_sprite(self._return_sprite_map())
        
    def get_map(self):
        return self._map

    def _return_sprite_map(self):
        """
        Creates a SpriteList of walls from the _map attribute

        Returns:
            SpriteList: List of wall sprites
        """
        sprite_list = SpriteList(use_spatial_hash=True, is_static=True)
        
        mapx = constants.MAPX
        mapy = constants.MAPY

        dx = constants.SCREEN_WIDTH / mapx
        dy = constants.SCREEN_HEIGHT / mapy

        for wall in self._map:
            sprite = Sprite(wall[1]) if len(wall) > 1 else Sprite(constants.DEFAULT_WALL)
            sprite.angle = wall[2] if len(wall) > 2 else 0

            sprite.width = dx
            sprite.height = dy

            sprite.position = ((wall[0][0] * dx) + (dx / 2), (wall[0][1] * dy) + (dy / 2))

            sprite_list.append(sprite)
        
        return sprite_list