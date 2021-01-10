from pathlib import Path
from collections import Counter


with open(Path(__file__).parent.parent / "data" / "puzzle02.txt", "r") as f:
    raw_data = f.read().splitlines()


def check_password_entry(entry: str) -> bool:
    policy, password = entry.split(': ')
    policy_char_range_string, policy_char = policy.split(' ')
    policy_char_range_list = [int(ele) for ele in policy_char_range_string.split('-')]
    policy_char_range = range(policy_char_range_list[0], policy_char_range_list[1] + 1)

    return Counter(password)[policy_char] in policy_char_range


def check_password_entry_complex(entry: str) -> bool:
    password = entry.split(':')[1].strip()
    policy = entry.split(':')[0]
    policy_char = policy.split(' ')[1]
    policy_char_range_list = list(map(int, policy.split(' ')[0].split('-')))
    first_occurrence = policy_char_range_list[0] - 1
    second_occurrence = policy_char_range_list[1] - 1

    return (password[first_occurrence] == policy_char) != (password[second_occurrence] == policy_char)


print(f'Solution for A is {sum(check_password_entry(password_entry) for password_entry in raw_data)}')  # 546
print(f'Solution for B is {sum(check_password_entry_complex(password_entry) for password_entry in raw_data)}')  # 275
