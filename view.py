
class Animator(object):

    def draw_tiles(self, atlas):
        for col_num, column in enumerate(atlas.atlas):
            for row_num, tile in enumerate(column):
               tile.image.blit(32*col_num, 32*row_num)

    def draw_hero(self, hero):
        hero.image.blit(32*hero.x, 32*hero.y)

    def draw_enemies(self, enemies):
        for enemy in enemies.enemies:
            enemy.image.blit(32*enemy.x, 32*enemy.y)
