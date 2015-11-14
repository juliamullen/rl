from settings import TILE_MAP
from player import Hero

import controller

import pyglet

class Tile(object):
    tile_type = None
    d = 192

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
        # self.d += 1
        # print self.d % len(TILE_MAP)
        self.image = TILE_MAP[self.d % len(TILE_MAP)]


if __name__ == "__main__":
    window = pyglet.window.Window()
    label = pyglet.text.Label("hello world", x=window.width//2, y=window.height//2)
    tile = Tile()
    hero = Hero(hero_type="ghost")
    @window.event
    def on_key_press(symbol, modifiers):
        controller.move_hero(symbol, modifiers, hero)
        tile.update_tile()

    @window.event
    def on_draw():
        window.clear()
        tile.draw()
        hero.draw()

    pyglet.app.run()
