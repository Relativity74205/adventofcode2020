from pathlib import Path
import itertools
from collections import defaultdict
from functools import reduce
from operator import mul

import numpy as np


with open(Path(__file__).parent / "data" / "puzzle20.txt", "r") as f:
    raw_data = f.read()

tiles = [tile for tile in raw_data.split('\n\n')]
tiles = [[row for row in tile.split('\n')] for tile in tiles]
tiles = {int(tile[0].replace('Tile ', '').replace(':', '')): tile[1:] for tile in tiles}
tiles = {tile_id: np.array([[1 if char == '#' else 0 for char in row] for row in tile])
         for tile_id, tile in tiles.items()}


def compare_tiles(t1_combinations, t2_combinations):
    for o1, t1 in t1_combinations.items():
        for o2, t2 in t2_combinations.items():
            if np.all(t1[0, :] == t2[-1, :]):
                return o1, o2

    return None


border_count = defaultdict(int)
borders = []

tiles_possibilities = {}
for tile_id, tile in tiles.items():
    tiles_possibilities[tile_id] = {'rot0': np.rot90(tile, 0),
                                    'rot0lr': np.fliplr(np.rot90(tile, 0)),
                                    'rot0ud': np.flipud(np.rot90(tile, 0)),
                                    'rot1': np.rot90(tile, 1),
                                    'rot1lr': np.fliplr(np.rot90(tile, 1)),
                                    'rot1ud': np.flipud(np.rot90(tile, 1)),
                                    'rot2': np.rot90(tile, 2),
                                    'rot2lr': np.fliplr(np.rot90(tile, 2)),
                                    'rot2ud': np.flipud(np.rot90(tile, 2)),
                                    'rot3': np.rot90(tile, 3),
                                    'rot3lr': np.fliplr(np.rot90(tile, 3)),
                                    'rot3ud': np.flipud(np.rot90(tile, 3)),
                                    }

for t1_id, t2_id in itertools.combinations(tiles.keys(), r=2):
    border = compare_tiles(tiles_possibilities[t1_id], tiles_possibilities[t2_id])
    if border:
        border_count[t1_id] += 1
        border_count[t2_id] += 1
        borders.append((t1_id, border[0], t2_id, border[1], ))

corners = [tile_id for tile_id, borders in border_count.items() if borders == 2]
print(f'{reduce(mul, corners)}')  # 59187348943703
