import pytest
import arcade
from data.actor import Actor

def test_get_sprite():
    actor = Actor()
    actor.set_sprite(arcade.Sprite("assets/blue_player.png", 1))
    
    assert type(actor.get_sprite()) == arcade.Sprite

def test_set_sprite() :
    actor = Actor()
    actor.set_sprite(arcade.Sprite("assets/blue_player.png", 1))
    
    assert type(actor.get_sprite()) == arcade.Sprite

def test_get_position():
    actor = Actor()
    actor.set_sprite(arcade.Sprite("assets/blue_player.png", 1))
    
    assert actor.get_position()[0] == 0
    assert actor.get_position()[1] == 0

def test_set_position():
    actor = Actor()
    actor.set_sprite(arcade.Sprite("assets/blue_player.png", 1))
    actor.set_position((5, 5))
    assert actor.get_position()[0] == 5
    assert actor.get_position()[1] == 5

def test_get_velocity():
    actor = Actor()
    assert actor.get_velocity()[0] == 0
    assert actor.get_velocity()[1] == 0

def test_set_velocity():
    actor = Actor()
    actor.set_sprite(arcade.Sprite("assets/blue_player.png", 1))
    actor.set_velocity((5, 5))
    assert actor.get_velocity()[0] == 5
    assert actor.get_velocity()[1] == 5

# pytest.main(["-v", "--tb=no", "test_actor.py"])