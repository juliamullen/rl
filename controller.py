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
}

def move_hero(symbol, modifiers, hero, atlas):
    direction = direction_dict.get(symbol)
    print atlas.valid_directions(hero.y, hero.y)
    if direction in atlas.valid_directions(hero.x, hero.y):
        hero.move(direction=direction)

def check_quit(symbol, modifiers):
    if symbol == key.Q:
        return True

def move_enemies(enemies, atlas):
    for enemy in enemies.enemies:
        enemy.move(atlas.valid_directions(enemy.x, enemy.y))

