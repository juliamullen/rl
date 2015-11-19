from pyglet.window import key

direction_dict = {
    key.LEFT:  'left',
    key.RIGHT: 'right',
    key.DOWN:  'down',
    key.UP:    'up',
}

directions = {
    'right': (1, 0),
    'left':  (-1, 0),
    'up':    (0, 1),
    'down':  (0, -1),
    'still': (0, 0),
}

def move_hero(symbol, modifiers, hero, atlas):
    atlas.remove_from_tile(hero, hero.x, hero.y)
    direction = direction_dict.get(symbol)

    if not direction:
        return

    if direction in atlas.valid_directions(hero.x, hero.y):
        hero.move(direction=direction)

    else:
        x_delt, y_delt = directions[direction]
        enemy_list = atlas.pos(hero.x + x_delt, hero.y + y_delt).contents
        for enemy in enemy_list:
            hero.attack(enemy)

    atlas.place_on_tile(hero, hero.x, hero.y)

def check_quit(symbol, modifiers):
    if symbol == key.Q:
        return True

def move_enemies(enemies, atlas):
    for enemy in enemies.enemies:
        atlas.remove_from_tile(enemy, enemy.x, enemy.y)
        enemy.move(atlas.valid_directions(enemy.x, enemy.y))
        atlas.place_on_tile(enemy, enemy.x, enemy.y)

