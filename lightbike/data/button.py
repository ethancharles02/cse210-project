"""
"""
from arcade import Sprite, Texture
from PIL import Image, ImageFont, ImageDraw

class Button(Sprite):
    """
    """
    def __init__(self, text="PLAY", text_color=(1, 93, 229), font="arial", color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=10, font_size = 50, selectable=True, selected=False, selected_color=(12, 255, 255)):
        super().__init__()
        self.texture = create_button(text=text, text_color=text_color, font=font, color=color, margin_width = margin_width, margin_height = margin_height, button_fill=button_fill, outline=outline, edge_thickness=edge_thickness, font_size = font_size)
        self.selectable = selectable
        self.selected = selected
        if selectable:
            self.append_texture(create_button(text=text, text_color=text_color, font=font, color=color, margin_width = margin_width, margin_height = margin_height, button_fill=button_fill, edge_thickness=edge_thickness, font_size = font_size, outline=selected_color))

    def coords_in_hitbox(self, x, y):
        return self.collides_with_point((x, y))

    def select(self):
        if self.selectable:
            # if self.selected:
            #     self.selected = False
            #     self.update_selection()
            # else:
            self.selected = True
            self.update_selection()
    
    def unselect(self):
        if self.selectable:
            # if self.selected:
            #     self.selected = False
            #     self.update_selection()
            # else:
            self.selected = False
            self.update_selection()
    
    def update_selection(self):
        if self.selectable:
            if self.selected:
                self.set_texture(1)
            else:
                self.set_texture(0)

    def is_selected(self):
        if self.selectable:
            return self.selected

def create_button(text="PLAY", text_color=(1, 93, 229), font="arial", color="black", margin_width = 40, margin_height = 20, button_fill="black", outline="white", edge_thickness=10, font_size = 50):
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

    return Texture(name="button", image=button_img)

if __name__ == "__main__":
    button = Button("test")

    print(button.position)
    print(button.width)
    print(button.height)
    print(button.coords_in_hitbox(19, 14))