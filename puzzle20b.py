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


def compare_tiles(t1, t2_combinations):
    for t2_orientation, t2 in t2_combinations.items():
        if np.all(t1[0, :] == t2[-1, :]):
            return 'o', t2_orientation
        elif np.all(t1[-1, :] == t2[0, :]):
            return 'u', t2_orientation
        elif np.all(t1[:, 0] == t2[:, -1]):
            return 'r', t2_orientation
        elif np.all(t1[:, -1] == t2[:, 0]):
            return 'l', t2_orientation

    return None, None


def get_borders(tiles):
    border_count = defaultdict(int)
    borders = defaultdict(list)
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

    for t1_id, t2_id in itertools.combinations(tiles.keys(), r=2):
        border, t2_orientation = compare_tiles(tiles[t1_id], tiles_possibilities[t2_id])
        if border:
            border_count[t1_id] += 1
            border_count[t2_id] += 1
            borders[t1_id].append((t2_id, border, t2_orientation))

    return border_count, borders


border_count, all_borders = get_borders(tiles)

corners = [tile_id for tile_id, borders in border_count.items() if borders == 2]
print(f'{reduce(mul, corners)}')  # 59187348943703


edge_length = int(np.sqrt(len(tiles)))
arr = np.zeros((edge_length * 10, edge_length * 10))
arr_ids = np.zeros((edge_length, edge_length))

start_corner = [corner for corner in corners if len(all_borders[corner]) == 2][0]
start_borders = [border[1] for border in all_borders[start_corner]]

start_x = 0 if 'r' in start_borders else edge_length - 1
start_y = 0 if 'u' in start_borders else edge_length - 1
arr_ids[start_x, start_y] = start_corner


def add_tiles(x, y, borders):
    for border_tile_id, border, orientation in borders:
        x_new = x
        y_new = y
        if border == 'r':
            x_new += 1
        elif border == 'l':
            x_new -= 1
        elif border == 'o':
            y_new -= 1
        else:
            y_new += 1
        # border_tile = tiles[border_tile_id]
        # border_tile = np.rot90(border_tile, int(orientation[0]))
        # if orientation[-2:] == 'lr':
        #     border_tile = np.fliplr(border_tile)
        # elif orientation[-2:] == 'ud':
        #     border_tile = np.flipud(border_tile)

        arr_ids[x_new, y_new] = border_tile_id
        try:
            add_tiles(x_new, y_new, all_borders[border_tile_id])
        except IndexError:
            pass


add_tiles(start_x, start_y, all_borders[start_corner])
