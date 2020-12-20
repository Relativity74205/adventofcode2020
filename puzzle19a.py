from typing import Dict
from pathlib import Path
from itertools import product
from functools import reduce


with open(Path(__file__).parent / "data" / "puzzle19.txt", "r") as f:
    raw_data = f.read().splitlines()


def parse_rule(rule: str, rules: Dict[int, str]):
    if rule in ('"a"', '"b"'):
        return [rule[1]]

    if '|' not in rule:
        results = []
        for sub_rule in rule.split(' '):
            sub_result = parse_rule(rules[int(sub_rule)], rules)
            results.append(sub_result)
        result_comb = list(product(*results))
        result = [reduce(lambda a, b: a + b, r) for r in result_comb]
        return result
    else:
        sub_rule1 = rule.split(' | ')[0]
        sub_rule2 = rule.split(' | ')[1]
        result1 = parse_rule(sub_rule1, rules)
        result2 = parse_rule(sub_rule2, rules)
        result = result1 + result2
        return result


rule_rows = [row for row in raw_data if ':' in row]
messages_rows = [row for row in raw_data if ':' not in row and row != '']

rules_dict = {int(rule.split(':')[0]): rule.split(':')[1][1:] for rule in rule_rows}

valid_massages = parse_rule(rules_dict[0], rules_dict)
valid_massages_set = set(valid_massages)

assert ({'aaaabb', 'aaabab', 'abbabb', 'abbbab', 'aabaab', 'aabbbb', 'abaaab', 'ababbb'}
        == set(parse_rule('4 1 5', {0: '4 1 5', 1: '2 3 | 3 2', 2: '4 4 | 5 5', 3: '4 5 | 5 4', 4: '"a"', 5: '"b"'}))
        )

message_is_valid = [message in valid_massages_set for message in messages_rows]
print(f'{sum(message_is_valid)=}')
