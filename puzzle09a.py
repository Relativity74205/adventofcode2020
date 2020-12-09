import sys
from pathlib import Path
from itertools import combinations

with open(Path(__file__).parent / "data" / "puzzle09.txt", "r") as f:
    raw_data = f.read().splitlines()


data = list(map(int, raw_data))

for i in range(25, len(raw_data)):
    current_window = data[i - 25:i + 1]
    last_25_sums = set(map(sum, combinations(current_window[:-1], 2)))
    if data[i] not in last_25_sums:
        print(current_window[-1])
        # sys.exit(0)
