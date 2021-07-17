"""
"""
from arcade import Sprite, Texture, load_texture
from PIL import Image, ImageFont, ImageDraw
from data import constants
from random import random

global num_buttons
num_buttons = -1

class Button(Sprite):
    """
    """
    def __init__(self, text="PLAY", text_color=(1, 93, 229), font=constants.DEFAULT_FONT, color="black", margin_width = 40, margin_height = 25, button_fill="black", outline="white", edge_thickness=5, font_size = 30, selectable=True, selected=False, selected_color=(12, 255, 255)):
        super().__init__()
        self.append_texture(create_button(text=text, text_color=text_color, font=font, color=color, margin_width = margin_width, margin_height = margin_height, button_fill=button_fill, outline=outline, edge_thickness=edge_thickness, font_size = font_size))
        if selectable:
            self.append_texture(create_button(text=text, text_color=text_color, font=font, color=color, margin_width = margin_width, margin_height = margin_height, button_fill=button_fill, edge_thickness=edge_thickness, font_size = font_size, outline=selected_color))
        
        self.set_texture(0 if not selected else 1)
        
        self.selectable = selectable
        self.selected = selected
        self.new_name = True


    def coords_in_hitbox(self, x, y):
        return self.collides_with_point((x, y))

    def select(self):
        if self.selectable:
            # if self.selected:
            #     self.selected = False
            #     self.update_selection()
            # else:
            self.selected = True
            if self.texture == self.textures[0]:
                global num_buttons
                num_buttons += 1
                self.texture.name = num_buttons
                self.set_texture(1)
            # self.update_selection()
    
    def unselect(self):
        if self.selectable:
            # if self.selected:
            #     self.selected = False
            #     self.update_selection()
            # else:
            self.selected = False
            if self.texture == self.textures[1]:
                global num_buttons
                num_buttons += 1
                self.texture.name = num_buttons
                self.set_texture(0)
            # self.update_selection()
    
    # def update_selection(self):
    #     if self.selectable:
    #         if self.selected:
                
    #             # self.texture.name = self._orig_name if self.texture.name != self._orig_name else self._orig_name + 0.5
    #         else:
                
                # self.texture.name = self._orig_name if self.texture.name != self._orig_name else self._orig_name + 0.5
    
    # def set_texture(self, texture_no):
    #     print("test")
    #     super().set_texture(texture_no)

def create_button(text="PLAY", text_color=(1, 93, 229), font=constants.DEFAULT_FONT, color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=10, font_size = 50):
    global num_buttons    
    font = ImageFont.truetype(font, size=font_size)

    # get text size
    text_size = font.getsize(text)

    # set button size + 10px margins
    button_size = (text_size[0] + margin_width, text_size[1] + margin_height)

    # create image with correct size and black background
    button_img = Image.new('RGBA', button_size, color)

    # put text on button with 10px margins
    button_draw = ImageDraw.Draw(button_img)
    width = button_size[0]
    height = button_size[1]
    button_draw.rounded_rectangle((0, 0, width, height), fill=button_fill, outline=outline, width=edge_thickness, radius=height/2)
    button_draw.text((margin_width / 2, margin_height / 2), text, font=font, fill=text_color)

    num_buttons += 1
    load_texture.texture_cache[num_buttons] = Texture(name=num_buttons, image=button_img)
    return load_texture.texture_cache[num_buttons]

if __name__ == "__main__":
    button = Button("test")

    print(button.position)
    print(button.width)
    print(button.height)
    print(button.coords_in_hitbox(19, 14))