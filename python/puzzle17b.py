from pathlib import Path
from itertools import product

import numpy as np


with open(Path(__file__).parent / "data" / "puzzle17.txt", "r") as f:
    raw_data = f.read().splitlines()

data = [[cell == '#' for cell in list(row)] for row in raw_data]
grid_arr = np.expand_dims(np.array(data), axis=0)
grid_arr = np.expand_dims(np.array(grid_arr), axis=0)
grid_arr = np.pad(grid_arr, 1, 'constant', constant_values=0)


def perform_cycle(arr):
    arr = np.pad(arr, 1, 'constant', constant_values=0)
    arr_copy = arr.copy()
    for coord in product(*([range(1, dim) for dim in arr.shape])):
        neighbor_window = tuple([slice(dim - 1, dim + 2) for dim in coord])
        active_neighbors = arr[neighbor_window].sum() - arr[coord]
        if arr[coord]:
            if active_neighbors not in (2, 3):
                arr_copy[coord] = 0
        else:
            if active_neighbors == 3:
                arr_copy[coord] = 1

    return arr_copy


for _ in range(6):
    grid_arr = perform_cycle(grid_arr)

print(grid_arr.sum())
