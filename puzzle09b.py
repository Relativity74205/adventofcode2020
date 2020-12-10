from typing import List
import sys
from pathlib import Path
from itertools import combinations
from functools import lru_cache

with open(Path(__file__).parent / "data" / "puzzle09.txt", "r") as f:
    raw_data = f.read().splitlines()


data = list(map(int, raw_data))
target_number = 20874512


def get_sum(start: int, end: int) -> int:
    return sum(data[start: end + 1])


for i in range(0, len(raw_data)):
    for j in range(i, len(raw_data)):
        if target_number == get_sum(i, j):
            print(f'start: {data[i]}; end: {data[j]}; sum: {data[i] + data[j]}')
            sys.exit(0)
