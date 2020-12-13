from functools import reduce
from pathlib import Path
from typing import List


with open(Path(__file__).parent / "data" / "puzzle13.txt", "r") as f:
    raw_data = f.read().splitlines()


entries = raw_data[1].split(',')


def find_sub_solution(sub_solution: int, new_n: int, lcm_sub: int, delay: int):
    i = 0
    while True:
        i += 1
        candidate = sub_solution + lcm_sub * i
        if (candidate + delay) % new_n == 0:
            return candidate


def find_solution(lines_dict, lines):
    solution = None
    for i in range(len(lines) - 1):
        if not solution:
            solution = lines[i]
        new_n = lines[i + 1]
        delay = lines_dict[lines[i + 1]]
        lcm = reduce(lambda a, b: a * b, lines[:(i + 1)])
        solution = find_sub_solution(solution, new_n, lcm, delay)

    return solution


def solve(data: List) -> int:
    lines_dict = {int(entry): i for i, entry in enumerate(data) if entry != 'x'}
    lines = list(lines_dict.keys())

    solution = find_solution(lines_dict, lines)

    return solution


final_solution = solve(entries)

print(f'{final_solution=}')
# 487905974205117
