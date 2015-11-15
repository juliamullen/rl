from settings import TILE_MAP

X_DIFF = 300
Y_DIFF = 200

class Tile(object):
    tile_type = None

    def __init__(self, tile_type=None, tile_num=0):
        print len(TILE_MAP)
        self.tile_type = tile_type
        self.tile_num = tile_num
        self.tile_number = 192
        self.image = self.image_for_type()

    def image_for_type(self):
        return TILE_MAP[self.tile_number % len(TILE_MAP)]

    def draw(self):
        for i in range(30):
            for j in range(15):
                self.image.blit(32*i + X_DIFF, 32*j + Y_DIFF)

    def update_tile(self):
        self.image = TILE_MAP[self.tile_number % len(TILE_MAP)]

