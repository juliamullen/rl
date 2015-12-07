from pyglet.window import key

"""
def move_hero(symbol, modifiers, hero, atlas):
    x_delt, y_delt = directions[direction]
    tile = atlas.pos(hero.x + x_delt, hero.y + y_delt)
    if tile:
        enemy_list = tile.contents
        for enemy in enemy_list:
            hero.attack(enemy)

"""
def check_quit(symbol, modifiers):
    if symbol == key.Q:
        return True

def move_enemies(enemies, atlas):
    for enemy in enemies.enemies:
        pass
