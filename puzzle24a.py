from pathlib import Path
from typing import Tuple
from collections import defaultdict


with open(Path(__file__).parent / "data" / "puzzle24.txt", "r") as f:
    raw_data = f.read().splitlines()


directions = {'e': (-10, 0, ),
              'se': (-5, -10, ),
              'sw': (5, -10, ),
              'w': (10, 0, ),
              'nw': (5, 10, ),
              'ne': (-5, 10, ),
              }


tiles_dict = defaultdict(bool)


def process_line(direction_sentence: str) -> Tuple[int, int]:
    direction = ''
    x, y = 0, 0
    for char in direction_sentence:
        direction += char
        try:
            delta = directions[direction]
        except KeyError:
            continue
        x += delta[0]
        y += delta[1]
        direction = ''

    return x, y


def switch_color(tiles: defaultdict, coord: Tuple[int, int]):
    if tiles[coord]:
        del tiles[coord]
    else:
        tiles[coord] = True

    return tiles


for line in raw_data:
    coord = process_line(line)
    tiles_dict = switch_color(tiles_dict, coord)

print(f'{sum(tiles_dict.values())}')
