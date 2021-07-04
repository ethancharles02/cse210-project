"""
The handle collisions action module contains the class and functions that detects when the actos collide with the walls or the trail
"""
from data import constants
from data.action import Action
# from data.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, game, cast):
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
                player.check_collision(trail_sprite_lists)
        for ai in ai_characters:
            if not ai.is_dead():
                ai.check_collision(trail_sprite_lists)
                ai.check_ai_collisions(trail_sprite_lists)

        player = players[0]
        playerx = player.get_position().get_x()
        playery = player.get_position().get_y()

        if playery >= constants.SCREEN_HEIGHT - player.get_sprite().width / 2 or playery <= 0 + player.get_sprite().width / 2:
            player.dead_sprite()

        if playerx >= constants.SCREEN_WIDTH - player.get_sprite().width / 2 or playerx <= 0 + player.get_sprite().width / 2:
            player.dead_sprite()