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

    def __iter__(self):
        return iter(self.atlas)

    def valid_directions(self, x, y):
        """
        Returns the possible valid movement directions from (x, y)
        """
        valid_list = []
        print "x, y {0}, {1}".format(x, y)
        try:
            right_tile = self.atlas[x+1][y]
            if right_tile.tile_type == 'regular' and right_tile.contents == []:
                valid_list.append('right')
        except IndexError:
            pass
        try:
            if x > 0:
                left_tile = self.atlas[x-1][y]
                if left_tile.tile_type == 'regular' and left_tile.contents == []:
                    valid_list.append('left')
        except IndexError:
            pass
        try:
            up_tile = self.atlas[x][y+1]
            if up_tile.tile_type == 'regular' and up_tile.contents == []:
                valid_list.append('up')
        except IndexError:
            pass
        try:
            if y > 0 and self.atlas[x][y-1].tile_type == 'regular':
                down_tile = self.atlas[x][y-1]
                if down_tile.tile_type == 'regular' and down_tile.contents == []:
                    valid_list.append('down')
        except IndexError:
            pass

        return valid_list
