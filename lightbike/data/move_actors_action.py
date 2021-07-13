"""
The move actors action module contains the class and functions that move the actor
"""

from data.action import Action

class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, delta_time):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for group in cast:
            if group != "buttons":
                for actor in cast[group]:
                    if not (actor.get_velocity()[0] == 0 and actor.get_velocity()[1] == 0):
                        self._move_actor(actor,  delta_time)

    def _move_actor(self, actor, delta_time):
        """Moves the given actor to its next position according to its 
        velocity.
        
        Args:
            actor (Actor): The actor to move.
        """
        position = actor.get_position()
        velocity = actor.get_velocity()
        x1 = position[0]
        y1 = position[1]
        x2 = velocity[0]
        y2 = velocity[1]
        x = x1 + (x2 * delta_time)
        y = y1 + (y2 * delta_time)
        position = (x, y)
        actor.set_position(position)