from collections import Counter

from puzzle02 import raw_data


def check_password_entry(entry: str) -> bool:
    password = entry.split(':')[1].strip()
    policy = entry.split(':')[0]
    policy_char = policy.split(' ')[1]
    policy_char_range_list = policy.split(' ')[0].split('-')
    policy_char_range = range(int(policy_char_range_list[0]), int(policy_char_range_list[1]) + 1)

    return Counter(password)[policy_char] in policy_char_range


valid_passwords = (check_password_entry(password_entry) for password_entry in raw_data)
print(f'{sum(valid_passwords)=}')  # 546
