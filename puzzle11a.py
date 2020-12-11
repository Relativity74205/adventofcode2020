from pathlib import Path

import numpy as np


with open(Path(__file__).parent / "data" / "puzzle11.txt", "r") as f:
    raw_data = f.read().splitlines()

seatplan = [list(line) for line in raw_data]
seatplan = np.array(seatplan)
seatplan = np.where(seatplan == 'L', 0, -1)
x_max, y_max = seatplan.shape


def get_occupied(arr, pos_x, pos_y) -> int:
    x1 = max(0, pos_x - 1)
    y1 = max(0, pos_y - 1)
    x2 = min(x_max, pos_x + 2)
    y2 = min(y_max, pos_y + 2)
    return (arr[x1:x2, y1:y2] == 1).sum()


rounds = 0
while True:
    seatplan_copy = seatplan.copy()
    for i in range(x_max):
        for j in range(y_max):
            occupied = get_occupied(seatplan, i, j) - seatplan[i, j]
            if seatplan[i, j] == 0 and occupied == 0:
                seatplan_copy[i, j] = 1
            elif seatplan[i, j] == 1 and occupied >= 4:
                seatplan_copy[i, j] = 0

    if (seatplan_copy == seatplan).all():
        print(f'{rounds=}')
        print((seatplan == 1).sum())
        break
    seatplan = seatplan_copy

    rounds += 1
