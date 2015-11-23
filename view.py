import math
from pyglet.text import Label

class View(object):
    def __init__(self, window, scale, left_percent, bottom_percent, width_percent, height_percent):
        self.left   = self.get_from_percent(window.width, left_percent)
        self.bottom = self.get_from_percent(window.height, bottom_percent)
        self.width  = self.get_from_percent(window.width, width_percent)
        self.height = self.get_from_percent(window.height, height_percent)
        self.scale_x = self.width / scale
        self.scale_y = self.height / scale

    def get_from_percent(self, window_attr, percent):
        return math.floor(window_attr * (percent / 100.))

    def translate(self, x, y, width, height):
        x_to_draw = (self.scale_x * x) + self.left
        y_to_draw = (self.scale_y * y) + self.bottom
        width_to_draw = math.floor(width * self.scale_x)
        height_to_draw = math.floor(height * self.scale_y)

        translated_points = {
            'x':      x_to_draw,
            'y':      y_to_draw,
            'width':  width_to_draw,
            'height': height_to_draw,
        }


        return translated_points

    def draw_item(self, image_to_blit, x, y, width, height, s=False):
        translated_values = self.translate(x, y, width, height)

        image_to_blit.blit(**translated_values)

    def draw_text(self, text_to_blit, x, y, width, height, **kwargs):
        translated = self.translate(x, y, width, height)
        Label(text_to_blit, font_name="Times New Roman", font_size=22, anchor_x='left',
                anchor_y="bottom", color=(255,255,255,255), **translated).draw()

class Animator(object):
    def __init__(self, window):
        self.views = []
        self.view = View(window, 10., 15, 30, 70, 68)
        self.messages = View(window, 2., 15, 0, 70, 30)
        self.message = "GAMETHON 3000"
        self.write_message()

    def write_message(self):
        self.messages.draw_text(self.message, 0, 0, 2, 2)

    def draw_tiles(self, atlas):
        for col_num, column in enumerate(atlas.atlas):
            for row_num, tile in enumerate(column):
                self.view.draw_item(tile.image, col_num, row_num,
                       width=1, height=1)

    def draw_hero(self, hero):
        self.view.draw_item(hero.image, hero.x, hero.y,
                width=1, height=1, s=True)

    def draw_enemies(self, enemies):
        for enemy in enemies.enemies:
            self.view.draw_item(enemy.image, enemy.x, enemy.y,
                    width=1, height=1)

    def reset_view(self, window):
        self.view = View(window, 10., 15, 30, 70, 68)
