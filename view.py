TILE_SIZE = 50

class Animator(object):

    def draw_tiles(self, atlas):
        for col_num, column in enumerate(atlas.atlas):
            for row_num, tile in enumerate(column):
               tile.image.blit(TILE_SIZE*col_num, TILE_SIZE*row_num,
                       width=TILE_SIZE, height=TILE_SIZE)

    def draw_hero(self, hero):
        hero.image.blit(TILE_SIZE*hero.x, TILE_SIZE*hero.y,
                width=TILE_SIZE, height=TILE_SIZE)

    def draw_enemies(self, enemies):
        for enemy in enemies.enemies:
            enemy.image.blit(TILE_SIZE*enemy.x, TILE_SIZE*enemy.y,
                    width=TILE_SIZE, height=TILE_SIZE)
