import sys
import math
from pathlib import Path

target_number = 2020

with open(Path(__file__).parent / "data" / "puzzle01.txt", "r") as f:
    data = f.read().splitlines()

# data_sorted = sorted([int(number) for number in data])

small_numbers = [int(number) for number in data if int(number) <= math.ceil(target_number / 2)]
large_numbers = [int(number) for number in data if int(number) >= math.floor(target_number / 2)]

for small_number in small_numbers:
    for large_number in large_numbers:
        if small_number + large_number == target_number:
            print(f'{small_number=} and {large_number}; multiplied: {small_number * large_number}')
            sys.exit()
