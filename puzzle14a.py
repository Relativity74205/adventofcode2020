import re
from pathlib import Path
from collections import defaultdict


with open(Path(__file__).parent / "data" / "puzzle14.txt", "r") as f:
    raw_data = f.read().splitlines()


data_groups = defaultdict(dict)
mask = None
for line in raw_data:
    if line.startswith('mask'):
        mask = line.split(' = ')[1]
    else:
        address = int(re.findall(r'\[(\d*)\]', line)[0])
        value = int(line.split(' = ')[1])
        data_groups[mask][address] = value


def process(bitmask: str, val: int):
    value_binary = str(bin(val))[2:].zfill(36)
    return ''.join([b if b != 'X' else v for b, v in zip(bitmask, value_binary)])


mem = {}
for mask, memory_value in data_groups.items():
    for address, value in memory_value.items():
        mem[address] = process(mask, value)

total_sum = sum(map(lambda a: int(a, 2), mem.values()))
print(f'{total_sum=}')
