from typing import Dict
from pathlib import Path
from itertools import product
from functools import reduce
from operator import add


with open(Path(__file__).parent / "data" / "puzzle19.txt", "r") as f:
    raw_data = f.read().splitlines()


rule_rows = [row for row in raw_data if ':' in row]
messages_rows = [row for row in raw_data if ':' not in row and row != '']
rules_dict = {int(rule.split(':')[0]): rule.split(':')[1][1:] for rule in rule_rows}


def parse_rule(rule: str, rules: Dict[int, str]):
    if rule in ('"a"', '"b"'):
        return [rule[1]]

    if '|' not in rule:
        results = [parse_rule(rules[int(sub_rule)], rules) for sub_rule in rule.split(' ')]
        return [reduce(add, r) for r in product(*results)]
    else:
        sub_results = [parse_rule(sub_rule, rules) for sub_rule in rule.split(' | ')]
        return reduce(add, sub_results)


valid_massages = set(parse_rule(rules_dict[0], rules_dict))
message_is_valid = [message in valid_massages for message in messages_rows]
print(f'{sum(message_is_valid)=}')  # 142
