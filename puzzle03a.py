import sys
from pathlib import Path
from dataclasses import dataclass

with open(Path(__file__).parent / "data" / "puzzle03.txt", "r") as f:
    data = f.read().splitlines()


@dataclass
class Pos:
    x: int
    y: int


pos = Pos(0, 0)
base_width = len(data[0])

amount_trees = 0
while True:
    try:
        line = data[pos.y]
    except IndexError:
        print(f'{amount_trees=}')
        sys.exit()

    try:
        cell = line[pos.x]
    except IndexError:
        pos.x = pos.x - base_width
        cell = line[pos.x]

    if cell == '#':
        amount_trees += 1

    pos.x += 3
    pos.y += 1
