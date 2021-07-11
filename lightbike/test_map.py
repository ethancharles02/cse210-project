import pytest
# import arcade
from data.actor import Actor
from data import constants
from arcade import SpriteList, Sprite

def test_set_map():
    pass

def test_get_mapxy():
    set_mapxy = constants()
    assert set_mapxy.get_mapx() == 20
    assert set_mapxy.get_mapy() == 15

def test_set_mapxy():
    pass

def test_return_sprite_map():
    pass



pytest.main(["-v", "--tb=no", "test_map.py"])