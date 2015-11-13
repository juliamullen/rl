import pyglet
TILE_MAP_IMAGE = pyglet.image.load('f-tilemap.png')
TILE_MAP = pyglet.image.ImageGrid(TILE_MAP_IMAGE, 14, 4)

class Tile(object):
    tile_type = None
    d = 12

    def __init__(self, tile_type=None, tile_num=0):
        print len(TILE_MAP)
        self.tile_type = tile_type
        self.tile_num = tile_num
        self.image = self.image_for_type()

    def image_for_type(self):
        return TILE_MAP[self.d % len(TILE_MAP)]

    def draw(self):
        for i in range(30):
            for j in range(15):
                self.image.blit(32*i, 32*j)

    def update_tile(self):
        self.d += 1
        self.image = TILE_MAP[self.d % len(TILE_MAP)]




if __name__ == "__main__":
    window = pyglet.window.Window()
    label = pyglet.text.Label("hello world", x=window.width//2, y=window.height//2)
    tile = Tile()
    @window.event
    def on_key_press(symbol, modifiers):
        tile.update_tile()

    @window.event
    def on_draw():
        window.clear()
        label.draw()
        tile.draw()

    pyglet.app.run()
