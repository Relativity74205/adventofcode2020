from pathlib import Path

import numpy as np


with open(Path(__file__).parent / "data" / "puzzle11.txt", "r") as f:
    raw_data = f.read().splitlines()


def get_next_seats(arr, pos_x, pos_y):
    directions = ((0, 1), (1, 1), (1, 0), (-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1))
    visible_seats = []
    for dx, dy in directions:
        x, y = pos_x, pos_y
        while True:
            x += dx
            y += dy
            if x < 0 or y < 0 or x >= x_max or y >= y_max:
                break
            elif arr[x, y] == 0:
                visible_seats.append((x, y))
                break

    return visible_seats


seatplan = np.array([list(line) for line in raw_data])
seatplan = np.where(seatplan == 'L', 0, -1)
x_max, y_max = seatplan.shape
visible_seats = [[get_next_seats(seatplan, i, j) for i in range(x_max)] for j in range(y_max)]


rounds = 0
while True:
    seatplan_copy = seatplan.copy()
    for i in range(x_max):
        for j in range(y_max):
            taken = sum([seatplan[ele] for ele in visible_seats[j][i]])
            if seatplan[i, j] == 0 and taken == 0:
                seatplan_copy[i, j] = 1
            elif seatplan[i, j] == 1 and taken >= 5:
                seatplan_copy[i, j] = 0

    if (seatplan_copy == seatplan).all():
        print(f'{rounds=}')
        print((seatplan == 1).sum())
        break
    seatplan = seatplan_copy

    rounds += 1
