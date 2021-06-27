# from data import constants

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    """
        
    def draw_actor(self, actor):
        """Renders the given actor's text on the screen.

        Args:
            actor (Actor): The actor to render.
        """
        actor.get_sprite().draw()

    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            actors (list): The actors to render.
        """ 
        for actor in actors:
            actor.get_sprite().draw() 