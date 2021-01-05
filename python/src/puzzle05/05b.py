from collections import defaultdict

from puzzle05 import raw_data, get_row, get_col


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


print(f'{get_free_id(raw_data)=}')
