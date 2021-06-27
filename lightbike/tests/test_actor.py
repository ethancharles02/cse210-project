import pytest
import arcade
from data.point import Point
from data.actor import Actor

def test_get_sprite():
    actor = Actor()
    actor.set_sprite(arcade.Sprite("assets/blue_player_resized.png", 1))
    
    assert type(actor.get_sprite()) == arcade.Sprite

def test_set_sprite() :
    actor = Actor()
    actor.set_sprite(arcade.Sprite("assets/blue_player_resized.png", 1))
    
    assert type(actor.get_sprite()) == arcade.Sprite

def test_get_position():
    actor = Actor()
    actor.set_sprite(arcade.Sprite("assets/blue_player_resized.png", 1))
    
    assert actor.get_position().get_x() == 0
    assert actor.get_position().get_y() == 0

def test_set_position():
    actor = Actor()
    actor.set_sprite(arcade.Sprite("assets/blue_player_resized.png", 1))
    actor.set_position(Point(5, 5))
    assert actor.get_position().get_x() == 5
    assert actor.get_position().get_y() == 5

def test_get_velocity():
    actor = Actor()
    assert actor.get_velocity().get_x() == 0
    assert actor.get_velocity().get_y() == 0

def test_set_velocity():
    actor = Actor()
    actor.set_velocity(Point(5, 5))
    assert actor.get_velocity().get_x() == 5
    assert actor.get_velocity().get_y() == 5

# pytest.main(["-v", "--tb=no", "test_actor.py"])