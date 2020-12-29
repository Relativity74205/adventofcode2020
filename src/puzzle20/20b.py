from typing import Dict, List
from itertools import combinations
from collections import defaultdict
from functools import reduce
from operator import mul, add

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

edge_length = int(np.sqrt(len(tiles)))
# tile_length = 10
# arr = np.zeros((edge_length * tile_length * 3, edge_length * tile_length * 3))
# x = int(edge_length * tile_length * 1.5 - tile_length / 2)
# y = int(edge_length * tile_length * 1.5 - tile_length / 2)
# x_id = int(edge_length + 1)
# y_id = int(edge_length + 1)
arr_id = np.zeros((edge_length, edge_length))


def get_neighbor_cells(arr: np.array, x: int, y: int):
    possible_cells = []
    x_max, y_max = arr.shape
    if x - 1 >= 0:
        possible_cells.append((x - 1, y, ))
    if x + 1 < x_max:
        possible_cells.append((x + 1, y, ))
    if y - 1 >= 0:
        possible_cells.append((x, y - 1, ))
    if y + 1 < y_max:
        possible_cells.append((x, y + 1, ))

    return possible_cells


def flatten_list(nested_list: List[List[int]]) -> List[int]:
    try:
        return reduce(add, nested_list)
    except TypeError:
        return []


def get_possible_cells(arr: np.array, x: int, y: int, neighbor, current_cell):
    possible_cells = get_neighbor_cells(arr, x, y)
    possible_cells = [cell for cell in possible_cells if arr[cell] == 0]
    for possible_cell in possible_cells:
        possible_cell_neighbors = get_neighbor_cells(arr, *possible_cell)
        possible_cell_neighbors_ids = [int(arr[cell]) for cell in possible_cell_neighbors
                                       if arr[cell] != 0 and arr[cell] != current_cell]
        possible_cell_neighbors_borders = flatten_list([borders[int(id)] for id in possible_cell_neighbors_ids])
        if neighbor in possible_cell_neighbors_borders:
            return [possible_cell]

    return possible_cells


x = 0
y = 0
start_id = corners[0]
arr_id[x, y] = start_id
from collections import deque
to_do = deque([start_id])
while to_do:
    to_do_tile_id = to_do.popleft()
    x = (arr_id == to_do_tile_id).nonzero()[0][0]
    y = (arr_id == to_do_tile_id).nonzero()[1][0]
    neighbors_full = borders[to_do_tile_id]
    neighbors = [neighbor for neighbor in neighbors_full if not (neighbor == arr_id).any()]
    while neighbors:
        d = {}
        for neighbor in neighbors:
            free_cells = get_possible_cells(arr_id, x, y, neighbor, to_do_tile_id)
            d[neighbor] = free_cells

        neighbor_id = sorted(d.items(), key=lambda item: len(item[1]))[0][0]
        arr_id[d[neighbor_id][0]] = neighbor_id
        neighbors.remove(neighbor_id)
        to_do.append(neighbor_id)
