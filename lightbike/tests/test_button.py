import pytest
from data.button import Button, create_button
from arcade import Texture

def test_coords_in_hitbox():
    button = Button(text="1 PLAYER", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=False, selected_color=(12, 255, 255))
    button.position = (100, 100)

    assert button.coords_in_hitbox(100, 100)
    assert button.coords_in_hitbox(80, 90)
    assert button.coords_in_hitbox(120, 110)

def test_select():
    button = Button(text="1 PLAYER", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=False, selected_color=(12, 255, 255))

    cur_texture = button.textures[0]
    selected_texture = button.textures[1]

    assert not button.selected
    assert button.texture == cur_texture
    button.select()
    assert button.selected
    assert button.texture == selected_texture

def test_unselect():
    button = Button(text="1 PLAYER", text_color=(1, 93, 229), color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=5, selectable=True, selected=True, selected_color=(12, 255, 255))
    
    cur_texture = button.textures[1]
    unselected_texture = button.textures[0]

    assert button.selected
    assert button.texture == cur_texture
    button.unselect()
    assert not button.selected
    assert button.texture == unselected_texture

def test_create_button():
    texture = create_button()

    assert type(texture) == Texture

# pytest.main(["-v", "--tb=no", "test_button.py"])