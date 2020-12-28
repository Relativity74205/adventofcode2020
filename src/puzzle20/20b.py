import math
from pathlib import Path
import itertools
from collections import defaultdict
from functools import reduce
from operator import mul

import numpy as np


with open(Path(__file__).parent / "data" / "puzzle20_debug.txt", "r") as f:
    raw_data = f.read()

tiles = [tile for tile in raw_data.split('\n\n')]
tiles = [[row for row in tile.split('\n')] for tile in tiles]
tiles = {int(tile[0].replace('Tile ', '').replace(':', '')): tile[1:] for tile in tiles}
tiles = {tile_id: np.array([[1 if char == '#' else 0 for char in row] for row in tile])
         for tile_id, tile in tiles.items()}


tiles_possibilities = {}
for tile_id, tile in tiles.items():
    tiles_possibilities[tile_id] = {'0_no': np.rot90(tile, 0),
                                    '0_lr': np.fliplr(np.rot90(tile, 0)),
                                    '0_ud': np.flipud(np.rot90(tile, 0)),
                                    '1_no': np.rot90(tile, 1),
                                    '1_lr': np.fliplr(np.rot90(tile, 1)),
                                    '1_ud': np.flipud(np.rot90(tile, 1)),
                                    '2_no': np.rot90(tile, 2),
                                    '2_lr': np.fliplr(np.rot90(tile, 2)),
                                    '2_ud': np.flipud(np.rot90(tile, 2)),
                                    '3_no': np.rot90(tile, 3),
                                    '3_lr': np.fliplr(np.rot90(tile, 3)),
                                    '3_ud': np.flipud(np.rot90(tile, 3)),
                                    }


def compare_tiles(t1, t2_combinations):
    for t2_orientation, t2 in t2_combinations.items():
        if np.all(t1[0, :] == t2[-1, :]):
            return [0, -1], t2_orientation
        elif np.all(t1[-1, :] == t2[0, :]):
            return [0, 1], t2_orientation
        elif np.all(t1[:, 0] == t2[:, -1]):
            return [-1, 0], t2_orientation
        elif np.all(t1[:, -1] == t2[:, 0]):
            return [1, 0], t2_orientation

    return None, None


def set_tiles(tiles, tiles_possibilities):
    edge_length = int(np.sqrt(len(tiles)))
    tile_length = 10
    arr = np.zeros((edge_length * tile_length * 3, edge_length * tile_length * 3))
    x = int(edge_length * tile_length * 1.5 - tile_length / 2)
    y = int(edge_length * tile_length * 1.5 - tile_length / 2)
    arr_id = np.zeros((edge_length * 3, edge_length * 3))
    x_id = int(edge_length + 1)
    y_id = int(edge_length + 1)

    tiles_set = set()
    for t1_id, t2_id in itertools.combinations(tiles.keys(), r=2):
        # slice_x = (start_x, tile_length, None)
        # slice_y = (start_y, tile_length, None)
        arr_id[x_id, y_id] = t1_id
        delta, t2_orientation = compare_tiles(tiles[t1_id], tiles_possibilities[t2_id])
        x_id, y_id = delta[0], delta[1]
        arr_id[x_id, y_id] = t2_id

    return arr


set_tiles(tiles, tiles_possibilities)