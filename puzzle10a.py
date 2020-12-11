from pathlib import Path
from collections import defaultdict

with open(Path(__file__).parent / "data" / "puzzle10.txt", "r") as f:
    raw_data = f.read().splitlines()

data = sorted(list(map(int, raw_data)))
d = defaultdict(int)
for i in range(len(data) - 1):
    d[data[i + 1] - data[i]] += 1
d[data[0]] += 1
d[3] += 1

print(f'{d[1]=}, {d[3]=}')
print(f'multiplication {d[1]*d[3]}')
