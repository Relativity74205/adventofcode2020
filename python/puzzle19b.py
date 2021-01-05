from typing import Dict, Set
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


def check_message(m: str, rule42: Set, rule31: Set, message_part_length: int) -> bool:
    message_parts_class = []
    for message_index in range(0, len(m), message_part_length):
        message_part = m[message_index: message_index + message_part_length]
        if message_part in rule42:
            message_parts_class.append('r42')
        elif message_part in rule31:
            message_parts_class.append('r31')
        else:
            return False

    message_parts_class_sorted = sorted(message_parts_class, reverse=True)
    cnt_r42 = len([ele for ele in message_parts_class if ele == 'r42'])
    cnt_r31 = len([ele for ele in message_parts_class if ele == 'r31'])
    if message_parts_class_sorted == message_parts_class and message_parts_class[-1] == 'r31' and cnt_r42 > cnt_r31:
        return True
    else:
        return False


r42 = set(parse_rule('42', rules_dict))
r31 = set(parse_rule('31', rules_dict))

message_is_valid = [check_message(message, r42, r31, 8) for message in messages_rows]
print(f'{sum(message_is_valid)=}')
