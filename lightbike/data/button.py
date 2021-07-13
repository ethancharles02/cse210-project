"""
"""
from arcade import Sprite, Texture
from PIL import Image, ImageFont, ImageDraw

class Button(Sprite):
    """
    """
    def __init__(self, text="Play", text_color="black", font="arial", color="white", selectable=True, selected=False, selected_color=(102, 102, 102)):
        super().__init__()
        self.texture = create_button(text=text, text_color=text_color, font=font, color=color)
        self.selectable = selectable
        self.selected = selected
        if selectable:
            self.append_texture(create_button(text=text, text_color=text_color, font=font, color=selected_color))

    def coords_in_hitbox(self, x, y):
        # if (self.center_x - self.width / 2) <= x <= (self.center_x + self.width / 2) and (self.center_y - self.height / 2) <= y <= (self.center_y + self.height / 2):
        #     return True
        # else:
        #     return False
        return self.collides_with_point((x, y))

    def select(self):
        if self.selectable:
            if self.selected:
                self.selected = False
                self.update_selection()
            else:
                self.selected = True
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

def create_button(text="Play", text_color="black", font="arial", color="white"):
    font = ImageFont.truetype(font)

    # get text size
    text_size = font.getsize(text)

    # set button size + 10px margins
    button_size = (text_size[0]+20, text_size[1]+20)

    # create image with correct size and black background
    button_img = Image.new('RGBA', button_size, color)

    # put text on button with 10px margins
    button_draw = ImageDraw.Draw(button_img)
    button_draw.text((10, 10), text, font=font, fill=text_color)

    return Texture(name="button", image=button_img)

if __name__ == "__main__":
    button = Button("test")

    print(button.position)
    print(button.width)
    print(button.height)
    print(button.coords_in_hitbox(19, 14))