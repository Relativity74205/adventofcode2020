import sys
from pathlib import Path


with open(Path(__file__).parent / "data" / "puzzle13.txt", "r") as f:
    data = f.read().splitlines()


earliest_start_time = int(data[0])
lines = [int(line) for line in data[1].split(',') if line != 'x']

start_time = earliest_start_time
while True:
    for line in lines:
        if start_time % line == 0:
            print(f'{start_time=}, wait_time: {start_time - earliest_start_time}, {line=}, '
                  f'factor: {(start_time - earliest_start_time)*line}')
            sys.exit()

    start_time += 1
