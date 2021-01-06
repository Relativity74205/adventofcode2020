from collections import Counter

from puzzle02 import raw_data


def check_password_entry(entry: str) -> bool:
    policy, password = entry.split(': ')
    policy_char_range_string, policy_char = policy.split(' ')
    policy_char_range_list = [int(ele) for ele in policy_char_range_string.split('-')]
    policy_char_range = range(policy_char_range_list[0], policy_char_range_list[1] + 1)

    return Counter(password)[policy_char] in policy_char_range


valid_passwords = (check_password_entry(password_entry) for password_entry in raw_data)
print(f'{sum(valid_passwords)=}')  # 546
