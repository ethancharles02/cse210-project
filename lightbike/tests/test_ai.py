import pytest
from data.ai import Ai
from data import constants
from arcade import Sprite, SpriteList

def test_check_ai_collisions():
    ai = Ai()
    ai.set_sprite(Sprite("assets/blue_player.png", constants.SPRITE_SCALING))
    ai.set_movement_speed(1)
    ai.set_velocity((0, 1))

    orig_width = ai.get_sprite().width * constants.SPRITE_SCALING**-1
    hitbox = ai.get_sprite().get_hit_box()
    ai.get_sprite().set_hit_box(tuple(map(lambda x: (x[0] + 2 + orig_width / 2, x[1]) if x[0] < 0 else (x[0], x[1]), hitbox)))
    ai.set_position((constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2))

    trail_sprite_list = SpriteList()
    trail_sprite_list.append(Sprite("assets/blue_wall.png", constants.SPRITE_SCALING))
    trail_sprite_list[0].position = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 5)

    sprite_list = {
        ai: trail_sprite_list
    }

    ai.check_ai_collisions(sprite_list)

    velocity = ai.get_velocity()
    assert velocity == (1, 0) or velocity == (-1, 0)

def test_turn():
    ai = Ai()
    ai.set_sprite(Sprite("assets/blue_player.png", constants.SPRITE_SCALING))
    ai.set_movement_speed(1)
    ai.set_velocity((0, -1))

    ai.turn()

    velocity = ai.get_velocity()
    assert velocity == (1, 0) or velocity == (-1, 0)

def test_set_velocity():
    ai = Ai()
    ai.set_sprite(Sprite("assets/blue_player.png", constants.SPRITE_SCALING))
    ai.set_movement_speed(1)
    ai.set_velocity((0, -1))

    assert ai.get_velocity() == (0, -1)
    ai.set_movement_speed(5)
    assert ai.get_velocity() == (0, -5)

def test_update_cooldown():
    ai = Ai()
    ai.set_sprite(Sprite("assets/blue_player.png", constants.SPRITE_SCALING))
    ai.set_movement_speed(1)
    ai.set_velocity((0, -1))
    ai.turn_cooldown = 3
    ai.cur_turn_cooldown = 3
    ai.update_cooldown(0.3)

    assert ai.cur_turn_cooldown == pytest.approx(2.7, 0.01)

    ai.update_cooldown(1.3)

    assert ai.cur_turn_cooldown == pytest.approx(1.4, 0.01)

    ai.update_cooldown(1.5)

    assert ai.cur_turn_cooldown == pytest.approx(-0.1, 0.01)

    ai.turn()

    assert ai.cur_turn_cooldown == pytest.approx(3, 0.01)

# pytest.main(["-v", "--tb=no", "test_ai.py"])