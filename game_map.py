from sprites import get_image

class Tile(object):
    tile_type = None

    def __init__(self, tile_type=None, tile_num=0):
        self.tile_type = tile_type
        self.tile_num  = tile_num
        self.image     = get_image('tile')
        self.contents  = []

    def update_tile(self, tile_type):
        self.tile_type = tile_type
        self.image = get_image(self.tile_type)

class Atlas(object):
    directions = {
        'right': (1, 0),
        'left':  (-1, 0),
        'up':    (0, 1),
        'down':  (0, -1),
    }
    def __init__(self, rows=None, cols=None):
        self.rows = rows if rows else 10
        self.cols = cols if cols else 10
        self.atlas = [[Tile(tile_type='regular') for row in range(self.rows)]
                for col in range(self.cols)]

    def __iter__(self):
        return iter([tile for row in self.atlas for tile in row])

    def is_location(self, x, y):
        if x in range(0, self.rows + 1) and y in range(0, self.cols + 1):
            try:
                return self.atlas[x][y].tile_type == 'regular'
            except IndexError:
                pass
        return False

    def pos(self, x, y):
        if self.is_location(x, y):
            return self.atlas[x][y]

    def place_on_tile(self, thing, x, y):
        tile = self.pos(x, y)
        if tile:
            tile.contents.append(thing)

    def remove_from_tile(self, thing, x, y):
        tile = self.pos(x,y)
        if tile:
            tile.contents.remove(thing)

    def valid_directions(self, x, y, if_hero=False):
        """
        Returns the possible valid movement directions from (x, y)
        """
        valid_list = []

        for direction, coordinates in self.directions.iteritems():
            del_x, del_y = coordinates
            tile = self.pos(x + del_x, y + del_y)
            if tile and not tile.contents:
                valid_list.append(direction)

        return valid_list
