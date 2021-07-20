"""
The handle collisions action module contains the class and functions that detects when the actos collide with the walls or the trail
"""
import arcade

from data import constants
from data.action import Action
from data.particles import Particle, Smoke

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, explosions_list=arcade.SpriteList()):
        """Executes the action using the given actors. Checks for collisions between walls and trails

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ai_characters = cast["ai"]
        players = cast["players"]

        trail_sprite_lists = {}
        map_sprite_list = {cast["map"][0]: cast["map"][0].get_sprite()}

        for player in players:
            trail_sprite_lists[player] = player.get_trail().get_sprite_list()

        for ai in ai_characters:
            trail_sprite_lists[ai] = ai.get_trail().get_sprite_list()


        for player in players:
            if not player.is_dead():
                if player.check_collision(trail_sprite_lists, map_sprite_list):
                    constants.SOUND_COLLISION.play(0.2)
                    append_explosion(explosions_list, player.get_position())
                    player.kill()

        for ai in ai_characters:
            if not ai.is_dead():
                if ai.check_collision(trail_sprite_lists, map_sprite_list):
                    constants.SOUND_COLLISION.play(0.2)
                    append_explosion(explosions_list, ai.get_position())
                    ai.kill()
                else:
                    ai.check_ai_collisions(trail_sprite_lists)
                    ai.check_ai_collisions(map_sprite_list)

def append_explosion(explosions_list, position):
    """
    Adds an explosion to the given list, this pulls from both Particle and Smoke to create it
    """
    for _ in range(constants.PARTICLE_COUNT):
        particle = Particle(explosions_list)
        particle.position = position
        explosions_list.append(particle)

    smoke = Smoke(50)
    smoke.position = position
    explosions_list.append(smoke)