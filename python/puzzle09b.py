import sys
from pathlib import Path

with open(Path(__file__).parent / "data" / "puzzle09.txt", "r") as f:
    raw_data = f.read().splitlines()


data = list(map(int, raw_data))
target_number = 20874512


for i in range(0, len(raw_data)):
    subtotal = 0
    for j in range(i, len(raw_data)):
        subtotal += data[j]
        if subtotal == target_number:
            print(f'start: {data[i]}; end: {data[j]}; sum: {data[i] + data[j]}')
            sys.exit(0)
        elif subtotal > target_number:
            break

