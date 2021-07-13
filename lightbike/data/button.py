"""
"""
from arcade import Sprite
class Button(Sprite):
    """
    """
    def __init__(self, text="Play"):
        super().__init__()

    def coords_in_hitbox(self, x, y):
        return True

    def select(self):
        pass

    def is_selected(self):
        pass