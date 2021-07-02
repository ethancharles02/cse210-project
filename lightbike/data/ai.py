# checks in front of it to see if it will collide (using the list of trail points checking between a range maybe of the sprite size)
# also checks if it will collide with boundary
# turns random direction

# if it doesn't detect a collision, have a random tick check that will make it turn

# Ai attributes:
# trail
# dead

# Ai methods:
# check_collision() (have a set range, if collision is too close, don't turn)
# is_dead()
# get_trail()
# set_trail()

import random
from data.actor import Actor
from data.trail import Trail

class Ai(Actor):
    def __init__(self):
        super().__init__()
        pass
    def check_collision(self, trails_point_lists):
        pass
    def is_dead(self):
        pass
    def get_trail(self):
        pass
    def set_trail(self):
        pass
    