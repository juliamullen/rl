import pyglet

TILE_MAP_IMAGE = pyglet.image.load('f-tilemap.png')
TILE_MAP = pyglet.image.ImageGrid(TILE_MAP_IMAGE, 26, 8)

def get_image(name):
    image_for_type = {
        'goblin':           24,
        'dude':             25,
        'sword-skellie':    26,
        'sword-zomb':       27,
        'spear-nude-hunk':  28,
        'bear-devil':       29,
        'battletoad':       30,
        'dog-devil':        31,
        'slimes':           32,
        'just-one-slime':   33,
        'scorpion':         34,
        'cthulu':           35,
        'dracula':          36,
        'pharoh':           37,
        'ghost':            38,
        'monsters-inc':     39,
        'shrooms':          40,
        'bunny':            41,
        'bat':              42,
        'goldbat':          43,
        'snake':            44,
        'dog':              45,
        'warthog':          46,
        'bear':             47,
        'rat':              48,
        'bugz':             49,
        'lizard':           50,
        'nasty-spider':     51,
        'frog':             52,
        'beetle':           53,
        'centipede':        54,
        'dragon':           55,
        'knife-orc':        56,
        'king':             57,
        'sword-orc':        58,
        'boobs-orc':        59,
        'bow-elf':          60,
        'paladin':          61,
        'dope-wizard':      62,
        'dark-priest':      63,
        'penta':            64,
        'ankh':             65,
        'kiss':             66,
        'luminati':         67,
        'compass':          68,
        'guy':              69,
        'scroll':           70,
        'sign':             71,
        'tile':             192,
    }

    image_index = image_for_type[name]

    if image_index and image_index < len(TILE_MAP):
        return TILE_MAP[image_index]

    return None
