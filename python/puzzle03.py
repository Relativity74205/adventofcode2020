import typing as ty
from pathlib import Path
from functools import reduce
from operator import mul


with open(Path(__file__).parent.parent / "data" / "puzzle03.txt", "r") as f:
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


result_a = solve(raw_data, (3, 1))
results_b = (solve(raw_data, strategy) for strategy in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2), ))
print(f'Solution for A is {result_a}')  # 211
print(f'Solution for A is {reduce(mul, results_b)}')  # 3584591857
