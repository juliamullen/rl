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
    def __init__(self, rows=None, cols=None):
        self.rows = rows if rows else 10
        self.cols = cols if cols else 10
        self.atlas = [[Tile(tile_type='regular') for row in range(self.rows)]
                for col in range(self.cols)]

    def valid_directions(self, x, y):
        """
        Returns the possible valid movement directions from (x, y)
        """
        valid_list = []
        try:
            if self.atlas[x+1][y].tile_type == 'regular':
                valid_list.append('right')
        except IndexError:
            pass
        try:
            if self.atlas[x-1][y].tile_type == 'regular':
                valid_list.append('left')
        except IndexError:
            pass
        try:
            if self.atlas[x][y+1].tile_type == 'regular':
                valid_list.append('up')
        except IndexError:
            pass
        try:
            if self.atlas[x][y-1].tile_type == 'regular':
                valid_list.append('down')
        except IndexError:
            pass

        return valid_list
