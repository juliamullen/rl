from sprites import get_image

import pyglet

class Character(object):
    def __init__(self, char_type=None, name=None, **kwargs):
        self.char_type = char_type
        self.name = name
        self.pronoun = kwargs.get('pronoun', "their")
        self.x = kwargs.get('x')
        self.y = kwargs.get('y')
        self.image = get_image(self.char_type)
