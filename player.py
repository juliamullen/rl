from sprites import get_image

import pyglet

class Hero(object):
    def __init__(self, hero_type=None, name=None):
        self.hero_type = hero_type
        self.name = name
        self.x = 10
        self.y = 10
        self.experience = 0
        self.level = 1
        self.image = get_image(self.hero_type)

    def move(self, direction=None):
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

    def gain_experience(experience_gained):
        self.experience += experience_gained
        if self.experience % 10 > self.level:
            self.gain_level(int(self.experience % 10))

    def gain_level(advance_to_level):
        self.level = advance_to_level
