import pytest

from arcade import Sprite, SpriteList

from data.lightbike import Lightbike
from data.trail import Trail
from data import constants

def test_set_get_name():
    lightbike = Lightbike()
    lightbike.set_name("Player1")
    
    assert lightbike.get_name() == "Player1"

def test_set_get_trail():
    lightbike = Lightbike()
    lightbike.set_trail(Trail())

    assert type(lightbike.get_trail()) == Trail

def test_update_trail():
    lightbike = Lightbike()
    lightbike.set_sprite(Sprite())
    lightbike.get_trail().add_point((0, 0))

    lightbike.set_position((1, 0))

    lightbike.update_trail()

    assert len(lightbike.get_trail().get_point_list()) == 1
    assert len(lightbike.get_trail().get_sprite_list()) == 1

def test_set_get_movement_speed():
    lightbike = Lightbike()
    lightbike.set_sprite(Sprite())
    lightbike.set_movement_speed(100)

    assert lightbike.get_movement_speed() == 100

def test_kill_is_dead():
    lightbike = Lightbike()
    lightbike.set_sprite(Sprite())

    assert not lightbike.is_dead()

    lightbike.kill()

    assert lightbike.is_dead()

def test_check_collision():
    lightbike = Lightbike()
    lightbike.set_sprite(Sprite("assets/blue_player.png", constants.SPRITE_SCALING))

    orig_width = lightbike.get_sprite().width * constants.SPRITE_SCALING**-1
    hitbox = lightbike.get_sprite().get_hit_box()
    lightbike.get_sprite().set_hit_box(tuple(map(lambda x: (x[0] + 2 + orig_width / 2, x[1]) if x[0] < 0 else (x[0], x[1]), hitbox)))
    lightbike.set_position((constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2))

    trail_sprite_list = SpriteList()
    trail_sprite_list.append(Sprite("assets/blue_wall.png", constants.SPRITE_SCALING))
    trail_sprite_list[0].position = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    sprite_list = {}

    assert not lightbike.check_collision(sprite_list)

    sprite_list = {
        lightbike: trail_sprite_list
    }

    assert lightbike.check_collision(sprite_list)



# pytest.main(["-v", "--tb=no", "test_lightbike.py"])