from pathlib import Path
from collections import defaultdict

with open(Path(__file__).parent.parent / "data" / "puzzle05.txt", "r") as f:
    raw_data = f.read().splitlines()


MAX_ROWS = 128
MAX_COLS = 8
COL_STEPS = {'L': -1,
             'R': 1,
             }
ROW_STEPS = {'F': -1,
             'B': 1,
             }


def get_row(row_str: str) -> int:
    region_length = MAX_ROWS
    steps = []
    for c in row_str:
        steps.append(region_length / 4 * (1 + ROW_STEPS[c]))
        region_length /= 2

    return int(sum(steps))


def get_col(col_str: str) -> int:
    region_width = MAX_COLS
    steps = []
    for c in col_str:
        steps.append(region_width / 4 * (1 + COL_STEPS[c]))
        region_width /= 2

    return int(sum(steps))


def get_free_id(data):
    seats = defaultdict(list)

    for seat in data:
        row = get_row(seat[:7])
        col = get_col(seat[7:])
        seats[row].append(col)

    for row, cols in seats.items():
        if len(cols) != 8 and row != min(seats.keys()) and row != max(seats.keys()):
            free_col = set(range(8)).difference(set(cols)).pop()
            return row * 8 + free_col


seat_ids = (get_row(seat[:7]) * 8 + get_col(seat[7:]) for seat in raw_data)
print(f'Solution for A is {max(seat_ids)}')  # 930
print(f'Solution for B is {get_free_id(raw_data)}')  # 515
