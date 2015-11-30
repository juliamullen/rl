from character import Character
import random
import pyglet
from direction import get_standard_directions

class Hero(Character):
    def __init__(self, hero_type=None, name=None):
        super(Hero, self).__init__(hero_type, name, x=3, y=3)
        self.experience = 0
        self.level = 1
        self.directions = get_standard_directions(has_controls=True)

    def gain_experience(experience_gained):
        self.experience += experience_gained
        if self.experience % 10 > self.level:
            self.gain_level(int(self.experience % 10))

    def gain_level(advance_to_level):
        self.level = advance_to_level

    def attack(self, enemy=None):
        attack = 3 + random.randint(0, 4)
        if attack == 7:
            print ("!" * 20) + "CRITICAL HIT!" + ("!" * 20)

        enemy.take_damage(attack)
        print "Attacking {0} for {1} damage!".format(enemy.name, attack)
        if enemy.status == "dead":
            print "You killed {0}!".format(enemy.name)
