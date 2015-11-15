from character import Character
import pyglet

class Hero(Character):
    def __init__(self, hero_type=None, name=None):
        super(Hero, self).__init__(hero_type, name, x=10, y=10)
        self.experience = 0
        self.level = 1

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
