from pyglet.window import key

import random
random.seed()

class Direction(object):
    def __init__(self, *args, **kwargs):
        self.name  = kwargs.get('name')
        self.delta = kwargs.get('delta')

    def get_adjacent_tile(self, x, y, atlas):
        del_x, del_y = self.delta
        return atlas.pos(x + del_x, y + del_y)


class ControlDirection(Direction):
    def __init__(self, *args, **kwargs):
        self.key = kwargs.get('key')
        _direction = kwargs.get('direction')
        if _direction:
            self.name  = _direction.name
            self.delta = _direction.delta

        super(ControlDirection, self).__init__(*args, **kwargs)

class ValidDirections(object):
    def __init__(self, *args, **kwargs):
        self.directions = kwargs.get('directions', [])

    def __iter__(self):
        return iter(self.directions)

    def get_adjacent_tiles(self, x, y, atlas):
        """
        Returns all the adjacent tiles from (x, y)
        """
        tiles = []

        for direction in self.directions:
            del_x, del_y = direction.delta
            tile = atlas.pos(x + del_x, y + del_y)
            if tile:
                tiles.append(tile)

        return tiles

    def get_valid_directions(self, x, y, atlas):
        """
        Returns the possible valid movement directions from (x, y)
        """
        valid_list = []

        for direction in self.directions:
            del_x, del_y = direction.delta
            if atlas.is_empty(x + del_x, y + del_y):
                valid_list.append(direction)

        return valid_list

    def adjacent_tile_contents(self, x, y, atlas):
        contents = []
        for tile in self.get_adjacent_tiles(x, y, atlas):
            contents.extend(tile.contents)

        return contents


    def get_random_direction(self, x, y, atlas):
        valid_directions = self.get_valid_directions(x, y, atlas)
        if valid_directions:
            return valid_directions[random.randint(0, len(valid_directions)-1)]
        else:
            return None


def get_standard_directions(has_controls=False):
    if has_controls:
        standard_directions = [
            ControlDirection(key=key.LEFT,  name='left',  delta=(-1, 0)),
            ControlDirection(key=key.RIGHT, name='right', delta=(1, 0)),
            ControlDirection(key=key.UP,    name='up',    delta=(0, 1)),
            ControlDirection(key=key.DOWN,  name='down',  delta=(0, -1)),
        ]
    else:
        standard_directions = [
            Direction(name='left',  delta=(-1, 0)),
            Direction(name='right', delta=(1, 0)),
            Direction(name='up',    delta=(0, 1)),
            Direction(name='down',  delta=(0, -1)),
        ]

    return ValidDirections(directions=standard_directions)
