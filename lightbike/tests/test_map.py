import pytest
from data.map import Map
from data import constants

def test_set_get_map():
    map = Map()

    map.set_map(
        [
            [(0, 0), constants.DEFAULT_WALL, 0],
            [(0, 1), constants.DEFAULT_WALL, 90],
            [(0, 2), constants.DEFAULT_WALL, 180]
        ]
    )
    
    assert map.get_map() == [
        [(0, 0), constants.DEFAULT_WALL, 0],
        [(0, 1), constants.DEFAULT_WALL, 90],
        [(0, 2), constants.DEFAULT_WALL, 180]
    ]

def test_set_get_mapxy():
    map = Map()

    map.set_mapx(20)
    map.set_mapy(15)

    assert map.get_mapx() == 20
    assert map.get_mapy() == 15

# pytest.main(["-v", "--tb=no", "test_map.py"])