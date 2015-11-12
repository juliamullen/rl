import pyglet
TILE_MAP_IMAGE = pyglet.image.load('tilemap.png')
TILE_MAP = pyglet.image.ImageGrid(TILE_MAP_IMAGE, 16, 16)

class Tile(object):
    tile_type = None

    def __init__(self, tile_type=None):
        self.tile_type = tile_type
        self.image = self.image_for_type()

    def image_for_type(self):
        return TILE_MAP[0]

    def draw(self):
        for i in range(30):
            for b in range(20):
                self.image = TILE_MAP[(b+1)**(i+1) % len(TILE_MAP)]
                self.image.blit(32*i, 32*b)




if __name__ == "__main__":
    window = pyglet.window.Window()
    label = pyglet.text.Label("hello world", x=window.width//2, y=window.height//2)
    tile = Tile()
    @window.event
    def on_draw():
        window.clear()
        label.draw()
        tile.draw()

    pyglet.app.run()
