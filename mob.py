from character import Character
from pathfinding import Path

import random
random.seed()

ENEMY_NAMES = [('Gunther', 'he'),
        ('Woman From Baltimore, MD', 'she'),
        ('Ozymandias', 'he'),
        ('Grammy Award Winning Artist Beck', 'he'),
        ('Literally Queen Elizabeth', 'she')]

class Mob(Character):
    def __init__(self, mob_type, name, **kwargs):
        super(Mob, self).__init__(mob_type, name, **kwargs)
        self.health = 7
        self.status = "alive"
        self.path = Path()

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.status = "dead"

    def move_step(self, atlas):
        direction = self.path.get_next_step()
        self.move(atlas, direction=direction)

class Enemies(object):
    def __init__(self, x, y):
        enemies = []
        for i in range(5):
            enemies.append(Mob('bunny',
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

    def move(self, atlas, hero):
        for enemy in self.enemies:
            if not direction:
                direction = enemy.directions.get_random_direction(enemy.x, enemy.y, atlas)
            enemy.move(atlas, direction=direction)

    def __iter__(self):
        return iter(self.enemies)
