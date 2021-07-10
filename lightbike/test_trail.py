import pytest
from arcade import SpriteList, Sprite
from data.trail import Trail

def test_set_point_list():
    trail = Trail()
    point_list = (0, 0), (0, 1), (0, 2)
    trail.set_point_list(point_list)
    
    assert trail.get_point_list() == ((0, 0), (0, 1), (0, 2))

def test_add_point():
    trail = Trail()
    point = (0, 0)
    trail.add_point(point)
    point = (0, 1)
    trail.add_point(point)
    point = (0, 2)
    trail.add_point(point)

    assert trail.get_point_list() == [(0, 0), (0, 1), (0, 2)]

def test_add_point_list():
    trail = Trail()
    point_list = (0, 0), (0, 1), (0, 2)
    trail.add_point_list(point_list)

    assert trail.get_point_list() == [(0, 0), (0, 1), (0, 2)]

def test_set_sprite_list():
    trail = Trail()
    sprite_list = SpriteList()
    sprite_list.append(Sprite())
    sprite_list.append(Sprite())
    sprite_list.append(Sprite())
    trail.set_sprite_list(sprite_list)
    
    assert type(trail.get_sprite_list()) == SpriteList
    assert len(trail.get_sprite_list()) == 3

def test_add_sprite():
    trail = Trail()
    sprite_list = SpriteList()
    trail.set_sprite_list(sprite_list)
    trail.add_sprite(Sprite())

    assert type(trail.get_sprite_list()) == SpriteList
    assert len(trail.get_sprite_list()) == 1

def test_update_temp_list():
    trail = Trail()
    sprite_list = SpriteList()
    point_list = [(0, 0), (0, 1)]
    trail.set_sprite_list(sprite_list)
    trail.update_temp_list(point_list)

    assert type(trail.get_sprite_list()) == SpriteList
    assert len(trail.get_sprite_list()) == 1

pytest.main(["-v", "--tb=no", "test_trail.py"])