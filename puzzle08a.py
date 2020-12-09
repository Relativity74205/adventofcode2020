from typing import Set
from pathlib import Path


with open(Path(__file__).parent / "data" / "puzzle08.txt", "r") as f:
    data = f.read().splitlines()


acc = 0
visited = set()

# def check_line(line: str, acc: int, visited: Set):

i = 0
while True:
    visited.add(i)
    print(f'{i=} {data[i]}')
    cmd = data[i].split(' ')[0]
    num = data[i].split(' ')[1]
    if cmd == 'acc':
        acc += int(num)
        i += 1
    elif cmd == 'jmp':
        i += int(num)
    elif cmd == 'nop':
        i += 1

    if i in visited:
        print('Infinite loop')
        break

    if i > len(data):
        print('Program finished')
        break


print(f'{acc=}')
