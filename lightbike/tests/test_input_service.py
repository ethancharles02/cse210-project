import pytest
from data.input_service import InputService
from data.point import Point
from arcade import key

def test_get_direction():
    input_service = InputService()
    input_service.set_movement_speed(1)

    assert input_service.get_direction(None, key.A).equals(Point(-1, 0))
    assert input_service.get_direction(None, key.D).equals(Point(1, 0))
    assert input_service.get_direction(None, key.W).equals(Point(0, 1))
    assert input_service.get_direction(None, key.S).equals(Point(0, -1))

def test_set_movement_speed():
    input_service = InputService()
    
    input_service.set_movement_speed(1)
    assert input_service.get_movement_speed() == 1

    input_service.set_movement_speed(5)
    assert input_service.get_movement_speed() == 5

def test_get_movement_speed():
    input_service = InputService()
    input_service.set_movement_speed(-10)
    assert input_service.get_movement_speed() == -10

    input_service.set_movement_speed(20)
    assert input_service.get_movement_speed() == 20

# pytest.main(["-v", "--tb=no", "test_input_service.py"])