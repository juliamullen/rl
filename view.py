import math

TILE_SIZE = 55

class View(object):
    def __init__(self, window, left_percent, bottom_percent, width_percent, height_percent):
        self.left   = self.get_from_percent(window.width, left_percent)
        self.bottom = self.get_from_percent(window.height, bottom_percent)
        self.width  = self.get_from_percent(window.width, width_percent)
        self.height = self.get_from_percent(window.height, height_percent)
        self.scale_x = window.width / self.width
        self.scale_y = window.height / self.height

    def get_from_percent(self, window_attr, percent):
        return math.floor(window_attr * (percent / 100.))

    def draw_item(self, image_to_blit, x, y, width, height, s=False):
        x_to_draw = math.floor(self.scale_x * (x + self.left))
        y_to_draw = math.floor(self.scale_y * (y + self.bottom))
        width_to_draw = math.floor(width * self.scale_x)
        height_to_draw = math.floor(height * self.scale_y)

        x_in_bound = self.left < x_to_draw < self.left + self.width
        y_in_bound = self.bottom < y_to_draw < self.bottom + self.height

        image_to_blit.blit(x_to_draw,
                    y_to_draw,
                    width=width_to_draw,
                    height=height_to_draw)

class Animator(object):

    def __init__(self, window):
        self.view = View(window, 10, 10, 90, 90)

    def draw_tiles(self, atlas):
        for col_num, column in enumerate(atlas.atlas):
            for row_num, tile in enumerate(column):
                self.view.draw_item(tile.image, TILE_SIZE*col_num, TILE_SIZE*row_num,
                       width=TILE_SIZE, height=TILE_SIZE)

    def draw_hero(self, hero):
        self.view.draw_item(hero.image, TILE_SIZE*hero.x, TILE_SIZE*hero.y,
                width=TILE_SIZE, height=TILE_SIZE, s=True)

    def draw_enemies(self, enemies):
        for enemy in enemies.enemies:
            self.view.draw_item(enemy.image, TILE_SIZE*enemy.x, TILE_SIZE*enemy.y,
                    width=TILE_SIZE, height=TILE_SIZE)
