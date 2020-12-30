from functools import reduce
from operator import mul

from puzzle20 import create_arrays, raw_data


arr_ids, arr_pixels = create_arrays(raw_data)
# arr_pixels = np.delete(arr_pixels, list(range(0, 120, 8)) + list(range(7, 120, 8)), axis=0)
# arr_pixels = np.delete(arr_pixels, list(range(0, 120, 8)) + list(range(7, 120, 8)), axis=1)

corners = [arr_ids[0, 0],
           arr_ids[0, arr_ids.shape[0] - 1],
           arr_ids[arr_ids.shape[0] - 1, 0],
           arr_ids[arr_ids.shape[0] - 1, arr_ids.shape[0] - 1]
           ]
print(f'{reduce(mul, map(int, corners))}')  # 59187348943703
