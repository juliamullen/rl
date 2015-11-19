from character import Character
from controller import directions

import random
random.seed()

ENEMY_NAMES = [('Gunther', 'he'),
        ('Erica', 'she'),
        ('Ozymandias', 'he'),
        ('Grammy Award Winning Artist Beck', 'he'),
        ('Rebecca', 'she')]

class Mob(Character):
    def __init__(self, mob_type, name, **kwargs):
        super(Mob, self).__init__(mob_type, name, **kwargs)
        self.health = 7
        self.status = "alive"

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.status = "dead"

    def move(self, valid_directions):
        if not valid_directions:
            return
        valid_directions = list(valid_directions)
        if len(valid_directions) == 1:
            random_direction = valid_directions[0]
        else:
            random_direction = valid_directions[random.randint(0, len(valid_directions)-1)]
        dx, dy = directions[random_direction]
        if random.randint(-1, 1):
            self.x += dx
            self.y += dy



class Enemies(object):
    def __init__(self, x, y):
        enemies = []
        for i in range(5):
            enemies.append(Mob('dog-devil',
                ENEMY_NAMES[i][0],
                x=random.randint(0, x),
                y=random.randint(0, y),
                pronoun=ENEMY_NAMES[i][1]))

        self.enemies = enemies

    def remove_dead_enemies(self, atlas):
        for enemy in self.enemies:
            if enemy.status == "dead":
                atlas.remove_from_tile(enemy, enemy.x, enemy.y)
                self.enemies.remove(enemy)

    def __iter__(self):
        return iter(self.enemies)
