# for now, we'll exit the program if the player collides with any of the borders
# for week 1, we are just checking for player collisions with the walls (from constants.py)

import sys
from game import constants
from game.action import Action
from game.point import Point

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
        # paddle = cast["paddle"][0] # there's only one
        # ball = cast["ball"][0] # there's only one
        # bricks = cast["brick"]

        # paddlex = paddle.get_position().get_x()
        # paddley = paddle.get_position().get_y()

        # ballx = ball.get_position().get_x()
        # bally = ball.get_position().get_y()
        # ballpos = ball.get_position()

        # balldx = ball.get_velocity().get_x()
        # balldy = ball.get_velocity().get_y()

        # collision = True
        # while collision:
        #     diag_brick = None
        #     block_hit = False

        #     if not bricks:
        #         sys.exit()

        #     for brick in bricks:
        #         brickpos = brick.get_position()

        #         if ballpos.add(Point(balldx, 0)).equals(brickpos):
        #             bricks.remove(brick)
        #             balldx *= -1
        #             ball.set_velocity(Point(balldx, balldy))
        #             block_hit = True

        #         elif ballpos.add(Point(0, balldy)).equals(brickpos):
        #             bricks.remove(brick)
        #             balldy *= -1
        #             ball.set_velocity(Point(balldx, balldy))
        #             block_hit = True

        #         elif ballpos.add(Point(balldx, balldy)).equals(brickpos):
        #             diag_brick = brick

        #         else:
        #             collision = False

        #     if diag_brick != None and not block_hit:
        #         bricks.remove(diag_brick)
        #         balldx *= -1
        #         balldy *= -1
        #         ball.set_velocity(Point(balldx, balldy))
        #         collision = True

        #     if bally + balldy == paddley:
        #         if paddlex <= (ballx + balldx) < paddlex + len(paddle.get_text()):
        #             balldy *= -1
        #             ball.set_velocity(Point(balldx, balldy))
        #             collision = True

        #     if ballx + balldx >= constants.MAX_X - 1 or ballx + balldx <= 0:
        #         balldx *= -1
        #         ball.set_velocity(Point(balldx, balldy))
        #         collision = True
            
        #     if bally + balldy <= 0:
        #         balldy *= -1
        #         ball.set_velocity(Point(balldx, balldy))
        #         collision = True

        #     elif bally + balldy >= constants.MAX_Y:
        #         # balldy *= -1
        #         # ball.set_velocity(Point(balldx, balldy))
        #         sys.exit()
        pass