from settings import TILE_MAP as SPRITE_MAP
from jobs    import image_for_type

import pyglet

class Hero(object):
    def __init__(self, hero_type=None, name=None):
        self.hero_type = hero_type
        self.name = name
        self.x = 10
        self.y = 10
        self.image = SPRITE_MAP[image_for_type[self.hero_type]]

    def draw(self):
        self.image.blit(32*self.x, 32*self.y)

    def move(self, direction=None, update_look=False):
        if direction:
            directions = {
                'right': (1, 0),
                'left':  (-1, 0),
                'up':    (0, 1),
                'down':  (0, -1),
            }
            x_delt, y_delt = directions[direction]
            self.x = self.x + x_delt
            self.y = self.y + y_delt


