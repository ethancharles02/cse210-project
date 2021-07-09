import pytest
# import arcade
from data.player import Player
from arcade import key, Sprite
from data import constants

def test_set_movement_speed():
    player = Player()
    player.set_sprite(Sprite("assets/blue_player.png", constants.SPRITE_SCALING))
    player.set_movement_speed(1)

    assert player.get_keys() == {
        key.A: (-1, 0),
        key.D: (1, 0),
        key.W: (0, 1),
        key.S: (0, -1)
    }

    player.set_movement_speed(10)

    assert player.get_keys() == {
        key.A: (-10, 0),
        key.D: (10, 0),
        key.W: (0, 10),
        key.S: (0, -10)
    }

def test_get_keys():
    player = Player()
    player.set_sprite(Sprite("assets/blue_player.png", constants.SPRITE_SCALING))
    player.set_movement_speed(1)

    assert player.get_keys() == {
        key.A: (-1, 0),
        key.D: (1, 0),
        key.W: (0, 1),
        key.S: (0, -1)
    }

def test_set_keys():
    player = Player()
    player.set_sprite(Sprite("assets/blue_player.png", constants.SPRITE_SCALING))
    player.set_movement_speed(1)

    assert player.get_keys() == {
        key.A: (-1, 0),
        key.D: (1, 0),
        key.W: (0, 1),
        key.S: (0, -1)
    }

    player.set_keys({
        key.LEFT: (-1, 0),
        key.RIGHT: (1, 0),
        key.UP: (0, 1),
        key.DOWN: (0, -1)
    })

    assert player.get_keys() == {
        key.LEFT: (-1, 0),
        key.RIGHT: (1, 0),
        key.UP: (0, 1),
        key.DOWN: (0, -1)
    }

pytest.main(["-v", "--tb=no", "test_player.py"])