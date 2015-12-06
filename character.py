from sprites import get_image
from direction import get_standard_directions

import pyglet

class Character(object):
    def __init__(self, char_type=None, name=None, **kwargs):
        self.char_type = char_type
        self.name = name
        self.pronoun = kwargs.get('pronoun', "their")
        self.x = kwargs.get('x')
        self.y = kwargs.get('y')
        self.image = get_image(self.char_type)
        self.directions = get_standard_directions()

    def move(self, atlas, symbol=None, direction=None):
        if not direction and symbol:
            direction = next((direction for direction in self.directions
                              if direction.key == symbol), None)
        if direction and direction in self.directions.get_valid_directions(self.x, self.y, atlas):
            del_x, del_y = direction.delta
            new_x = self.x + del_x
            new_y = self.y + del_y
            if not atlas.has_contents(new_x, new_y):
                atlas.remove_from_tile(self, self.x, self.y)
                self.x = new_x
                self.y = new_y
                atlas.place_on_tile(self, self.x, self.y)
