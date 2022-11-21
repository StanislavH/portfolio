from settings import *

text_map = [
    "111111111111111111111111",
    "1.......1.....1...11...1",
    "1......111.........11...",
    "1..11....111...........1",
    "1..1.........11...1....1",
    "1..1.11.111.11.......111",
    "1......................1",
    "111111111111111111111111",
    ]
WORLD_WIDTH = len(text_map[0]) * TILE
WORLD_HEIGHT = len(text_map) * TILE
world_map = {}


def get_map():
    for j, row in enumerate(text_map):
        for i, char in enumerate(row):
            if char == '1':
                world_map[(i * TILE, j * TILE)] = 1


get_map()
