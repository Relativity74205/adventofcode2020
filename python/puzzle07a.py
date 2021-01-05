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
        rules[outer_bag] = []
    else:
        inner_bags = inner_bags.split(', ')
        inner_bags = [' '.join(bag.split(' ')[1:]) for bag in inner_bags]
        rules[outer_bag] = inner_bags


def check_bag(bag: str, path: str, valid_paths: List[str]):
    bags = rules[bag]
    for inner_bag in bags:
        if inner_bag == target_bag:
            valid_paths.append(f'{path}_{inner_bag}')
        else:
            check_bag(inner_bag, f'{path}_{inner_bag}', valid_paths)

    return valid_paths


valid_paths_full = []
for rule in rules:
    valid_paths_rule = check_bag(rule, f'{rule}', [])
    valid_paths_full += valid_paths_rule

valid_bags = set([path.split('_')[0] for path in valid_paths_full])
print(f'{len(valid_bags)}')
