import typing as ty
from pathlib import Path

with open(Path(__file__).parent / "puzzle03.txt", "r") as f:
    raw_data = f.read().splitlines()


def solve(data: ty.List, strategy: ty.Tuple):
    x, y = 0, 0
    base_width = len(data[0])

    amount_trees = 0
    while True:
        try:
            line = data[y]
        except IndexError:
            return amount_trees

        try:
            cell = line[x]
        except IndexError:
            x -= base_width
            cell = line[x]

        x += strategy[0]
        y += strategy[1]

        amount_trees += cell == '#'
