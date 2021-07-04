# from data import constants
from arcade import color

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider
    """
        
    def draw_actor(self, actor, group=""):
        """Renders the given actor's text on the screen.

        Args:
            actor (Actor): The actor to render.
        """
        # if group == "players" or group == "ai":
        if group == "players" or group == "ai":
            actor.update_trail()
            for sprite_list in actor.get_trail().get_sprite_list():
                sprite_list.draw()
        actor.get_sprite().draw()
        # actor.get_sprite().draw_hit_box(color.WHITE)
        
        # if group == "players" or group == "ai":
        #     self._draw_trail(actor)

    # def _draw_trail(self, actor):
    #     actor.get_trail().get_sprite_list().draw()

    def draw_actors(self, actors, group=""):
        """Renders the given list of actors on the screen.

        Args:
            actors (list): The actors to render.
        """ 
        for actor in actors:
            self.draw_actor(actor, group)
            # actor.get_sprite().draw() 