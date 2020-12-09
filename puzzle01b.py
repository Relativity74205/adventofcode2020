import sys
from pathlib import Path

target_number = 2020

with open(Path(__file__).parent / "data" / "puzzle01.txt", "r") as f:
    data = f.read().splitlines()

numbers = [int(number) for number in data]

for n1 in numbers:
    for n2 in numbers:
        for n3 in numbers:
            if n1 + n2 + n3 == target_number:
                print(f'{n1=} and {n2} and {n3}; multiplied: {n1 * n2 * n3}')
                sys.exit()
