from pathlib import Path
from dataclasses import dataclass
from collections import defaultdict
from functools import reduce

with open(Path(__file__).parent / "data" / "puzzle03.txt", "r") as f:
    data = f.read().splitlines()


@dataclass
class Pos:
    x: int
    y: int


base_width = len(data[0])
strategies = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2), )

amount_trees = defaultdict(int)

for strategy in strategies:
    pos = Pos(0, 0)
    while True:
        try:
            line = data[pos.y]
        except IndexError:
            break

        try:
            cell = line[pos.x]
        except IndexError:
            pos.x = pos.x - base_width
            cell = line[pos.x]

        if cell == '#':
            amount_trees[strategy] += 1

        pos.x += strategy[0]
        pos.y += strategy[1]


print(reduce(lambda x, y: x*y, amount_trees.values()))
