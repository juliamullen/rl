from pyglet.window import key

direction_dict = {
    key.LEFT:  'left',
    key.RIGHT: 'right',
    key.DOWN:  'down',
    key.UP:    'up',
}

def move_hero(symbol, modifiers, hero):
    direction = direction_dict.get(symbol)
    hero.move(direction=direction)

def check_quit(symbol, modifiers):
    if symbol == key.Q:
        return True
