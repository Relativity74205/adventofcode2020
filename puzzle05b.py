from pathlib import Path
from collections import defaultdict

with open(Path(__file__).parent / "data" / "puzzle05.txt", "r") as f:
    data = f.read().splitlines()


seats = defaultdict(list)
max_rows = 128
max_cols = 8
step_dict = {'F': -1,
             'B': 1,
             'L': -1,
             'R': 1}


def get_row(row_str: str) -> int:
    region_length = max_rows
    steps = []
    for c in row_str:
        steps.append(region_length / 4 * (1 + step_dict[c]))
        region_length /= 2

    return int(sum(steps))


def get_col(col_str: str) -> int:
    region_width = max_cols
    steps = []
    for c in col_str:
        steps.append(region_width / 4 * (1 + step_dict[c]))
        region_width /= 2

    return int(sum(steps))


max_seat_id = -1
for seat in data:
    row = get_row(seat[:7])
    col = get_col(seat[7:])
    seat_id = row * 8 + col
    max_seat_id = max(max_seat_id, seat_id)
    seats[row].append(col)

print(f'{max_seat_id=}')

for row, cols in seats.items():
    if len(cols) != 8 and row != min(seats.keys()) and row != max(seats.keys()):
        free_col = set(range(8)).difference(set(cols)).pop()

        print(f'{row=}{free_col} id:{row*8+free_col}')
