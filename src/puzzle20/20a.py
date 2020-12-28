from typing import Dict, List
from itertools import combinations
from collections import defaultdict
from functools import reduce
from operator import mul

import numpy as np

from puzzle20 import raw_data, get_tiles, get_tiles_orientations


tiles = get_tiles(raw_data)
tiles_possibilities = get_tiles_orientations(tiles)


def compare_tiles(t1, t2_orientations):
    for t2_orientation, t2 in t2_orientations.items():
        if np.all(t1[0, :] == t2[-1, :]):
            return [0, -1], t2_orientation
        elif np.all(t1[-1, :] == t2[0, :]):
            return [0, 1], t2_orientation
        elif np.all(t1[:, 0] == t2[:, -1]):
            return [-1, 0], t2_orientation
        elif np.all(t1[:, -1] == t2[:, 0]):
            return [1, 0], t2_orientation

    return None, None


def get_border_count(tiles, tiles_possibilities) -> Dict[int, List[int]]:
    borders = defaultdict(list)
    for t1_id, t2_id in combinations(tiles.keys(), r=2):
        delta, t2_orientation = compare_tiles(tiles[t1_id], tiles_possibilities[t2_id])
        if delta:
            borders[t1_id].append(t2_id)
            borders[t2_id].append(t1_id)

    return borders


borders = get_border_count(tiles, tiles_possibilities)
corners = [tile_id for tile_id, neighbors in borders.items() if len(neighbors) == 2]
print(f'{reduce(mul, corners)}')  # 59187348943703
