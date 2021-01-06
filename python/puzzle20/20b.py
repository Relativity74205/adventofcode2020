from collections import defaultdict

import numpy as np

from puzzle20 import create_arrays, raw_data, TILE_WIDTH, get_tile_orientation


MONSTER = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
monster_list = [list(line) for line in MONSTER.split('\n')]
arr_monster = np.array([[1 if char == '#' else 0 for char in row] for row in monster_list])

arr_ids, arr_pixels = create_arrays(raw_data)
marker_cols_rows = (list(range(0, arr_ids.shape[0] * TILE_WIDTH, TILE_WIDTH)) +
                    list(range(TILE_WIDTH - 1, arr_ids.shape[0] * TILE_WIDTH, TILE_WIDTH)))
arr_pixels = np.delete(arr_pixels, marker_cols_rows, axis=0)
arr_pixels = np.delete(arr_pixels, marker_cols_rows, axis=1)


from itertools import product
cnt_monster = defaultdict(int)
for i, arr in enumerate(get_tile_orientation(arr_pixels)):
    ref_coords = product(range(0, arr.shape[0] - arr_monster.shape[0]), range(0, arr.shape[1] - arr_monster.shape[1]))
    for coord in ref_coords:
        if (arr[coord[0]:coord[0]+arr_monster.shape[0], coord[1]:coord[1]+arr_monster.shape[1]] * arr_monster).sum() == arr_monster.sum():
            cnt_monster[i] += 1


cnt_rough_water = arr_pixels.sum() - max(cnt_monster.values()) * arr_monster.sum()
print(f'{cnt_rough_water=}')
