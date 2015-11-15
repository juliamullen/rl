from player import Hero
from game_map import Tile

import controller

import pyglet


if __name__ == "__main__":
    window = pyglet.window.Window(fullscreen=True)
    tile = Tile()
    hero = Hero(hero_type="ghost")
    event_loop = pyglet.app.EventLoop()
    @window.event
    def on_key_press(symbol, modifiers):
        if controller.move_hero(symbol, modifiers, hero):
            window.close()

        tile.update_tile()

    @window.event
    def on_draw():
        window.clear()
        tile.draw()
        hero.draw()

    pyglet.app.run()
