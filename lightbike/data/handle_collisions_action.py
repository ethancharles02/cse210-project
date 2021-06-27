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
        player = cast["players"][0]

        playerx = player.get_position().get_x()
        playery = player.get_position().get_y()
        # player_pos = player.get_position()

        # playervx = player.get_velocity().get_x()
        # playervy = player.get_velocity().get_y()

        if playery >= constants.SCREEN_HEIGHT - 1 or playery <= 0:
            game.close()

        if playerx >= constants.SCREEN_WIDTH - 1 or playerx <= 0:
            game.close()

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