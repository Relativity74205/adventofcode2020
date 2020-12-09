from typing import List
from pathlib import Path


with open(Path(__file__).parent / "data" / "puzzle07.txt", "r") as f:
    data = f.read().splitlines()

target_bag = 'shiny gold bag'

rules = {}
for rule in data:
    rule = rule.replace('.', '').replace('bags', 'bag')
    outer_bag = rule.split(' contain ')[0]
    inner_bags = rule.split(' contain ')[1]
    if inner_bags == 'no other bag':
        rules[outer_bag] = {}
    else:
        inner_bags = inner_bags.split(', ')
        inner_bag_parts = [bag.split(' ') for bag in inner_bags]
        inner_bags = {' '.join(bag_parts[1:]): int(bag_parts[0]) for bag_parts in inner_bag_parts}
        rules[outer_bag] = inner_bags


def count_bags(bag: str, cnt_bags: str):
    bags = rules[bag]
    if len(bags) > 0:
        # cnt_bags += '*('
        for inner_bag, cnt_inner_bags in bags.items():
            cnt_bags += f'{str(cnt_inner_bags)} + {str(cnt_inner_bags)} * ('
            cnt_bags = count_bags(inner_bag, cnt_bags)
            cnt_bags += ') + '
    else:
        cnt_bags += '0'

    if cnt_bags.endswith(' + '):
        cnt_bags = cnt_bags[:-3]

    return cnt_bags


cnt_bags_total = count_bags(target_bag, '')

print(f'{cnt_bags_total=}')
print(f'{eval(cnt_bags_total)=}')
