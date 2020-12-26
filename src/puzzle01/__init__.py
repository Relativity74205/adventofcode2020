from functools import reduce
from operator import mul
import itertools
from typing import Iterator
from pathlib import Path


with open(Path(__file__).parent / "puzzle01.txt", "r") as f:
    raw_data = f.read().splitlines()


def solve(target: int, numbers: Iterator[int], amount_numbers):
    combinations = itertools.combinations(numbers, amount_numbers)
    for combination in combinations:
        if sum(combination) == target:
            return reduce(mul, combination)

