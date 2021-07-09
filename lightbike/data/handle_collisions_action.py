"""
The handle collisions action module contains the class and functions that detects when the actos collide with the walls or the trail
"""
import arcade

from data import constants
from data.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ai_characters = cast["ai"]
        players = cast["players"]

        trail_sprite_lists = {}
        
        for player in players:
            trail_sprite_lists[player] = player.get_trail().get_sprite_list()

        for ai in ai_characters:
            trail_sprite_lists[ai] = ai.get_trail().get_sprite_list()


        for player in players:
            if not player.is_dead():
                if player.check_collision(trail_sprite_lists):
                    constants.SOUND_COLLISION.play(0.2)
                    player.kill()

        for ai in ai_characters:
            if not ai.is_dead():
                if ai.check_collision(trail_sprite_lists):
                    constants.SOUND_COLLISION.play(0.2)
                    ai.kill()
                else:
                    ai.check_ai_collisions(trail_sprite_lists)