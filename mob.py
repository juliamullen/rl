from character import Character
from controller import directions

import random
random.seed()

class Mob(Character):
    def __init__(self, mob_type, name, **kwargs):
        super(Mob, self).__init__(mob_type, name, **kwargs)

    def move(self, valid_directions):
        if valid_directions is None:
            return
        valid_directions = list(valid_directions)
        random_direction = valid_directions[random.randint(0, len(valid_directions)-1)]
        dx, dy = directions[random_direction]
        self.x += dx
        self.y += dy



class Enemies(object):
    def __init__(self, x, y):
        enemies = []
        for i in range(5):
            enemies.append(Mob('dog-devil',
                "Harry",
                x=random.randint(0, x),
                y=random.randint(0, y)))

        self.enemies = enemies
