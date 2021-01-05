from puzzle02 import raw_data


def check_password_entry(entry: str) -> bool:
    password = entry.split(':')[1].strip()
    policy = entry.split(':')[0]
    policy_char = policy.split(' ')[1]
    policy_char_range_list = list(map(int, policy.split(' ')[0].split('-')))
    first_occurrence = policy_char_range_list[0] - 1
    second_occurrence = policy_char_range_list[1] - 1

    return (password[first_occurrence] == policy_char) != (password[second_occurrence] == policy_char)


valid_passwords = (check_password_entry(password_entry) for password_entry in raw_data)
print(f'{sum(valid_passwords)=}')  # 275
