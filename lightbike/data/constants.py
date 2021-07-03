from arcade import color

from arcade import key
from data.point import Point

SCREEN_TITLE = "Lightbike"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_SCALING = 0.3
MOVEMENT_SPEED = 100
DEFAULT_KEYS = {
    key.A: Point(-1, 0), # a
    key.D: Point(1, 0),  # d
    key.W: Point(0, 1),  # w
    key.S: Point(0, -1)  # s
}
AI_RANGE = 5
AI_BLINDSPOT_RANGE = 3 
BACKGROUND_COLOR = color.BLACK