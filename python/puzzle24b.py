from pathlib import Path
from typing import List, Tuple
from collections import defaultdict
from functools import reduce
from operator import add


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
        tiles.pop(coord)
    else:
        tiles[coord] = True

    return tiles


def get_black_neighbors(tiles: defaultdict, coord: Tuple[int, int]) -> int:
    black_neighbors = [(coord[0] + direction[0], coord[1] + direction[1]) in tiles.keys()
                       for direction in directions.values()]

    return sum(black_neighbors)


def get_relevant_tiles(coord: Tuple[int, int]) -> List[Tuple[int, int]]:
    relevant_tiles = [(coord[0] + direction[0], coord[1] + direction[1])
                      for direction in directions.values()]

    return [coord] + relevant_tiles


def process_tiles(tiles: defaultdict) -> defaultdict:
    tiles_copy = tiles.copy()
    relevant_tiles = [get_relevant_tiles(coord) for coord in tiles.keys()]
    relevant_tiles = set(reduce(add, relevant_tiles))

    for tile_coord in relevant_tiles:
        neighbor_value = get_black_neighbors(tiles, tile_coord)
        black_color = tile_coord in tiles.keys()
        if (black_color and (neighbor_value == 0 or neighbor_value > 2) or
                not black_color and neighbor_value == 2):
            tiles_copy = switch_color(tiles_copy, tile_coord)

    return tiles_copy


for line in raw_data:
    tiles_dict = switch_color(tiles_dict, process_line(line))

for i in range(1, 101):
    tiles_dict = process_tiles(tiles_dict)
    print(f'{i=} {sum(tiles_dict.values())=}')
