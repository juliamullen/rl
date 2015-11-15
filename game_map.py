from sprites import get_image

X_DIFF = 300
Y_DIFF = 200


class Tile(object):
    tile_type = None

    def __init__(self, tile_type=None, tile_num=0):
        self.tile_type = tile_type
        self.tile_num = tile_num
        self.image = get_image('tile')

    def draw(self):
        for i in range(30):
            for j in range(15):
                self.image.blit(32*i + X_DIFF, 32*j + Y_DIFF)

    def update_tile(self, tile_type):
        self.tile_type = tile_type
        self.image = get_image(self.tile_type)

class Atlas(object):
    def __init__(self):
        self.rows = 40
        self.cols = 40
        self.atlas = [[Tile(tile_type='regular') for row in range(self.rows)]
                for col in range(self.cols)]
