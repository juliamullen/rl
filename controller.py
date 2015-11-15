from pyglet.window import key

direction_dict = {
    key.LEFT:  'left',
    key.RIGHT: 'right',
    key.DOWN:  'down',
    key.UP:    'up',
}

class Quit(object):
    pass

action_dict = {
    key.A: True,
}

def move_hero(symbol, modifiers, hero):

    direction = direction_dict.get(symbol)

    hero.move(direction=direction, update_look=action_dict.get(symbol))

    if symbol == key.Q:
        return True
