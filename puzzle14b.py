import re
from pathlib import Path
from collections import defaultdict
from functools import reduce
import itertools
from operator import add


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


def process_char(bitmask_char: str, address_char: str):
    if bitmask_char == '0':
        return [address_char]
    elif bitmask_char == '1':
        return [bitmask_char]
    else:
        return ['0', '1']


def process(bitmask: str, mem_address: int):
    mem_address_binary = str(bin(mem_address))[2:].zfill(36)
    address_combinations = [process_char(b, v) for b, v in zip(bitmask, mem_address_binary)]
    addresses = map(lambda a: ''.join(a), itertools.product(*address_combinations))

    return list(addresses)


mem = {}
for mask, memory_value in data_groups.items():
    for address, value in memory_value.items():
        addresses = process(mask, address)
        for key in addresses:
            mem[key] = value


total_sum = reduce(add, mem.values())
print(f'{total_sum=}')
