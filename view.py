import math

TILE_SIZE = 55

class View(object):
    def __init__(self, window, scale, left_percent, bottom_percent, width_percent, height_percent):
        self.left   = self.get_from_percent(window.width, left_percent)
        self.bottom = self.get_from_percent(window.height, bottom_percent)
        self.width  = self.get_from_percent(window.width, width_percent)
        self.height = self.get_from_percent(window.height, height_percent)
        self.scale_x = self.width / scale
        self.scale_y = self.height / scale
        print "{0} {1}".format(self.scale_x, self.scale_y)

    def get_from_percent(self, window_attr, percent):
        return math.floor(window_attr * (percent / 100.))

    def draw_item(self, image_to_blit, x, y, width, height, s=False):
        x_to_draw = (self.scale_x * x) + self.left
        y_to_draw = (self.scale_y * y) + self.bottom
        width_to_draw = math.floor(width * self.scale_x)
        height_to_draw = math.floor(height * self.scale_y)

        x_in_bound = self.left < x_to_draw < self.left + self.width
        y_in_bound = self.bottom < y_to_draw < self.bottom + self.height

        if s:
            print "{0} {1} {2} {3}".format(x_to_draw, y_to_draw, width_to_draw, height_to_draw)

        image_to_blit.blit(x_to_draw,
                    y_to_draw,
                    width=width_to_draw,
                    height=height_to_draw)

class Animator(object):

    def __init__(self, window):
        self.view = View(window, 10., 15, 30, 70, 68)

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
