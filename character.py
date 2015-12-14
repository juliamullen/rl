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
        self.side = kwargs.get('side')
        self.health = kwargs.get('health')
        self.status = "alive"

    def get_direction(self, symbol):
        direction = next((direction for direction in self.directions
                          if direction.key == symbol), None)
        return direction

    def move(self, atlas, symbol=None, direction=None):
        if not direction and symbol:
            direction = self.get_direction(symbol)
            r = self.side == "good"
            for direction in self.directions.get_valid_directions(self.x, self.y, atlas, z=r):
                print direction
                print atlas.pos(self.x + direction.delta[0],
                                self.y + direction.delta[1]).contents
        if direction and direction in self.directions.get_valid_directions(self.x, self.y, atlas):
            del_x, del_y = direction.delta
            new_x = self.x + del_x
            new_y = self.y + del_y
            if not atlas.has_contents(new_x, new_y):
                atlas.remove_from_tile(self, self.x, self.y)
                self.x = new_x
                self.y = new_y
                atlas.place_on_tile(self, self.x, self.y)

    def can_attack(self, atlas):
        for thing in self.directions.adjacent_tile_contents(self.x, self.y, atlas):
            if thing.side not in [self.side, 'item']:
                self.attack(thing)
                return True
        return False

    def attack(self, thing):
        damage = self.get_damage(thing)
        thing.take_damage(damage)

    def get_damage(self, thing):
        return 1

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.status = "dead"
