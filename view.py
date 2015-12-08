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
        self.message = ""
        self.write_message()
        self.window_left = 0
        self.window_right = 10
        self.window_bottom = 0
        self.window_top = 10
        self.center_x = 5
        self.center_y = 5

    def write_message(self):
        if self.message:
            self.messages.draw_text(self.message, 0, 0, 2, 2)

    def reassign_center(self, center=None, width=10, height=10):
        """
        Returns a tuple containing the four indices to use when drawing the tiles
        """
        if center:
            self.window_left   = center.x - int(width / 2)
            self.window_right  = center.x + int(width / 2)
            self.window_bottom = center.y - int(height / 2)
            self.window_top    = center.y + int(height / 2)
            self.center_x = center.x
            self.center_y = center.y

    def translate_from_center(self, x, y):
        new_x = x - self.window_left
        new_y = y - self.window_bottom
        return new_x, new_y

    def draw_tiles(self, atlas):
        for col_num, column in enumerate(atlas.return_tiles(self.window_left,
                                                            self.window_right,
                                                            self.window_bottom,
                                                            self.window_top)):
            for row_num, tile in enumerate(column):
                self.view.draw_item(tile.image, col_num, row_num,
                       width=1, height=1)

    def draw_hero(self, hero):
        hero_x, hero_y = self.translate_from_center(hero.x, hero.y)
        self.view.draw_item(hero.image, hero_x, hero_y,
                width=1, height=1)

    def draw_enemies(self, enemies):
        for enemy in enemies.enemies:
            enemy_x, enemy_y = self.translate_from_center(enemy.x, enemy.y)
            self.view.draw_item(enemy.image, enemy_x, enemy_y,
                    width=1, height=1)

    def reset_view(self, window):
        self.view = View(window, 10., 15, 30, 70, 68)
