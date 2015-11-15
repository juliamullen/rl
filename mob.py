from character import Character

import random
random.seed()

class Mob(Character):
    def __init__(self, mob_type, name, **kwargs):
        super(Mob, self).__init__(mob_type, name, **kwargs)

    def move(self):
        self.x = self.x + random.randint(-1, 1)
        self.y = self.y + random.randint(-1, 1)

class Enemies(object):
    def __init__(self):
        enemies = []
        for i in range(5):
            enemies.append(Mob('dog-devil',
                "Harry",
                x=random.randint(5, 14),
                y=random.randint(5, 14)))

        self.enemies = enemies
