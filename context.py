from player   import Hero
from game_map import Atlas
from view     import Animator
from mob      import Enemies

import controller

import pyglet


if __name__ == "__main__":
    window     = pyglet.window.Window(resizable=True, width=700, height=700)
    atlas      = Atlas(10, 10)
    hero       = Hero(hero_type="ghost")
    animator   = Animator(window)
    event_loop = pyglet.app.EventLoop()
    enemies    = Enemies(7, 7)
    atlas.atlas[hero.x][hero.y].contents.append(hero)
    for enemy in enemies:
        atlas.atlas[enemy.x][enemy.y].contents.append(enemy)
    @window.event
    def on_key_press(symbol, modifiers):
        if controller.check_quit(symbol, modifiers):
            window.close()
        hero.move(atlas, symbol=symbol)
        enemies.remove_dead_enemies(atlas)
        enemies.move(atlas, hero)

    @window.event
    def on_draw():
        window.clear()
        animator.draw_tiles(atlas)
        animator.draw_hero(hero)
        animator.draw_enemies(enemies)
        animator.write_message()
    @window.event
    def on_resize(width, height):
        animator.reset_view(window)

    pyglet.app.run()
