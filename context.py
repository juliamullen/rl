from player   import Hero
from game_map import Atlas
from view     import Animator
from mob      import Enemies

import controller

import pyglet


if __name__ == "__main__":
    window     = pyglet.window.Window(resizable=True, width=700, height=700)
    atlas      = Atlas()
    hero       = Hero(hero_type="ghost")
    animator   = Animator(window)
    event_loop = pyglet.app.EventLoop()
    enemies    = Enemies(99, 99)
    atlas.atlas[hero.x][hero.y].contents.append(hero)
    for enemy in enemies:
        atlas.atlas[enemy.x][enemy.y].contents.append(enemy)
    @window.event
    def on_key_press(symbol, modifiers):
        if controller.check_quit(symbol, modifiers):
            window.close()
        if not hero.check_attack(atlas, symbol):
            hero.move(atlas, symbol=symbol)
        enemies.remove_dead_enemies(atlas)
        if len(enemies.enemies) == 0:
            print "YOU WIN!"

        for enemy in enemies:
            if not enemy.can_attack(atlas):
                enemy.path.update(x1=enemy.x,
                        y1=enemy.y,
                        x2=hero.x,
                        y2=hero.y,
                        atlas=atlas,
                        directions=enemy.directions)
                enemy.move_step(atlas)

    @window.event
    def on_draw():
        window.clear()
        animator.reassign_center(center=hero)
        animator.draw_tiles(atlas)
        animator.draw_hero(hero)
        animator.draw_enemies(enemies)
        animator.write_message()
    @window.event
    def on_resize(width, height):
        animator.reset_view(window)

    pyglet.app.run()
