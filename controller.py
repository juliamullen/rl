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
    atlas.atlas[hero.x][hero.y].contents.remove(hero)
    direction = direction_dict.get(symbol)
    print hero
    if direction in atlas.valid_directions(hero.x, hero.y):
        hero.move(direction=direction)
    atlas.atlas[hero.x][hero.y].contents.append(hero)

def check_quit(symbol, modifiers):
    if symbol == key.Q:
        return True

def move_enemies(enemies, atlas):
    for enemy in enemies.enemies:
        atlas.atlas[enemy.x][enemy.y].contents.remove(enemy)
        print enemy
        enemy.move(atlas.valid_directions(enemy.x, enemy.y))
        atlas.atlas[enemy.x][enemy.y].contents.append(enemy)

