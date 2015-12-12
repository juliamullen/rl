from sprites import get_image
import random

class Tile(object):
    tile_type = None

    def __init__(self, tile_type='tile', tile_num=0):
        self.tile_type = tile_type
        self.tile_num  = tile_num
        self.image     = get_image('tile')
        self.update_tile(self.tile_type)
        self.contents  = []

    def update_tile(self, tile_type):
        self.tile_type = tile_type
        self.image = get_image(self.tile_type)

    def __repr__(self):
        return "[]" if self.tile_type == 'tile' else '{}'

def generate_map(height, width, style):
    if style == 'random':
        return [[Tile(tile_type_generator())
            for row in range(height)]
            for col in range(width)]
    if style == 'rooms':
        room_row = [Tile('tile' if ((y % 12) < 8) else "scroll") for y in range(height)]
        corridor_row = [Tile('tile') for y in range(height)]
        return [room_row if x % 10 else corridor_row for x in range(width)]



def tile_type_generator():
    if not random.randint(0, 20):
        return 'scroll'
    z = random.randint(0, 16)
    return [
        'tile',
        'tile',
        'tile',
        'tile',
        'tile',
        'tile',
        'tile',
        'tile',
        'tile',
        'tile',
        'tile',
        'tile',
        'othertile',
        'othertile',
        'othertile',
        'othertile',
        'otherothertile',
    ][z]

class Atlas(object):
    def __init__(self, rows=None, cols=None):
        self.rows = rows if rows else 100
        self.cols = cols if cols else 100
        self.atlas = generate_map(self.rows, self.cols, style='rooms')
    def __iter__(self):
        return iter([tile for row in self.atlas for tile in row])

    def is_location(self, x, y):
        if x in range(0, self.rows + 1) and y in range(0, self.cols + 1):
            try:
                return 'tile' in self.atlas[x][y].tile_type
            except IndexError:
                pass
        return False

    def pos(self, x, y):
        if self.is_location(x, y):
            return self.atlas[x][y]

    def has_contents(self, x, y, tile=None):
        if not tile:
            tile = self.pos(x, y)
        if tile.contents:
            return True

        return False

    def is_empty(self,x, y, tile=None):
        if not tile:
            tile = self.pos(x, y)
        if tile:
            return True

        return False

    def place_on_tile(self, thing, x, y):
        tile = self.pos(x, y)
        if tile:
            tile.contents.append(thing)

    def remove_from_tile(self, thing, x, y):
        tile = self.pos(x,y)
        if tile:
            tile.contents.remove(thing)

    def return_tiles(self, left, right, bottom, top):
        def return_tile(atlas, x, y):
            tile = atlas.pos(x, y)
            if tile:
                return tile
            else:
                return Tile(tile_type='scroll')

        tiles_to_return = [[return_tile(self, j, i)
                for i in range(bottom, top)]
                for j in range(left, right)]
        return tiles_to_return
