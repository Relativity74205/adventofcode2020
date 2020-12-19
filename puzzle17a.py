from pathlib import Path

import numpy as np


with open(Path(__file__).parent / "data" / "puzzle17.txt", "r") as f:
    raw_data = f.read().splitlines()

data = [list(row) for row in raw_data]
data = [[1 if cell == '#' else 0 for cell in row] for row in data]
grid_arr = np.expand_dims(np.array(data), axis=0)
grid_arr = np.pad(grid_arr, 1, 'constant', constant_values=0)


def perform_cycle(arr):
    arr = np.pad(arr, 1, 'constant', constant_values=0)
    arr_copy = arr.copy()
    for x in range(1, arr.shape[0]):
        for y in range(1, arr.shape[1]):
            for z in range(1, arr.shape[2]):
                active_neighbors = arr[x - 1:x + 2, y - 1:y + 2, z - 1:z + 2].sum() - arr[x, y, z]
                if arr[x, y, z]:
                    if not 2 <= active_neighbors <= 3:
                        arr_copy[x, y, z] = 0
                else:
                    if active_neighbors == 3:
                        arr_copy[x, y, z] = 1

    return arr_copy


for _ in range(6):
    grid_arr = perform_cycle(grid_arr)

print(grid_arr.sum())
