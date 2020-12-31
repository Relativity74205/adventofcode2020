from pathlib import Path

with open(Path(__file__).parent / "puzzle05.txt", "r") as f:
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
