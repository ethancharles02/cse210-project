import pytest
from data.player import Player

def test_get_name():
    player = Player()
    player.set_name("Player1")
    
    assert player.get_name() == "Player1"

def test_set_name():
    player = Player()
    player.set_name("Player2")

    assert player.get_name() == "Player2"

# pytest.main(["-v", "--tb=no", "test_player.py"])