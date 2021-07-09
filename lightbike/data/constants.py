"""
The constants module holds global variables for the lightbike game
"""
from arcade import color
from arcade import key
from arcade import Sound

SCREEN_TITLE = "Lightbike"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_SCALING = 1

MOVEMENT_SPEED = 100
DEFAULT_KEYS = {
    key.A: (-1, 0), # a
    key.D: (1, 0),  # d
    key.W: (0, 1),  # w
    key.S: (0, -1)  # s
}

NUM_PLAYERS = 1
NUM_AI = 10

AI_RANGE = 5
AI_BLINDSPOT_RANGE = 3
AI_TURN_COOLDOWN = 0.5

SOUND_BACKGROUND = Sound("assets/Sci-Fi-Dramatic-Theme.wav")
SOUND_COLLISION = Sound("assets/mi_explosion_03_hpx.wav")

__corner = "assets/corner"
__parallel = "assets/parallel"
__one = "assets/one"
__three = "assets/three"
__wall = "assets/blue_wall.png"

DEFAULT_WALL = "assets/blue_wall.png"
MAPX = 20
MAPY = 15

# Default map
MAP0 = [

]

MAP1 = [
    [(4, 3), __wall, 0],
    [(4, 4), __wall, 90],
    [(4, 11), __wall, 180],
]

# MAP2

# MAP3

BACKGROUND_COLOR = color.BLACK