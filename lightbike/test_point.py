import pytest
from data.point import Point

def test_get_xy():
    point = Point(5, 10)
    assert point.get_x() == 5
    assert point.get_y() == 10

def test_equals():
    point_1 = Point(1, 2)
    point_2 = Point(2, 4)
    assert not point_1.equals(point_2)
    point_1 = Point(1, 2)
    point_2 = Point(1, 2)
    assert point_1.equals(point_2)

def test_reverse_xy():
    reverse_xy = Point(1, 1)
    assert reverse_xy.reverse().get_x() == -1
    assert reverse_xy.reverse().get_y() == -1

def test_is_zero():
    is_zero = Point(0, 0)
    assert is_zero.is_zero() == True

def test_add_xy():
    add_xy = Point(1, 1)
    assert add_xy.add(Point(1, 1)).get_x() == 2
    assert add_xy.add(Point(1, 1)).get_y() == 2
    

pytest.main(["-v", "--tb=no", "test_point.py"])