from functools import reduce
from pathlib import Path
from typing import Dict


with open(Path(__file__).parent / "data" / "puzzle13.txt", "r") as f:
    data = f.read().splitlines()


entries = data[1].split(',')

lines_dict = {int(entry): i for i, entry in enumerate(entries) if entry != 'x'}


def sub_solution(sub_solution: int, new_n: int, lcm_sub: int, delay: int):
    i = 0
    while True:
        i += 1
        candidate = sub_solution + lcm_sub * i
        if (candidate + delay) % new_n == 0:
            return candidate


def solution(lines_dict: Dict) -> int:
    lines = list(lines_dict.keys())
    time = None
    for i in range(len(lines) - 1):
        if not time:
            time = lines[i]
        n1 = lines[i]
        n2 = lines[i + 1]
        delta = lines_dict[lines[i + 1]]
        lcm = reduce(lambda a, b: a * b, lines[:(i+1)])
        time = sub_solution(time, n2, lcm, delta)

    return time


solution = solution(lines_dict)

print(f'{solution=}')
# 487905974205117
